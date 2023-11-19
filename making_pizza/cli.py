import time
from random import randint
from typing import Literal, Union

import click
from pizza import Hawaiian, Margherita, Pepperoni
from utils import log, log_with_template

pizza_classes = {"margherita": Margherita, "pepperoni": Pepperoni, "hawaiian": Hawaiian}

pizza_emoji_dict = {
    "margherita": "🧀",
    "pepperoni": "🍕",
    "hawaiian": "🍍",
}


@log
def bake(pizza: str) -> str:
    """
    Bake the specified pizza.

    :param pizza: The name of the pizza to bake.
    :type pizza: str
    :return: A string indicating the pizza has been baked.
    :rtype: str
    """
    time.sleep(randint(1, 3))
    return f"Baked {pizza}!"


@log_with_template("🚚 Delivered in {}s!")
def deliver(pizza: str) -> str:
    """
    Deliver the specified pizza.

    :param pizza: The name of the pizza to deliver.
    :type pizza: str
    :return: A string indicating the pizza has been delivered.
    :rtype: str
    """
    time.sleep(randint(1, 3))
    return f"Delivered {pizza}!"


@log_with_template("🏠 Picked up in {}s!")
def pickup(pizza: str) -> str:
    """
    Pick up the specified pizza.

    :param pizza: The name of the pizza for pickup.
    :type pizza: str
    :return: A string indicating the pizza has been picked up.
    :rtype: str
    """
    time.sleep(randint(1, 3))
    return f"Picked up {pizza}!"


@click.group()
def cli() -> None:
    """
    Pizza Ordering CLI.
    """
    pass


@cli.command()
@click.argument(
    "pizza_name",
    type=click.Choice(["margherita", "pepperoni", "hawaiian"], case_sensitive=False),
)
@click.option(
    "--size", type=click.Choice(["L", "XL"], case_sensitive=False), default="L"
)
@click.option(
    "--delivery", is_flag=True, help="Include this flag to have the pizza delivered"
)
def order(
    pizza_name: str, size: Union[Literal["XL"], Literal["L"]], delivery: bool
) -> None:
    """
    Order a pizza with optional delivery.

    :param pizza_name: The name of the pizza to order.
    :param size: The size of the pizza.
    :param delivery: Flag to indicate if the pizza needs to be delivered.
    """
    pizza_class = pizza_classes[pizza_name.lower()]
    pizza = pizza_class(size)
    delivery_message = " with delivery" if delivery else ""
    click.echo(f"Ordered a {size} {pizza_name.capitalize()} Pizza{delivery_message}!")
    click.echo(f"Ingredients: {', '.join(filter(None, pizza.dict().values()))}")
    click.echo(f"{bake(pizza_name.lower())}")
    if delivery:
        click.echo(deliver(pizza_name.lower()))
    else:
        click.echo(pickup(pizza_name.lower()))


@cli.command()
def menu() -> None:
    """
    Show the pizza menu.
    """
    click.echo("Our pizza menu:")
    for name, cls in pizza_classes.items():
        pizza = cls("L")
        click.echo(
            f"{name.capitalize()} "
            f"{pizza_emoji_dict[name]}: {', '.join(pizza.dict().values())} "
        )


if __name__ == "__main__":
    cli()

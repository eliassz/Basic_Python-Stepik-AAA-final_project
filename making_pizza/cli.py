import click
from pizza import Margherita, Pepperoni, Hawaiian

pizza_classes = {
    'margherita': Margherita,
    'pepperoni': Pepperoni,
    'hawaiian': Hawaiian
}

pizza_emoji_dict = {
    'margherita': '🧀',
    'pepperoni': '🍕',
    'hawaiian': '🍍',
}

@click.group()
def cli():
    """Pizza Ordering CLI"""
    pass

@cli.command()
@click.argument('pizza_name', type=click.Choice(['margherita', 'pepperoni', 'hawaiian'], case_sensitive=False))
@click.option('--size', type=click.Choice(['L', 'XL'], case_sensitive=False), default='L')
@click.option('--delivery', is_flag=True, help='Include this flag to have the pizza delivered')
def order(pizza_name, size, delivery):
    """Order a pizza with optional delivery."""
    pizza_class = pizza_classes[pizza_name.lower()]
    pizza = pizza_class(size)
    delivery_message = " and will be delivered" if delivery else ""
    click.echo(f"Ordered a {size} {pizza_name.capitalize()} Pizza{delivery_message}!")
    click.echo(', '.join(filter(None, pizza.dict().values())))

@cli.command()
def menu():
    """Show the pizza menu."""
    click.echo("Our pizza menu:")
    for name, cls in pizza_classes.items():
        pizza = cls('L')
        click.echo(f"{name.capitalize()} {pizza_emoji_dict[name]}: {', '.join(filter(None, pizza.dict().values()))}")

if __name__ == "__main__":
    cli()

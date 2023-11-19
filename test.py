import pytest
from click.testing import CliRunner

from cli import bake, cli, deliver, pickup


@pytest.fixture
def runner() -> CliRunner:
    """
    Pytest fixture to provide a CliRunner object for testing CLI commands.

    :return: A CliRunner instance for testing.
    :rtype: CliRunner
    """
    return CliRunner()


def test_bake() -> None:
    """
    Test the bake function to ensure it returns the correct response.
    """
    pizza = "margherita"
    result = bake(pizza)
    assert "Baked margherita!" in result


def test_deliver() -> None:
    """
    Test the deliver function to ensure it returns the correct response.
    """
    pizza = "pepperoni"
    result = deliver(pizza)
    assert "Delivered pepperoni!" in result


def test_pickup() -> None:
    """
    Test the pickup function to ensure it returns the correct response.
    """
    pizza = "hawaiian"
    result = pickup(pizza)
    assert "Picked up hawaiian!" in result


def test_order(runner: CliRunner) -> None:
    """
    Test the 'order' CLI command to ensure it processes orders correctly.

    :param runner: A CliRunner instance for testing.
    :type runner: CliRunner
    """
    result = runner.invoke(cli, ["order", "margherita", "--size", "L"])
    assert "Ordered a L Margherita Pizza!" in result.output
    assert "Baked margherita!" in result.output


def test_order_with_delivery(runner: CliRunner) -> None:
    """
    Test the 'order' CLI command with delivery option to ensure it
    processes orders correctly.

    :param runner: A CliRunner instance for testing.
    :type runner: CliRunner
    """
    result = runner.invoke(cli, ["order", "pepperoni", "--size", "XL", "--delivery"])
    assert "Ordered a XL Pepperoni Pizza with delivery!" in result.output
    assert "Delivered pepperoni!" in result.output


def test_menu(runner: CliRunner) -> None:
    """
    Test the 'menu' CLI command to ensure it displays the correct pizza menu.

    :param runner: A CliRunner instance for testing.
    :type runner: CliRunner
    """
    result = runner.invoke(cli, ["menu"])
    assert "Our pizza menu:" in result.output
    assert "Margherita 🧀" in result.output
    assert "Pepperoni 🍕" in result.output
    assert "Hawaiian 🍍" in result.output

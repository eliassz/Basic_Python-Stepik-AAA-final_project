import pytest
from click.testing import CliRunner
from making_pizza.cli import cli, bake, deliver, pickup

@pytest.fixture
def runner():
    return CliRunner()

def test_bake():
    pizza = 'margherita'
    result = bake(pizza)
    assert 'Baked margherita!' in result

def test_deliver():
    pizza = 'pepperoni'
    result = deliver(pizza)
    assert 'Delivered pepperoni!' in result

def test_pickup():
    pizza = 'hawaiian'
    result = pickup(pizza)
    assert 'Picked up hawaiian!' in result

def test_order(runner):
    result = runner.invoke(cli, ['order', 'margherita', '--size', 'L'])
    assert 'Ordered a L Margherita Pizza!' in result.output
    assert 'Baked margherita!' in result.output

def test_order_with_delivery(runner):
    result = runner.invoke(cli, ['order', 'pepperoni', '--size', 'XL', '--delivery'])
    assert 'Ordered a XL Pepperoni Pizza with delivery!' in result.output
    assert 'Delivered pepperoni!' in result.output

def test_menu(runner):
    result = runner.invoke(cli, ['menu'])
    assert 'Our pizza menu:' in result.output
    assert 'Margherita 🧀' in result.output
    assert 'Pepperoni 🍕' in result.output
    assert 'Hawaiian 🍍' in result.output

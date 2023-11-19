from typing import Dict, Literal

class Pizza:
    """
    Base class for Pizza, representing common properties and behaviors of pizzas.
    """

    receipt: Dict[str, str] = {}

    def __init__(self, size: Literal['XL', 'L']) -> None:
        """
        Initialize the Pizza with a specific size.

        :param size: Size of the pizza, either 'XL' or 'L'.
        :type size: Literal['XL', 'L']
        :raises ValueError: If the size is not 'XL' or 'L'.
        """
        if size not in ['XL', 'L']:
            raise ValueError(f'Not such size: {size} only "XL" or "L"')
        self.size = size

    def dict(self) -> Dict[str, str]:
        """
        Returns the receipt of the pizza.

        :return: A dictionary representing the receipt of the pizza.
        :rtype: Dict[str, str]
        """
        return type(self).receipt


class Margherita(Pizza):
    """
    Margherita pizza class, inheriting from Pizza.
    """

    receipt = {
       'ingredient_1': 'tomato sauce',
       'ingredient_2': 'mozzarella',
       'ingredient_3': 'tomatoes',
       'ingredient_4': None,
    }


class Pepperoni(Pizza):
    """
    Pepperoni pizza class, inheriting from Pizza.
    """

    receipt = {
       'ingredient_1': 'tomato sauce',
       'ingredient_2': 'mozzarella',
       'ingredient_3': 'pepperoni',
       'ingredient_4': None,
    }


class Hawaiian(Pizza):
    """
    Hawaiian pizza class, inheriting from Pizza.
    """

    receipt = {
       'ingredient_1': 'tomato sauce',
       'ingredient_2': 'mozzarella',
       'ingredient_3': 'chicken',
       'ingredient_4': 'pineapples',
    }

from typing import Literal

class Pizza:
    receipt = {}

    def __init__(self, size: Literal['XL', 'L']):
        if size not in ['XL', 'L']:
            raise ValueError(f'Not such size: {size} only "XL" or "L"')
        self.size = size

    def dict(self):
        return type(self).receipt


class Margherita(Pizza):
    receipt = {
       'ingredient_1': 'tomato sauce',
       'ingredient_2': 'mozzarella',
       'ingredient_3': 'tomatoes',
       'ingredient_4': None,
    }

class Pepperoni(Pizza):
    receipt = {
       'ingredient_1': 'tomato sauce',
       'ingredient_2': 'mozzarella',
       'ingredient_3': 'pepperoni',
       'ingredient_4': None,
    }

class Hawaiian(Pizza):
    receipt = {
       'ingredient_1': 'tomato sauce',
       'ingredient_2': 'mozzarella',
       'ingredient_3': 'chicken',
       'ingredient_4': 'pineapples',
    }
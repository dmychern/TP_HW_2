import pytest
from src.recipes import Ingredient, Recipe, ShoppingList

def test_ingredient_creation():
    ing = Ingredient("Сахар", 100, "г")
    assert ing.name == "Сахар"
    assert ing.quantity == 100
    assert ing.unit == "г"

def test_recipe_creation():
    ing = Ingredient("Сахар", 100, "г")
    recipe = Recipe("Чай", [ing])
    assert recipe.title == "Чай"
    assert len(recipe.ingredients) == 1

def test_shopping_list():
    ing = Ingredient("Сахар", 100, "г")
    recipe = Recipe("Чай", [ing])
    sl = ShoppingList()
    sl.add_recipe(recipe, 2)
    items = sl.get_list()
    assert len(items) == 1
    assert items[0].name == "Сахар"
    assert items[0].quantity == 200

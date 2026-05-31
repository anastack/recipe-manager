import pytest
from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe

def test_ingredient_creation():
    ing = Ingredient("Мука", 500, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"
    
def test_ingredient_str():
    ing = Ingredient("Мука", 500, "г")
    assert str(ing) == "Мука: 500.0 г"
    
def test_ingredient_eq():
    assert Ingredient("Мука", 100, "г") == Ingredient("Мука", 999, "г")
    assert Ingredient("Мука", 100, "г") != Ingredient("Сахар", 100, "г")
    assert Ingredient("Мука", 100, "г") != Ingredient("Мука", 100, "кг")

def test_ingredient_negative():
    with pytest.raises(ValueError):
        Ingredient("Milk", -1, "l")




    

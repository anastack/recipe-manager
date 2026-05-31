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
        


def test_recipe_creation():
    ing = Ingredient("Мука", 500, "г")
    recipe = Recipe("Пицца", [ing])
    assert recipe.title == "Пицца"
    assert recipe.ingredients == [ing]
    
def test_recipe_add_new_ingredient():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    assert len(recipe) == 1
    
def test_recipe_add_existing_ingredient():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    recipe.add_ingredient(Ingredient("Мука", 100, "г"))
    assert len(recipe) == 1
    assert recipe.ingredients[0].quantity == 600.0
    
def test_recipe_scale():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    scaled = recipe.scale(2)
    assert scaled is not recipe
    assert recipe.ingredients[0].quantity == 500.0   
    assert scaled.ingredients[0].quantity == 1000.0
    

def test_recipe_scale_incorrect_ratio():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    with pytest.raises(ValueError):
        recipe.scale(0)

def test_recipe_len():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    recipe.add_ingredient(Ingredient("Сыр", 200, "г"))
    assert len(recipe) == 2

        

    




    

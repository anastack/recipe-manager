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

        
        
        
@pytest.fixture
def pizza():
    recipe = Recipe("Маргарита")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    recipe.add_ingredient(Ingredient("Сыр", 200, "г"))
    return recipe

def test_shoppinglist_add_recipe(pizza):
    sl = ShoppingList()
    sl.add_recipe(pizza, 1)
    assert len(sl.get_list()) == 2
    
def test_shoppinglist_add_recipe_incorrect(pizza):
    sl = ShoppingList()
    with pytest.raises(ValueError):
        sl.add_recipe(pizza, 0)
        
def test_shoppinglist_remove(pizza):
    sl = ShoppingList()
    sl.add_recipe(pizza, 1)
    sl.remove_recipe("Маргарита")
    assert len(sl.get_list()) == 0
    
def test_shoppinglist_remove_nonexisting(pizza):
    sl = ShoppingList()
    sl.add_recipe(pizza, 1)
    sl.remove_recipe("Какой-то")
    assert len(sl.get_list()) == 2


def test_shoppinglist_get_list_sums():
    pizza = Recipe("Пицца")
    pizza.add_ingredient(Ingredient("Мука", 500, "г"))
    bread = Recipe("Хлеб")
    bread.add_ingredient(Ingredient("Мука", 300, "г"))

    sl = ShoppingList()
    sl.add_recipe(pizza, 1)
    sl.add_recipe(bread, 1)

    result = sl.get_list()
    assert len(result) == 1
    assert result[0].quantity == pytest.approx(800.0)
    

def test_shoppinglist_get_list_sorted():
    recipe = Recipe("Блюдо")
    recipe.add_ingredient(Ingredient("Сыр", 200, "г"))
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    recipe.add_ingredient(Ingredient("Приправа", 10, "г"))

    sl = ShoppingList()
    sl.add_recipe(recipe, 1)

    names = [ing.name for ing in sl.get_list()]
    assert names == ["Мука", "Приправа", "Сыр"]
    

def test_shoppinglist_add_combine(pizza):
    sl1 = ShoppingList()
    sl1.add_recipe(pizza, 1)

    bread = Recipe("Хлеб")
    bread.add_ingredient(Ingredient("Мука", 300, "г"))
    sl2 = ShoppingList()
    sl2.add_recipe(bread, 1)

    res = sl1 + sl2
    result = res.get_list()
    quantities = {ing.name: ing.quantity for ing in result}
    assert quantities["Мука"] == pytest.approx(800.0)
    assert quantities["Сыр"] == pytest.approx(200.0)
    
    
    
def test_shoppinglist_not_change_originals(pizza):
    sl1 = ShoppingList()
    sl1.add_recipe(pizza, 1)
    bread = Recipe("Хлеб")
    bread.add_ingredient(Ingredient("Мука", 300, "г"))
    sl2 = ShoppingList()
    sl2.add_recipe(bread, 1)
    res = sl1 + sl2
    assert len(sl1.get_list()) == 2
    assert len(sl2.get_list()) == 1




    

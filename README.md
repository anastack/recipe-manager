# Recipe Manager

Консольное приложение для управления рецептами. Позволяет создавать ингредиенты
и рецепты, масштабировать порции, объединять ингредиенты из нескольких рецептов
в общий список покупок и работать с диетическими рецептами.

## Возможности

- `Ingredient` — отдельный продукт с названием, количеством и единицей измерения
- `Recipe` — рецепт блюда: добавление ингредиентов, масштабирование порций
- `DietaryRecipe` — рецепт с диетической категорией (веган, без глютена и т.д.)
- `ShoppingList` — список покупок с суммированием одинаковых ингредиентов

## Установка

```bash
git clone https://github.com/anastack/recipe-manager.git
cd recipe-manager
pip install -r requirements.txt
```

## Использование

Пример:

```python
from recipes import Ingredient, Recipe, ShoppingList

pizza = Recipe("Маргарита")
pizza.add_ingredient(Ingredient("Мука", 500, "г"))
pizza.add_ingredient(Ingredient("Сыр", 200, "г"))

shopping = ShoppingList()
shopping.add_recipe(pizza, portions=2)

for ingredient in shopping.get_list():
    print(ingredient)
```

Запуск тестов:

```bash
pytest
```


## Автор

Солодовникова Анастасия, группа ББИ-2502
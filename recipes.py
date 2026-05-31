from copy import deepcopy


class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str) -> None:
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self) -> float:
        return self._quantity

    @quantity.setter
    def quantity(self, val: float) -> None:
        val = float(val)
        if val <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = val

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self) -> str:
        return f"Ingredient({self.name!r}, {self.quantity}, {self.unit!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Ingredient):
            return NotImplemented
        return self.name == other.name and self.unit == other.unit
    



class Recipe:
    def __init__(self, title: str, ingredients: list = None) -> None:
        self.title = title
        if ingredients is None:
            ingredients = []
        self.ingredients = ingredients

    def add_ingredient(self, ingredient: "Ingredient") -> None:
        for ing in self.ingredients:
            if ing == ingredient:
                ing.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        if isinstance(ratio, bool):
            return False
        if not isinstance(ratio, (int, float)):
            return False
        return ratio > 0

    def scale(self, ratio: float) -> "Recipe":
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен быть положительным числом")
        new_ingredients = []
        for ing in self.ingredients:
            new_ing = deepcopy(ing)
            new_ing.quantity = new_ing.quantity*ratio
            new_ingredients.append(new_ing)
        return Recipe(self.title, new_ingredients)

    def __len__(self) -> int:
        return len(self.ingredients)

    def __str__(self) -> str:
        lines = [self.title+":"]
        for ing in self.ingredients:
            lines.append(f" - {ing}")
        return "\n".join(lines)
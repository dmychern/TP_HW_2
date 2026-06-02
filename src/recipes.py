
class Ingredient:
    def __init__(self, name: str, quantity: str, unit: str):
        self.name = name
        self.unit = unit
        self.quantity = quantity
    
    @property
    def quantity(self) -> float:
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        val = float(value)
        if val <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = val

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"
    
    def __repr__(self):
        return f"Ingridient('{self.name}', '{self.quantity}', '{self.unit}')"
    
    def __eq__(self, other):
        if isinstance(other, Ingredient):
            return self.name == other.name and self.unit == other.unit
        return False

class Recipe:
    def __init__(self, title: str, ingredients: list):
        self.title = title
        self.ingredients = []
        
        if ingredients:
            for item in ingredients:
                self.add_ingredient(item)

    def add_ingredient(self, ingredient):
        for existing in self.ingredients:
            if existing.name == ingredient.name and existing.unit == ingredient.unit:
                existing.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        if isinstance(ratio, (int, float)) and ratio > 0:
            return True
        return False
    
    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэффициент масштабирования должен быть положительным числом")
        
        scaled_ingredients = [
            Ingredient(item.name, item.quantity * ratio, item.unit)
            for item in self.ingredients
        ]

        return Recipe(self.title, scaled_ingredients)
    
    def __len__(self):
        return len(self.ingredients)
    
    def __str__(self):
        output = [f"Рецепт: {self.title}", "Ингредиенты:"]
        for item in self.ingredients:
            output.append(f" - {item}")
        return "\n".join(output)

    class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        
        scaled_recipe = recipe.scale(portions)

        for ingredient in scaled_recipe.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title: str):
        self._items = [item for item in self._items if item[1] != title]

    def get_list(self) -> list:
        summary = {}

        for ingredient, _ in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in summary:
                summary[key] += ingredient.quantity
            else:
                summary[key] = ingredient.quantity
        
        result = [Ingredient(name, quantity, unit) for (name, unit), quantity in summary.items()]

        result.sort(key=lambda x: x.name)
        return result
    
    def __add__(self, other):
        if isinstance(other, ShoppingList):
            new_list = ShoppingList()
            new_list._items = self._items + other._items
            return new_list
        raise TypeError("Складывать можно только объекты ShoppingList")

class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: list = None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type
    
    def scale(self, ratio: float):
        base_scaled = super().scale(ratio)
        return DietaryRecipe(base_scaled.title, self.diet_type, base_scaled.ingredients)
    
    def __str__(self):
        base_str = super().__str__()
        return base_str.replace("Рецепт:", f"[{self.diet_type}] Рецепт:")
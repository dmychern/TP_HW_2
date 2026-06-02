
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
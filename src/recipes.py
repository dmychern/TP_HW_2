
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
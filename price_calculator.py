class PriceCalculator:
    def calculate(self, age: int) -> int:
        if age < 0:
            raise ValueError("Åldern kan inte vara negativ.")

        if age < 13:
            result = 50
            
            return result

        if age < 65:
            result = 100
            
            return result

        
        result = 80
            
        return result
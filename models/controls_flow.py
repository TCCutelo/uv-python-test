"""
Model: Control Flow Operations
Contains business logic for Chapter 4 - conditionals, loops, functions
"""

class AgeClassifier:
    """Handle age classification logic"""
    
    @staticmethod
    def classify(age: int) -> dict:
        """
        Classify age into categories
        
        Args:
            age: Age to classify
            
        Returns:
            Dictionary with category and emoji
        """
        if age < 13:
            return {"category": "Child", "emoji": "👶", "color": "success"}
        elif age < 18:
            return {"category": "Teenager", "emoji": "🧑", "color": "info"}
        elif age < 65:
            return {"category": "Adult", "emoji": "👨", "color": "warning"}
        else:
            return {"category": "Senior", "emoji": "👴", "color": "error"}


class MultiplicationTable:
    """Generate multiplication tables"""
    
    @staticmethod
    def generate(number: int, up_to: int = 10) -> list:
        """
        Generate multiplication table
        
        Args:
            number: Number to multiply
            up_to: Maximum multiplier (default 10)
            
        Returns:
            List of tuples (multiplier, result)
        """
        return [(i, number * i) for i in range(1, up_to + 1)]
    
    @staticmethod
    def format_table(number: int, up_to: int = 10) -> list:
        """
        Generate formatted multiplication table strings
        
        Args:
            number: Number to multiply
            up_to: Maximum multiplier
            
        Returns:
            List of formatted strings
        """
        return [f"{number} × {i} = {number * i}" for i in range(1, up_to + 1)]


class HealthCalculator:
    """Calculate and classify health metrics"""
    
    @staticmethod
    def calculate_bmi(weight: float, height: float) -> float:
        """
        Calculate Body Mass Index
        
        Args:
            weight: Weight in kg
            height: Height in meters
            
        Returns:
            BMI value
        """
        if height <= 0:
            raise ValueError("Height must be positive")
        return weight / (height ** 2)
    
    @staticmethod
    def classify_bmi(bmi: float) -> dict:
        """
        Classify BMI into categories
        
        Args:
            bmi: BMI value
            
        Returns:
            Dictionary with category and color
        """
        if bmi < 18.5:
            return {"category": "Underweight", "color": "info"}
        elif bmi < 25:
            return {"category": "Normal weight", "color": "success"}
        elif bmi < 30:
            return {"category": "Overweight", "color": "warning"}
        else:
            return {"category": "Obesity", "color": "error"}


class FizzBuzz:
    """FizzBuzz game logic"""
    
    @staticmethod
    def generate(up_to: int = 30) -> list:
        """
        Generate FizzBuzz sequence
        
        Args:
            up_to: Maximum number
            
        Returns:
            List of FizzBuzz results
        """
        result = []
        for i in range(1, up_to + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result


class ControlFlowExamples:
    """Example code for control flow concepts"""
    
    @staticmethod
    def conditional_example() -> dict:
        """Return conditional logic example"""
        age = 25
        
        if age < 18:
            category = "Minor"
        elif age < 65:
            category = "Adult"
        else:
            category = "Senior"
        
        return {"age": age, "category": category}
    
    @staticmethod
    def for_loop_example() -> dict:
        """Return for loop example"""
        fruits = ["apple", "banana", "orange"]
        numbers = list(range(1, 6))
        
        return {"fruits": fruits, "numbers": numbers}
    
    @staticmethod
    def while_loop_example() -> list:
        """Return while loop example (countdown)"""
        counter = 5
        numbers = []
        
        while counter > 0:
            numbers.append(counter)
            counter -= 1
        
        return numbers
    
    @staticmethod
    def function_examples() -> dict:
        """Return function examples"""
        
        def greet(name: str) -> str:
            return f"Hello, {name}!"
        
        def calculate_rectangle_area(width: float, height: float) -> float:
            return width * height
        
        def power(base: float, exponent: float = 2) -> float:
            return base ** exponent
        
        return {
            'greeting': greet("Maria"),
            'area': calculate_rectangle_area(5, 3),
            'power_default': power(5),
            'power_custom': power(2, 3)
        }
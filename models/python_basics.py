"""
Model: Python Basics Operations
Contains business logic for Chapter 3 - numbers, strings, lists
"""

class NumberOperations:
    """Handle number operations and calculations"""
    
    @staticmethod
    def basic_operations(num1: float, num2: float) -> dict:
        """
        Perform basic arithmetic operations
        
        Args:
            num1: First number
            num2: Second number
            
        Returns:
            Dictionary with operation results
        """
        return {
            'sum': num1 + num2,
            'subtraction': num1 - num2,
            'multiplication': num1 * num2,
            'division': num1 / num2 if num2 != 0 else None,
            'integer_division': num1 // num2 if num2 != 0 else None,
            'remainder': num1 % num2 if num2 != 0 else None,
            'power': num1 ** num2
        }
    
    @staticmethod
    def get_examples() -> dict:
        """Return example number operations"""
        return {
            'sum': 10 + 5,
            'division': 10 / 3,
            'integer_division': 10 // 3,
            'remainder': 10 % 3,
            'power': 2 ** 3
        }


class StringOperations:
    """Handle string operations and manipulations"""
    
    @staticmethod
    def analyze_string(text: str) -> dict:
        """
        Analyze a string and return various properties
        
        Args:
            text: Input string to analyze
            
        Returns:
            Dictionary with string properties
        """
        return {
            'original': text,
            'uppercase': text.upper(),
            'lowercase': text.lower(),
            'length': len(text),
            'words': text.split(),
            'word_count': len(text.split()),
            'first_letter': text[0] if text else '',
            'last_letter': text[-1] if text else ''
        }
    
    @staticmethod
    def get_examples() -> dict:
        """Return example string operations"""
        name = "Python"
        version = "3.11"
        
        return {
            'concatenation': name + " " + version,
            'f_string': f"Learning {name} version {version}",
            'slicing': name[0:3],
            'uppercase': name.upper(),
            'lowercase': name.lower(),
            'length': len(name)
        }


class ListOperations:
    """Handle list operations and manipulations"""
    
    @staticmethod
    def create_movie_list() -> list:
        """Create example movie list"""
        return ["Inception", "Matrix", "Interstellar", "The Prestige", "Tenet"]
    
    @staticmethod
    def analyze_list(items: list) -> dict:
        """
        Analyze a list and return properties
        
        Args:
            items: List to analyze
            
        Returns:
            Dictionary with list properties
        """
        return {
            'items': items,
            'length': len(items),
            'first': items[0] if items else None,
            'last': items[-1] if items else None,
            'first_two': items[0:2] if len(items) >= 2 else items
        }
    
    @staticmethod
    def get_examples() -> dict:
        """Return example list operations"""
        numbers = [1, 2, 3, 4, 5]
        fruits = ["apple", "banana", "orange"]
        
        # Modify fruits (create a copy to not mutate original)
        fruits_modified = fruits.copy()
        fruits_modified.append("strawberry")
        
        return {
            'numbers': numbers,
            'fruits': fruits,
            'first_fruit': fruits[0],
            'last_fruit': fruits[-1],
            'modified_fruits': fruits_modified,
            'first_two_numbers': numbers[0:2]
        }
"""
Model: Data Structures Operations
Contains business logic for Chapter 5 - lists, dicts, sets, tuples, comprehensions
"""

class ListOperations:
    """Advanced list operations"""
    
    @staticmethod
    def get_example() -> dict:
        """Return example list operations"""
        numbers = [1, 2, 3, 4, 5]
        
        # Create a copy to demonstrate modifications
        modified = numbers.copy()
        modified.append(6)
        modified.insert(0, 0)
        modified.remove(3) if 3 in modified else None
        last = modified.pop() if modified else None
        
        return {
            'original': numbers,
            'modified': modified,
            'last_popped': last,
            'length': len(modified),
            'sum': sum(modified),
            'max': max(modified) if modified else None
        }


class DictionaryOperations:
    """Dictionary operations and management"""
    
    @staticmethod
    def create_user_example() -> dict:
        """Create example user dictionary"""
        return {
            'name': 'Maria Silva',
            'email': 'maria@email.com',
            'age': 28,
            'active': True
        }
    
    @staticmethod
    def get_user_info(user: dict) -> dict:
        """
        Get formatted user information
        
        Args:
            user: User dictionary
            
        Returns:
            Formatted user info
        """
        return {
            'display': f"{user.get('name', 'N/A')} ({user.get('age', 'N/A')} years)",
            'contact': user.get('email', 'N/A'),
            'status': 'Active' if user.get('active', False) else 'Inactive'
        }


class InventoryManager:
    """Manage inventory using dictionaries"""
    
    @staticmethod
    def create_default_inventory() -> dict:
        """Create default inventory"""
        return {
            'apples': 50,
            'bananas': 30,
            'oranges': 40
        }
    
    @staticmethod
    def add_product(inventory: dict, product: str, quantity: int) -> dict:
        """Add or update product in inventory"""
        inventory[product] = quantity
        return inventory
    
    @staticmethod
    def get_total_items(inventory: dict) -> int:
        """Calculate total items in inventory"""
        return sum(inventory.values())
    
    @staticmethod
    def format_inventory(inventory: dict) -> list:
        """Format inventory for display"""
        return [f"{product}: {qty} units" for product, qty in inventory.items()]


class ListComprehensions:
    """List comprehension examples and operations"""
    
    @staticmethod
    def generate_cubes(up_to: int = 10) -> list:
        """Generate list of cubes"""
        return [x**3 for x in range(1, up_to + 1)]
    
    @staticmethod
    def filter_divisible_by_3(up_to: int = 30) -> list:
        """Filter numbers divisible by 3"""
        return [x for x in range(1, up_to + 1) if x % 3 == 0]
    
    @staticmethod
    def celsius_to_fahrenheit(celsius_list: list) -> list:
        """Convert Celsius to Fahrenheit"""
        return [(c * 9/5) + 32 for c in celsius_list]
    
    @staticmethod
    def extract_initials(names: list) -> list:
        """Extract first letter from each name"""
        return [name[0] for name in names if name]
    
    @staticmethod
    def get_all_examples() -> dict:
        """Get all comprehension examples"""
        celsius = [0, 10, 20, 30, 40]
        names = ['Ana', 'Bruno', 'Carlos', 'Diana']
        
        return {
            'cubes': ListComprehensions.generate_cubes(10),
            'divisible_by_3': ListComprehensions.filter_divisible_by_3(30),
            'fahrenheit': ListComprehensions.celsius_to_fahrenheit(celsius),
            'initials': ListComprehensions.extract_initials(names),
            'squares_dict': {x: x**2 for x in range(5)}
        }


class SetOperations:
    """Set operations and examples"""
    
    @staticmethod
    def get_example_sets() -> dict:
        """Return example sets for operations"""
        return {
            'set_a': {1, 2, 3, 4, 5},
            'set_b': {4, 5, 6, 7, 8}
        }
    
    @staticmethod
    def perform_operations(set_a: set, set_b: set) -> dict:
        """
        Perform all set operations
        
        Args:
            set_a: First set
            set_b: Second set
            
        Returns:
            Dictionary with operation results
        """
        return {
            'union': set_a | set_b,
            'intersection': set_a & set_b,
            'difference_a_b': set_a - set_b,
            'difference_b_a': set_b - set_a,
            'symmetric_difference': set_a ^ set_b
        }
    
    @staticmethod
    def remove_duplicates(items: list) -> list:
        """Remove duplicates from list using set"""
        return list(set(items))


class SalesAnalyzer:
    """Analyze sales data"""
    
    @staticmethod
    def get_sample_sales() -> list:
        """Return sample sales data"""
        return [
            {'product': 'Laptop', 'price': 1200, 'quantity': 2},
            {'product': 'Mouse', 'price': 25, 'quantity': 5},
            {'product': 'Keyboard', 'price': 75, 'quantity': 3},
        ]
    
    @staticmethod
    def calculate_sale_total(sale: dict) -> float:
        """Calculate total for a single sale"""
        return sale['price'] * sale['quantity']
    
    @staticmethod
    def analyze_sales(sales: list) -> dict:
        """
        Analyze all sales data
        
        Args:
            sales: List of sale dictionaries
            
        Returns:
            Analysis results
        """
        totals = [SalesAnalyzer.calculate_sale_total(s) for s in sales]
        
        return {
            'individual_totals': totals,
            'total_revenue': sum(totals),
            'total_products': sum([s['quantity'] for s in sales]),
            'average_sale': sum(totals) / len(totals) if totals else 0
        }


class WordAnalyzer:
    """Analyze words and letter frequency"""
    
    @staticmethod
    def count_letters(words: list) -> dict:
        """
        Count letter frequency in words
        
        Args:
            words: List of words to analyze
            
        Returns:
            Dictionary with letter counts
        """
        text = ''.join(words).lower()
        count = {}
        
        for letter in text:
            count[letter] = count.get(letter, 0) + 1
        
        return count
    
    @staticmethod
    def get_top_letters(words: list, top_n: int = 5) -> list:
        """
        Get most common letters
        
        Args:
            words: List of words
            top_n: Number of top letters to return
            
        Returns:
            List of tuples (letter, count)
        """
        count = WordAnalyzer.count_letters(words)
        sorted_letters = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return sorted_letters[:top_n]
    
    @staticmethod
    def analyze(words: list) -> dict:
        """
        Complete word analysis
        
        Args:
            words: List of words
            
        Returns:
            Complete analysis dictionary
        """
        text = ''.join(words)
        
        return {
            'total_letters': len(text),
            'unique_letters': len(set(text.lower())),
            'letter_count': WordAnalyzer.count_letters(words),
            'top_5': WordAnalyzer.get_top_letters(words, 5)
        }
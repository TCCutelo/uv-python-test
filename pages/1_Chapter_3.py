import streamlit as st
from models.data_structures import (
    ListOperations,
    DictionaryOperations,
    InventoryManager,
    ListComprehensions,
    SetOperations,
    SalesAnalyzer,
    WordAnalyzer
)

st.set_page_config(page_title="Chapter 5 - Data Structures", page_icon="📄", layout="wide")

st.title("Chapter 5: Data Structures")

st.markdown("""
[Official Documentation](https://docs.python.org/3/tutorial/datastructures.html)
""")

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["Theory", "Examples", "Exercises"])

with tab1:
    st.header("Main Concepts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Lists")
        st.markdown("""
        **Ordered** and **mutable** collection:
```python
        list = [1, 2, 3, 4]
        list.append(5)      # add
        list.remove(2)      # remove
        list[0] = 10        # modify
```
        
        **Useful methods:**
        - `append()`, `extend()`, `insert()`
        - `remove()`, `pop()`, `clear()`
        - `sort()`, `reverse()`
        """)
        
        st.subheader("2. Tuples")
        st.markdown("""
        **Ordered** and **immutable** collection:
```python
        tuple = (1, 2, 3)
        # You cannot modify it!
```
        
        **When to use:**
        - Data that shouldn't change
        - Coordinates: `(x, y)`
        - Return multiple values
        """)
    
    with col2:
        st.subheader("3. Dictionaries")
        st.markdown("""
        **Key-value** pairs, **unordered**:
```python
        person = {
            'name': 'Ana',
            'age': 30,
            'city': 'Lisbon'
        }
        person['age'] = 31  # modify
```
        
        **Useful methods:**
        - `keys()`, `values()`, `items()`
        - `get()`, `pop()`, `update()`
        """)
        
        st.subheader("4. Sets")
        st.markdown("""
        **Unordered**, **no duplicates**:
```python
        set = {1, 2, 3, 3}
        # result: {1, 2, 3}
```
        
        **Operations:**
        - Union: `a | b`
        - Intersection: `a & b`
        - Difference: `a - b`
        """)
    
    st.markdown("---")
    
    st.subheader("5. List Comprehensions")
    st.markdown("""
    Elegant way to create lists:
```python
    # Traditional
    squares = []
    for x in range(10):
        squares.append(x**2)
    
    # List comprehension
    squares = [x**2 for x in range(10)]
    
    # With condition
    evens = [x for x in range(10) if x % 2 == 0]
```
    """)

with tab2:
    st.header("Practical Examples")
    
    st.subheader("Lists - Common Operations")
    
    # Get example from model
    list_ex = ListOperations.get_example()
    
    st.code(f"""
numbers = {list_ex['original']}

numbers.append(6)
numbers.insert(0, 0)
numbers.remove(3)
last = numbers.pop()

# Results:
modified = {list_ex['modified']}
last_popped = {list_ex['last_popped']}
length = {list_ex['length']}
sum = {list_ex['sum']}
max = {list_ex['max']}
""", language="python")
    
    st.markdown("---")
    
    st.subheader("Dictionaries - Data Management")
    
    # Get example from model
    user = DictionaryOperations.create_user_example()
    user_info = DictionaryOperations.get_user_info(user)
    
    st.code(f"""
user = {{
    'name': '{user['name']}',
    'email': '{user['email']}',
    'age': {user['age']},
    'active': {user['active']}
}}

# Access data
name = user['name']          # "{user['name']}"
email = user.get('email')    # "{user['email']}"

# Iterate
for key, value in user.items():
    print(f"{{key}}: {{value}}")
""", language="python")
    
    st.markdown("---")
    
    st.subheader("List Comprehensions")
    
    # Get all examples from model
    comp_examples = ListComprehensions.get_all_examples()
    
    st.code(f"""
# Squares
cubes = [x**3 for x in range(1, 11)]
# Result: {comp_examples['cubes']}

# Filter
divisible_by_3 = [x for x in range(1, 31) if x % 3 == 0]
# Result: {comp_examples['divisible_by_3']}

# Transform
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
# Result: {comp_examples['fahrenheit']}

# Extract
names = ['Ana', 'Bruno', 'Carlos', 'Diana']
initials = [name[0] for name in names]
# Result: {comp_examples['initials']}

# Dictionary comprehension
squares_dict = {{x: x**2 for x in range(5)}}
# Result: {comp_examples['squares_dict']}
""", language="python")
    
    st.markdown("---")
    
    st.subheader("Sets - Set Operations")
    
    # Get examples from model
    sets = SetOperations.get_example_sets()
    operations = SetOperations.perform_operations(sets['set_a'], sets['set_b'])
    
    st.code(f"""
a = {sets['set_a']}
b = {sets['set_b']}

# Operations
union = a | b              # {operations['union']}
intersection = a & b       # {operations['intersection']}
difference = a - b         # {operations['difference_a_b']}

# Remove duplicates
list_with_dupes = [1, 2, 2, 3, 3, 3, 4]
no_dupes = list(set(list_with_dupes))  # {SetOperations.remove_duplicates([1, 2, 2, 3, 3, 3, 4])}
""", language="python")

with tab3:
    st.header("Practical Exercises")
    
    st.subheader("Exercise 1: Inventory Management")
    
    st.markdown("Create a simple inventory system using dictionary:")
    
    st.code("""
inventory = {
    'apples': 50,
    'bananas': 30,
    'oranges': 40
}

# Add product
inventory['strawberries'] = 25

# Update quantity
inventory['apples'] = 45

# Remove sold out product
inventory.pop('bananas')

# Show inventory
for product, quantity in inventory.items():
    print(f"{product}: {quantity} units")

# Total products
total = sum(inventory.values())
print(f"\\nTotal items: {total}")
    """, language="python")
    
    with st.expander("Interactive Version"):
        # Initialize inventory in session state
        if 'inventory' not in st.session_state:
            st.session_state.inventory = InventoryManager.create_default_inventory()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Current Inventory:**")
            # Use model to format inventory
            for line in InventoryManager.format_inventory(st.session_state.inventory):
                st.write(f"- {line}")
            
            # Use model to calculate total
            total = InventoryManager.get_total_items(st.session_state.inventory)
            st.metric("Total", total)
        
        with col2:
            new_product = st.text_input("Add product:")
            new_qty = st.number_input("Quantity:", min_value=1, value=10)
            
            if st.button("Add"):
                # Use model to add product
                st.session_state.inventory = InventoryManager.add_product(
                    st.session_state.inventory,
                    new_product,
                    new_qty
                )
                st.rerun()
    
    st.markdown("---")
    
    st.subheader("Exercise 2: List Comprehensions")
    
    st.markdown("Practice list comprehensions:")
    
    st.code("""
# 1. Create list of first 10 cubes
cubes = [x**3 for x in range(1, 11)]

# 2. Filter numbers divisible by 3
divisible_by_3 = [x for x in range(1, 31) if x % 3 == 0]

# 3. Transform Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(c * 9/5) + 32 for c in celsius]

# 4. Extract first letters from names
names = ['Ana', 'Bruno', 'Carlos', 'Diana']
initials = [name[0] for name in names]
    """, language="python")
    
    with st.expander("See Results"):
        # Use model for all results
        st.write(f"**Cubes:** {ListComprehensions.generate_cubes(10)}")
        st.write(f"**Divisible by 3:** {ListComprehensions.filter_divisible_by_3(30)}")
        
        celsius = [0, 10, 20, 30, 40]
        st.write(f"**Fahrenheit:** {ListComprehensions.celsius_to_fahrenheit(celsius)}")
        
        names = ['Ana', 'Bruno', 'Carlos', 'Diana']
        st.write(f"**Initials:** {ListComprehensions.extract_initials(names)}")
    
    st.markdown("---")
    
    st.subheader("Exercise 3: Simple Data Analysis")
    
    st.markdown("Use dictionaries and lists to analyze sales:")
    
    st.code("""
sales = [
    {'product': 'Laptop', 'price': 1200, 'quantity': 2},
    {'product': 'Mouse', 'price': 25, 'quantity': 5},
    {'product': 'Keyboard', 'price': 75, 'quantity': 3},
]

# Calculate total for each sale
for sale in sales:
    total = sale['price'] * sale['quantity']
    print(f"{sale['product']}: €{total}")

# Total revenue
total_revenue = sum([s['price'] * s['quantity'] for s in sales])
print(f"\\nTotal Revenue: €{total_revenue}")

# Products sold
total_products = sum([s['quantity'] for s in sales])
print(f"Total products sold: {total_products}")
    """, language="python")
    
    with st.expander("Interactive Solution"):
        # Get sample sales from model
        sales = SalesAnalyzer.get_sample_sales()
        analysis = SalesAnalyzer.analyze_sales(sales)
        
        st.write("**Sales Details:**")
        for i, sale in enumerate(sales):
            total = analysis['individual_totals'][i]
            st.write(f"- {sale['product']}: €{sale['price']} × {sale['quantity']} = €{total}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Revenue", f"€{analysis['total_revenue']}")
        with col2:
            st.metric("Products Sold", analysis['total_products'])
    
    st.markdown("---")
    
    st.subheader("Final Challenge: Word Game")
    
    st.markdown("""
    Create a program that:
    1. Takes a list of words
    2. Counts how many times each letter appears
    3. Shows the 5 most common letters
    """)
    
    st.code("""
words = ['python', 'data', 'science', 'machine', 'learning']

# Join all words
text = ''.join(words)

# Count letters
count = {}
for letter in text:
    count[letter] = count.get(letter, 0) + 1

# Sort by frequency
sorted_letters = sorted(count.items(), key=lambda x: x[1], reverse=True)

# Top 5
for letter, freq in sorted_letters[:5]:
    print(f"{letter}: {freq}")
    """, language="python")
    
    with st.expander("Solution with Visualization"):
        words_input = st.text_input(
            "Enter words (comma-separated):",
            "python,data,science,machine,learning"
        )
        
        if st.button("Analyze"):
            words = words_input.split(',')
            
            # Use model for analysis
            top_letters = WordAnalyzer.get_top_letters(words, 5)
            
            st.write("**Top 5 Letters:**")
            for i, (letter, freq) in enumerate(top_letters, 1):
                st.write(f"{i}. '{letter}': {freq} times")
                st.progress(freq / top_letters[0][1] if top_letters else 0)

st.markdown("---")

st.success("Congratulations! You've completed the Python fundamentals review!")

st.info("""
**Next Steps:**
1. Practice these exercises in your editor
2. Combine lists, dictionaries and functions in small projects
3. Start **Hands-On Machine Learning** - Chapter 2!
""")

# Navigation
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.page_link("pages/2_Chapter_4.py", label="← Previous")
with col3:
    st.page_link("main.py", label="Home")
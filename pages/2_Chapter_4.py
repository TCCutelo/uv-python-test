import streamlit as st
from models.controls_flow import (
    AgeClassifier,
    MultiplicationTable,
    HealthCalculator,
    FizzBuzz,
    ControlFlowExamples
)

st.set_page_config(page_title="Chapter 4 - Control Flow", page_icon="📄", layout="wide")

st.title("Chapter 4: More Control Flow Tools")

st.markdown("""
[Official Documentation](https://docs.python.org/3/tutorial/controlflow.html)
""")

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["Theory", "Examples", "Exercises"])

with tab1:
    st.header("Main Concepts")
    
    st.subheader("1. Conditionals (if/elif/else)")
    st.markdown("""
    Make decisions in your code:
    ```python
    if condition:
        # do something
    elif another_condition:
        # do something else
    else:
        # otherwise
    ```
    """)
    
    st.subheader("2. For Loop")
    st.markdown("""
    Iterate over sequences:
    ```python
    for item in list:
        print(item)
    
    for i in range(5):  # 0, 1, 2, 3, 4
        print(i)
    ```
    """)
    
    st.subheader("3. While Loop")
    st.markdown("""
    Repeat while condition is true:
    ```python
    counter = 0
    while counter < 5:
        print(counter)
        counter += 1
    ```
    """)
    
    st.subheader("4. Functions (def)")
    st.markdown("""
    Create reusable blocks of code:
    ```python
    def function_name(param1, param2):
        result = param1 + param2
        return result
    
    # Use the function
    total = function_name(5, 3)
    ```
    """)

with tab2:
    st.header("Practical Examples")
    
    st.subheader("Conditionals (if/elif/else)")
    
    # Get example from model
    conditional_ex = ControlFlowExamples.conditional_example()
    
    st.code(f"""
age = {conditional_ex['age']}

if age < 18:
    category = "Minor"
elif age < 65:
    category = "Adult"
else:
    category = "Senior"

# Result: category = "{conditional_ex['category']}"
""", language="python")
    
    st.markdown("---")
    
    st.subheader("For Loop")
    
    # Get examples from model
    loop_ex = ControlFlowExamples.for_loop_example()
    
    st.code(f"""
# Iterate over list
fruits = {loop_ex['fruits']}

for fruit in fruits:
    print(f"- {{fruit}}")

# Range
for i in range(1, 6):
    print(f"Number {{i}}")

# Result: {loop_ex['numbers']}
""", language="python")
    
    st.markdown("---")
    
    st.subheader("While Loop")
    
    # Get example from model
    while_ex = ControlFlowExamples.while_loop_example()
    
    st.code(f"""
counter = 5
numbers = []

while counter > 0:
    numbers.append(counter)
    counter -= 1

# Result: numbers = {while_ex}
""", language="python")
    
    st.markdown("---")
    
    st.subheader("Functions")
    
    # Get examples from model
    func_ex = ControlFlowExamples.function_examples()
    
    st.code(f"""
def greet(name):
    return f"Hello, {{name}}!"

def calculate_rectangle_area(width, height):
    return width * height

def power(base, exponent=2):
    return base ** exponent

# Results:
greeting = greet("Maria")              # "{func_ex['greeting']}"
area = calculate_rectangle_area(5, 3)  # {func_ex['area']}
power_default = power(5)               # {func_ex['power_default']}
power_custom = power(2, 3)             # {func_ex['power_custom']}
""", language="python")

with tab3:
    st.header("Practical Exercises")
    
    st.subheader("Exercise 1: Age Classifier")
    age_input = st.number_input("Enter an age:", min_value=0, max_value=120, value=25)
    
    if st.button("Classify"):
        # Use model for classification
        result = AgeClassifier.classify(age_input)
        
        # Display with appropriate color
        message = f"{result['emoji']} {result['category']}"
        
        if result['color'] == 'success':
            st.success(message)
        elif result['color'] == 'info':
            st.info(message)
        elif result['color'] == 'warning':
            st.warning(message)
        else:
            st.error(message)
    
    st.markdown("---")
    
    st.subheader("Exercise 2: Multiplication Table")
    number = st.selectbox("Choose a number:", range(1, 11))
    
    if st.button("Show Table"):
        # Use model to generate table
        table = MultiplicationTable.format_table(number)
        
        st.write(f"**Multiplication table of {number}:**")
        for line in table:
            st.write(line)
    
    st.markdown("---")
    
    st.subheader("Exercise 3: Create a Function")
    
    st.markdown("Try creating this function in your editor:")
    st.code("""
def calculate_bmi(weight, height):
    \"\"\"
    Calculate Body Mass Index
    weight: in kg
    height: in meters
    \"\"\"
    bmi = weight / (height ** 2)
    return bmi

# Test it
my_bmi = calculate_bmi(70, 1.75)
print(f"BMI: {my_bmi:.2f}")

# Add classification
if my_bmi < 18.5:
    print("Underweight")
elif my_bmi < 25:
    print("Normal weight")
elif my_bmi < 30:
    print("Overweight")
else:
    print("Obesity")
    """, language="python")
    
    with st.expander("Interactive Solution"):
        col1, col2 = st.columns(2)
        with col1:
            weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
        with col2:
            height = st.number_input("Height (m)", min_value=1.0, max_value=2.5, value=1.75)
        
        if st.button("Calculate BMI"):
            try:
                # Use model for calculation and classification
                bmi = HealthCalculator.calculate_bmi(weight, height)
                classification = HealthCalculator.classify_bmi(bmi)
                
                st.metric("BMI", f"{bmi:.1f}")
                
                # Display with appropriate color
                if classification['color'] == 'success':
                    st.success(classification['category'])
                elif classification['color'] == 'info':
                    st.info(classification['category'])
                elif classification['color'] == 'warning':
                    st.warning(classification['category'])
                else:
                    st.error(classification['category'])
            except ValueError as e:
                st.error(str(e))
    
    st.markdown("---")
    
    st.subheader("Exercise 4: FizzBuzz (Classic!)")
    st.markdown("""
    Challenge: Print numbers from 1 to 30, but:
    - If divisible by 3: print "Fizz"
    - If divisible by 5: print "Buzz"
    - If divisible by both: print "FizzBuzz"
    """)
    
    st.code("""
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    """, language="python")
    
    with st.expander("See Result"):
        # Use model to generate FizzBuzz
        result = FizzBuzz.generate(30)
        st.write(", ".join(result))

st.markdown("---")

# Navigation
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.page_link("pages/1_Chapter_3.py", label="← Previous")
with col3:
    st.page_link("pages/3_Chapter_5.py", label="Next →")
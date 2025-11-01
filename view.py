import streamlit as st

def main():
    st.set_page_config(
        page_title="Python Basics Recap",
        page_icon="📄",  # Só este fica (ícone da aba do browser - não aparece na página)
        layout="wide"
    )
    
    # Main title
    st.title("Python Basics - Recap")
    st.markdown("---")
    
    # Introduction
    st.markdown("""
    ## Welcome to your Python notebook
    
    This project is an interactive guide to review **Python fundamentals** 
    before diving into the "Hands-On Machine Learning" book.
    
    ### Objective
    Quickly review essential concepts from the official Python documentation 
    to be prepared for Machine Learning projects.
    """)
    
    # Course structure
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Available Chapters
        
        Use the sidebar to navigate between chapters:
        
        1. **Chapter 3** - Informal Introduction
           - Numbers, strings, lists
           - Basic operations
           
        2. **Chapter 4** - Control Flow
           - if, for, while
           - Functions (def)
           
        3. **Chapter 5** - Data Structures
           - Lists, tuples, dictionaries
           - List comprehensions
        """)
    
    with col2:
        st.markdown("""
        ### Suggested Study Plan
        
        - **Day 1-2**: Chapter 3 (basics)
        - **Day 3-4**: Chapter 4 (control flow)
        - **Day 5**: Chapter 5 (data structures)
        - **Day 6-7**: Free practice
        
        ### Useful Links
        
        - [Official Python Documentation](https://docs.python.org/3/tutorial/)
        - [Hands-On ML GitHub](https://github.com/ageron/handson-ml3)
        - [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
        """)
    
    st.markdown("---")
    
    # Progress
    st.markdown("### Your Progress")
    
    progress_col1, progress_col2, progress_col3 = st.columns(3)
    
    with progress_col1:
        st.metric("Chapters", "0/3", "Start now")
    with progress_col2:
        st.metric("Exercises", "0/15", "")
    with progress_col3:
        st.metric("Estimated Time", "3-4h", "")
    
    # Call to action
    st.info("Start now! Select Chapter 3 in the sidebar to begin your review.")
import streamlit as st

def main():
    st.title('Simple Calculator')
    
    # Get user input for two numbers
    num1 = st.number_input('Enter the first number:')
    num2 = st.number_input('Enter the second number:')
    
    # Calculate the sum
    result = num1 + num2
    
    # Display the result
    st.write(f'The sum of {num1} and {num2} is {result}')

if __name__ == '__main__':
    main()

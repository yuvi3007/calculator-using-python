# calculator_app.py

import streamlit as st

st.title("🧮 Python Calculator")

operator = st.selectbox("Choose an operator", ["+", "-", "*", "/"])
num1 = st.number_input("Enter the 1st number")
num2 = st.number_input("Enter the 2nd number")

if st.button("Calculate"):
    if operator == "+":
        result = round(num1 + num2, 2)
        st.success(f"Result: {result}")
    elif operator == "-":
        result = round(num1 - num2, 2)
        st.success(f"Result: {result}")
    elif operator == "*":
        result = round(num1 * num2, 2)
        st.success(f"Result: {result}")
    elif operator == "/":
        if num2 != 0:
            result = round(num1 / num2, 2)
            st.success(f"Result: {result}")
        else:
            st.error("❌ Division by zero is not allowed!")
    else:
        st.error(f"{operator} is not a valid operator")
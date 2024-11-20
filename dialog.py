import streamlit as st


@st.dialog("Weight less than 10 grams")
def ten_below():
    st.warning("Any jewelry piece less than 10 grams is sold at \"PIECE PRICE\".")
    st.info("Please talk with the Manager before proceeding.")


@st.dialog("No Response from kitco.com")
def kitco_down():
    st.warning("Kitco.com is not responding. Unable to fetch gold prices.")


@st.dialog("Unable to Calculate")
def no_calc():
    st.warning("Price Per Carat and the Profit Margin is exceeding predefined limits.")
    st.info("Please ask the manager for the breakdown.")


@st.dialog("Invalid Input")
def invalid_input():
    st.error("Please enter a valid Numeric Value")
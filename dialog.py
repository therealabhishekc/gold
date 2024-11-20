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


@st.dialog("How to use?", width='large')
def dialog_scrap_gold():
    st.write("to be updated sg")


@st.dialog("How to use?", width='large')
def dialog_gold_bd():
    st.write("to be updated gbd")


@st.dialog("How to use?", width='large')
def dialog_hyd_bd():
    st.write("to be updated hbd")


@st.dialog("How to use?", width='large')
def dialog_ant_bd():
    st.write("to be updated abd")


@st.dialog("How to use?", width='large')
def dialog_dia_bd():
    st.write("to be updated dbd")
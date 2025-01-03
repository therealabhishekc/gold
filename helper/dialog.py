import streamlit as st


@st.dialog("Weight less than 10 grams")
def ten_below():
    st.warning("Any jewelry piece less than 10 grams is sold at \"PIECE PRICE\".")
    st.warning("The labor and margin would be higher than usual.")


@st.dialog("No Response")
def kitco_down():
    st.error("Kitco.com is not responding. Unable to fetch gold prices.")


@st.dialog("Unable to Calculate")
def no_calc():
    st.error("The Price Per Carat OR the Profit Margin is exceeding predefined limits.")
    st.info("Please ask the manager for the breakdown.")


@st.dialog("Invalid Input")
def invalid_input():
    st.error("Please enter a valid Numeric Value")


@st.dialog("Missing Value")
def missing_value():
    st.error("Please enter all the details before generating the report.")


@st.dialog("About | Scrap Gold Purchase", width='large')
def dialog_scrap_gold():
    st.write("This page calculates the Cash value and the Trade-in value for Gold.")

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Key Points to Remember:")
    st.markdown("""
            - Understand the customer's intent with the gold they are bringing (e.g., to sell, trade, or estimate).
            - Verify the Gold Karat by consulting one of **Yogesh**, **Pradip**, or **Himesh**.
            - At the same time, determine the selections for `Refinery Cost` and `Gold Calculation`.
            - If the jewelry includes gems, ask how much weight should be subtracted from the `Gross Weight` and record it 
                in the `Reduction` section.
        """)

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Field Descriptions")
    st.markdown("#### Global Settings")
    st.markdown('''
            - `Refinery Cost`: Option to include or exclude the refinery cost.
                - **Include**: A refinery cost of \$4.5 for trade-in and \$5.5 for cash value will be deducted per gram.
                - **Exclude**: No deductions will be applied.
            - `Gold Calculation`: Method of calculating the price per gram.
                - **0.916**: The 24k gold price per gram is multiplied by 0.916 for calculations.
                - **0.80**: The 24k gold price per gram is multiplied by 0.80 for calculations.
        ''')
    st.info("Note: The above global settings apply to all items.")

    st.markdown("#### Item-Specific Fields")
    st.markdown('''
            - `Description` [text]: _Optional_. A brief one or two-word description of the jewelry item.
            - `Gross Weight` [number]: _Required_. The total weight of the jewelry item as measured on a scale.
            - `Reduction` [number]: _Required_. The weight of the gems and other stones in the jewelry.
            - `Gold Karat` [selection]: _Required_. Select the gold karat from options: 10K, 14K, 18K, 21K, 22K, or 24K.
                Note: To get both cash and trade-in value for 24K gold, make sure to include the refinery cost.
        ''')

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)
    
    st.markdown("## Action Buttons")
    st.markdown('''
            - `+ Add Items`: Add a new item with all the above four fields.
            - `Generate`: A button to generate the report. Ensure that all required fields are filled before generating the report.
            - `View Report`: This button appears after the report is generated. Clicking it opens the report in a new tab.
            - `Download Report`: Allows downloading the generated report in PDF format. Be sure to download the report for printing.
        ''')

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Error Messages")
    st.markdown("- **Invalid Input**: Appears when an invalid value is entered into a numerical field.")
    _, img1, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img1:
        st.image("images/invalid_input.png")
    st.markdown("- **No Response**: Appears when kitco.com is offline.")
    _, img2, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img2:
        st.image("images/iresponse_no.png")

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Contact Information")
    st.markdown("Developer: abskchsk@gmail.com")


@st.dialog("About | Gold Jewelry Breakdown", width='large')
def dialog_gold_bd():
    st.write("This page calculates the detailed breakdown for plain gold jewelry without any gem stones.")
    st.info("Note: For any Hyderabadi or Antique jewelry without any gem stones, use Gold Jewelry Breakdown \
             to generate the report.")

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Field Descriptions")
    st.markdown('''
            - `Show Percentages` [checkbox]: _Required_. Displays the percentages for labor, margin, and duty when selected.
            - `Item Code` [text]: _Optional_. The item code as given on the tag.
            - `Price` [number]: _Required_. The final price from the iPad.
            - `Gross Weight` [number]: _Required_. The total weight of the jewelry piece.
        ''')
    
    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Action Buttons")
    st.markdown('''
            - `Generate`: A button to generate the report. Ensure that all required fields are filled before generating the report.
            - `View Report`: This button appears after the report is generated. Clicking it opens the report in a new tab.
            - `Download Report`: Allows downloading the generated report in PDF format. Be sure to download the report for printing.
        ''')
    
    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Warning Messages")
    
    st.markdown("- **Weight less than 10 grams**: Appears when the jewelry’s gross weight is under 10 grams. \
                 This warning ensures the salesperson is aware of higher labor and margin costs.")
    _, img0, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img0:
        st.image("images/less_than_10.png")

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Error Messages")
    
    st.markdown("- **Invalid Input**: Appears when an invalid value is entered into a numerical field.")
    _, img1, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img1:
        st.image("images/invalid_input.png")

    st.markdown("- **Misssing Value**: Appears when a required field is not filled out before generating the report.")
    _, img1, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img1:
        st.image("images/missing_val.png")
    
    st.markdown("- **No Response**: Appears when kitco.com is offline.")
    _, img2, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img2:
        st.image("images/iresponse_no.png")
    
    # st.markdown("- **Unable to Calculate**: Appears when the algorithm fails to compute the margin and \
    #             stone price due to predefined limits in the algorithm.")
    # _, img3, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    # with img3:
    #     st.image("images\calc_no.png")

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Contact Information")
    st.markdown("Developer: abskchsk@gmail.com")


@st.dialog("About | Hyderabadi Breakdown", width='large')
def dialog_hyd_bd():
    st.write("This page calculates the detailed breakdown for Hyderabadi Jewelry.")
    st.info("Note: Use Gold Breakdown for any hyderabadi jewelry without any gems.")

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Field Descriptions")
    
    st.markdown('''
            - `Show Percentages` [checkbox]: _Required_. Displays the percentages for labor, margin, and duty when selected.
            - `Item Code` [text]: _Optional_. The unique identifier as displayed on the tag. Providing \
                the item code secures consistency in labor-profit distribution and gemstone pricing \
                for each version.
            - `Price` [number]: _Required_. The final price from the iPad.
            - `Gross Weight` [number]: _Required_. The total weight of the jewelry piece.
        ''')
    
    st.markdown("#### Gem Stones Fields")

    st.markdown('''
            - `Gem Stone` [selection]: _Required_. Choose a gem stone from the dropdown menu.
            - `Gem Stone Carat` [number]: _Required_. Enter the carat weight of the selected gem stone.
        ''')

    st.info("Note: If a gem stone is not available in the dropdown, select 'Other/All stones' and proceed.")

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Action Buttons")
    st.markdown('''
            - `+ Add Gems`: Add a new gem stone with all the above two fields.
            - `Generate`: A button to generate the report. Ensure that all required fields are filled before generating the report.
            - `View Report`: This button appears after the report is generated. Clicking it opens the report in a new tab.
            - `Download Report`: Allows downloading the generated report in PDF format. Be sure to download the report for printing.
        ''')

    st.info("Note: Avoid generating the report if any `Gem Stone Carat` value is set to zero, as this will result in an error.")
                                                                        
    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Warning Messages")
    
    st.markdown("- **Weight less than 10 grams**: Appears when the jewelry’s gross weight is under 10 grams. \
                 This warning ensures the salesperson is aware of higher labor and margin costs.")
    _, img0, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img0:
        st.image("images/less_than_10.png")

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Error Messages")
    
    st.markdown("- **Invalid Input**: Appears when an invalid value is entered into a numerical field.")
    _, img1, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img1:
        st.image("images/invalid_input.png")

    st.markdown("- **Misssing Value**: Appears when a required field is not filled out before generating the report.")
    _, img1, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img1:
        st.image("images/missing_val.png")
    
    st.markdown("- **No Response**: Appears when kitco.com is offline.")
    _, img2, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img2:
        st.image("images/iresponse_no.png")
    
    st.markdown("- **Unable to Calculate**: Appears when the algorithm fails to compute the margin and \
                stone price due to predefined limits in the algorithm.")
    _, img3, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img3:
        st.image("images/calc_no.png")

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Contact Information")
    st.markdown("Developer: abskchsk@gmail.com")


@st.dialog("About | Antique Breakdown", width='large')
def dialog_ant_bd():
    st.write("This page calculates the detailed breakdown for Antique Jewelry.")
    st.info("Note: Use Gold Breakdown for any antique jewelry without any gems.")

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Field Descriptions")
    
    st.markdown('''
            - `Show Percentages` [checkbox]: _Required_. Displays the percentages for labor, margin, and duty when selected.
            - `Item Code` [text]: _Optional_. The unique identifier as displayed on the tag. Providing \
                the item code secures consistency in labor-profit distribution and gemstone pricing \
                for each version.
            - `Price` [number]: _Required_. The final price from the iPad. The pricing for antique jewelry \
                featuring Polki diamonds follows a different method. If you're unsure how to determine \
                the price, seek guidance.
            - `Gross Weight` [number]: _Required_. The total weight of the jewelry piece.
        ''')
    
    st.markdown("#### Gem Stones Fields")

    st.markdown('''
            - `Gem Stone` [selection]: _Required_. Choose a gem stone from the dropdown menu.
            - `Gem Stone Carat` [number]: _Required_. Enter the carat weight of the selected gem stone.
        ''')

    st.info("Note: If a gem stone is not available in the dropdown, select 'Other/All stones' and proceed.")

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Action Buttons")
    st.markdown('''
            - `+ Add Gems`: Add a new gem stone with all the above two fields.
            - `Generate`: A button to generate the report. Ensure that all required fields are filled before generating the report.
            - `View Report`: This button appears after the report is generated. Clicking it opens the report in a new tab.
            - `Download Report`: Allows downloading the generated report in PDF format. Be sure to download the report for printing.
        ''')

    st.info("Note: Avoid generating the report if any `Gem Stone Carat` value is set to zero, as this will result in an error.")

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Warning Messages")
    
    st.markdown("- **Weight less than 10 grams**: Appears when the jewelry’s gross weight is under 10 grams. \
                 This warning ensures the salesperson is aware of higher labor and margin costs.")
    _, img0, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img0:
        st.image("images/less_than_10.png")

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Error Messages")
    
    st.markdown("- **Invalid Input**: Appears when an invalid value is entered into a numerical field.")
    _, img1, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img1:
        st.image("images/invalid_input.png")

    st.markdown("- **Misssing Value**: Appears when a required field is not filled out before generating the report.")
    _, img1, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img1:
        st.image("images/missing_val.png")
    
    st.markdown("- **No Response**: Appears when kitco.com is offline.")
    _, img2, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img2:
        st.image("images/iresponse_no.png")
    
    st.markdown("- **Unable to Calculate**: Appears when the algorithm fails to compute the margin and \
                stone price due to predefined limits in the algorithm.")
    _, img3, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img3:
        st.image("images/calc_no.png")

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Contact Information")
    st.markdown("Developer: abskchsk@gmail.com")


@st.dialog("About | Diamond Breakdown", width='large')
def dialog_dia_bd():
    st.write("This page calculates the detailed breakdown for Diamond Jewelry.")

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Field Descriptions")
    
    st.markdown('''
            - `Show Percentages` [checkbox]: _Required_. Displays the percentages for labor, margin, and duty when selected.
            - `Diamond Price Per Carat` [slider]: _Required_. The estimated diamond price per carat for the \
                given jewelry. Ask one of the managers to figure out the right price. Defaults to $795.
            - `Item Code` [text]: _Optional_. The unique identifier as displayed on the tag. Providing \
                the item code secures consistency in labor-profit distribution and gemstone pricing \
                for each version.
            - `Price` [number]: _Required_. The final price from the iPad. The pricing for antique jewelry \
                featuring Polki diamonds follows a different method. If you're unsure how to determine \
                the price, seek guidance.
            - `Gross Weight` [number]: _Required_. The total weight of the jewelry piece.
            - `Diamond Carat Weight` [number]: _Required_. The total diamond carat weight in the jewelry piece.
        ''')
    
    st.markdown("#### Gem Stones Fields")

    st.markdown('''
            - `Gem Stone` [selection]: _Required_. Choose a gem stone from the dropdown menu.
            - `Gem Stone Carat` [number]: _Required_. Enter the carat weight of the selected gem stone.
        ''')

    st.info("Note: If a gem stone is not available in the dropdown, select 'Other/All stones-D' and proceed.")

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Action Buttons")
    st.markdown('''
            - `+ Add Gems`: Add a new gem stone with all the above two fields.
            - `Generate`: A button to generate the report. Ensure that all required fields are filled before generating the report.
            - `View Report`: This button appears after the report is generated. Clicking it opens the report in a new tab.
            - `Download Report`: Allows downloading the generated report in PDF format. Be sure to download the report for printing.
        ''')

    st.info("Note: Avoid generating the report if any `Gem Stone Carat` value is set to zero, as this will result in an error.")

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Warning Messages")
    
    st.markdown("- **Weight less than 10 grams**: Appears when the jewelry’s gross weight is under 10 grams. \
                 This warning ensures the salesperson is aware of higher labor and margin costs.")
    _, img0, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img0:
        st.image("images/less_than_10.png")

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Error Messages")
    
    st.markdown("- **Invalid Input**: Appears when an invalid value is entered into a numerical field.")
    _, img1, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img1:
        st.image("images/invalid_input.png")

    st.markdown("- **Misssing Value**: Appears when a required field is not filled out before generating the report.")
    _, img1, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img1:
        st.image("images/missing_val.png")
    
    st.markdown("- **No Response**: Appears when kitco.com is offline.")
    _, img2, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img2:
        st.image("images/iresponse_no.png")
    
    st.markdown("- **Unable to Calculate**: Appears when the algorithm fails to compute the margin and \
                stone price due to predefined limits in the algorithm.")
    _, img3, _ = st.columns([1, 2, 1], vertical_alignment="bottom")
    with img3:
        st.image("images/calc_no.png")

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    st.markdown("## Contact Information")
    st.markdown("Developer: abskchsk@gmail.com")

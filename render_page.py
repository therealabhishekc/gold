import streamlit as st
from generate_pdf import sample_pdf, pdf_scrap_gold, pdf_gold_bd, pdf_hyd_bd, pdf_ant_bd
from streamlit_extras.stylable_container import stylable_container

@st.dialog("Weight less than 10 grams")
def ten_below():
    st.error("Any jewellery piece less than 10 grams is sold at \"PIECE PRICE\",")
    st.warning("Please enter a jewellery weight of more than 10 grams to continue.")


# on_change callback
def on_change1():
    pass


# Function to add widgets
def add_widgets(var):
    if var == 'scrap_gold':
        st.session_state['widget_count'] += 1
        st.session_state['widget_data'].append({
            'desc': '',
            'gold_wt': 0.0,
            'gold_kt': '10K',
            'gold_pur_place' : "Govindji's"
        })
    elif var == 'hyd':
        st.session_state['hyd_stones_count'] += 1
        st.session_state['hyd_stones_data'].append({
            'hyd_stone': 'Ruby',
            'hyd_ct': 0.0
        })
    elif var == 'ant':
        st.session_state['ant_stones_count'] += 1
        st.session_state['ant_stones_data'].append({
            'ant_stone': 'Polki Diamond',
            'ant_ct': 0.0
        })
    elif var == 'dia':
        pass


# Function to delete a widget
def delete_widget(index, var):
    if var == 'scrap_gold':
        if st.session_state['widget_count'] > 1:  # Ensure at least one widget remains
            st.session_state['widget_count'] -= 1
            st.session_state['widget_data'].pop(index)
    elif var == 'hyd':
        if st.session_state['hyd_stones_count'] > 1:
            st.session_state['hyd_stones_count'] -= 1
            st.session_state['hyd_stones_data'].pop(index)
    elif var == 'ant':
        if st.session_state['ant_stones_count'] > 1:
            st.session_state['ant_stones_count'] -= 1
            st.session_state['ant_stones_data'].pop(index)
    elif var == 'dia':
        if st.session_state['hyd_stones_count'] > 1:
            st.session_state['hyd_stones_count'] -= 1
            st.session_state['hyd_stones_data'].pop(index)


def render_gold_scrap():
    
    # Initialize session state for tracking the widgets and their values
    if 'widget_count' not in st.session_state:
        st.session_state['widget_count'] = 1  # Start with at least one widget
    if 'widget_data' not in st.session_state:
        st.session_state['widget_data'] = [{
            'desc': '',
            'gold_wt': 0.0,
            'gold_kt': '10K',
            'gold_pur_place' : "Govindji's"
        }]  # Start with initial data for one widget
    if 'show_calc' not in st.session_state:
        st.session_state['show_calc'] = False
    
    colm1, colm2= st.columns([3, 3], vertical_alignment="bottom")
    with colm1: 
        st.write("### Scrap Gold Purchase")
    with colm2:
        st.session_state['show_calc'] = st.checkbox("Show Formula",
                                                    value=st.session_state['show_calc'])

    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

    # Display and update the widgets
    for i in range(st.session_state['widget_count']):
        # st.write(f"##### Item {i+1}")
        # Use columns to place text inputs side by side
        with stylable_container(
                    key=f'delete_{i}',
                    css_styles="""
                        button{
                            background: linear-gradient(to left, #FF0000, #FF2C2C);
                            color: white;
                            border-radius: 7px;
                            height: 35px !important;
                            min-height: 30px !important;
                            max-height: 30px !important;
                        }
                        """
                ):
            col1, col2= st.columns([3, 3])
            with col1:
                st.write(f"##### Item {i+1}")
            
            with col2:
                if st.session_state['widget_count'] > 1:
                    if st.button(f"Delete", 
                                 key=f'delete_{i}'):
                        delete_widget(i, 'scrap_gold')
                        st.rerun()

        # Use columns to place text inputs side by side
        col1, col2, col3, col4 = st.columns([4,4,4,4], 
                                            vertical_alignment="bottom")
        # description box
        with col1:
            desc = st.text_input("Description",
                                value=st.session_state['widget_data'][i]['desc'],
                                key=f'desc_{i}')
            st.session_state['widget_data'][i]['desc'] = desc

        # gold weight box
        with col2:
            gold_wt = st.number_input("Gold Weight in grams",
                                      value=st.session_state['widget_data'][i]['gold_wt'],
                                      key=f'gold_wt_{i}',
                                      min_value=0.0)
            st.session_state['widget_data'][i]['gold_wt'] = gold_wt

        # gold karat dropdown
        with col3:
            gold_kt = st.selectbox("Select Gold Karat", 
                                options = ["10K", "14K", "18K", "21K", "22K", "24K"],
                                index = ["10K", "14K", "18K", "21K", "22K", "24K"].index(st.session_state['widget_data'][i]['gold_kt']),
                                key = f'gold_kt_{i}')
            st.session_state['widget_data'][i]['gold_kt'] = gold_kt

        # jewellery purchase dropdown
        with col4:
            gold_pur_place = st.selectbox("Gold Purchased at?", 
                                        options = ["Govindji's", "Other jeweller"],
                                        index = ["Govindji's", "Other jeweller"].index(st.session_state['widget_data'][i]['gold_pur_place']),
                                        key = f'gold_pur_place_{i}')
            st.session_state['widget_data'][i]['gold_pur_place'] = gold_pur_place


        # Divider
        st.markdown("<hr style='margin: 20px 0;'>", unsafe_allow_html=True)            

    # Button to trigger adding of widgets
    with stylable_container(
                    key='add',
                    css_styles="""
                        button{
                            background: linear-gradient(to right, #434343 , #000000 );;
                            color: white;
                            border-radius: 7px;
                            height: 50px !important;
                            min-height: 35px !important;
                            max-height: 35px !important;
                            width: 100%;
                        }
                        """
                ):
            _, col, _ = st.columns([2, 1.2, 2])
            with col:
                with stylable_container(
                    key="container_with_border",
                    css_styles=r"""
                        button p:before {
                            font-family: 'Font Awesome 5 Free';
                            content: '\2b';  /* Plus sign */
                            display: inline-block;
                            padding-right: 10px;
                            vertical-align: top;
                        }
                        """,
                ):
                    if st.button("Add Items", 
                                 key="add"):
                        add_widgets('scrap_gold')
                        st.rerun()

    view_pdf = False

    # Generate button 
    with stylable_container(
            key='generate',
            css_styles="""
                button{
                    background: linear-gradient(to right, #005C97 , #363795 );
                    color: white;
                    border-radius: 7px;
                    height: 50px !important;
                    min-height: 35px !important;
                    max-height: 35px !important;
                }
                """
        ):
        if st.button("Generate", key="generate"):
            pdf_scrap_gold(st.session_state['widget_data'], 
                           st.session_state['show_calc'])
            view_pdf = True
    return view_pdf
         

def render_gold_breakdown():
    st.write("#### Gold Jewellery Breakdown")
    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

    col1, col2, col3 = st.columns(3)

    with col1:
        item_code_g = st.text_input("Item code")
    
    with col2:
        price_g = st.number_input("Price",
                                min_value=0)

    with col3:
        gold_wt_g = st.number_input("Gross Gold Weight in grams",
                                  min_value=0.0)

    view_pdf = False

    st.write("")

    # Generate button 
    with stylable_container(
            key='generate',
            css_styles="""
                button{
                    background: linear-gradient(to right, #005C97 ,#363795);
                    color: white;
                    border-radius: 7px;
                    height: 50px !important;
                    min-height: 35px !important;
                    max-height: 35px !important;
                }
                """
        ):
        if st.button("Generate", key="generate"):
            if gold_wt_g < 10.00:
                ten_below()
            else:
                pdf_gold_bd(item_code_g, price_g, gold_wt_g)
                view_pdf = True
    return view_pdf


def render_hyd_breakdown():
    st.write("#### Hyderabadi Jewellery Breakdown")
    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

        # Initialize session state for tracking the widgets and their values
    if 'hyd_stones_count' not in st.session_state:
        st.session_state['hyd_stones_count'] = 1  # Start with at least one widget
    if 'hyd_stones_data' not in st.session_state:
        st.session_state['hyd_stones_data'] = [{
            'hyd_stone': 'Ruby',
            'hyd_ct': 0.0
        }]  # Start with initial data for one widget

    col1, col2, col3 = st.columns([3, 3, 3])

    with col1:
        item_code_h = st.text_input("Item code")
    
    with col2:
        price_h = st.number_input("Price",
                                min_value=0)

    with col3:
        gold_wt_h = st.number_input("Gross Gold Weight in grams",
                                  min_value=0.0)

    st.markdown("<h4 style='font-size:18px;'>Stone Details</h4>", 
                unsafe_allow_html=True)
    # Display and update the widgets
    for i in range(st.session_state['hyd_stones_count']):

        # Use columns to place text inputs side by side
        col1, col2, col3, _ = st.columns([3,3,1,2], vertical_alignment="bottom")
        # stone selection box
        with col1:
            options = ['Ruby', 'Emerald', 'Pearls', 'Coral', 'Navaratna', 'Cubic Zirconia', 'Color Stone', 'Other/All stones']
            index = ['Ruby', 'Emerald', 'Pearls', 'Coral', 'Navaratna', 'Cubic Zirconia', 'Color Stone', 'Other/All stones']
            hyd_stone = st.selectbox("Select Stone", 
                                options = options,
                                index = index.index(st.session_state['hyd_stones_data'][i]['hyd_stone']),
                                key = f'hyd_stone_{i}')
            st.session_state['hyd_stones_data'][i]['hyd_stone'] = hyd_stone

        # stone carat
        with col2:
            hyd_ct = st.number_input("Stone carat",
                                     value=st.session_state['hyd_stones_data'][i]['hyd_ct'],
                                     min_value=0.0,
                                     key=f'hyd_ct_{i}')
            st.session_state['hyd_stones_data'][i]['hyd_ct'] = round(hyd_ct, 2)

        # delete button
        with col3:
            with stylable_container(
                key=f'delete_hyd_{i}',
                css_styles="""
                    button{
                        background: linear-gradient(to left, #FF0000, #FF2C2C);
                        color: white;
                        border-radius: 7px;
                        height: 35px !important;
                        min-height: 40px !important;
                        max-height: 40px !important;
                        width: 100%;
                    }
                    """
            ):
                if st.session_state['hyd_stones_count'] > 1:
                    if st.button(f"Delete", key=f'delete_hyd_{i}'):
                        delete_widget(i, 'hyd')
                        st.rerun()         

    # Button to trigger adding of widgets
    with stylable_container(
                    key='add',
                    css_styles="""
                        button{
                            background: linear-gradient(to right, #434343 , #000000 );;
                            color: white;
                            border-radius: 7px;
                            height: 50px !important;
                            min-height: 35px !important;
                            max-height: 35px !important;
                            width: 100%;
                        }
                        """
                ):
            _, col, _ = st.columns([2, 1.2, 2])
            with col:
                with stylable_container(
                    key="container_with_border",
                    css_styles=r"""
                        button p:before {
                            font-family: 'Font Awesome 5 Free';
                            content: '\2b';  /* Plus sign */
                            display: inline-block;
                            padding-right: 10px;
                            vertical-align: top;
                        }
                        """,
                ):
                    if st.button("Add Stone", key="add"):
                        add_widgets('hyd')
                        st.rerun()


    view_pdf = False

    # Generate button 
    with stylable_container(
            key='generate',
            css_styles="""
                button{
                    background: linear-gradient(to right, #005C97 , #363795 );
                    color: white;
                    border-radius: 7px;
                    height: 50px !important;
                    min-height: 35px !important;
                    max-height: 35px !important;
                }
                """
        ):
        if st.button("Generate", key="generate"):
            if gold_wt_h < 10.00:
                ten_below()
            else:
                pdf_hyd_bd(item_code_h, 
                           price_h, 
                           gold_wt_h, 
                           st.session_state['hyd_stones_data'])
                view_pdf = True
    return view_pdf


def render_ant_breakdown():
    st.write("#### Antique Jewellery Breakdown")
    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

        # Initialize session state for tracking the widgets and their values
    if 'ant_stones_count' not in st.session_state:
        st.session_state['ant_stones_count'] = 1  # Start with at least one widget
    if 'ant_stones_data' not in st.session_state:
        st.session_state['ant_stones_data'] = [{
            'ant_stone': 'Polki Diamond',
            'ant_ct': 0.0
        }]  # Start with initial data for one widget

    col1, col2, col3 = st.columns([3, 3, 3])

    with col1:
        item_code_a = st.text_input("Item code")
    
    with col2:
        price_a = st.number_input("Price",
                                min_value=0)

    with col3:
        gold_wt_a = st.number_input("Gross Gold Weight in grams",
                                  min_value=0.0)

    st.markdown("<h4 style='font-size:18px;'>Stone Details</h4>", 
                unsafe_allow_html=True)

    # Display and update the widgets
    for i in range(st.session_state['ant_stones_count']):

        # Use columns to place text inputs side by side
        col1, col2, col3, _ = st.columns([3,3,1,2], vertical_alignment="bottom")
        # stone selection box
        with col1:
            options = ['Polki Diamond', 'Ruby', 'Emerald', 'Pearls', 'Coral', 'Navaratna', 'Cubic Zirconia', 'Color Stone', 'Other/All stones']
            index = ['Polki Diamond', 'Ruby', 'Emerald', 'Pearls', 'Coral', 'Navaratna', 'Cubic Zirconia', 'Color Stone', 'Other/All stones']
            ant_stone = st.selectbox("Select Stone", 
                                options = options,
                                index = index.index(st.session_state['ant_stones_data'][i]['ant_stone']),
                                key = f'ant_stone_{i}')
            st.session_state['ant_stones_data'][i]['ant_stone'] = ant_stone

        # gold weight box
        with col2:
            ant_ct = st.number_input("Stone carat",
                                    value=st.session_state['ant_stones_data'][i]['ant_ct'],
                                    key=f'ant_ct_{i}',
                                    min_value=0.0)
            st.session_state['ant_stones_data'][i]['ant_ct'] = ant_ct

        # gold karat dropdown
        with col3:
            with stylable_container(
                key=f'delete_ant_{i}',
                css_styles="""
                    button{
                        background: linear-gradient(to left, #FF0000, #FF2C2C);
                        color: white;
                        border-radius: 7px;
                        height: 35px !important;
                        min-height: 40px !important;
                        max-height: 40px !important;
                        width: 100%;
                    }
                    """
            ):
                if st.session_state['ant_stones_count'] > 1:
                    if st.button(f"Delete", key=f'delete_ant_{i}'):
                        delete_widget(i, 'ant')
                        st.rerun()         

    # Button to trigger adding of widgets
    with stylable_container(
                    key='add',
                    css_styles="""
                        button{
                            background: linear-gradient(to right, #434343 , #000000 );;
                            color: white;
                            border-radius: 7px;
                            height: 50px !important;
                            min-height: 35px !important;
                            max-height: 35px !important;
                            width: 100%;
                        }
                        """
                ):
            _, col, _ = st.columns([2, 1.2, 2])
            with col:
                with stylable_container(
                    key="container_with_border",
                    css_styles=r"""
                        button p:before {
                            font-family: 'Font Awesome 5 Free';
                            content: '\2b';  /* Plus sign */
                            display: inline-block;
                            padding-right: 10px;
                            vertical-align: top;
                        }
                        """,
                ):
                    if st.button("Add Stone", key="add"):
                        add_widgets('ant')
                        st.rerun()


    view_pdf = False

    # Generate button 
    with stylable_container(
            key='generate',
            css_styles="""
                button{
                    background: linear-gradient(to right, #005C97 , #363795 );
                    color: white;
                    border-radius: 7px;
                    height: 50px !important;
                    min-height: 35px !important;
                    max-height: 35px !important;
                }
                """
        ):
        if st.button("Generate", key="generate"):
            if gold_wt_a < 10.00:
                ten_below()
            else:
                pdf_ant_bd(item_code_a, 
                           price_a, 
                           gold_wt_a, 
                           st.session_state['ant_stones_data'])
                view_pdf = True
    return view_pdf


def render_dia_breakdown():
    st.write("#### Diamond Jewellery Breakdown")
    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

    # Use columns to place text inputs side by side
    col1, col2 = st.columns(2)

    with col1:
        options = ["10K", "14K", "18K", "21K", "22K", "24K"]
        gold_kt = st.selectbox("Select Gold Karat", options)

    with col2:
        options = ["Govindji's", "Other jeweller"]
        gold_pur_place = st.selectbox("Where was the gold purchased?", options)

    col11, _ = st.columns(2)

    with col11:
        gold_wt = st.text_input("Enter Gold Weight in grams")

    view_pdf = False

    # Generate button 
    with stylable_container(
            key='generate',
            css_styles="""
                button{
                    background: linear-gradient(to right, #005C97 , #363795 );
                    color: white;
                    border-radius: 7px;
                    height: 50px !important;
                    min-height: 35px !important;
                    max-height: 35px !important;
                }
                """
        ):
        if st.button("Generate", key="generate"):
            sample_pdf(st.session_state['widget_data'], 'gold_pur_place', 'gold_wt', "")
            view_pdf = True
    return view_pdf
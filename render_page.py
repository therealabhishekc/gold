import streamlit as st
from generate_pdf import sample_pdf, pdf_scrap_gold, pdf_gold_bd
from streamlit_extras.stylable_container import stylable_container

# Function to add widgets
def add_widgets(var):
    if var == 'scrap_gold':
        st.session_state['widget_count'] += 1
        st.session_state['widget_data'].append({
            'desc': '',
            'gold_wt': '',
            'gold_kt': '10K',
            'gold_pur_place' : "Govindji's"
        })
    elif var == 'hyd':
        st.session_state['hyd_stones_count'] += 1
        st.session_state['hyd_stones_data'].append({
            'hyd_stone': 'Ruby',
            'hyd_ct': ''
        })
    elif var == 'ant':
        st.session_state['ant_stones_count'] += 1
        st.session_state['ant_stones_data'].append({
            'ant_stone': 'Ruby',
            'ant_ct': ''
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
    
    colm1, colm2= st.columns([3, 3], vertical_alignment="bottom")
    with colm1: 
        st.write("### Scrap Gold Purchase")
    with colm2:
        show_calc = st.checkbox("Show Formula")

    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

    # Initialize session state for tracking the widgets and their values
    if 'widget_count' not in st.session_state:
        st.session_state['widget_count'] = 1  # Start with at least one widget
    if 'widget_data' not in st.session_state:
        st.session_state['widget_data'] = [{
            'desc': '',
            'gold_wt': '',
            'gold_kt': '10K',
            'gold_pur_place' : "Govindji's"
        }]  # Start with initial data for one widget

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
                    if st.button(f"Delete", key=f'delete_{i}'):
                        delete_widget(i, 'scrap_gold')
                        st.rerun()

        # Use columns to place text inputs side by side
        col1, col2, col3, col4 = st.columns([4,4,4,4], vertical_alignment="bottom")
        # description box
        with col1:
            desc = st.text_input("Description",
                                value=st.session_state['widget_data'][i]['desc'],
                                key=f'desc_{i}')
            st.session_state['widget_data'][i]['desc'] = desc

        # gold weight box
        with col2:
            gold_wt = st.text_input("Gold Weight in grams",
                                    value=st.session_state['widget_data'][i]['gold_wt'],
                                    key=f'gold_wt_{i}')
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
                    if st.button("Add Items", key="add"):
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
            pdf_scrap_gold(st.session_state['widget_data'], show_calc)
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
            'hyd_ct': ''
        }]  # Start with initial data for one widget

    col1, col2 = st.columns(2)

    with col1:
        item_code = st.text_input("Item code")
    
    with col2:
        gold_wt = st.text_input("Gross Gold Weight in grams")

    # Display and update the widgets
    for i in range(st.session_state['hyd_stones_count']):

        # Use columns to place text inputs side by side
        col1, col2, col3 = st.columns([3.2,3.2,1], vertical_alignment="bottom")
        # stone selection box
        with col1:
            options = ['Ruby', 'Emerald', 'Pearls', 'Coral', 'Polki Diamond', 'Navaratna', 'Cubic Zirconia', 'Color Stone']
            index = ['Ruby', 'Emerald', 'Pearls', 'Coral', 'Polki Diamond', 'Navaratna', 'Cubic Zirconia', 'Color Stone']
            hyd_stone = st.selectbox("Select Stone", 
                                options = options,
                                index = index.index(st.session_state['hyd_stones_data'][i]['hyd_stone']),
                                key = f'hyd_stone_{i}')
            st.session_state['hyd_stones_data'][i]['hyd_stone'] = hyd_stone

        # gold weight box
        with col2:
            hyd_ct = st.text_input("Stone carat",
                                    value=st.session_state['hyd_stones_data'][i]['hyd_ct'],
                                    key=f'hyd_ct_{i}')
            st.session_state['hyd_stones_data'][i]['hyd_ct'] = hyd_ct

        # gold karat dropdown
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
            sample_pdf(st.session_state['widget_data'], 'gold_pur_place', 'gold_wt', "")
            view_pdf = True
    return view_pdf


def render_gold_breakdown():
    st.write("#### Gold Jewellery Breakdown")
    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

    col1, col2, col3 = st.columns(3)

    with col1:
        item_code = st.text_input("Item code")
    
    with col2:
        price = st.text_input("Price")

    with col3:
        gold_wt = st.text_input("Gross Gold Weight in grams")

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
            pdf_gold_bd(item_code, price, gold_wt)
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
            'ant_stone': 'Ruby',
            'ant_ct': ''
        }]  # Start with initial data for one widget

    col1, col2 = st.columns(2)

    with col1:
        item_code = st.text_input("Item code")
    
    with col2:
        gold_wt = st.text_input("Gross Gold Weight in grams")

    # Display and update the widgets
    for i in range(st.session_state['ant_stones_count']):

        # Use columns to place text inputs side by side
        col1, col2, col3 = st.columns([3.2,3.2,1], vertical_alignment="bottom")
        # stone selection box
        with col1:
            options = ['Ruby', 'Emerald', 'Pearls', 'Coral', 'Polki Diamond', 'Navaratna', 'Cubic Zirconia', 'Color Stone']
            index = ['Ruby', 'Emerald', 'Pearls', 'Coral', 'Polki Diamond', 'Navaratna', 'Cubic Zirconia', 'Color Stone']
            ant_stone = st.selectbox("Select Stone", 
                                options = options,
                                index = index.index(st.session_state['ant_stones_data'][i]['ant_stone']),
                                key = f'ant_stone_{i}')
            st.session_state['ant_stones_data'][i]['ant_stone'] = ant_stone

        # gold weight box
        with col2:
            ant_ct = st.text_input("Stone carat",
                                    value=st.session_state['ant_stones_data'][i]['ant_ct'],
                                    key=f'ant_ct_{i}')
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
            sample_pdf(st.session_state['widget_data'], 'gold_pur_place', 'gold_wt', "")
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
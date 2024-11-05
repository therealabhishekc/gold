import streamlit as st
from generate_pdf import sample_pdf, pdf_scrap_gold, pdf_gold_bd, pdf_hyd_bd, pdf_ant_bd
from streamlit_extras.stylable_container import stylable_container

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


def add_callback(var):
    if var == 'scrap_gold':
        st.session_state['scrap_gold_count'] += 1
        st.session_state['scrap_gold_data'].append({
            'desc': '',
            'gold_wt': 0.00,
            'gold_kt': '10K',
            'gold_pur_place' : "Govindji's"
        })
    elif var == 'hyd':
        st.session_state['hyd_stones_count'] += 1
    elif var == 'ant':
        st.session_state['ant_stones_count'] += 1
    elif var == 'dia':
        pass


def del_callback(index, var):
    if var == 'scrap_gold':
        if st.session_state['scrap_gold_count'] > 1:  # Ensure at least one widget remains
            st.session_state['scrap_gold_count'] -= 1
            st.session_state['scrap_gold_data'].pop(index)
    elif var == 'hyd':
        if st.session_state['hyd_stones_count'] > 1:
            st.session_state['hyd_stones_count'] -= 1
    elif var == 'ant':
        if st.session_state['ant_stones_count'] > 1:
            st.session_state['ant_stones_count'] -= 1
    elif var == 'dia':
        pass


# updating the session state of the sections
def update_scrap_gold(i, field):
    if field == 'desc':
        st.session_state['scrap_gold_data'][i]['desc'] = st.session_state[f'desc_{i}']
    elif field == 'gold_wt':
        st.session_state['scrap_gold_data'][i]['gold_wt'] = st.session_state[f'gold_wt_{i}']
    elif field == 'gold_kt':
        st.session_state['scrap_gold_data'][i]['gold_kt'] = st.session_state[f'gold_kt_{i}']
    elif field == 'gold_pur_place':
        st.session_state['scrap_gold_data'][i]['gold_pur_place'] = st.session_state[f'gold_pur_place_{i}']


def update_gold_breakdown(field):
    if field == "item_code":
        st.session_state['ss_item_code_g'] = st.session_state['item_code_g']
    elif field == "price":
        st.session_state['ss_price_g'] = st.session_state['price_g']
    elif field == "gold_wt":
        st.session_state['ss_gold_wt_g'] = st.session_state['gold_wt_g']


def update_hyd_breakdown(field, i):
    if field == "item_code":
        st.session_state['ss_item_code_h'] = st.session_state['item_code_h']
    elif field == "price":
        st.session_state['ss_price_h'] = st.session_state['price_h']
    elif field == "gold_wt":
        st.session_state['ss_gold_wt_h'] = st.session_state['gold_wt_h']
    elif field == "hyd_stone":
        st.session_state['ss_hyd_stones'][i]['hyd_stone'] = st.session_state[f'hyd_stone_{i}']
    elif field == "hyd_ct":
        try:
            st.session_state['ss_hyd_stones'][i]['hyd_ct'] = float(st.session_state[f'hyd_ct_{i}'])
        except ValueError:
            invalid_input()


def update_ant_breakdown(field, i):
    if field == "item_code":
        st.session_state['ss_item_code_a'] = st.session_state['item_code_a']
    elif field == "price":
        st.session_state['ss_price_a'] = st.session_state['price_a']
    elif field == "gold_wt":
        st.session_state['ss_gold_wt_a'] = st.session_state['gold_wt_a']
    elif field == "ant_stone":
        st.session_state['ss_ant_stones'][i]['ant_stone'] = st.session_state[f'ant_stone_{i}']
    elif field == "ant_ct":
        try:
            st.session_state['ss_ant_stones'][i]['ant_ct'] = float(st.session_state[f'ant_ct_{i}'])
        except ValueError:
            invalid_input()


# rendering the actual page
def render_gold_scrap():
    
    # Initialize session state for tracking the widgets and their values
    if 'scrap_gold_count' not in st.session_state:
        st.session_state['scrap_gold_count'] = 1  # Start with at least one widget
    if 'scrap_gold_data' not in st.session_state:
        st.session_state['scrap_gold_data'] = [{
            'desc': '',
            'gold_wt': 0.00,
            'gold_kt': '10K',
            'gold_pur_place' : "Govindji's"
        }]  # Start with initial data for one widget
    if 'show_calc' not in st.session_state:
        st.session_state['show_calc'] = False
    if 'ref_cost' not in st.session_state:
        st.session_state['ref_cost'] = False
    
    colm1, colm2, colm3= st.columns([3, 1.5, 1.5], vertical_alignment="bottom")
    with colm1: 
        st.write("### Scrap Gold Purchase")
    with colm2:
        st.session_state['ref_cost'] = st.checkbox("Remove Refinery Cost",
                                                    value=st.session_state['ref_cost'],
                                                    disabled=False)
    with colm3:
        st.session_state['show_calc'] = st.checkbox("Show Formula",
                                                    value=st.session_state['show_calc'],
                                                    disabled=True)

    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

    # Display and update the widgets
    for i in range(st.session_state['scrap_gold_count']):
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
                if st.session_state['scrap_gold_count'] > 1:
                    st.button("Delete",
                              key=f'delete_{i}',
                              on_click=del_callback,
                              args=(i, 'scrap_gold'))

        # Use columns to place text inputs side by side
        col1, col2, col3, col4 = st.columns([4,4,4,4], 
                                            vertical_alignment="bottom")
        # description box
        with col1:
            st.text_input("Description",
                            value=st.session_state['scrap_gold_data'][i]['desc'],
                            key=f'desc_{i}',
                            on_change=update_scrap_gold,
                            args=(i, 'desc'))

        # gold weight box
        with col2:
            st.text_input("Gold Weight in grams",
                            value=st.session_state['scrap_gold_data'][i]['gold_wt'],
                            key=f'gold_wt_{i}',
                            on_change=update_scrap_gold,
                            args=(i, 'gold_wt'))
            
        try:
            val = float(st.session_state['scrap_gold_data'][i]['gold_wt'])
        except ValueError:
            invalid_input()

        # gold karat dropdown
        with col3:
            st.selectbox("Select Gold Karat", 
                            options = ["10K", "14K", "18K", "21K", "22K", "24K"],
                            index = ["10K", "14K", "18K", "21K", "22K", "24K"].index(st.session_state['scrap_gold_data'][i]['gold_kt']),
                            key = f'gold_kt_{i}',
                            on_change=update_scrap_gold,
                            args=(i, 'gold_kt'))

        # jewellery purchase dropdown
        with col4:
            st.selectbox("Gold Purchased at?", 
                            options = ["Govindji's", "Other jeweller"],
                            index = ["Govindji's", "Other jeweller"].index(st.session_state['scrap_gold_data'][i]['gold_pur_place']),
                            key = f'gold_pur_place_{i}',
                            on_change=update_scrap_gold,
                            args=(i, 'gold_pur_place'))


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
                    st.button("Add items",
                              on_click=add_callback,
                              args=('scrap_gold',),
                              key='add_scrp')

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
            with st.spinner('Preparing Report!'):
                val = pdf_scrap_gold(st.session_state['scrap_gold_data'], 
                                     st.session_state['show_calc'],
                                     st.session_state['ref_cost'])
                if val == 'kitco_down':
                    return kitco_down()
            view_pdf = True
    return view_pdf
         

def render_gold_breakdown():
    st.write("#### Gold Jewelry Breakdown")
    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

    if 'ss_item_code_g' not in st.session_state:
        st.session_state['ss_item_code_g'] = ''
    if 'ss_price_g' not in st.session_state:
        st.session_state['ss_price_g'] = 0
    if 'ss_gold_wt_g' not in st.session_state:
        st.session_state['ss_gold_wt_g'] = 0.0

    col1, col2, col3 = st.columns(3)

    with col1:
        item_code_g = st.text_input("Item code", 
                                    key='item_code_g',
                                    value=st.session_state['ss_item_code_g'],
                                    on_change=update_gold_breakdown,
                                    args=('item_code',))
    
    with col2:
        price_g = st.text_input("Price", 
                                key='price_g',
                                value=st.session_state['ss_price_g'],
                                on_change=update_gold_breakdown,
                                args=('price',))  

    try:
        price_g = float(st.session_state['ss_price_g'])
    except ValueError:
        invalid_input()

    with col3:
        gold_wt_g = st.text_input("Gross Gold Weight in grams",
                                    key='gold_wt_g',
                                    value=st.session_state['ss_gold_wt_g'],
                                    on_change=update_gold_breakdown,
                                    args=('gold_wt',))

    try:
        gold_wt_g = float(st.session_state['ss_gold_wt_g'])
    except ValueError:
        invalid_input()

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
            with st.spinner('Preparing Report!'):
                if gold_wt_g < 10.00:
                    ten_below()
                val = pdf_gold_bd(item_code_g, price_g, gold_wt_g)
                if val == 'kitco_down':
                    return kitco_down()
            view_pdf = True
    return view_pdf


def render_hyd_breakdown():
    st.write("#### Hyderabadi Jewelry Breakdown")
    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

        # Initialize session state for tracking the widgets and their values
    if 'hyd_stones_count' not in st.session_state:
        st.session_state['hyd_stones_count'] = 1  # Start with at least one widget

    # intializing sessions states for all the fields
    if 'ss_item_code_h' not in st.session_state:
        st.session_state['ss_item_code_h'] = ''
    if 'ss_price_h' not in st.session_state:
        st.session_state['ss_price_h'] = 0
    if 'ss_gold_wt_h' not in st.session_state:
        st.session_state['ss_gold_wt_h'] = 0.0
    if 'ss_hyd_stones' not in st.session_state:
        st.session_state['ss_hyd_stones'] = [{'hyd_stone': 'Ruby', 'hyd_ct': 0} for _ in range(10)]

    col1, col2, col3 = st.columns([3, 3, 3])

    with col1:
        item_code_h = st.text_input("Item code",
                                    key='item_code_h',
                                    value=st.session_state['ss_item_code_h'],
                                    on_change=update_hyd_breakdown,
                                    args=("item_code", 0))
    
    with col2:
        price_h = st.text_input("Price",
                                key='price_h',
                                value=st.session_state['ss_price_h'],
                                on_change=update_hyd_breakdown,
                                args=("price", 0))

    try:
        price_h = float(st.session_state['ss_price_h'])
    except ValueError:
        invalid_input()

    with col3:
        gold_wt_h = st.text_input("Gross Gold Weight in grams",
                                    key='gold_wt_h',
                                    value=st.session_state['ss_gold_wt_h'],
                                    on_change=update_hyd_breakdown,
                                    args=("gold_wt", 0))
        
    try:
        gold_wt_h = float(st.session_state['ss_gold_wt_h'])
    except ValueError:
        invalid_input()

    st.markdown("<h4 style='font-size:18px;'>Stone Details</h4>", 
                unsafe_allow_html=True)
    # Display and update the widgets
    for i in range(st.session_state['hyd_stones_count']):

        # Use columns to place text inputs side by side
        col1, col2, col3, _ = st.columns([3,3,1.5,1.5], vertical_alignment="bottom")
        # stone selection box
        with col1:
            options = ['Ruby', 'Emerald', 'Ruby/Emerald', 'Sapphire','Pearl', 'Coral', 
                       'Navratna', 'Cubic Zirconia', 'South Sea Pearls', 'Other/All stones']
            index = ['Ruby', 'Emerald', 'Ruby/Emerald', 'Sapphire', 'Pearl', 'Coral', 
                     'Navratna', 'Cubic Zirconia', 'South Sea Pearls', 'Other/All stones']
            st.selectbox("Select Stone", 
                            options = options,
                            index = index.index(st.session_state['ss_hyd_stones'][i]['hyd_stone']),
                            key = f'hyd_stone_{i}',
                            on_change=update_hyd_breakdown,
                            args=("hyd_stone", i))

        # stone carat
        with col2:
            st.text_input("Stone carat",
                            key=f'hyd_ct_{i}',
                            value=st.session_state['ss_hyd_stones'][i]['hyd_ct'],
                            on_change=update_hyd_breakdown,
                            args=("hyd_ct", i))
            
            try:
                float(st.session_state['ss_hyd_stones'][i]['hyd_ct'])
            except ValueError:
                invalid_input()

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
                    st.button("Delete",
                              key=f'delete_hyd_{i}',
                              on_click=del_callback,
                              args=(i, 'hyd'))        

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
                    st.button("Add Gems",
                              on_click=add_callback,
                              args=('hyd',),
                              key='add_hyd')


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
            with st.spinner('Preparing Report!'):
                val = pdf_hyd_bd(item_code_h, 
                                 price_h, 
                                 gold_wt_h, 
                                 st.session_state['ss_hyd_stones'][:st.session_state['hyd_stones_count']])
                if val == 'kitco_down':
                    return kitco_down()
                if val == "no_calc":
                    return no_calc()
            view_pdf = True
    return view_pdf


def render_ant_breakdown():
    st.write("#### Antique Jewelry Breakdown")
    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

        # Initialize session state for tracking the widgets and their values
    if 'ant_stones_count' not in st.session_state:
        st.session_state['ant_stones_count'] = 1  # Start with at least one widget

    # intializing sessions states for all the fields
    if 'ss_item_code_a' not in st.session_state:
        st.session_state['ss_item_code_a'] = ''
    if 'ss_price_a' not in st.session_state:
        st.session_state['ss_price_a'] = 0
    if 'ss_gold_wt_a' not in st.session_state:
        st.session_state['ss_gold_wt_a'] = 0.0
    if 'ss_ant_stones' not in st.session_state:
        st.session_state['ss_ant_stones'] = [{'ant_stone': 'Ruby', 'ant_ct': 0} for _ in range(10)]

    col1, col2, col3 = st.columns([3, 3, 3])

    with col1:
        item_code_a = st.text_input("Item code",
                                    key='item_code_a',
                                    value=st.session_state['ss_item_code_a'],
                                    on_change=update_ant_breakdown,
                                    args=("item_code", 0))
    
    with col2:
        price_a = st.text_input("Price",
                                key='price_a',
                                value=st.session_state['ss_price_a'],
                                on_change=update_ant_breakdown,
                                args=("price", 0))
        
    try:
        price_a = float(st.session_state['ss_price_a'])
    except ValueError:
        invalid_input()

    with col3:
        gold_wt_a = st.text_input("Gross Gold Weight in grams",
                                  key='gold_wt_a',
                                  value=st.session_state['ss_gold_wt_a'],
                                  on_change=update_ant_breakdown,
                                  args=("gold_wt", 0))
        
    try:
        gold_wt_a = float(st.session_state['ss_gold_wt_a'])
    except ValueError:
        invalid_input()

    st.markdown("<h4 style='font-size:18px;'>Stone Details</h4>", 
                unsafe_allow_html=True)

    # Display and update the widgets
    for i in range(st.session_state['ant_stones_count']):

        # Use columns to place text inputs side by side
        col1, col2, col3, _ = st.columns([3,3,1.5,1.5], vertical_alignment="bottom")
        # stone selection box
        with col1:
            options = ['Polki Diamond', 'Ruby', 'Emerald', 'Ruby/Emerald', 'Pearl', 
                       'Coral', 'Navaratna', 'Cubic Zirconia', 'Kundan', 'Other/All stones']
            index = ['Polki Diamond', 'Ruby', 'Emerald', 'Ruby/Emerald', 'Pearl', 
                     'Coral', 'Navaratna', 'Cubic Zirconia', 'Kundan', 'Other/All stones']
            st.selectbox("Select Stone", 
                            options = options,
                            index = index.index(st.session_state['ss_ant_stones'][i]['ant_stone']),
                            key = f'ant_stone_{i}',
                            on_change=update_ant_breakdown,
                            args=("ant_stone", i))

        # stone carat
        with col2:
            st.text_input("Stone carat",
                          value=st.session_state['ss_ant_stones'][i]['ant_ct'],
                          key=f'ant_ct_{i}',
                          on_change=update_ant_breakdown,
                          args=("ant_ct", i))
            
            try:
                float(st.session_state['ss_ant_stones'][i]['ant_ct'])
            except ValueError:
                invalid_input()

        # delete option
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
                    st.button("Delete",
                              key=f'delete_ant_{i}',
                              on_click=del_callback,
                              args=(i, 'ant'))

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
                    st.button("Add Gems",
                              on_click=add_callback,
                              args=('ant',),
                              key='add_ant')

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
            with st.spinner('Preparing Report!'):
                val = pdf_ant_bd(item_code_a, 
                                price_a, 
                                gold_wt_a, 
                                st.session_state['ss_ant_stones'][:st.session_state['ant_stones_count']])
                if val == 'kitco_down':
                    return kitco_down()
                if val == "no_calc":
                    return no_calc()
            view_pdf = True
    return view_pdf


def render_dia_breakdown():
    st.write("#### Diamond Jewelry Breakdown")
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
            sample_pdf(st.session_state['scrap_gold_data'], 'gold_pur_place', 'gold_wt', "")
            view_pdf = True
    return view_pdf
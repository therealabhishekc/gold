import streamlit as st
from helper.generate_pdf import *
from streamlit_extras.stylable_container import stylable_container
from helper.dialog import *
from helper.tax_rate import *
from streamlit_js_eval import get_geolocation
import geopy
import requests
import json


# functions to add and remove widgets
def add_callback(var):
    if var == 'scrap_gold':
        st.session_state['scrap_gold_count'] += 1
        st.session_state['scrap_gold_data'].append({
            'desc': '',
            'gold_wt': 0.0,
            'gold_reduc': 0.0,
            'gold_kt': '10K',
            #'gold_pur_place' : "Govindji's"
        })
    elif var == 'hyd':
        st.session_state['hyd_stones_count'] += 1
    elif var == 'ant':
        st.session_state['ant_stones_count'] += 1
    elif var == 'dia':
        st.session_state['dia_stones_count'] += 1


def del_callback(index, var):
    if var == 'scrap_gold':
        if st.session_state['scrap_gold_count'] > 1:  # Ensure at least one widget remains
            st.session_state['scrap_gold_count'] -= 1
            st.session_state['scrap_gold_data'].pop(index)
    elif var == 'hyd':
        if st.session_state['hyd_stones_count'] > 1:
            st.session_state['hyd_stones_count'] -= 1
            st.session_state['ss_hyd_stones'].pop(index)
            st.session_state['ss_hyd_stones'].append({'hyd_stone': 'Ruby', 'hyd_ct': 0.0})
    elif var == 'ant':
        if st.session_state['ant_stones_count'] > 1:
            st.session_state['ant_stones_count'] -= 1
            st.session_state['ss_ant_stones'].pop(index)
            st.session_state['ss_ant_stones'].append({'ant_stone': 'Polki Diamond', 'ant_ct': 0.0})
    elif var == 'dia':
        if st.session_state['dia_stones_count'] > 0:
            st.session_state['dia_stones_count'] -= 1
            st.session_state['ss_dia_stones'].pop(index)
            st.session_state['ss_dia_stones'].append({'dia_stone': 'Polki Diamond', 'dia_ct': 0.0})


# updating the session state of the sections
def update_scrap_gold(i, field):
    if field == 'desc':
        st.session_state['scrap_gold_data'][i]['desc'] = st.session_state[f'desc_{i}']
    elif field == 'gold_wt':
        st.session_state['scrap_gold_data'][i]['gold_wt'] = st.session_state[f'gold_wt_{i}']
    elif field == 'gold_reduc':
        st.session_state['scrap_gold_data'][i]['gold_reduc'] = st.session_state[f'gold_reduc_{i}']
    elif field == 'gold_kt':
        st.session_state['scrap_gold_data'][i]['gold_kt'] = st.session_state[f'gold_kt_{i}']
    elif field == 'gold_calc':
        st.session_state['gold_calc'] = st.session_state[f'gold_calc1']
    elif field == 'ref_cost':
        st.session_state['ref_cost'] = st.session_state[f'ref_cost1']
    # elif field == 'gold_pur_place':
    #     st.session_state['scrap_gold_data'][i]['gold_pur_place'] = st.session_state[f'gold_pur_place_{i}']


def update_gold_breakdown(field):
    if field == "item_code":
        st.session_state['ss_item_code_g'] = st.session_state['item_code_g']
    elif field == "price":
        st.session_state['ss_price_g'] = st.session_state['price_g']
    elif field == "gold_wt":
        st.session_state['ss_gold_wt_g'] = st.session_state['gold_wt_g']
    elif field == "gb_perc":
        st.session_state['ss_gb_perc'] = st.session_state['gb_perc']
    elif field == "gb_loc":
        st.session_state['ss_gb_loc'] = st.session_state['gb_loc']


def update_hyd_breakdown(field, i):
    if field == "item_code":
        st.session_state['ss_item_code_h'] = st.session_state['item_code_h']
    elif field == "hy_perc":
        st.session_state['ss_hy_perc'] = st.session_state['hy_perc']
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
    elif field == "hy_loc":
        st.session_state['ss_hy_loc'] = st.session_state['hy_loc']


def update_ant_breakdown(field, i):
    if field == "item_code":
        st.session_state['ss_item_code_a'] = st.session_state['item_code_a']
    elif field == "an_perc":
        st.session_state['ss_an_perc'] = st.session_state['an_perc']
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
    elif field == "an_loc":
        st.session_state['ss_an_loc'] = st.session_state['an_loc']


def update_dia_breakdown(field, i):
    if field == 'dia_ppc':
        st.session_state['ss_dia_ppc_d'] = st.session_state['dia_ppc_d']
    elif field == "di_perc":
        st.session_state['ss_di_perc'] = st.session_state['di_perc']
    elif field == "item_code":
        st.session_state['ss_item_code_d'] = st.session_state['item_code_d']
    elif field == "price":
        st.session_state['ss_price_d'] = st.session_state['price_d']
    elif field == "gold_wt":
        st.session_state['ss_gold_wt_d'] = st.session_state['gold_wt_d']
    elif field == 'dia_ct':
        st.session_state['ss_dia_ct_d'] = st.session_state['dia_ct_d']
    elif field == "dia_stone":
        st.session_state['ss_dia_stones'][i]['dia_stone'] = st.session_state[f'dia_stone_{i}']
    elif field == "dia_stone_ct":
        try:
            st.session_state['ss_dia_stones'][i]['dia_stone_ct'] = float(st.session_state[f'dia_stone_ct_{i}'])
        except ValueError:
            invalid_input()
    elif field == "di_loc":
        st.session_state['ss_di_loc'] = st.session_state['di_loc']


# rendering the actual page
def render_gold_scrap():
    
    # Initialize session state for tracking the widgets and their values
    if 'scrap_gold_count' not in st.session_state:
        st.session_state['scrap_gold_count'] = 1  # Start with at least one widget
    if 'scrap_gold_data' not in st.session_state:
        st.session_state['scrap_gold_data'] = [{
            'desc': '',
            'gold_wt': '',
            'gold_reduc': '',
            'gold_kt': '10K',
            #'gold_pur_place' : "Govindji's"
        }] 
    if 'show_calc' not in st.session_state:
        st.session_state['show_calc'] = False
    if 'ref_cost' not in st.session_state:
        st.session_state['ref_cost'] = 'Include'
    if 'gold_calc' not in st.session_state:
        st.session_state['gold_calc'] = '0.80'
    
    colm1, colm2 = st.columns([3, 1], vertical_alignment="bottom")
    with colm1: 
        st.write("### Scrap Gold Purchase")
        
    with colm2:
        with stylable_container(
            key='help',
            css_styles="""
                button{
                    background: white;
                    color: black;
                    border-radius: 20px;
                    height: 50px !important;
                    min-height: 35px !important;
                    max-height: 35px !important;
                    display: block;
                    margin-left: auto; 
                    margin-right: 0;
                    border: none;
                }
                """
            ):
            if st.button("", key="help", icon=":material/help:"):
                dialog_scrap_gold()

    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

    # global options
    coln1, coln2, coln3 = st.columns([2.5, 2.5, 2], 
                                     gap='large',
                                     vertical_alignment='center')
    # refinery cost
    with coln1:
        ref_options = ['Exclude', 'Include']
        st.session_state['ref_cost'] = st.segmented_control("Refinery Cost",
                                                            options = ref_options,
                                                            selection_mode = 'single',
                                                            default=st.session_state['ref_cost'],
                                                            key=f'ref_cost1',
                                                            on_change=update_scrap_gold,
                                                            args=(0, 'ref_cost'))

    # gold calculation
    with coln2:
        gold_options = ['0.916', '0.80']
        st.session_state['gold_calc'] = st.segmented_control("Gold Calculation",
                                                            options = gold_options,
                                                            selection_mode = 'single',
                                                            default=st.session_state['gold_calc'],
                                                            key=f'gold_calc1',
                                                            on_change=update_scrap_gold,
                                                            args=(0, 'gold_calc'))
        
    # show calculation
    with coln3:
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
            st.text_input("Gross Weight in grams",
                            value=st.session_state['scrap_gold_data'][i]['gold_wt'],
                            key=f'gold_wt_{i}',
                            on_change=update_scrap_gold,
                            args=(i, 'gold_wt'))

        if st.session_state['scrap_gold_data'][i]['gold_wt'] != "":    
            try:
                float(st.session_state['scrap_gold_data'][i]['gold_wt'])
            except ValueError:
                invalid_input()

        # reductions
        with col3:
            st.text_input("Reduction in grams",
                            value=st.session_state['scrap_gold_data'][i]['gold_reduc'],
                            key=f'gold_reduc_{i}',
                            on_change=update_scrap_gold,
                            args=(i, 'gold_reduc'))
        
        if st.session_state['scrap_gold_data'][i]['gold_reduc'] != "":
            try:
                float(st.session_state['scrap_gold_data'][i]['gold_reduc'])
            except ValueError:
                invalid_input()

        # gold karat dropdown
        with col4:
            st.selectbox("Gold Karat", 
                            options = ["10K", "14K", "18K", "21K", "22K", "24K"],
                            index = ["10K", "14K", "18K", "21K", "22K", "24K"].index(st.session_state['scrap_gold_data'][i]['gold_kt']),
                            key = f'gold_kt_{i}',
                            on_change=update_scrap_gold,
                            args=(i, 'gold_kt'))

        # # jewellery purchase dropdown
        # with col4:
        #     st.selectbox("Gold Purchased at?", 
        #                     options = ["Govindji's", "Other jeweller"],
        #                     index = ["Govindji's", "Other jeweller"].index(st.session_state['scrap_gold_data'][i]['gold_pur_place']),
        #                     key = f'gold_pur_place_{i}',
        #                     on_change=update_scrap_gold,
        #                     args=(i, 'gold_pur_place'))


        # Divider
        st.markdown("<hr style='margin: 20px 0;'>", unsafe_allow_html=True)       


    # Button to trigger adding of widgets
    with stylable_container(
                    key='add',
                    css_styles="""
                        button{
                            background: linear-gradient(to right, #434343, #000000);
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
                    background: linear-gradient(to right, #005C97 , #363795);
                    color: white;
                    border-radius: 7px;
                    height: 50px !important;
                    min-height: 35px !important;
                    max-height: 35px !important;
                    display: block;
                    margin-left: 0; 
                    margin-right: auto;
                }
                """
        ):
        if st.button("Generate", key="generate"):
            with st.spinner('Preparing Report!'):
                val = pdf_scrap_gold(st.session_state['scrap_gold_data'], 
                                     st.session_state['show_calc'],
                                     st.session_state['ref_cost'],
                                     st.session_state['gold_calc'])
                if val == 'kitco_down':
                    return kitco_down()
            view_pdf = True
    return view_pdf
         

def render_gold_breakdown():
    
    # initializing the state variables
    if 'ss_item_code_g' not in st.session_state:
        st.session_state['ss_item_code_g'] = ''
    if 'ss_price_g' not in st.session_state:
        st.session_state['ss_price_g'] = ''
    if 'ss_gold_wt_g' not in st.session_state:
        st.session_state['ss_gold_wt_g'] = ''
    if 'ss_gb_perc' not in st.session_state:
        st.session_state['ss_gb_perc'] = False
    if 'ss_gb_loc' not in st.session_state:
        st.session_state['ss_gb_loc'] = False

    colm1, colm2 = st.columns([3, 1], vertical_alignment="bottom")
    with colm1: 
        st.write("### Gold Jewelry Breakdown")
        
    with colm2:
        with stylable_container(
            key='help',
            css_styles="""
                button{
                    background: white;
                    color: black;
                    border-radius: 20px;
                    height: 50px !important;
                    min-height: 35px !important;
                    max-height: 35px !important;
                    display: block;
                    margin-left: auto; 
                    margin-right: 0;
                    border: none;
                }
                """
            ):
            if st.button("", key="help", icon=":material/help:"):
                dialog_gold_bd()

    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

    col01, col02, col03, col04 = st.columns([2, 1, 0.1, 1],
                                     vertical_alignment='center')

    with col01:
        st.session_state['ss_gb_perc'] = st.checkbox("Show Percentages for Labor, Margin and Duty",
                                                    value=st.session_state['ss_gb_perc'],
                                                    key='gb_perc',
                                                    on_change=update_gold_breakdown,
                                                    args=('gb_perc',))
        
    with col02:
        location = st.toggle("Enable Location",
                             value=st.session_state['ss_gb_loc'],
                             key='gb_loc',
                             on_change=update_gold_breakdown,
                             args=('gb_loc',))
        
    with col03:
        tax_rate = 0
        zip_code = 0
        if location:
            loc = get_geolocation()
            if loc:
                # extract coordinates
                lat = loc['coords']['latitude']
                lon = loc['coords']['longitude']

                # extract zip code
                geolocator = geopy.Nominatim(user_agent='gold')
                location = geolocator.reverse((lat, lon))
                zip_code = location.raw['address']['postcode']

                # extarct the tax rates
                api_url = 'https://api.api-ninjas.com/v1/salestax?zip_code={}'.format(zip_code)
                response = requests.get(api_url, headers={'X-Api-Key': 
                                                          'sGhg355U0zFi6kLq5oJ6dw==cmIKqhUVUGtNjJGJ'})
                if response.status_code == requests.codes.ok:
                    json_string = response.text
                    data = json.loads(json_string)
                    tax_rate = data[0]["total_rate"]
                else:
                    pass

    with col04: 
        if zip_code != 0:
            st.write(f":white_check_mark: Zip code: {zip_code}")
    
    st.markdown("<hr style='margin: 2.5px 0;'>", unsafe_allow_html=True)

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
    if price_g != "":
        try:
            price_g = float(st.session_state['ss_price_g'])
        except ValueError:
            invalid_input()

    with col3:
        gold_wt_g = st.text_input("Gross Weight in grams",
                                    key='gold_wt_g',
                                    value=st.session_state['ss_gold_wt_g'],
                                    on_change=update_gold_breakdown,
                                    args=('gold_wt',))

    if gold_wt_g != "":
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
                # checking for missing values
                if price_g == "" or gold_wt_g == "":
                    missing_value()
                    return
                if gold_wt_g < 10.00:
                    ten_below()  

                val = pdf_gold_bd(item_code_g, price_g, gold_wt_g, 
                                      st.session_state['ss_gb_perc'],
                                      zip_code, tax_rate)
                
                if val == 'kitco_down':
                    return kitco_down()
                if val == "no_calc":
                    return no_calc()
            view_pdf = True
    return view_pdf


def render_hyd_breakdown():
    
    colm1, colm2 = st.columns([3, 1], vertical_alignment="bottom")
    with colm1: 
        st.write("### Hyderabadi Jewelry Breakdown")
        
    with colm2:
        with stylable_container(
            key='help',
            css_styles="""
                button{
                    background: white;
                    color: black;
                    border-radius: 20px;
                    height: 50px !important;
                    min-height: 35px !important;
                    max-height: 35px !important;
                    display: block;
                    margin-left: auto; 
                    margin-right: 0;
                    border: none;
                }
                """
            ):
            if st.button("", key="help", icon=":material/help:"):
                dialog_hyd_bd()

        # Initialize session state for tracking the widgets and their values
    if 'hyd_stones_count' not in st.session_state:
        st.session_state['hyd_stones_count'] = 1  # Start with at least one widget

    # intializing sessions states for all the fields
    if 'ss_item_code_h' not in st.session_state:
        st.session_state['ss_item_code_h'] = ''
    if 'ss_price_h' not in st.session_state:
        st.session_state['ss_price_h'] = ''
    if 'ss_gold_wt_h' not in st.session_state:
        st.session_state['ss_gold_wt_h'] = ''
    if 'ss_hyd_stones' not in st.session_state:
        st.session_state['ss_hyd_stones'] = [{'hyd_stone': 'Ruby', 'hyd_ct': ''} for _ in range(50)]
    if 'ss_hy_perc' not in st.session_state:
        st.session_state['ss_hy_perc'] = False
    if 'ss_hy_loc' not in st.session_state:
        st.session_state['ss_hy_loc'] = False

    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

    col01, col02, col03, col04 = st.columns([2, 1, 0.1, 1],
                                     vertical_alignment='center')

    with col01:
        st.session_state['ss_hy_perc'] = st.checkbox("Show Percentages for Labor, Margin and Duty",
                                                value=st.session_state['ss_hy_perc'],
                                                key='hy_perc',
                                                on_change=update_gold_breakdown,
                                                args=('hy_perc',))
        
    with col02:
        location = st.toggle("Enable Location",
                             value=st.session_state['ss_hy_loc'],
                             key='hy_loc',
                             on_change=update_gold_breakdown,
                             args=('hy_loc',))
        
    with col03:
        tax_rate = 0
        zip_code = 0
        if location:
            loc = get_geolocation()
            if loc:
                # extract coordinates
                lat = loc['coords']['latitude']
                lon = loc['coords']['longitude']

                # extract zip code
                geolocator = geopy.Nominatim(user_agent='gold')
                location = geolocator.reverse((lat, lon))
                zip_code = location.raw['address']['postcode']

                # extarct the tax rates
                api_url = 'https://api.api-ninjas.com/v1/salestax?zip_code={}'.format(zip_code)
                response = requests.get(api_url, headers={'X-Api-Key': 
                                                          'sGhg355U0zFi6kLq5oJ6dw==cmIKqhUVUGtNjJGJ'})
                if response.status_code == requests.codes.ok:
                    json_string = response.text
                    data = json.loads(json_string)
                    tax_rate = data[0]["total_rate"]
                else:
                    pass

    with col04: 
        if zip_code != 0:
            st.write(f":white_check_mark: Zip code: {zip_code}")
    
    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

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

    if price_h != "":
        try:
            price_h = float(st.session_state['ss_price_h'])
        except ValueError:
            invalid_input()

    with col3:
        gold_wt_h = st.text_input("Gross Weight in grams",
                                    key='gold_wt_h',
                                    value=st.session_state['ss_gold_wt_h'],
                                    on_change=update_hyd_breakdown,
                                    args=("gold_wt", 0))

    if gold_wt_h != "":   
        try:
            gold_wt_h = float(st.session_state['ss_gold_wt_h'])
        except ValueError:
            invalid_input()

    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

    st.markdown("<h4 style='font-size:18px;'>Gem Stone Details</h4>", 
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
            st.selectbox("Gem Stone", 
                            options = options,
                            index = index.index(st.session_state['ss_hyd_stones'][i]['hyd_stone']),
                            key = f'hyd_stone_{i}',
                            on_change=update_hyd_breakdown,
                            args=("hyd_stone", i))

        # stone carat
        with col2:
            st.text_input("Gem Stone Carat",
                            key=f'hyd_ct_{i}',
                            value=st.session_state['ss_hyd_stones'][i]['hyd_ct'],
                            on_change=update_hyd_breakdown,
                            args=("hyd_ct", i))
            
            if st.session_state['ss_hyd_stones'][i]['hyd_ct'] != "":
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
            if price_h == "" or gold_wt_h == "":
                return missing_value()
            if gold_wt_h < 10.00:
                ten_below()
            with st.spinner('Preparing Report!'):
                val = pdf_hyd_bd(item_code_h, 
                                 price_h, 
                                 gold_wt_h, 
                                 st.session_state['ss_hyd_stones'][:st.session_state['hyd_stones_count']],
                                 st.session_state['ss_hy_perc'],
                                 zip_code, tax_rate)
                if val == 'kitco_down':
                    return kitco_down()
                if val == "no_calc":
                    return no_calc()
            view_pdf = True
    return view_pdf


def render_ant_breakdown():
    
    colm1, colm2 = st.columns([3, 1], vertical_alignment="bottom")
    with colm1: 
        st.write("### Antique Jewelry Breakdown")
        
    with colm2:
        with stylable_container(
            key='help',
            css_styles="""
                button{
                    background: white;
                    color: black;
                    border-radius: 20px;
                    height: 50px !important;
                    min-height: 35px !important;
                    max-height: 35px !important;
                    display: block;
                    margin-left: auto; 
                    margin-right: 0;
                    border: none;
                }
                """
            ):
            if st.button("", key="help", icon=":material/help:"):
                dialog_ant_bd()

    # Initialize session state for tracking the widgets and their values
    if 'ant_stones_count' not in st.session_state:
        st.session_state['ant_stones_count'] = 1  # Start with at least one widget

    # intializing sessions states for all the fields
    if 'ss_item_code_a' not in st.session_state:
        st.session_state['ss_item_code_a'] = ''
    if 'ss_price_a' not in st.session_state:
        st.session_state['ss_price_a'] = ''
    if 'ss_gold_wt_a' not in st.session_state:
        st.session_state['ss_gold_wt_a'] = ''
    if 'ss_ant_stones' not in st.session_state:
        st.session_state['ss_ant_stones'] = [{'ant_stone': 'Polki Diamond', 'ant_ct': ''} for _ in range(50)]
    if 'ss_an_perc' not in st.session_state:
        st.session_state['ss_an_perc'] = False
    if 'ss_an_loc' not in st.session_state:
        st.session_state['ss_an_loc'] = False

    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

    col01, col02, col03, col04 = st.columns([2, 1, 0.1, 1],
                                     vertical_alignment='center')

    with col01:
        st.session_state['ss_an_perc'] = st.checkbox("Show Percentages for Labor, Margin and Duty",
                                                value=st.session_state['ss_an_perc'],
                                                key='an_perc',
                                                on_change=update_gold_breakdown,
                                                args=('an_perc',))
        
    with col02:
        location = st.toggle("Enable Location",
                             value=st.session_state['ss_an_loc'],
                             key='an_loc',
                             on_change=update_gold_breakdown,
                             args=('an_loc',))
        
    with col03:
        tax_rate = 0
        zip_code = 0
        if location:
            loc = get_geolocation()
            if loc:
                # extract coordinates
                lat = loc['coords']['latitude']
                lon = loc['coords']['longitude']

                # extract zip code
                geolocator = geopy.Nominatim(user_agent='gold')
                location = geolocator.reverse((lat, lon))
                zip_code = location.raw['address']['postcode']

                # extarct the tax rates
                api_url = 'https://api.api-ninjas.com/v1/salestax?zip_code={}'.format(zip_code)
                response = requests.get(api_url, headers={'X-Api-Key': 
                                                          'sGhg355U0zFi6kLq5oJ6dw==cmIKqhUVUGtNjJGJ'})
                if response.status_code == requests.codes.ok:
                    json_string = response.text
                    data = json.loads(json_string)
                    tax_rate = data[0]["total_rate"]
                else:
                    pass

    with col04: 
        if zip_code != 0:
            st.write(f":white_check_mark: Zip code: {zip_code}")
    
    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

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

    if price_a != "":
        try:
            price_a = float(st.session_state['ss_price_a'])
        except ValueError:
            invalid_input()

    with col3:
        gold_wt_a = st.text_input("Gross Weight in grams",
                                  key='gold_wt_a',
                                  value=st.session_state['ss_gold_wt_a'],
                                  on_change=update_ant_breakdown,
                                  args=("gold_wt", 0))

    if gold_wt_a != "":
        try:
            gold_wt_a = float(st.session_state['ss_gold_wt_a'])
        except ValueError:
            invalid_input()

    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

    st.markdown("<h4 style='font-size:18px;'>Gem Stone Details</h4>", 
                unsafe_allow_html=True)

    # Display and update the widgets
    for i in range(st.session_state['ant_stones_count']):

        # Use columns to place text inputs side by side
        col1, col2, col3, _ = st.columns([3,3,1.5,1.5], vertical_alignment="bottom")
        # stone selection box
        with col1:
            options = ['Polki Diamond', 'Diamond','Ruby', 'Emerald', 'Ruby/Emerald', 'Pearl', 
                       'South Sea Pearls', 'Coral', 'Navratna', 'Cubic Zirconia', 'Kundan', 'Other/All stones']
            index = ['Polki Diamond', 'Diamond', 'Ruby', 'Emerald', 'Ruby/Emerald', 'Pearl', 
                     'South Sea Pearls', 'Coral', 'Navratna', 'Cubic Zirconia', 'Kundan', 'Other/All stones']
            st.selectbox("Select Gem Stone", 
                            options = options,
                            index = index.index(st.session_state['ss_ant_stones'][i]['ant_stone']),
                            key = f'ant_stone_{i}',
                            on_change=update_ant_breakdown,
                            args=("ant_stone", i))

        # stone carat
        with col2:
            st.text_input("Gem Stone Carat",
                          value=st.session_state['ss_ant_stones'][i]['ant_ct'],
                          key=f'ant_ct_{i}',
                          on_change=update_ant_breakdown,
                          args=("ant_ct", i))
            
            if st.session_state['ss_ant_stones'][i]['ant_ct'] != "":
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
            if price_a == "" or gold_wt_a == "":
                missing_value()
                return
            if gold_wt_a < 10.00:
                ten_below()
            with st.spinner('Preparing Report!'):
                val = pdf_ant_bd(item_code_a, 
                                price_a, 
                                gold_wt_a, 
                                st.session_state['ss_ant_stones'][:st.session_state['ant_stones_count']],
                                st.session_state['ss_an_perc'],
                                zip_code, tax_rate)
                if val == 'kitco_down':
                    return kitco_down()
                if val == "no_calc":
                    return no_calc()
            view_pdf = True
    return view_pdf


def render_dia_breakdown():
    
    colm1, colm2 = st.columns([3, 1], vertical_alignment="bottom")
    with colm1: 
        st.write("### Diamond Jewelry Breakdown")
        
    with colm2:
        with stylable_container(
            key='help',
            css_styles="""
                button{
                    background: white;
                    color: black;
                    border-radius: 20px;
                    height: 50px !important;
                    min-height: 35px !important;
                    max-height: 35px !important;
                    display: block;
                    margin-left: auto; 
                    margin-right: 0;
                    border: none;
                }
                """
            ):
            if st.button("", key="help", icon=":material/help:"):
                dialog_dia_bd()

    # Initialize session state for tracking the widgets and their values
    if 'dia_stones_count' not in st.session_state:
        st.session_state['dia_stones_count'] = 0  # Start with at least one widget

    if 'ss_item_code_d' not in st.session_state:
        st.session_state['ss_item_code_d'] = ''
    if 'ss_price_d' not in st.session_state:
        st.session_state['ss_price_d'] = ''
    if 'ss_gold_wt_d' not in st.session_state:
        st.session_state['ss_gold_wt_d'] = ''
    if 'ss_dia_ct_d' not in st.session_state:
        st.session_state['ss_dia_ct_d'] = ''
    if 'ss_dia_stones' not in st.session_state:
        st.session_state['ss_dia_stones'] = [{'dia_stone': 'Colored Stone', 'dia_stone_ct': ''} for _ in range(50)]
    if 'ss_di_perc' not in st.session_state:
        st.session_state['ss_di_perc'] = False
    if 'ss_di_loc' not in st.session_state:
        st.session_state['ss_di_loc'] = False

    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

    col01, col02, col03, col04 = st.columns([2, 1, 0.1, 1],
                                     vertical_alignment='center')

    with col01:
        st.session_state['ss_di_perc'] = st.checkbox("Show Percentages for Labor, Margin and Duty",
                                                value=st.session_state['ss_di_perc'],
                                                key='di_perc',
                                                on_change=update_gold_breakdown,
                                                args=('di_perc',))
        
    with col02:
        location = st.toggle("Enable Location",
                             value=st.session_state['ss_di_loc'],
                             key='di_loc',
                             on_change=update_gold_breakdown,
                             args=('di_loc',))
        
    with col03:
        tax_rate = 0
        zip_code = 0
        if location:
            loc = get_geolocation()
            if loc:
                # extract coordinates
                lat = loc['coords']['latitude']
                lon = loc['coords']['longitude']

                # extract zip code
                geolocator = geopy.Nominatim(user_agent='gold')
                location = geolocator.reverse((lat, lon))
                zip_code = location.raw['address']['postcode']

                # extarct the tax rates
                api_url = 'https://api.api-ninjas.com/v1/salestax?zip_code={}'.format(zip_code)
                response = requests.get(api_url, headers={'X-Api-Key': 
                                                          'sGhg355U0zFi6kLq5oJ6dw==cmIKqhUVUGtNjJGJ'})
                if response.status_code == requests.codes.ok:
                    json_string = response.text
                    data = json.loads(json_string)
                    tax_rate = data[0]["total_rate"]
                else:
                    pass

    with col04: 
        if zip_code != 0:
            st.write(f":white_check_mark: Zip code: {zip_code}")
    
    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

    # diamond price per carat
    st.markdown("<h4 style='font-size:18px;'>Diamond Price Per Carat</h4>", 
                unsafe_allow_html=True)
    dia_ct_price_d = st.slider("Diamond Price Per Carat", 
                        min_value=495, 
                        max_value=1495,
                        step=5, 
                        key='dia_ppc_d',
                        value=795,
                        label_visibility='collapsed',
                        format='$%d')
    
    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 
    
    # other columns
    col1, col2 = st.columns([3, 3])

    with col1:
        item_code_d = st.text_input("Item code",
                                    key='item_code_d',
                                    value=st.session_state['ss_item_code_d'],
                                    on_change=update_dia_breakdown,
                                    args=("item_code", 0))
    
    with col2:
        price_d = st.text_input("Price",
                                key='price_d',
                                value=st.session_state['ss_price_d'],
                                on_change=update_dia_breakdown,
                                args=("price", 0))
    
    if price_d != "":
        try:
            price_d = float(st.session_state['ss_price_d'])
        except ValueError:
            invalid_input()

    col3, col4 = st.columns([3, 3])

    with col3:
        gold_wt_d = st.text_input("Gross Weight in grams",
                                  key='gold_wt_d',
                                  value=st.session_state['ss_gold_wt_d'],
                                  on_change=update_dia_breakdown,
                                  args=("gold_wt", 0))

    if gold_wt_d != "":    
        try:
            gold_wt_d = float(st.session_state['ss_gold_wt_d'])
        except ValueError:
            invalid_input()

    with col4:
        dia_ct_d = st.text_input("Diamond Carat Weight",
                                  key='dia_ct_d',
                                  value=st.session_state['ss_dia_ct_d'],
                                  on_change=update_dia_breakdown,
                                  args=("dia_ct", 0))

    if dia_ct_d != "":    
        try:
            dia_ct_d = float(st.session_state['ss_dia_ct_d'])
        except ValueError:
            invalid_input()

    st.markdown("<hr style='margin: 3px 0;'>", unsafe_allow_html=True) 

    st.markdown("<h4 style='font-size:18px;'>Gem Stone Details</h4>", 
                unsafe_allow_html=True)

    # Display and update the widgets
    for i in range(st.session_state['dia_stones_count']):

        # Use columns to place text inputs side by side
        col1, col2, col3, _ = st.columns([3,3,1.5,1.5], vertical_alignment="bottom")

        # stone selection box
        with col1:
            options = ['Colored Stone', 'Blue/Pink Sapphire', 'Ruby-D', 'Emerald-D', 'Navratna-D', 'Coral-D',
                       'South Sea Pearls', 'Tanzanite', 'Turquoise', 'Tourmaline', 'Other/All stones-D'] 
            index = ['Colored Stone', 'Blue/Pink Sapphire', 'Ruby-D', 'Emerald-D', 'Navratna-D', 'Coral-D',
                     'South Sea Pearls', 'Tanzanite', 'Turquoise', 'Tourmaline', 'Other/All stones-D']
            st.selectbox("Select Gem Stone", 
                            options = options,
                            index = index.index(st.session_state['ss_dia_stones'][i]['dia_stone']),
                            key = f'dia_stone_{i}',
                            on_change=update_dia_breakdown,
                            args=("dia_stone", i))
            
        # stone carat
        with col2:
            st.text_input("Gem Stone Carat",
                          value=st.session_state['ss_dia_stones'][i]['dia_stone_ct'],
                          key=f'dia_stone_ct_{i}',
                          on_change=update_dia_breakdown,
                          args=("dia_stone_ct", i))
        
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
                if st.session_state['dia_stones_count'] > 0:     
                    st.button("Delete",
                              key=f'delete_dia_{i}',
                              on_click=del_callback,
                              args=(i, 'dia'))

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
                              args=('dia',),
                              key='add_dia')

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
            if price_d == "" or gold_wt_d == "" or dia_ct_d == "":
                missing_value()
                return
            val = pdf_dia_bd(dia_ct_price_d, 
                            item_code_d, 
                            price_d, 
                            gold_wt_d, 
                            dia_ct_d, 
                            st.session_state['ss_dia_stones'][:st.session_state['dia_stones_count']],
                            st.session_state['ss_di_perc'],
                            zip_code, tax_rate)
            if val == 'kitco_down':
                return kitco_down()
            if val == "no_calc":
                return no_calc()
            view_pdf = True
    return view_pdf
# import streamlit as st
# import base64

# def displayPDF(file):
#     # Opening file from file path
#     with open(file, "rb") as f:
#         base64_pdf = base64.b64encode(f.read()).decode('utf-8')

#     # Embedding PDF in HTML
#     pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

#     # Displaying File
#     st.markdown(pdf_display, unsafe_allow_html=True)

# displayPDF('F:\govindjis\gold\output.pdf')



# import streamlit as st
# import base64

# def displayPDF(file):
#     # Opening file from file path
#     with open(file, "rb") as f:
#         base64_pdf = base64.b64encode(f.read()).decode('utf-8')

#     # Embedding PDF in HTML
#     pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

#     # Displaying File
#     st.markdown(pdf_display, unsafe_allow_html=True)

# def main():

#     list_options = ["Pear", "Banana", "Guanabana"]

#     fruit = st.query_params.get("fruit", None)

#     if fruit:
#         f"## {fruit} is a great choice! "
#         st.image(f"https://placehold.co/200x100?text={fruit}", caption=f"{fruit}!")
#         displayPDF('output.pdf')

#     else:
#         st.title("High level MATH")
#         selection = st.selectbox("Select:", list_options, index=None)
#         if selection:
#             st.link_button(
#                 "See more!",
#                 url=f"http://localhost:8501/?fruit={selection}",
#                 use_container_width=True
#             )

# if __name__ == "__main__":
#     main()

# import streamlit as st

# # Load the CSS file
# with open("styles-copy.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# # Define HTML for each button
# button_html_red = '<a href="#" class="custom-button button-red">Red Button</a>'
# button_html_blue = '<a href="#" class="custom-button button-blue">Blue Button</a>'
# button_html_green = '<a href="#" class="custom-button button-green">Green Button</a>'
# button_html_orange = '<a href="#" class="custom-button button-orange">Orange Button</a>'
# button_html_purple = '<a href="#" class="custom-button button-purple">Purple Button</a>'

# # Display the buttons in Streamlit
# st.markdown(button_html_red, unsafe_allow_html=True)
# st.markdown(button_html_blue, unsafe_allow_html=True)
# st.markdown(button_html_green, unsafe_allow_html=True)
# st.markdown(button_html_orange, unsafe_allow_html=True)
# st.markdown(button_html_purple, unsafe_allow_html=True)


# import streamlit as st
# from streamlit_option_menu import option_menu

# # 3. CSS style definitions
# selected3 = option_menu(
#     menu_title=None,
#     options=["Home", "Upload",  "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal",
#     styles={
#         "container": {"padding": "0!important", "background-color": "#fafafa"},
#         "icon": {"color": "orange", "font-size": "25px"}, 
#         "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#         "nav-link-selected": {"background-color": "green"},
#     }
# )




    # # set font (font, styles(B, U, I, BU, ''))
    # # title logo
    # page_width = pdf.w
    # x_position = (page_width - 40) / 2
    # pdf.image("images\logo.png", x=x_position, y=10, w=40)
    # # pdf.set_font(family="Arial", style="B" ,size=20)
    # # pdf.cell(0, 9, txt="Govindji's", ln=True, align="C", border=0)
    # # address 
    # pdf.set_font(family="Arial", style="" ,size=7)
    # pdf.ln(8)
    # pdf.cell(0, 3, txt=f"4646 Dubai Way Suite 100   Frisco, TX 75034", ln=True, border=0, align="C")
    # pdf.ln(0.7)
    # # phone
    # pdf.cell(0, 3, txt=f"Phone: 972-231 6776   Facsimile: 972-231 3232", ln=True, border=0, align="C")

    # # Draw line
    # start_x = 10   
    # end_x = 200    
    # y_position = 27  
    # pdf.line(start_x, y_position, end_x, y_position)




# from fpdf import FPDF
# from PyPDF2 import PdfReader, PdfWriter
# from spot_price import get_price
# from calculations import scrap_gold


# # Function to generate the PDF
# def pdf_scrap_gold(data=""):

#     # Step 1: Read the existing PDF
#     reader = PdfReader("template.pdf")
#     writer = PdfWriter()

#     # create FPDF object
#     pdf = FPDF('L', 'mm', 'A5')
#     # add page
#     pdf.add_page()
#     pdf.ln(18) 

#     op, gp, time, date = get_price()

#     pdf.set_font(family="Helvetica", style="" ,size=9)
#     pdf.write(7, "Spot price on")
#     pdf.set_text_color(0, 0, 255)
#     pdf.write(7, " kitko.com ", link="https://www.kitco.com/")
#     pdf.set_text_color(0, 0, 0)
#     pdf.write(7, f" as of {date} on {time} is $")

#     # Set font to Helvetica (bold) for the price
#     pdf.set_font(family="Helvetica", style="B", size=9)
#     pdf.write(7, f"{op}")

#     # Switch back to regular style for the rest of the text
#     pdf.set_font(family="Helvetica", style="", size=9)
#     pdf.write(7, " per Troy Ounce")

#     pdf.ln(6)

#     # 24K
#     pdf.set_font(family="Helvetica", style="", size=9)
#     pdf.cell(45, 6, txt=f"24K gold one gram: ${gp} ", ln=False, border=0)
#     pdf.set_font(family="Helvetica", style="I", size=9)
#     pdf.cell(0, 6, txt="(1 Troy Ounce = 31.103 grams)", ln=True, border=0)
    
#     # 22K
#     gold_22k_gov = round(gp*0.916, 2)
#     gold_22k_oth = round(gp*0.8, 2)
#     pdf.set_font(family="Helvetica", style="", size=9)
#     pdf.cell(45, 6, txt=f"22K gold one gram: ${gold_22k_gov} ", ln=False, border=0)
#     pdf.set_font(family="Helvetica", style="I", size=9)
#     pdf.cell(70, 6, txt="(24K gold * 0.916 = 22K gold)", ln=False, border=0)
#     pdf.set_font(family="Helvetica", style="", size=10)
#     pdf.cell(45, 6, txt=f"22K gold one gram: ${gold_22k_oth} ", ln=True, border=0)

#     # refiner_cost
#     gold_trade_gov = round(gold_22k_gov-4.5, 2)
#     gold_trade_oth = round(gold_22k_oth-4.5, 2)
#     pdf.set_font(family="Helvetica", style="", size=9)
#     pdf.cell(45, 6, txt=f"22K gold one gram: ${gold_trade_gov} ", ln=False, border=0)
#     pdf.set_font(family="Helvetica", style="I", size=9)
#     pdf.cell(70, 6, txt="(after refinery cost)", ln=False, border=0)
#     pdf.set_font(family="Helvetica", style="", size=10)
#     pdf.cell(45, 6, txt=f"22K gold one gram: ${gold_trade_oth} ", ln=False, border=0)

#     pdf.ln(9)

#     # Set font for table
#     pdf.set_font("Helvetica", "B", size=9)

#     # Add table header
#     header = ['Description', 'Weight', 'Gold Karat', 'Cash Value', 'Trade-in Value']
#     for col_name in header:
#         pdf.cell(38, 8, col_name, border=1, align='C')
#     pdf.ln()

#     data = [
#         {'desc': 'Gold Necklace', 'gold_wt': '20.9', 'gold_kt': '22K', 'gold_pur_place': "Tanishq"},
#         {'desc': 'Gold Ring', 'gold_wt': '5.9', 'gold_kt': '18K', 'gold_pur_place': "Malabar Gold"},
#         {'desc': 'Gold Bracelet', 'gold_wt': '15.9', 'gold_kt': '14K', 'gold_pur_place': "Kalyan Jewellers"},
#         {'desc': 'Gold Earrings', 'gold_wt': '8.9', 'gold_kt': '10K', 'gold_pur_place': "Joyalukkas"},
#         {'desc': 'Gold Chain', 'gold_wt': '12.9', 'gold_kt': '24K', 'gold_pur_place': "PC Jeweller"},
#     ]
    
#     pdf.set_font("Helvetica", size=8)
#     # Add table rows
#     for item in data:
#         wt, kt, place = item['gold_wt'], item['gold_kt'], item['gold_pur_place']
#         cash, trade, marker = scrap_gold(gp, wt, kt, place)
#         pdf.cell(38, 8, item['desc']+marker, border=1, align='C')
#         pdf.cell(38, 8, wt, border=1, align='C')
#         pdf.cell(38, 8, kt, border=1, align='C')
#         pdf.cell(38, 8, str(cash), border=1, align='C')
#         pdf.cell(38, 8, str(trade), border=1, align='C')
#         pdf.ln()
        

#     # Save the temporary PDF to a file
#     temp_pdf_path = "temp.pdf"
#     pdf.output(temp_pdf_path)

#     # Merge the temporary PDF with the original PDF
#     with open(temp_pdf_path, "rb") as temp_pdf_file:
#         temp_reader = PdfReader(temp_pdf_file)
#         for i, page in enumerate(reader.pages):
#             if i == 0:
#                 page.merge_page(temp_reader.pages[0])
#             writer.add_page(page)
        
#         # Add the extra pages created by the text
#         for j in range(1, len(temp_reader.pages)):
#             writer.add_page(temp_reader.pages[j])

#     # Write the modified content to a new PDF
#     with open("output1.pdf", "wb") as output_pdf_file:
#         writer.write(output_pdf_file)
    
# pdf_scrap_gold()





# import streamlit as st
# from streamlit_extras.stylable_container import stylable_container

# # Initialize session state for tracking the widgets and their values
# if 'widget_count' not in st.session_state:
#     st.session_state['widget_count'] = 1  # Start with at least one widget
# if 'widget_data' not in st.session_state:
#     st.session_state['widget_data'] = [{
#         'text': '',
#         'checkbox1': False,
#         'dropdown': 'Option 1'
#     }]  # Start with initial data for one widget

# # Function to add widgets
# def add_widgets():
#     st.session_state['widget_count'] += 1
#     st.session_state['widget_data'].append({
#         'text': '',
#         'checkbox1': False,
#         'dropdown': 'Option 1'
#     })

# # Function to delete a widget
# def delete_widget(index):
#     if st.session_state['widget_count'] > 1:  # Ensure at least one widget remains
#         st.session_state['widget_count'] -= 1
#         st.session_state['widget_data'].pop(index)

# # Display and update the widgets
# for i in range(st.session_state['widget_count']):
#     st.write(f"### Widget Set {i+1}")
    
#     # Text input
#     text_value = st.text_input(f"Text Input {i+1}", 
#                                value=st.session_state['widget_data'][i]['text'],
#                                key=f'text_{i}')
#     st.session_state['widget_data'][i]['text'] = text_value
    
#     # Checkboxes
#     checkbox1_value = st.checkbox(f"Checkbox 1 - Set {i+1}", 
#                                   value=st.session_state['widget_data'][i]['checkbox1'],
#                                   key=f'checkbox1_{i}')
#     st.session_state['widget_data'][i]['checkbox1'] = checkbox1_value
    
#     # Dropdown menu
#     dropdown_value = st.selectbox(f"Dropdown {i+1}", 
#                                   options=["Option 1", "Option 2", "Option 3"],
#                                   index=["Option 1", "Option 2", "Option 3"].index(st.session_state['widget_data'][i]['dropdown']),
#                                   key=f'dropdown_{i}')
#     st.session_state['widget_data'][i]['dropdown'] = dropdown_value
    
#     # Delete button for the widget
#     if st.session_state['widget_count'] > 1:
#         with stylable_container(
#                     key=f'delete_{i}',
#                     css_styles="""
#                         button{
#                             background-color: red;
#                             color: white;
#                             border-radius: 20px;
#                         }
#                         """
#                 ):
#             if st.button(f"Delete Widget Set {i+1}", key=f'delete_{i}'):
#                 delete_widget(i)
#                 st.rerun()
#     else:
#         st.write("Cannot delete the last remaining widget.")

# # Button to trigger adding of widgets
# if st.button("Add Widgets"):
#     add_widgets()
#     st.rerun()




# import streamlit as st
# from streamlit_option_menu import option_menu

# # 1. as sidebar menu
# with st.sidebar:
#     selected = option_menu("Main Menu", ["Home", 'Settings'], 
#         icons=['house', 'gear'], menu_icon="cast", default_index=1)
#     selected

# # 2. horizontal menu
# selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal")
# selected2

# # 3. CSS style definitions
# selected3 = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal",
#     styles={
#         "container": {"padding": "0!important", "background-color": "#fafafa"},
#         "icon": {"color": "orange", "font-size": "25px"}, 
#         "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#         "nav-link-selected": {"background-color": "green"},
#     }
# )

# # 4. Manual item selection
# if st.session_state.get('switch_button', False):
#     st.session_state['menu_option'] = (st.session_state.get('menu_option', 0) + 1) % 4
#     manual_select = st.session_state['menu_option']
# else:
#     manual_select = None
    
# selected4 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     orientation="horizontal", manual_select=manual_select, key='menu_4')
# st.button(f"Move to Next {st.session_state.get('menu_option', 1)}", key='switch_button')
# selected4

# 5. Add on_change callback
# def on_change(key):
#     selection = st.session_state[key]
#     st.write(f"Selection changed to {selection}")
    
# selected5 = option_menu(None, ["Homee", "Uploade", "Tasksee", 'Settingse'],
#                         icons=['house', 'cloud-upload', "list-task", 'gear'],
#                         on_change=on_change, 
#                         key='menu_5', 
#                         orientation="horizontal")
# selected5




# import streamlit as st

# # Initialize selectbox count in session state if not already present
# if 'selectbox_count' not in st.session_state:
#     st.session_state.selectbox_count = 0

# # Callback to increase selectbox count and show a custom message
# def add_callback(increment, message):
#     st.session_state.selectbox_count += increment
#     st.write(message)

# # Display selectboxes dynamically
# for i in range(st.session_state.selectbox_count):
#     st.selectbox(f"Options {i + 1}:", ("a", "b", "c"))

# # Add the button at the bottom, passing two arguments to the callback
# add_clicked = st.button(
#     "Add", 
#     on_click=add_callback, 
#     args=(1, "A new selectbox has been added!"),  # Passing 1 and a custom message
#     help="Add a new test", 
#     key="Add"
# )




# from fpdf import FPDF

# def template():

#     # create FPDF object
#     pdf = FPDF('L', 'mm', 'A5')

#     # add page
#     pdf.add_page()

#     # set background color (RGB format)
#     pdf.set_fill_color(198, 234, 211)  # Light blue background color
#     pdf.rect(0, 0, 210, 148, 'F')  # Fills the entire A5 landscape page

#     # set font (font, styles(B, U, I, BU, ''))
#     # title logo
#     page_width = pdf.w
#     x_position = (page_width - 50) / 2
#     pdf.image("images\logo.png", x=x_position, y=10, w=50)
#     # pdf.set_font(family="Arial", style="B" ,size=20)
#     # pdf.cell(0, 9, txt="Govindji's", ln=True, align="C", border=0)
#     # address 
#     pdf.set_font(family="Arial", style="" ,size=7)
#     pdf.ln(11)
#     pdf.cell(65, 3, txt=f"4646 Dubai Way Suite 100   Frisco, TX 75034", border=0, align="R")
#     pdf.cell(60, 3, txt=f"", border=0, align="C")
#     pdf.cell(65, 3, txt=f"Phone: 972-231 6776   www.govindjis.com", border=0, align="L")

#     # Draw line
#     start_x = 10   
#     end_x = 200    
#     y_position = 27  
#     pdf.line(start_x, y_position, end_x, y_position)

#     pdf.output("template.pdf")

# template()


# from fpdf import FPDF

# def template_a4():

#     # create FPDF object for A4 landscape
#     pdf = FPDF('L', 'mm', 'A4')

#     # add page
#     pdf.add_page()

#     # set background color (RGB format)
#     pdf.set_fill_color(198, 234, 211)  # Light blue background color
#     pdf.rect(0, 0, 297, 210, 'F')  # Fills the entire A4 landscape page

#     # set font (font, styles(B, U, I, BU, ''))
#     # title logo
#     page_width = pdf.w
#     x_position = (page_width - 50) / 2  # Adjust for A4 width
#     pdf.image("images\logo.png", x=x_position, y=10, w=50)

#     # address
#     pdf.set_font(family="Arial", style="", size=9)  # Increased font size for A4
#     pdf.ln(15)  # Increased line spacing for A4
#     pdf.cell(100, 5, txt=f"4646 Dubai Way Suite 100   Frisco, TX 75034", border=0, align="R")
#     pdf.cell(80, 5, txt=f"", border=0, align="C")
#     pdf.cell(100, 5, txt=f"Phone: 972-231 6776   www.govindjis.com", border=0, align="L")

#     # Draw line
#     start_x = 10  # Starting x-position of the line
#     end_x = 287  # Ending x-position of the line for A4 landscape width
#     y_position = 35  # Adjusted y-position for A4
#     pdf.line(start_x, y_position, end_x, y_position)

#     # Save the PDF
#     pdf.output("template.pdf")

# # Call the function to create the template
# template_a4()





# import streamlit as st

# # Initialize session state variables for x and y
# if "x" not in st.session_state:
#     st.session_state.x = 50

# if "y" not in st.session_state:
#     st.session_state.y = 50

# # Callback functions to update x and y based on the equation x + y = 100
# def update_x():
#     st.session_state.y = 100 - st.session_state.x

# def update_y():
#     st.session_state.x = 100 - st.session_state.y

# # Slider for x with a callback to update y
# st.slider("Select the value of x", 
#           min_value=0, max_value=100, 
#           value=st.session_state.x, 
#           key="x", on_change=update_x)

# # Slider for y with a callback to update x
# st.slider("Select the value of y", 
#             min_value=0, max_value=100, 
#           value=st.session_state.y, 
#                 key="y", on_change=update_y)

# # Display the current values of x and y
# st.write(f"Current value of x: {st.session_state.x}")
# st.write(f"Current value of y: {st.session_state.y}")


#Get the browser details
# import streamlit as st
# from streamlit_js_eval import get_user_agent
# from user_agents import parse

# # Retrieve the user agent

# print('#############################################################################')
# # Parse the user agent string
# try:
#     user_agent_str = get_user_agent()
#     user_agent = parse(user_agent_str)
# except Exception as e:
#     val = e
# print(user_agent_str)

# # Extract browser information
# browser_name = user_agent.browser.family
# browser_version = user_agent.browser.version_string
# print('****************************************************************************')
# Display the result
# st.write(user_agent_str)
# st.write(user_agent)
# st.write(f"You are using: {browser_name} version {browser_version}")


# import streamlit as st
# from browser_detection import browser_detection_engine

# def get():
#     st.session_state['browser'] = browser_detection_engine(singleRun=False)

# # Retrieve the browser info from session state
# get()

# # Display the browser info (for debugging)
# st.write('**************************************')
# st.write(st.session_state['browser']['name']) 



# import streamlit as st

# left, middle, right = st.columns(3)
# if left.button("Plain button", use_container_width=True):
#     left.markdown("You clicked the plain button.")
# if middle.button("", icon="😃", use_container_width=True):
#     middle.markdown("You clicked the emoji button.")
# if right.button("Material button", icon=":material/help:", use_container_width=True):
#     right.markdown("You clicked the Material button.")

import streamlit as st

# Create columns with specified widths
colm1, colm2, colm3 = st.columns([3, 3, 3], gap="medium", vertical_alignment='center')

# Add content to the first column
with colm1:
    st.write("### Scrap Gold Purchase")

# Add an invisible spacer in the second column for alignment
with colm2:
    st.write("hello")  # Leave blank to create spacing

# Add the checkbox in the third column aligned to the right
with colm3:
    # Use Markdown with custom CSS to align the checkbox to the right
    st.markdown(
        """
        <style>
            .stCheckbox {
                display: flex;
                justify-content: flex-end;
                align-items: right;
                height: 100%;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Streamlit native checkbox to handle the state (for interaction purposes)
    show_formula = st.checkbox("Show Formula", key="show_calc", value=st.session_state.get('show_calc', False), disabled=False)

# Check the checkbox state and display the result
if show_formula:
    st.write("The checkbox is checked.")
else:
    st.write("The checkbox is unchecked.")


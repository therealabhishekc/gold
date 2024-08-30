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




from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter
from spot_price import get_price
from calculations import scrap_gold


# Function to generate the PDF
def pdf_scrap_gold(data=""):

    # Step 1: Read the existing PDF
    reader = PdfReader("template.pdf")
    writer = PdfWriter()

    # create FPDF object
    pdf = FPDF('L', 'mm', 'A5')
    # add page
    pdf.add_page()
    pdf.ln(18) 

    op, gp, time, date = get_price()

    pdf.set_font(family="Helvetica", style="" ,size=9)
    pdf.write(7, "Spot price on")
    pdf.set_text_color(0, 0, 255)
    pdf.write(7, " kitko.com ", link="https://www.kitco.com/")
    pdf.set_text_color(0, 0, 0)
    pdf.write(7, f" as of {date} on {time} is $")

    # Set font to Helvetica (bold) for the price
    pdf.set_font(family="Helvetica", style="B", size=9)
    pdf.write(7, f"{op}")

    # Switch back to regular style for the rest of the text
    pdf.set_font(family="Helvetica", style="", size=9)
    pdf.write(7, " per Troy Ounce")

    pdf.ln(6)

    # 24K
    pdf.set_font(family="Helvetica", style="", size=9)
    pdf.cell(45, 6, txt=f"24K gold one gram: ${gp} ", ln=False, border=0)
    pdf.set_font(family="Helvetica", style="I", size=9)
    pdf.cell(0, 6, txt="(1 Troy Ounce = 31.103 grams)", ln=True, border=0)
    
    # 22K
    gold_22k_gov = round(gp*0.916, 2)
    gold_22k_oth = round(gp*0.8, 2)
    pdf.set_font(family="Helvetica", style="", size=9)
    pdf.cell(45, 6, txt=f"22K gold one gram: ${gold_22k_gov} ", ln=False, border=0)
    pdf.set_font(family="Helvetica", style="I", size=9)
    pdf.cell(70, 6, txt="(24K gold * 0.916 = 22K gold)", ln=False, border=0)
    pdf.set_font(family="Helvetica", style="", size=10)
    pdf.cell(45, 6, txt=f"22K gold one gram: ${gold_22k_oth} ", ln=True, border=0)

    # refiner_cost
    gold_trade_gov = round(gold_22k_gov-4.5, 2)
    gold_trade_oth = round(gold_22k_oth-4.5, 2)
    pdf.set_font(family="Helvetica", style="", size=9)
    pdf.cell(45, 6, txt=f"22K gold one gram: ${gold_trade_gov} ", ln=False, border=0)
    pdf.set_font(family="Helvetica", style="I", size=9)
    pdf.cell(70, 6, txt="(after refinery cost)", ln=False, border=0)
    pdf.set_font(family="Helvetica", style="", size=10)
    pdf.cell(45, 6, txt=f"22K gold one gram: ${gold_trade_oth} ", ln=False, border=0)

    pdf.ln(9)

    # Set font for table
    pdf.set_font("Helvetica", "B", size=9)

    # Add table header
    header = ['Description', 'Weight', 'Gold Karat', 'Cash Value', 'Trade-in Value']
    for col_name in header:
        pdf.cell(38, 8, col_name, border=1, align='C')
    pdf.ln()

    data = [
        {'desc': 'Gold Necklace', 'gold_wt': '20.9', 'gold_kt': '22K', 'gold_pur_place': "Tanishq"},
        {'desc': 'Gold Ring', 'gold_wt': '5.9', 'gold_kt': '18K', 'gold_pur_place': "Malabar Gold"},
        {'desc': 'Gold Bracelet', 'gold_wt': '15.9', 'gold_kt': '14K', 'gold_pur_place': "Kalyan Jewellers"},
        {'desc': 'Gold Earrings', 'gold_wt': '8.9', 'gold_kt': '10K', 'gold_pur_place': "Joyalukkas"},
        {'desc': 'Gold Chain', 'gold_wt': '12.9', 'gold_kt': '24K', 'gold_pur_place': "PC Jeweller"},
    ]
    
    pdf.set_font("Helvetica", size=8)
    # Add table rows
    for item in data:
        wt, kt, place = item['gold_wt'], item['gold_kt'], item['gold_pur_place']
        cash, trade, marker = scrap_gold(gp, wt, kt, place)
        pdf.cell(38, 8, item['desc']+marker, border=1, align='C')
        pdf.cell(38, 8, wt, border=1, align='C')
        pdf.cell(38, 8, kt, border=1, align='C')
        pdf.cell(38, 8, str(cash), border=1, align='C')
        pdf.cell(38, 8, str(trade), border=1, align='C')
        pdf.ln()
        

    # Save the temporary PDF to a file
    temp_pdf_path = "temp.pdf"
    pdf.output(temp_pdf_path)

    # Merge the temporary PDF with the original PDF
    with open(temp_pdf_path, "rb") as temp_pdf_file:
        temp_reader = PdfReader(temp_pdf_file)
        for i, page in enumerate(reader.pages):
            if i == 0:
                page.merge_page(temp_reader.pages[0])
            writer.add_page(page)
        
        # Add the extra pages created by the text
        for j in range(1, len(temp_reader.pages)):
            writer.add_page(temp_reader.pages[j])

    # Write the modified content to a new PDF
    with open("output1.pdf", "wb") as output_pdf_file:
        writer.write(output_pdf_file)
    
pdf_scrap_gold()







# from PyPDF2 import PdfReader, PdfWriter
# from fpdf import FPDF

# def add_text_to_pdf(text, start_page=0):
#     # Step 1: Read the existing PDF
#     reader = PdfReader("template.pdf")
#     writer = PdfWriter()

#     # Create a temporary PDF with the text overlay
#     pdf = FPDF('L', 'mm', 'A5')
#     pdf.set_font("Arial", size=12)
    
#     # Split the text into lines
#     lines = text.split('\n')
#     line_height = pdf.font_size * 2.5
#     max_lines_per_page = int((148 - 10) / line_height)  # A4 size: 210x297mm

#     current_page = start_page
#     line_counter = 0
#     flag = True
#     while line_counter < len(lines):
#         pdf.add_page()
#         if flag:
#             pdf.ln(10)
#             flag = False
        
#         # Write lines to the current page
#         for i in range(max_lines_per_page):
#             if line_counter >= len(lines):
#                 break
#             pdf.text(10, 10 + i * line_height, lines[line_counter])
#             line_counter += 1
        
#         current_page += 1

#     # Save the temporary PDF to a file
#     temp_pdf_path = "temp.pdf"
#     pdf.output(temp_pdf_path)

#     # Merge the temporary PDF with the original PDF
#     with open(temp_pdf_path, "rb") as temp_pdf_file:
#         temp_reader = PdfReader(temp_pdf_file)
#         for i, page in enumerate(reader.pages):
#             if i == start_page:
#                 page.merge_page(temp_reader.pages[0])
#             writer.add_page(page)
        
#         # Add the extra pages created by the text
#         for j in range(1, len(temp_reader.pages)):
#             writer.add_page(temp_reader.pages[j])

#     # Write the modified content to a new PDF
#     with open("output1.pdf", "wb") as output_pdf_file:
#         writer.write(output_pdf_file)

# # Example usage:
# input_pdf = "template.pdf"
# text = "This is a very long ahh text...\n" * 100  # Example long text
# add_text_to_pdf(text, start_page=0)







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




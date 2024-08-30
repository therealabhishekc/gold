from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter
from spot_price import get_price
from calculations import scrap_gold


# Function to generate the PDF
def pdf_scrap_gold(data):

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
    pdf.write(7, f"{round(op, 2)}")

    # Switch back to regular style for the rest of the text
    pdf.set_font(family="Helvetica", style="", size=9)
    pdf.write(7, " per Troy Ounce")

    pdf.ln(6)

    # 24K
    pdf.set_font(family="Helvetica", style="", size=9)
    pdf.cell(45, 6, txt=f"24K gold one gram: ${round(gp, 2)} ", ln=False, border=0)
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
    with open("output.pdf", "wb") as output_pdf_file:
        writer.write(output_pdf_file)

# Function to generate the PDF
def sample_pdf(prompt1="", prompt2="", prompt3="", prompt4=""):
    # create FPDF object
    pdf = FPDF('L', 'mm', 'A5')

    # add page
    pdf.add_page()

    # set font (font, styles(B, U, I, BU, ''))
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Generated PDF", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Prompt 1: {prompt1}", ln=True)
    pdf.cell(200, 10, txt=f"Prompt 2: {prompt2}", ln=True)
    pdf.cell(200, 10, txt=f"Prompt 3: {prompt3}", ln=True)
    pdf.cell(200, 10, txt=f"Prompt 4: {prompt4}", ln=True)
    
    # Save the PDF to a file
    pdf.output("output.pdf")
    
    return 
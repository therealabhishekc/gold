from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter
from spot_price import get_price, CustomError
from calculations import scrap_gold, gold_bd, hyd_bd, ant_bd


# Function to generate the Scrap gold purhcase PDF
def pdf_scrap_gold(data, show_calc):

    #Read the existing PDF
    reader = PdfReader("template.pdf")
    writer = PdfWriter()

    # create FPDF object
    pdf = FPDF('L', 'mm', 'A5')
    # add page
    pdf.add_page()
    
    pdf.ln(18) 

    try:
        op, gp, time, date = get_price()
    except CustomError as e:
        return "kitco_down"
    op = op - 1
    gp = round(op/31.105, 2)

    pdf.set_font(family="Helvetica", style="" ,size=9)
    pdf.write(7, "Spot price on")
    #pdf.set_text_color(0, 0, 255)
    pdf.write(7, " kitko.com", link="https://www.kitco.com/")
    #pdf.set_text_color(0, 0, 0)
    pdf.write(7, f" as of {date} on {time} is $")

    # Set font to Helvetica (bold) for the price
    pdf.set_font(family="Helvetica", style="B", size=9)
    pdf.write(7, f"{round(op, 2)}")

    # Switch back to regular style for the rest of the text
    pdf.set_font(family="Helvetica", style="", size=9)
    pdf.write(7, " per Troy Ounce")

    pdf.ln(6)

    if show_calc:
        pdf.ln(1)
        # set headers
        pdf.set_font(family="Helvetica", style="B", size=9)
        pdf.cell(90, 6, txt=f"Purchased at Govindji's", ln=False)
        pdf.cell(35, 6, txt=f"Purchased at other jeweller", ln=True)

        # 24K
        pdf.set_font(family="Helvetica", style="", size=9)
        pdf.cell(40, 6, txt=f"24K gold one gram: ${round(gp, 2)} ", ln=False, border=0)
        pdf.set_font(family="Helvetica", style="I", size=8)
        pdf.cell(50, 6, txt="(1 Troy Ounce = 31.103 grams)", ln=False, border=0)
        pdf.set_font(family="Helvetica", style="", size=9)
        pdf.cell(40, 6, txt=f"24K gold one gram: ${round(gp, 2)} ", ln=False, border=0)
        pdf.set_font(family="Helvetica", style="I", size=8)
        pdf.cell(40, 6, txt="(1 Troy Ounce = 31.103 grams)", ln=True, border=0)
        
        # 22K
        gold_22k_gov = round(gp*0.916, 2)
        gold_22k_oth = round(gp*0.8, 2)
        pdf.set_font(family="Helvetica", style="", size=9)
        pdf.cell(40, 6, txt=f"22K gold one gram: ${gold_22k_gov} ", ln=False, border=0)
        pdf.set_font(family="Helvetica", style="I", size=8)
        pdf.cell(50, 6, txt="(24K gold * 0.916 = 22K gold)", ln=False, border=0)
        pdf.set_font(family="Helvetica", style="", size=9)
        pdf.cell(40, 6, txt=f"22K gold one gram: ${gold_22k_oth} ", ln=False, border=0)
        pdf.set_font(family="Helvetica", style="I", size=8)
        pdf.cell(40, 6, txt="(24K gold * 0.8 = 22K gold)", ln=True, border=0)

        # refiner_cost
        gold_trade_gov = round(gold_22k_gov-4.5, 2)
        gold_trade_oth = round(gold_22k_oth-4.5, 2)
        pdf.set_font(family="Helvetica", style="", size=9)
        pdf.cell(40, 6, txt=f"22K gold one gram: ${gold_trade_gov} ", ln=False, border=0)
        pdf.set_font(family="Helvetica", style="I", size=8)
        pdf.cell(50, 6, txt="(after refinery cost [-4.5])", ln=False, border=0)
        pdf.set_font(family="Helvetica", style="", size=9)
        pdf.cell(40, 6, txt=f"22K gold one gram: ${gold_trade_oth} ", ln=False, border=0)
        pdf.set_font(family="Helvetica", style="I", size=8)
        pdf.cell(50, 6, txt="(after refinery cost [-4.5])", ln=False, border=0)

        pdf.ln(9)

    else:
        pdf.ln(2)

    # Set font for table
    pdf.set_font("Helvetica", "B", size=9)

    # Add table header
    header = ['Description', 'Weight', 'Gold Karat', 'Cash Value', 'Trade-in Value']
    for col_name in header:
        pdf.cell(38, 8, col_name, border=1, align='C')
    pdf.ln()

    total_cash, total_trade = 0, 0
    
    pdf.set_font("Helvetica", size=9)
    # Add table rows
    for item in data:
        wt, kt, place = item['gold_wt'], item['gold_kt'], item['gold_pur_place']
        cash, trade, marker = scrap_gold(gp, wt, kt, place)
        total_cash += cash
        total_trade += trade
        pdf.cell(38, 8, item['desc']+marker, border=1, align='C')
        pdf.cell(38, 8, str(wt), border=1, align='C')
        pdf.cell(38, 8, str(kt), border=1, align='C')
        pdf.cell(38, 8, "$"+str(cash), border=1, align='C')
        pdf.cell(38, 8, "$"+str(trade), border=1, align='C')
        pdf.ln()

    pdf.set_font("Helvetica", "BI", size=10)
    pdf.cell(76, 8)        
    pdf.cell(38, 8, txt=f"Total", align='C', border=0)
    pdf.cell(38, 8, txt=f"${total_cash}", align='C', border=0)
    pdf.cell(38, 8, txt=f"${total_trade}", align='C', border=0)


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


# Function to generate the gold breakdown PDF
def pdf_gold_bd(item_code, price, gold_wt):

    #Read the existing PDF
    reader = PdfReader("template.pdf")
    writer = PdfWriter()

    # create FPDF object
    pdf = FPDF('L', 'mm', 'A5')
    
    # add page
    pdf.add_page()
    
    pdf.ln(18) 

    pdf.set_font(family="Helvetica", style="B" ,size=12)
    pdf.cell(70, 9, txt=f"Detailed Breakdown for {item_code.upper()}",
             border=False,
             ln=True)

    try:
        op, gp, time, date = get_price()
    except CustomError as e:
        return "kitco_down"

    # disp kitko prices
    pdf.set_font(family="Helvetica", style="" ,size=9)
    pdf.write(7, "Spot price on")
    #pdf.set_text_color(0, 0, 255)
    pdf.write(7, " kitko.com", link="https://www.kitco.com/")
    #pdf.set_text_color(0, 0, 0)
    pdf.write(7, f" as of {date} on {time} is ")
    pdf.set_font(family="Helvetica", style="B", size=9)
    pdf.write(7, f"${round(op, 2)}")
    pdf.set_font(family="Helvetica", style="", size=9)
    pdf.write(7, " per Troy Ounce")

    pdf.ln()

    # 24K
    pdf.set_font(family="Helvetica", style="", size=9)
    pdf.cell(40, 6, txt=f"24K gold one gram: ${round(gp, 2)} ", ln=False, border=0)
    pdf.set_font(family="Helvetica", style="I", size=8)
    pdf.cell(50, 6, txt="(1 Troy Ounce = 31.103 grams)", ln=True, border=0)
    
    # 22K
    gold_22k = round(gp*0.93, 2)
    pdf.set_font(family="Helvetica", style="B", size=9)
    pdf.cell(42, 6, txt=f"22K gold one gram: ${gold_22k} ", ln=False, border=0)
    pdf.set_font(family="Helvetica", style="I", size=8)
    pdf.cell(50, 6, txt="(24K gold * 0.93 = 22K gold)", ln=True, border=0)

    pdf.ln(4)

    pdf.set_font(family="Helvetica", style="B", size=10)
    pdf.cell(50, 6, txt=f"Net weight: {gold_wt} grams")

    pdf.ln(12)

    # column headers
    pdf.cell(25, 8, txt=f"Gold", border=True, align='C')
    pdf.cell(10, 8)
    pdf.cell(25, 8, txt=f"Labor", border=True, align='C')
    pdf.cell(10, 8)
    pdf.cell(25, 8, txt=f"Margin", border=True, align='C')
    pdf.cell(10, 8)
    pdf.cell(25, 8, txt=f"Duty", border=True, align='C', ln=True)

    price_gold, price_labor, price_profit, price_duty, price_pre_tax = gold_bd(price, gold_wt, gold_22k)

    #actual values
    pdf.cell(25, 8, txt=f"${price_gold}", border=True, align='C')
    pdf.cell(10, 8)
    pdf.cell(25, 8, txt=f"${price_labor}", border=True, align='C')
    pdf.cell(10, 8)
    pdf.cell(25, 8, txt=f"${price_profit}", border=True, align='C')
    pdf.cell(10, 8)
    pdf.cell(25, 8, txt=f"${price_duty}", border=True, align='C', ln=True)

    # percentages and stone/ct
    pdf.set_font(family="Helvetica", style="I", size=8)
    lbr = round((price_labor/price_pre_tax)*100, 2)
    prf = round((price_labor/price_pre_tax)*100, 2)
    pdf.cell(35, 8)
    pdf.cell(25, 8, txt=f"{lbr}%", border=0, align='C')
    pdf.cell(10, 8)
    pdf.cell(25, 8, txt=f"{prf}%", border=0, align='C')
    pdf.cell(10, 8)
    pdf.cell(25, 8, txt=f"6.5%", border=0, align='C')

    pdf.ln(10)

    pdf.set_font(family="Helvetica", style="", size=10)
    pdf.cell(105, 8)
    pdf.cell(25, 8, txt=f"${price_pre_tax}", align='C', border=0)
    pdf.cell(25, 8, txt=f"  +  Tax (8.25%)")

    pdf.ln(13)
    pdf.set_font(family="Helvetica", style="B", size=10)
    pdf.cell(70, 8)
    pdf.cell(35, 8, txt=f"Final Price:", align='R')
    pdf.cell(25, 8, txt=f"${price}", align='C', border=1)

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


# Function to generate the hyderabadi breakdown PDF
def pdf_hyd_bd(item_code, price, gross_wt, hyd_stones):

    total_stone_ct = 0
    stones = {}
    
    # go through each stone 
    for stone in hyd_stones:
        stones[stone['hyd_stone']] = stone['hyd_ct']
        total_stone_ct += stone['hyd_ct']
    
    total_stone_ct = round(total_stone_ct, 2)

    total_stone_wt = round(total_stone_ct/5, 2)
    net_wt = gross_wt - total_stone_wt

    try:
        op, gp, time, date = get_price()
    except CustomError as e:
        return "kitco_down"
    gold_22k = round(gp*0.93, 2)

    price_gold, price_per_stone, price_stones, price_labor, price_profit, price_duty, price_pre_tax = \
        hyd_bd(item_code, price, net_wt, gold_22k, stones)
    
    #Read the existing PDF
    reader = PdfReader("template.pdf")
    writer = PdfWriter()

    # create FPDF object
    pdf = FPDF('L', 'mm', 'A5')
    # add page
    pdf.add_page()
    pdf.ln(18) 

    pdf.set_font(family="Helvetica", style="B" ,size=11.5)
    pdf.cell(70, 7, txt=f"Detailed Breakdown for {item_code.upper()}",
             border=False,
             ln=True)

    # disp kitko prices
    pdf.set_font(family="Helvetica", style="" ,size=8)
    pdf.write(7, "Spot price on")
    #pdf.set_text_color(0, 0, 255)
    pdf.write(7, " kitko.com", link="https://www.kitco.com/")
    #pdf.set_text_color(0, 0, 0)
    pdf.write(7, f" as of {date} on {time} is ")
    pdf.set_font(family="Helvetica", style="B", size=8)
    pdf.write(7, f"${round(op, 2)}")
    pdf.set_font(family="Helvetica", style="", size=8)
    pdf.write(7, " per Troy Ounce")

    pdf.ln(4.6)

    # 24K
    pdf.set_font(family="Helvetica", style="", size=8)
    pdf.cell(40, 6, txt=f"24K gold one gram: ${round(gp, 2)} ", ln=False, border=0)
    pdf.set_font(family="Helvetica", style="I", size=7)
    pdf.cell(50, 6, txt="(1 Troy Ounce = 31.103 grams)", ln=True, border=0)
    
    pdf.ln(-1.8)

    # 22K
    pdf.set_font(family="Helvetica", style="B", size=8)
    pdf.cell(40, 6, txt=f"22K gold one gram: ${gold_22k} ", ln=False, border=0)
    pdf.set_font(family="Helvetica", style="I", size=7)
    pdf.cell(50, 6, txt="(24K gold * 0.93 = 22K gold)", ln=True, border=0)

    pdf.ln(2)

    pdf.set_font(family="Helvetica", style="B", size=10)
    pdf.cell(50, 6, txt=f"Gross weight: {gross_wt} grams", border=0, ln=True)
    pdf.ln(1.5)
    pdf.cell(65, 6, txt=f"Total Gems weight: {total_stone_wt} grams", border=0)
    pdf.cell(65, 6, txt=f"Net Gold weight: {round(net_wt, 2)} grams", border=0)

    pdf.ln(5)

    cnt = 0
    formula = ["Net weight = Gross weight - Total Gems weight",
               "Total Gems Weight = Total Gems Carat / 5",
               "5 carats = 1 gram"]

    for stone in stones.keys():
        pdf.set_font(family="Helvetica", style="", size=7)
        pdf.cell(20, 5, txt=f"{stone} : ", border=0, align='R')
        pdf.cell(12, 5, txt=f"{stones[stone]}ct", border=0, align='L')
        pdf.cell(33, 5, txt=f"PPC: ${price_per_stone[stone]}", border=0, align='L')
        if cnt<2:
            pdf.set_font(family="Helvetica", style="I", size=7)
            pdf.cell(65, 5, txt=f"{formula[cnt]}", border=0)
            cnt += 1
        pdf.ln(2.8)

    pdf.set_font(family="Helvetica", style="BI", size=7)
    pdf.ln(0.8)
    pdf.cell(20, 5, txt=f"Total Carat : ", border=0, align='R')
    pdf.cell(12, 5, txt=f"{total_stone_ct}ct", border=0, align='L')
    pdf.cell(33, 5, txt=f"${price_stones}", border=0, align='L')
    pdf.set_font(family="Helvetica", style="I", size=7)
    if cnt<2:
        pdf.set_font(family="Helvetica", style="I", size=7)
        pdf.cell(65, 5, txt=f"{formula[cnt]}", border=0)
    
    pdf.ln(7)

    pdf.set_font(family="Helvetica", style="B", size=10)

    # column headers
    pdf.cell(22, 8, txt=f"Gold", border=True, align='C')
    pdf.cell(8, 8)
    pdf.cell(22, 8, txt=f"Gems", border=True, align='C')
    pdf.cell(8, 8)
    pdf.cell(22, 8, txt=f"Labor", border=True, align='C')
    pdf.cell(8, 8)
    pdf.cell(22, 8, txt=f"Margin", border=True, align='C')
    pdf.cell(8, 8)
    pdf.cell(22, 8, txt=f"Duty", border=True, align='C', ln=True)
    
    #actual values
    pdf.cell(22, 7, txt=f"${price_gold}", border=True, align='C')
    pdf.cell(8, 7)
    pdf.cell(22, 7, txt=f"${price_stones}", border=True, align='C')
    pdf.cell(8, 7)
    pdf.cell(22, 7, txt=f"${price_labor}", border=True, align='C')
    pdf.cell(8, 7)
    pdf.cell(22, 7, txt=f"${price_profit}", border=True, align='C')
    pdf.cell(8, 7)
    pdf.cell(22, 7, txt=f"${price_duty}", border=True, align='C', ln=1)

    # percentages and stone/ct
    pdf.set_font(family="Helvetica", style="I", size=7)
    ppc = round(price_stones/total_stone_ct, 2)
    lbr = round((price_labor/price_pre_tax)*100, 2)
    prf = round((price_labor/price_pre_tax)*100, 2)
    pdf.cell(30, 7)
    pdf.cell(22, 7, txt=f"(Avg: {ppc}/ct)", border=0, align='C')
    pdf.cell(8, 7)
    pdf.cell(22, 7, txt=f"({lbr}%)", border=0, align='C')
    pdf.cell(8, 7)
    pdf.cell(22, 7, txt=f"({prf}%)", border=0, align='C')
    pdf.cell(8, 7)
    pdf.cell(22, 7, txt=f"(6.5%)", border=0, align='C')

    pdf.ln(6)
    pdf.set_font(family="Helvetica", style="", size=10)
    pdf.cell(120, 7)
    pdf.cell(22, 7, txt=f"${price_pre_tax}", align='C', border=0)
    pdf.cell(25, 7, txt=f"  +  Tax (8.25%)")

    pdf.ln(8)
    pdf.set_font(family="Helvetica", style="B", size=10)
    pdf.cell(90, 7)
    pdf.cell(30, 7, txt=f"Final Price:", align='R')
    pdf.cell(22, 7, txt=f"${price}", align='C', border=True)


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


# Function to generate the antique breakdown PDF
def pdf_ant_bd(item_code, price, gross_wt, ant_stones):

    total_stone_ct = 0
    stones = {}
    polki_flag = False
    polki_ct = 0
    
    # go through each stone 
    for stone in ant_stones:
        if stone['ant_stone'] == 'Polki Diamond':
            polki_flag = True
            polki_ct = stone['ant_ct']
        else:
            stones[stone['ant_stone']] = stone['ant_ct']
            total_stone_ct += stone['ant_ct']
    
    total_stone_ct = round(total_stone_ct, 2)

    total_stone_wt = round(total_stone_ct/5, 2)
    if polki_flag:
        net_wt = gross_wt - total_stone_wt - round(polki_ct/5, 2)
    else:
        net_wt = gross_wt - total_stone_wt

    try:
        op, gp, time, date = get_price()
    except CustomError as e:
        return "kitco_down"
    gold_22k = round(gp*0.93, 2)

    price_gold, price_per_stone, price_stones, price_labor, price_profit, price_duty, price_pre_tax, price_polki = \
        ant_bd(item_code, price, net_wt, gold_22k, stones, polki_flag, polki_ct)
    
    #Read the existing PDF
    reader = PdfReader("template.pdf")
    writer = PdfWriter()

    # create FPDF object
    pdf = FPDF('L', 'mm', 'A5')
    # add page
    pdf.add_page()
    pdf.ln(18) 

    pdf.set_font(family="Helvetica", style="B" ,size=11.5)
    pdf.cell(70, 7, txt=f"Detailed Breakdown for {item_code.upper()}",
             border=False,
             ln=True)

    # disp kitko prices
    pdf.set_font(family="Helvetica", style="" ,size=8)
    pdf.write(7, "Spot price on")
    #pdf.set_text_color(0, 0, 255)
    pdf.write(7, " kitko.com", link="https://www.kitco.com/")
    #pdf.set_text_color(0, 0, 0)
    pdf.write(7, f" as of {date} on {time} is ")
    pdf.set_font(family="Helvetica", style="B", size=8)
    pdf.write(7, f"${round(op, 2)}")
    pdf.set_font(family="Helvetica", style="", size=8)
    pdf.write(7, " per Troy Ounce")

    pdf.ln(4.6)

    # 24K
    pdf.set_font(family="Helvetica", style="", size=8)
    pdf.cell(40, 6, txt=f"24K gold one gram: ${round(gp, 2)} ", ln=False, border=0)
    pdf.set_font(family="Helvetica", style="I", size=7)
    pdf.cell(50, 6, txt="(1 Troy Ounce = 31.103 grams)", ln=True, border=0)
    
    pdf.ln(-1.8)

    # 22K
    pdf.set_font(family="Helvetica", style="B", size=8)
    pdf.cell(40, 6, txt=f"22K gold one gram: ${gold_22k} ", ln=False, border=0)
    pdf.set_font(family="Helvetica", style="I", size=7)
    pdf.cell(50, 6, txt="(24K gold * 0.93 = 22K gold)", ln=True, border=0)

    pdf.ln(2)

    pdf.set_font(family="Helvetica", style="B", size=10)
    pdf.cell(50, 6, txt=f"Gross weight: {gross_wt} grams", border=0, ln=True)
    pdf.ln(1.5)
    pdf.cell(65, 6, txt=f"Total Gems weight: {total_stone_wt} grams", border=0)
    pdf.cell(65, 6, txt=f"Net Gold weight: {round(net_wt, 2)} grams", border=0)
    if polki_flag:
        pdf.cell(65, 6, txt=f"Polki Diamond Carat: {round(polki_ct, 2)} ct", border=0)

    pdf.ln(5)

    cnt = 0
    formula = ["Net weight = Gross weight - Total Gems weight",
               "Total Gems Weight = Total Gems Carat / 5",
               "5 carats = 1 gram"]

    for stone in stones.keys():
        pdf.set_font(family="Helvetica", style="", size=7)
        pdf.cell(20, 5, txt=f"{stone} : ", border=0, align='R')
        pdf.cell(12, 5, txt=f"{stones[stone]}ct", border=0, align='L')
        pdf.cell(33, 5, txt=f"PPC: ${price_per_stone[stone]}", border=0, align='L')
        if cnt<2:
            pdf.set_font(family="Helvetica", style="I", size=7)
            pdf.cell(65, 5, txt=f"{formula[cnt]}", border=0)
            if polki_flag:
                pdf.set_font(family="Helvetica", style="BI", size=7)
                pdf.cell(65, 5, txt=f"Polki Diamond/ct: $295", border=0)
            cnt += 1
        pdf.ln(2.8)

    pdf.set_font(family="Helvetica", style="BI", size=7)
    pdf.ln(0.8)
    pdf.cell(20, 5, txt=f"Total Carat : ", border=0, align='R')
    pdf.cell(12, 5, txt=f"{total_stone_ct}ct", border=0, align='L')
    pdf.cell(33, 5, txt=f"${price_stones}", border=0, align='L')
    pdf.set_font(family="Helvetica", style="I", size=7)
    if cnt<2:
        pdf.set_font(family="Helvetica", style="I", size=7)
        pdf.cell(65, 5, txt=f"{formula[cnt]}", border=0)
    
    pdf.ln(7)

    pdf.set_font(family="Helvetica", style="B", size=10)

    # column headers
    pdf.cell(20, 8, txt=f"Gold", border=True, align='C')
    pdf.cell(6, 8)
    pdf.cell(20, 8, txt=f"Gems", border=True, align='C')
    pdf.cell(6, 8)
    pdf.cell(20, 8, txt=f"Labor", border=True, align='C')
    pdf.cell(6, 8)
    pdf.cell(20, 8, txt=f"Margin", border=True, align='C')
    if polki_flag:
        pdf.cell(6, 8)
        pdf.cell(20, 8, txt=f"Polki Dia", border=True, align='C')
    pdf.cell(6, 8)
    pdf.cell(20, 8, txt=f"Duty", border=True, align='C', ln=True)
    
    #actual values
    pdf.cell(20, 7, txt=f"${price_gold}", border=True, align='C')
    pdf.cell(6, 7)
    pdf.cell(20, 7, txt=f"${price_stones}", border=True, align='C')
    pdf.cell(6, 7)
    pdf.cell(20, 7, txt=f"${price_labor}", border=True, align='C')
    pdf.cell(6, 7)
    pdf.cell(20, 7, txt=f"${price_profit}", border=True, align='C')
    if polki_flag:
        pdf.cell(6, 8)
        pdf.cell(20, 8, txt=f"{price_polki}", border=True, align='C')
    pdf.cell(6, 7)
    pdf.cell(20, 7, txt=f"${price_duty}", border=True, align='C', ln=1)

    # percentages and stone/ct
    pdf.set_font(family="Helvetica", style="I", size=7)
    ppc = round(price_stones/total_stone_ct, 2)
    lbr = round((price_labor/price_pre_tax)*100, 2)
    prf = round((price_labor/price_pre_tax)*100, 2)
    pdf.cell(26, 7)
    pdf.cell(20, 7, txt=f"(Avg: {ppc}/ct)", border=0, align='C')
    pdf.cell(6, 7)
    pdf.cell(20, 7, txt=f"({lbr}%)", border=0, align='C')
    pdf.cell(6, 7)
    pdf.cell(20, 7, txt=f"({prf}%)", border=0, align='C')
    if polki_flag:
        pdf.cell(26, 8)
    pdf.cell(6, 7)
    pdf.cell(20, 7, txt=f"(6.5%)", border=0, align='C')

    pdf.ln(6)
    pdf.set_font(family="Helvetica", style="", size=10)
    pdf.cell(120, 7)
    pdf.cell(22, 7, txt=f"${price_pre_tax}", align='C', border=0)
    pdf.cell(25, 7, txt=f"  +  Tax (8.25%)")

    pdf.ln(8)
    pdf.set_font(family="Helvetica", style="B", size=10)
    pdf.cell(90, 7)
    pdf.cell(30, 7, txt=f"Final Price:", align='R')
    pdf.cell(22, 7, txt=f"${price}", align='C', border=True)


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

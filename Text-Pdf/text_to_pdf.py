from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
file1 = open('hr', 'r')
Lines = file1.readlines()
count = 1
# Strips the newline character
for line in Lines:
    pdf.cell(200, 10, txt=line, ln=count, align="L")
    count = count + 1

pdf.output("2.pdf")

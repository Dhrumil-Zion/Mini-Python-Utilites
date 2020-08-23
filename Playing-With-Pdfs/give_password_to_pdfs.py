from PyPDF2 import PdfFileWriter, PdfFileReader

write = PdfFileWriter()
pdf = PdfFileReader("1.pdf")

for num in range(pdf.numPages):
    write.addPage(pdf.getPage(num))

password = "dhrumil"
write.encrypt(password)

with open("pass_protected_1.pdf", 'wb') as f:
    write.write(f)
    f.close()

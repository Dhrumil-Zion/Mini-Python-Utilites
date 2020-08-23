from PyPDF2 import PdfFileMerger
import os

merge = PdfFileMerger()

for pdfs in os.listdir():                   # my pdfs are in same dir
    if pdfs.endswith('.pdf'):
        merge.append(pdfs)

merge.write('Final.pdf')
merge.close()

from pypdf import PdfMerger
import os

def merge_pdfs(pdfs, output_file="combinedPDF.pdf", order=None):
    merger = PdfMerger()

    try:
        if order:
            for index in order:
                merger.append(pdfs[index])
        else:
            for pdf in pdfs:
                merger.append(pdf)
        
        merger.write(output_file)
        merger.close()
        print("PDFs merged successfully!")

    except Exception as error_name: 
        print(f"Error merging PDFs: {error_name}")
        if os.path.exists(output_file):
            os.remove(output_file)

# add the PDF documents in the same file as main.pyl
pdfs = ['PDF1.pdf', 'PDF2.pdf', 'PDF3.pdf'] # change file names

first = int(input("First page: "))
second = int(input("Second page: "))
third = int(input("Third page: "))

merge_pdfs(pdfs, order=[first, second, third])

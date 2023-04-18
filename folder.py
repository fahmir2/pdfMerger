import PyPDF2
import os

#This script prompts the user for a folder directory where all the pdfs that should be merge are located.

# Prompt the user for the directory path where the PDF files are located
pdf_dir = input("Enter the directory path where the PDF files are located: ")

# Get a list of all PDF files in the directory
pdf_list = [os.path.join(pdf_dir, f) for f in os.listdir(pdf_dir) if f.endswith('.pdf')]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('/Users/eze/Desktop/super.pdf')

    # Open the super.pdf and watermark.pdf files
    with open('super.pdf', 'rb') as super_pdf_file, open('wtr.pdf', 'rb') as watermark_file:
        super_pdf = PyPDF2.PdfFileReader(super_pdf_file)
        watermark = PyPDF2.PdfFileReader(watermark_file)

        # Get the first page of the watermark PDF
        watermark_page = watermark.getPage(0)

        # Create a new PDF file to hold the watermarked pages
        output_pdf = PyPDF2.PdfFileWriter()

        # Loop through all the pages of the super.pdf file and add the watermark to each page
        for i in range(super_pdf.getNumPages()):
            page = super_pdf.getPage(i)
            page.mergePage(watermark_page)
            output_pdf.addPage(page)

        # Save the watermarked PDF as a new file
        with open('/Users/eze/Desktop/super_watermarked.pdf', 'wb') as output_file:
            output_pdf.write(output_file)


pdf_combiner(pdf_list)

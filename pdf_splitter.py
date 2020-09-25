import os 
from PyPDF2 import PdfFileReader, PdfFileWriter
fname=raw_input("Enter the name of the file without the pdf extension: ")
file_name=(str(fname)+'.pdf')
def pdf_splitter(file_name):
	pdf_file=PdfFileReader(file_name)
	for page in range(pdf_file.getNumPages()):
		pdf_writer=PdfFileWriter()
		pdf_writer.addPage(pdf_file.getPage(page))
		output_filename='{}_page_{}.pdf'.format(fname,page+1)
		with open(output_filename,'wb') as out:
			pdf_writer.write(out)
			
		print("Created file name:{}".format(output_filename))

pdf_splitter(file_name)

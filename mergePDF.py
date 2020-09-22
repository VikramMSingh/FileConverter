import PyPDF2
file1=raw_input("Enter name of first file: ")
file2=raw_input("Enter name of second file: ")
#Access and open the files to merge
pdfFile_1=open("%s" %file1 + '.pdf','rb')
pdfFile_2=open("%s" %file2 + '.pdf','rb')

#Read the two files
pdfRead_1=PyPDF2.PdfFileReader(pdfFile_1)
pdfRead_2=PyPDF2.PdfFileReader(pdfFile_2)

#Create a blank pdf document
pdfWriter=PyPDF2.PdfFileWriter()

#Copy all the pages from file 1 
for pageNum in range(pdfRead_1.numPages):
	pageObj=pdfRead_1.getPage(pageNum)
	pdfWriter.addPage(pageObj)

#Copy all the pages from file 2 
for pageNum in range(pdfRead_2.numPages):
	pageObj=pdfRead_2.getPage(pageNum)
	pdfWriter.addPage(pageObj)

#Create a new merged file 
outputFile=open("NewFile.pdf",'wb')
pdfWriter.write(outputFile)

#Close all files
outputFile.close()
pdfFile_1.close()
pdfFile_2.close()


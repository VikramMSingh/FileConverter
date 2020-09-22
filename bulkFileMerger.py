from PyPDF2 import PdfFileReader, PdfFileMerger

number_of_files=input("Enter number of files to merge: ")
file_name=raw_input("Enter file pattern to merge:")
num=int(number_of_files)
def bulkMergePDF(num,fname):
	mergedObject=PdfFileMerger()
	for fileNumber in range(1,num+1):
		mergedObject.append(PdfFileReader("%s" %(fname) + str(fileNumber) + '.pdf','rb'))

	mergedObject.write("merged_files.pdf")

bulkMergePDF(num,file_name)

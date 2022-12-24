import PyPDF2

file=open("sample.pdf","rb")
reader=PyPDF2.PdfReader(file)
print(reader.getPage(0).extractText())
file.close()
#print(reader.numPages)


import  img2pdf

pdfData=img2pdf.convert("vv.png")
file=open("myreport.pdf","wb")
file.write(pdfData)
file.close()
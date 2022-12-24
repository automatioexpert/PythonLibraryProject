import  img2pdf

file=open("myreportFinalMerged.pdf","wb")
file.write(img2pdf.convert(["vv.png","Code.png"]))
file.close()
print("PDF is converted")
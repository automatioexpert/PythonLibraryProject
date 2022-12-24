import  img2pdf
import os

list=os.listdir(".")
newList=[x for x in list if x.endswith(".png")]
print("Total no of images to convert is : ",len(newList))
pdf=img2pdf.convert(newList)
file=open("MyNewReport3.pdf","wb")
file.write(pdf)
file.close()

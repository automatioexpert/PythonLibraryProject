import os

list = os.listdir(".")
# ['Code.png', 'ConvertImgToPDF.py', 'ConvertImgToPDF2.py', 'ListCompDemo.py', 'ListCompDemo2.py', 'myreport.pdf', 'myreportFinalMerged.pdf', 'readPDF.py', 'sample.pdf', 'vv.png', '__init__.py']
print(list)
print([x for x in list if x.endswith(".png")])  # ['Code.png', 'vv.png']
print([x for x in list if x.endswith(".py")])
print([x for x in list if x.endswith(".pdf")])

""" OUTPUT:
['Code.png', 'ConvertImgToPDF.py', 'ConvertImgToPDF2.py', 'ListCompDemo.py', 'ListCompDemo2.py', 'myreport.pdf', 'myreportFinalMerged.pdf', 'readPDF.py', 'sample.pdf', 'vv.png', '__init__.py']
['Code.png', 'vv.png']
['ConvertImgToPDF.py', 'ConvertImgToPDF2.py', 'ListCompDemo.py', 'ListCompDemo2.py', 'readPDF.py', '__init__.py']
['myreport.pdf', 'myreportFinalMerged.pdf', 'sample.pdf']
"""

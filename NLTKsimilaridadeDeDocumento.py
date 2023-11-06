from PyPDF2 import PdfReader
from NLTKsimilaridadeDefrases import preProcessing
from NLTKsimilaridadeDefrases import sentSimilarity

reader = PdfReader("EmentaTestePDF.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
text = preProcessing(text)

reader2 = PdfReader("teste.pdf")
number_of_pages2 = len(reader2.pages)
page2 = reader2.pages[0]
text2 = page2.extract_text()
text2 = preProcessing(text2)

print(sentSimilarity(text, text2))


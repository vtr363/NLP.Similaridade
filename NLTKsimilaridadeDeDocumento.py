from PyPDF2 import PdfReader
from NLTKsimilaridadeDefrases import preProcessing
from NLTKsimilaridadeDefrases import sentSimilarity
from tika import parser

def compareDocs(docURL, docURL2):
    if docURL.endswith('.pdf'):
        
        # # PyPDF2
        # reader = PdfReader(docURL)
        # text = ''
        # for i in range(len(reader.pages)):
        #     page = reader.pages[i]
        #     text += page.extract_text()
        # text = preProcessing(text)

        # reader2 = PdfReader(docURL2)
        # text2 = ''
        # for i in range(len(reader2.pages)):
        #     page2 = reader2.pages[i]
        #     text2 += page2.extract_text()
        # text2 = preProcessing(text2)
        
        #tika
        raw = parser.from_file(docURL)
        text = raw['content']
        text = preProcessing(text)
        # print(text.encode('utf-8'))
        
        raw = parser.from_file(docURL2)
        text2 = raw['content']
        text2 = preProcessing(text2)
        # print(text2.encode('utf-8'))
    else: 
        text = ""
        with open(docURL, "r") as doc:
            for linha in doc:
                text += linha

        text2 = ""
        with open(docURL2, "r") as doc:
            for linha in doc:
                text2 += linha
        

    return sentSimilarity(text, text2)

print(compareDocs("./test/EmentaTestePDF.pdf", "./test/EmentaTestePDF2.pdf"))
import re
import nltk
import string
from nltk.cluster.util import cosine_distance

# nltk.download('punkt')
# nltk.download('stopwords')

stopwords = nltk.corpus.stopwords.words("portuguese")


def preProcessing(text):
    # deixar texto em caixa baixa
    formatedText = text.lower()
    tokens = []
    # separar palavras
    for token in nltk.word_tokenize(formatedText):
        tokens.append(token)
    # retirar stopwords e pontuações/simbolos
    tokens = [palavra for palavra in tokens if palavra not in stopwords and palavra not in string.punctuation]
    formatedText = ' '.join([str(elemento) for elemento in tokens])
        
    return formatedText


def sentSimilarity(sent1, sent2):
    # separa as palavras
    words1 = [palavra for palavra in nltk.word_tokenize(sent1)]
    words2 = [palavra for palavra in nltk.word_tokenize(sent2)]
    
    # cria um vetor com todas as palavras sem repetição
    allWords = list(set(words1 + words2))
    
    # cria os vetores para comparação
    vet1 = [0] * len(allWords)
    vet2 = [0] * len(allWords)
    
    # preenche os vetores
    for word in words1:
        vet1[allWords.index(word)]+= 1
    
    for word in words2:
        vet2[allWords.index(word)]+= 1

    # print(vet1)
    # print(vet2)
    
    # faz o calculo/ verificação da semelhança
    return round(1 - cosine_distance(vet1, vet2), 2)



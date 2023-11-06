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
    formatedText = ' '.join([str(elemento) for elemento in tokens if not elemento.isdigit()])
        
    return formatedText

text = """Este artigo descreve um comparativo entre dois algoritmos da área
de mineração de textos, os quais são utilizados na tarefa de sumarização
automática de documentos. Foram comparados nos experimentos o algoritmo
clássico de Luhn e o algoritmo GistSumm, sendo realizadas dois tipos de
avaliação, ambas utilizando o Português do Brasil como idioma alvo. A
primeira consistiu em gerar um resumo de um texto fonte com cada
algoritmo,e a avaliação foi conduzida utilizando avaliadores humanos que
indicaram a coerência nos resumos de cada um. Por outro lado, a segunda foi
conduzida por meio de uma avaliação baseada no resumo, no qual os
avaliadores responderam perguntas sobre o texto original possuindo como
fonte de consulta somente o resumo gerado pelos algoritmos. Após as análises,
foi demonstrado que o algoritmo GistSumm possui maior capacidade para
gerar resumos que mantenham a ideia principal do texto, sendo classificado
com 81,6% de eficiência no primeiro experimento e 90% no segundo
experimento."""

# print(preProcessing(text))

originalSentence = [sentence for sentence in nltk.sent_tokenize(text)]
formatedSentence = [preProcessing(originalSentence) for originalSentence in nltk.sent_tokenize(text)]
 
# print(originalSentence)

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
    
    # faz o calculo/ verificação
    return 1 - cosine_distance(vet1, vet2)

# print(sentSimilarity(formatedSentence[0], formatedSentence[3]))
# print(formatedSentence[0], formatedSentence[3])


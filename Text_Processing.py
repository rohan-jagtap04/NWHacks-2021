# pip install spacy
# python -m spacy download en_core_web_sm
import spacy
from collections import Counter

class Text_Processing(object):
    
    # Class constructor
    def __init__(self, text):
        self.text = text
        self.nlp = spacy.load("en_core_web_sm")

    # Removes the different types of whitespaces in the text file
    def whitespaceRemover(self, string):
        text2 = string.replace("\n","")
        text3 = text2.replace("\r","")
        return text3
    
    # Returns a list of 5 of the most frequent words that are not stop words and not punctuation
    def getTopics(self):
        text2 = self.whitespaceRemover(self.text)
        doc = self.nlp(text2)
        potentialTopics = [token.text for token in doc if not token.is_stop and not token.is_punct]
        freq = Counter(potentialTopics)
        del freq[" "]
        listOfTopics = self.checkTheTopFive(freq)
        return listOfTopics.most_common(5)
    
    # Returns a list of sentences
    def getSentences(self):
        doc = self.nlp(self.text)
        sentences = list(doc.sents)
        return sentences
    
    def getRelevantSentences(self, topic):
        relevantSentenceArray = []
        for sentence in self.getSentences():
            if topic in sentence.text and sentence.text not in relevantSentenceArray:
                relevantSentenceArray.append(self.whitespaceRemover(sentence.text))
        return relevantSentenceArray

    # Checks the top five and changes it if repetition is detected
    def checkTheTopFive(self, dictionary_var):
        delList = []
        newDic = {}
        for i in range(len(dictionary_var)):
            for j in range(len(dictionary_var)-1):
                if i != j:
                    dupKeySum = 0
                    compare1 = list(dictionary_var.keys())[i]
                    compare2 = list(dictionary_var.keys())[j]
                    if (compare1.lower() == compare2.lower()):
                        if compare1 not in delList and compare2 not in delList:
                            dupKeySum += dictionary_var[compare1]
                            dupKeySum += dictionary_var[compare2]
                            delList.append(compare1)
                            delList.append(compare2)
                            newDic[compare1.lower()] = dupKeySum
                        elif compare1 in delList and compare2 not in delList:
                            dupKeySum += dictionary_var[compare2]
                            delList.append(compare2)
                            newDic[compare1.lower()] += dupKeySum
                        elif compare1 not in delList and compare2 in delList:
                            dupKeySum += dictionary_var[compare1]
                            delList.append(compare1)
                            newDic[compare1.lower()] += dupKeySum
        for key in delList:
            del dictionary_var[key]
        dictionary_var.update(newDic)
        return dictionary_var

 
        
            
    
            
            
            
        
            
            

    


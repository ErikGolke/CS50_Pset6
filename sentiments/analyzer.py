import nltk
from nltk.tokenize import TweetTokenizer

class Analyzer():
    """Implements sentiment analysis."""
    

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        
        self.positive = []
        self.negative = []

        # Strips ; and newline characters from positive-words.txt
        with open(positives) as lines:
            for line in lines:
                if line.startswith(";"):
                    continue
                if line is "\n":
                    continue
                else:
                    i = line.strip()
                    self.positive.append(i)
                
        # Strips ; and newline characters from negative-words.txt
        with open(negatives) as lines:
            for line in lines:
                if line.startswith(";"):
                    continue
                if line is "\n":
                    continue
                else:
                    i = line.strip()
                    self.negative.append(i)

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        score = 0
        
        for i in tokens:
            
            i = i.lower()
            
            if i in self.positive:
                score += 1
            
            elif i in self.negative:
                score -= 1
            
            else:
                score += 0
                
        return score

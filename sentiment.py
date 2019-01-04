#How to perform sentiment analysis in python?
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
message_text = '''kiddy is a good boy'''
print(message_text)
scores = sid.polarity_scores(message_text)
for key in sorted(scores):
        print('{0}: {1}, '.format(key, scores[key]), end='')


#output:
    
#good
#compound: 0.4404, neg: 0.0, neu: 0.0, pos: 1.0 

#bad
#compound: -0.5423, neg: 1.0, neu: 0.0, pos: 0.0

#pranay is a bad boy. he is a psycho. i hate him. i want to kill him.
#compound: -0.9118, neg: 0.536, neu: 0.405, pos: 0.059, 

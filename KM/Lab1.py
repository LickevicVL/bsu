from requests import get
from scipy import spatial
import re
from numpy import array

"""1"""
# holmes_url = "http://www.gutenberg.org/cache/epub/1661/pg1661.txt"
# response = get(holmes_url)
# text = response.text.replace('\r', '').replace('\n', '')
text = ''
with open('Lab1.txt') as file:
    for line in file:
        text += line

# text = text.replace('\r\n', '').replace('\n', '')
# print(text)

"""2"""
text_lowercase = text.lower()

"""3"""
words = re.split('[^a-z]', text_lowercase)
print(len(words))

"""4"""
def fil(word):
    if not word:
        return False
    if word == '\n' or word == '\r' or word == '\n\r':
        return False
    else:
        return True

words = list(filter(fil, words))
print(len(words))
words = list(set(words))
print(len(words))

"""5"""
reg = re.compile('[A-Z0-9\"][A-Za-z 0-9\'\",:;\-]+')

text = text.replace('\n', '').replace('\r', '')

sentences = reg.findall(text)
print(len(sentences))
def filt(sentence):
    if len(sentence) <= 1:
        return False
    else:
        return True

sentences = list(filter(filt, sentences))

print(len(sentences))

"""6"""
def num(word, sentences):
    return len([w for w in sentences.lower().split() if w == word])


M = array([[num(word, sentence.lower()) for word in words] for sentence in sentences])
print(M.shape)

"""7"""
sen = M[1994]
for i in range(7368):
    print(spatial.distance.cosine(sen, M[i]))
# res = [spatial.distance.cosine(sen, sentence) for sentence in M]
# min_res = res.argmin()
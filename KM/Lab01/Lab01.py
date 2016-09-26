from requests import get
from scipy import spatial
import re
from numpy import array
from time import time

"""1"""
holmes_url = "http://www.gutenberg.org/cache/epub/1661/pg1661.txt"
response = get(holmes_url)
text = response.text
# text = ''
# with open('Lab1.txt') as file:
#     for line in file:
#         text += line


"""2"""
text_lowercase = text.lower()

"""3"""
words = re.split('[^a-z]', text_lowercase)
print(len(words))
print('==================================')

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
print('==================================')

"""5"""
reg = re.compile('[A-Za-z0-9 \'"@#,:;\(\)\*-]{2,}(?=[\.!?" ]+[0-9A-Z"\'])')
text = text.replace('\r', ' ').replace('\n', ' ').replace('\r\n', ' ').\
    replace('\\', '').replace('Mr.', 'Mr').\
    replace('Mrs.', 'Mrs').replace('St.', 'St')
sentences = reg.findall(text)


print(len(sentences))
def filt(sentence):
    if len(sentence) <= 1 or sentence in ['\r', '\n', '\r\n', '  ', "' ",
                                          "'  ", '"  ', '" ', '  1', ' 1',
                                          ' 4', '"    ', '    ', "'   ",
                                          '    1', '    4', "'    "]:
        return False
    else:
        return True

sentences = list(filter(filt, sentences))

print(len(sentences))
print('==================================')


"""6"""
def num(word, sentences):
    return len([w for w in sentences.lower().split() if word in w])

M = array([[num(word, sentence) for word in words] for sentence in sentences])
print(M.shape)
print('==================================')

"""7"""
sen = M[1510]
print(sentences[1510])
tmpM = list(M)
tmpM.pop(1510)

res = array([spatial.distance.cosine(sen, sentence) for sentence in tmpM])
min_res = res.argmin()
min_sen = min_res + 1 if min_res >= 1510 else min_res
print(min_res)
print(res[min_res])
print(sentences[min_sen])
print('==================================')

"""8"""
def simple_sentence(Matrix, number):
    sen = Matrix[number]
    M = list(Matrix)
    M.pop(number)
    res = array([spatial.distance.cosine(sen, sentence) for sentence in M])
    max_simp = res.argmin()
    return max_simp + 1 if max_simp >= number else max_simp

m = int(str(time())[-3:])
print(m)
print(sentences[m])
n = simple_sentence(M, m)
print(n)
print(sentences[n])


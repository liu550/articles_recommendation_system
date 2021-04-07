from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor
import spacy
from spacy import displacy
import csv
import numpy as np
import tensorflow as tf

'''
nlp = spacy.load('en_core_web_sm')
model = model = tf.keras.models.load_model('model1')

nouns = ['NN', 'NNS', 'NNP', 'NNPS']
verbs = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
ws = ['WDT', 'WP', 'WP$', 'WRB']
relations = ['aux', 'conj', 'punct']

def structureIsValid(doc):
    counter = 0
    for token in doc:
        if counter == 3:
            break
        elif token.dep_ == 'punct':
            counter = 0
        elif token.tag_ in nouns:
            if counter == 0:
                counter += 1
            elif counter == 2:
                counter += 1
        elif token.tag_ in verbs:
            if counter == 1:
                counter += 1
    if counter == 3:
        return 1
    else:
        return 0

def containsW(doc):
    for token in doc:
        if token.tag_ in ws:
            return 1
    return 0

def containsRelations(doc):
    for token in doc:
        if token.dep_ in relations:
            return 1
    return 0

def isTitle(text):
    doc = nlp(text)
    array = np.array([[len(doc), structureIsValid(doc), containsW(doc), containsRelations(doc)]])
    result = model.predict(array)
    if result >= 0.9:
        return True
    else:
        return False
''' 


visited = {}
otherLinks = {}
data = []

def crawl(node):
    links = []
    try:
        result = requests.get(node)
        bs = BeautifulSoup(result.content, 'html.parser')
       
        tags = bs.find_all('a')
    
        for tag in tags:
            #if tag.has_attr('class') and tag.has_attr('href') and tag['href'] not in visited and (case1(tag['class']) or case2(tag['class'])):
            

            if tag.has_attr('href'):
    
                link = tag['href']
                print(link)

                #annoying bbc
                if 'bbc' in node and 'https://www.bbc.co.uk' not in link and 'http://www.bbc.co.uk' not in link and 'https://www.bbc.com' not in link:
                    link = 'https://www.bbc.co.uk' + link
                
                #whether the link is (1) not visited and (2) valid
                if link not in visited:
                    links.append(link)
                    visited[link] = tag.text
                #else put it in otherLinks
                else:
                    otherLinks[link] = tag.text
        return links
    except Exception as e:
        print(e)
        return links
    #finally

executor = ThreadPoolExecutor(200)

startNodes = [
    'https://www.bbc.com/news/science-environment-55662985'
    'https://www.bbc.com/news/world-asia-china-55666153',
    'https://www.bbc.com/news/technology-55683745',
    'https://www.bbc.com/news/business-55673183',
    'https://www.wsj.com/articles/ant-group-is-moving-quickly-to-comply-with-regulations-chinas-central-bank-says-11610709387?mod=markets_lead_pos6',
    'https://www.wsj.com/articles/groceries-prove-a-pandemic-bright-spot-for-bp-and-shell-11610793001?mod=business_lead_pos3',
    'https://www.wsj.com/articles/pro-trump-discussion-board-faces-possible-shutdown-over-violent-racist-posts-11610819176?mod=politics_lead_pos4',
    'https://www.nytimes.com/live/2021/01/16/sports/nfl-playoffs',
    'https://www.nytimes.com/2021/01/15/world/americas/mexico-general-drug-charges.html',
    'https://www.nytimes.com/2021/01/15/science/hypersonic-missile-weapons.html'
]


'''
startNodes = [
    #bbc
    'https://www.bbc.com/news/world-us-canada-55265477',
    'https://www.bbc.com/sport/football/55681467',


    #wsj
    'https://www.wsj.com/articles/americas-big-banks-girded-for-a-wave-of-bad-loans-theyre-still-waiting-11610734848?mod=markets_lead_pos1',
    'https://www.wsj.com/articles/are-videogames-the-future-of-remote-work-11610773203?mod=business_lead_pos10',

    #nyt
    'https://www.nytimes.com/2021/01/15/us/politics/inauguration-security.html',
    'https://www.nytimes.com/2021/01/15/technology/when-tech-antitrust-failed.html',


    'https://www.bbc.com/news/science-environment-55662985',
    'https://www.bbc.com/news/entertainment-arts-55674300',
    'https://www.bbc.com/news/world-us-canada-55679623',
    'https://www.bbc.com/news/world-asia-china-55666153',
    'https://www.bbc.com/news/technology-55683745',
    'https://www.bbc.com/news/business-55673183',
    'https://www.bbc.com/news/world-us-canada-55265477'
    'https://www.bbc.com/sport/football/55681467',
    'https://www.bbc.com/worklife/article/20210113-can-reality-tv-shows-help-lead-the-way-for-inclusivity',
    'https://www.bbc.com/future/article/20210112-heres-what-sex-with-neanderthals-was-like',
    'https://www.bbc.com/culture/article/20210113-how-the-arab-spring-changed-cinema',
]
'''

#try modifying the CSV data
'''
with open('data.csv', 'rU') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    rows = list(reader)
    for row in rows:
        row.append(row[0])
    with open('data.csv', mode='w') as csv_file:
        fields = ['text', 'link', 'isTitle', 'text']
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
]]]
'''

tempNodes = []
futures = []
allLinks = []
for i in range(3):
    print(str(i) + "th iteration")
    for startNode in startNodes:
        print(startNode + '\n')
        future = executor.submit(crawl, startNode)
        futures.append(future)
    for future in futures:
        results = future.result()
        for result in results:
            tempNodes.append(result)
    
    startNodes = tempNodes
    print("Before: \n")
    print(tempNodes)
    tempNodes = []
    print("After: \n")
    print(tempNodes)

#print out news
print(len(visited))
print(len(otherLinks))
f = open('news.txt', 'w')
print("Visited" + '\n')
for link, title in visited.items():
    print("link:" + link)
    print("title:" + title + '\n')
    try: 
        f.write(link + ': ' + title + '\n')
    except Exception as e:
        print(e)
print("Other" + '\n')
f2 = open('garbage.txt', 'w')
for link, title in otherLinks.items():
    print("link:" + link)
    print("title:" + title)
    print('\n')
    try:
        f2.write(link + ': ' + title + '\n')
    except Exception as e:
        print(e)









#print (len(allLinks))
#print out data
'''
print(data)
print(len(data))
with open('data.csv', mode='w') as csv_file:
    fields = ['text', 'link', 'isTitle']
    writer = csv.DictWriter(csv_file, fieldnames=fields)
    writer.writeheader()
    for d in data:
        writer.writerow(d)
'''



'''
visited = set()
sources = ['https://www.bbc.com/news/uk-politics-55678259', 'https://www.bbc.com/news/world-asia-55657257']
for source in sources:
    result = requests.get(source)
    bs = BeautifulSoup(result.content, 'html.parser')
    links = []
    tags = bs.find_all('a')
    for tag in tags:
        
        if tag['class'][1] == 'e1f5wbog6' and tag['href'] not in visited:
            links.append((tag.text, tag['href']))
            visited.add(tag['href'])
    print(len(links))
    f = open('news.txt', 'a')
    for news in links:
        f.write(news[0] + ': ' + news[1] + '\n')
    f.write('\n')
'''

'''
def test(i):
    print("test: " + str(i+1) + "\n")
    return i + 1

executor = ThreadPoolExecutor(10)
result = 0
futures = []
for i in range(10):
    future = executor.submit(test, i)
    futures.append(future)

print("start to add things up")

for future in futures:
    print("the result of the future is: " + str(future.result()))
    result += future.result()

print("Done. the result is: " + str(result))
'''

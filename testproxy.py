import requests
import random
import csv
import concurrent.futures

#opens a csv file of proxies and prints out the ones that work with the url in the extract function

proxylist = []

target = 'https://homestars.com/on/toronto/categories/'


with open('Free_Proxy_List.csv', 'r') as f:
    reader = csv.reader(f)
    for column in reader:
        proxylist.append(column[0] + ':' + column[7])

def extract(proxy):
    #this was for when we took a list into the function, without conc futures.
    #proxy = random.choice(proxylist)
    headers = {'User-Agent': 'Googlebot/2.1 (+http://www.google.com/bot.html)'}
    try:
        r = requests.get(target , headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=2)
        if r.status_code == 200:
            f = open('amazon_reviews/proxies.txt', 'a')
            f.write(proxy+'\n')
            f.close()
        print(r.status_code, ' | Works')
    except:
        pass
    return proxy

with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract, proxylist)
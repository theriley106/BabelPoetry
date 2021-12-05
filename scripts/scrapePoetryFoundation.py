import requests
import glob
import os
import bs4
import json
import threading

URL = "https://www.poetryfoundation.org/ajax/poems?page={0}&sort_by=recently_added"

def get_id_from_url(url):
    return url.partition("https://www.poetryfoundation.org/poetrymagazine/poems/")[2].partition("/")[0]

def download(url):
    print("DOWNLOADING: {}".format(url))
    res = requests.get(url)
    x = bs4.BeautifulSoup(res.text, 'lxml').title
    if x != None:
        print(x.string)
    return res

def get_url(url):
    filename = "pages/poem-{}.txt".format(get_id_from_url(url))
    if os.path.exists(filename) == False:
        res = download(url)
        with open(filename, "w") as f:
            f.write(res.text)
    return open(filename).read()



def get_page(number):
    filename = "pages/page-{}.txt".format(number)
    if os.path.exists(filename) == False:
        res = download(URL.format(number))
        with open(filename, "w") as f:
            f.write(res.text)
    return open(filename).read()

def get_poem_text(url):
    res = get_url(url)
    page = bs4.BeautifulSoup(res, 'lxml')
    # print(page.title.string)
    x = ""
    for val in page.select('.c-feature-bd')[0].select("div"):
        v = val.getText()
        if len(v) > 0:
            x += v + "\n"
    return x.strip()

count = 0

numbers = [[]]

for i in range(1, 500):
    numbers[-1].append(i)
    if len(numbers[-1]) == 50:
        numbers.append([])

COUNT = [0]

def get_list_of_nums(list_of_nums):
    for i in list_of_nums:
        try:
            values = json.loads(get_page(i))
            for poem in values['Entries']:
                try:
                    url = poem['link']
                    get_poem_text(url)
                except KeyError as e:
                    raise
                except:
                    print("ERROR")
                COUNT[0] += 1
                print("COUNT: {}".format(COUNT[0]))
        except:
            print("Error")
            pass


threads = [threading.Thread(target=get_list_of_nums, args=(ar,)) for ar in numbers]

for thread in threads:
	thread.start()
for thread in threads:
	thread.join()


    # print(url)
# print()

# print(get_poem_text("https://www.poetryfoundation.org/poetrymagazine/poems/41729/0-"))
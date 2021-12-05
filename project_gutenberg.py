import csv
import requests
import os

def read_csv(csv_file):
    with open(csv_file) as my_file:
        reader = csv.reader(my_file)
        return [list([str(k) for k in x]) for x in reader]

def download(idVal):
    res = requests.get("https://www.gutenberg.org/files/{}/".format(idVal))
    fileVal = str(res.text).partition('.txt">')[2].partition("</a>")[0]
    url = "https://www.gutenberg.org/files/{}/{}".format(idVal, fileVal)
    res = requests.get(url)
    f = open("{}.txt".format(idVal), "w")
    f.write(res.text)
    f.close()

def get_book(idVal):
    if not os.path.exists("{}.txt".format(idVal)):
        download(idVal)
        
    text = open("{}.txt".format(idVal)).read()
    text = text.partition("***")[2]
    text = text.partition("***")[2]
    text = text.partition("End of the Project Gutenberg")[0]
    text = text.replace("***", "")
    text = text.strip()
    return text

if __name__ == "__main__":
    x = read_csv("pg_catalog.csv")
    all_vals = {}
    for val in x:

        info = {

        }
        for i in range(len(x[0])):
            info[x[0][i]] = val[i]
        info['Bookshelves'] = info['Bookshelves'].split(";")
        
        if 'Poetry' in info['Bookshelves']:
            info['Contents'] = get_book(val[0])
            all_vals[val[0]] = info

    # info_vals = [all_vals[str(i)] for i in all_vals.keys() if 'Poetry' in all_vals[str(i)]['Bookshelves']]
    # print(len(all_vals[0]))
    authors = {}
    for _, val in all_vals.items():
        for author in val['Authors'].split(";"):
            author = author.strip()
            if author not in authors:
                authors[author] = []
            authors[author].append(val)
    print(len(authors.keys()))
    print(x[0])
    quit()

    for val in all_vals.keys():
        print(get_book(val))
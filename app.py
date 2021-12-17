from flask import Flask, render_template, jsonify, redirect
import json
import random
import parsegenerated
import random
import os

app = Flask(__name__, static_url_path='/static/')


poems = set()
for val in json.load(open("poems.json"))['poems']:
    poems.add(val['text'])

poems = list(poems)
GOOD_POEMS = open("good.txt").read().split("\n")
BAD_POEMS = open("bad.txt").read().split("\n")

DATASET = json.load(open("dataset.json"))
to_rate = []

for poem in DATASET['human']:
    if poem['id'] not in (GOOD_POEMS + BAD_POEMS):
        to_rate.append(poem)

def get_poem(generated=False, maxLength=500):
    x = None
    while x == None or (len(x) > maxLength or len(x) < 10):
        if generated == True:
            x = parsegenerated.generate()
        else:
            x = random.choice(poems)
    return x

@app.route('/api', methods=['GET'])
def api():

    x = [DATASET['by_id'].get(x, 'None') for x in open("good.txt").read().split("\n")]
    return render_template("safe.html", values=x)

def color():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())

def mark_as_good(idVal):
    os.system("echo '{}' >> good.txt".format(idVal))

def mark_as_bad(idVal):
    os.system("echo '{}' >> bad.txt".format(idVal))

@app.route('/isGood/<idVal>', methods=['GET'])
def is_good(idVal):
    if 'good' in idVal:
        idVal = idVal.replace("good", "")
        mark_as_good(idVal)
        print("MARKED AS GOOD")
    else:
        idVal = idVal.replace("bad", "")
        mark_as_bad(idVal)
        print("MARKED AS BAD")
    
    return "Okay"

def poem_to_api_response(poem):
    if poem['generated']:
        about = """
            This is an auto-generated poem by GPT-2
        """
        classVal = "generated"
    else:
        about = """
            This is not an auto-generated poem
        """
        classVal = "human"
    
    return {
        "generated": poem['generated'],
        "about": about,
        "text": poem['text'],
        "title": poem['title'],
        "author": poem['author'],
        "color": color(),
        "class": classVal,
        "id": poem['id'],

    }

def get_good_poem():
    a = open("good.txt").read().split("\n")
    b = "FAKE_KEY"
    while b not in DATASET['by_id']:
        b = random.choice(a)

        print(b)
    return DATASET['by_id'][b]

def get_gen_poem():
    a = open("good.txt").read().split("\n")
    b = "FAKE_KEY"
    while b not in DATASET['by_id'] and "gen" not in b:
        b = random.choice(a)
    return DATASET['by_id'][b]
HUMAN_POEMS = []

a = open("good.txt").read().split("\n")
for val in a:
    if "gen" not in val and len(val) > 0:
        HUMAN_POEMS.append(DATASET['by_id'][val])
def get_human_poems():
    random.shuffle(HUMAN_POEMS)
    return HUMAN_POEMS[:5]



@app.route('/rate', methods=['GET'])
def rate():
    values = []
    for i in range(10):
        values.append(poem_to_api_response(to_rate.pop(0)))

    return render_template("rate.html", values=values)

@app.route('/onlyGood', methods=['GET'])
def onlyGood():
    values = []
    for i in range(10):
        x = poem_to_api_response(get_good_poem())
        x['id_val'] = "about-{}".format(x['id'])
        values.append(x)

    return render_template("swipe.html", values=values)

@app.route('/', methods=['GET'])
def index():
    values = []
    for i in range(5):
        x = poem_to_api_response(get_good_poem())
        x['id_val'] = "about-{}".format(x['id'])
        values.append(x)

    for val in get_human_poems():
        x = poem_to_api_response(val)
        x['id_val'] = "about-{}".format(x['id'])
        values.append(x)

    random.shuffle(values)

    

    return render_template("swipe.html", values=values)
    about = """
        This is an auto-generated poem by GPT-2
    """

    about = """
        This is not an auto-generated poem
    """
    values = []
    for i in range(10):
        if random.randint(1,3) == 1:
            values.append({
                "generated": True,
                "about": about,
                "text": "generated" + get_poem(True),
                "title": "",
                "author": "",
                "color": color(),
                "class": "generated",
                "id_val": "about-{}".format(i),
                "id": 24,

            })
            
        else:
            values.append({
                "generated": False,
                "about": about,
                "text": get_poem(False),
                "title": "",
                "author": "",
                "color": color(),
                "class": "",
                "id_val": "about-{}".format(i),
                "id": 24,

            })

    return render_template("swipe.html", values=values)

@app.route('/new', methods=['GET'])
def newQuestion():
    return jsonify({
        "generated": False,
        "text": "Testing",
        "title": "",
        "author": "",

    })

@app.route('/list', methods=['GET'])
def newQuestions():
    return jsonify([{
        "generated": False,
        "text": "Testing",
        "title": "",
        "author": "",
        "id": 24,

    } for i in range(10)])

@app.route('/map', methods=['GET'])
def map():
    return render_template("map.html")

def return_my_coordinates():
    # Read the file
    my_coordinates = open("static/heatmap.txt").read()
    # Split each coordinate on new line
    new_line_character = "\n"
    return my_coordinates.split(new_line_character)

@app.route('/geojson')
def geojson():
    features = []
    counts = {}
    for val in return_my_coordinates():
        if val not in counts:
            counts[val] = 0
        counts[val] += 1

    for key, count in counts.items():
        longitude, latitude = [float(x) for x in key.split(",")]
        features.append({ "type": "Feature", "properties": { "id": key, "mag": count }, "geometry": { "type": "Point", "coordinates": [ longitude, latitude, 1.0 ] } })
    
    return jsonify({
        "type": "FeatureCollection",
        "crs": { "type": "name", "properties": { "name": "heatmap" } },
        "features": features
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
from flask import Flask, render_template, jsonify, redirect
import json
import random

app = Flask(__name__, static_url_path='/static/')

def color():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())

@app.route('/', methods=['GET'])
def index():
    about = """
        This is an auto-generated poem by GPT-2
    """

    about = """
        This is a poem called <b>Testin Poem</b>
        written by <b>Testing Again</b>
    """
    return render_template("swipe.html", values=[{
        "generated": False,
        "about": about,
        "text": "Testing",
        "title": "",
        "author": "",
        "color": color(),
        "class": "generated",
        "id_val": "about-{}".format(i),
        "id": 24,

    } for i in range(10)])

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
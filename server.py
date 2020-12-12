#!flask/bin/python
from flask import Flask, url_for, request, redirect, abort, jsonify
from AlbumDao import albumDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/albums')
def getAll():
    return jsonify(albumDao.getAll())

@app.route('/albums/<int:code>')
def findById(code):
    return jsonify(albumDao.findById(code))

# create 
# curl -X POST -d "{\"code\":\"code\", \"artist\":\"artist\", \"title\":\"title\", \"price\":\"price\"}" -H Content-Type:application/json http://127.0.0.1:5000/albums


@app.route('/albums', methods=['POST'])
def create():

    if not request.json:
        abort(400)

    album = {
        "code": request.json["code"],
        "artist": request.json["artist"],
        "title": request.json["title"],
        "price": request.json["price"]
    }
    return jsonify(albumDao.create(album))

    #return "served by Create"

@app.route('/albums/<int:code>', methods=['PUT'])
def update(code):
    foundAlbum=albumDao.findById(code)
    print(foundAlbum)
    if foundAlbum == {}:
        return jsonify({}), 404
    currentAlbum = foundAlbum
    if 'artist' in request.json:
        currentAlbum['artist'] = request.json['artist']
    if 'title' in request.json:
        currentAlbum['title'] = request.json['title']
    if 'price' in request.json:
        currentAlbum['price'] = request.json['price']
    albumDao.update(currentAlbum)

    return jsonify(currentAlbum)

@app.route('/albums/<int:code>', methods=['DELETE'])
def delete(code):
    albumDao.delete(code)
    
    return jsonify({"done": True})

if __name__ == "__main__":
    app.run(debug=True)
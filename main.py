from fastapi import FastAPI
import json

app = FastAPI()
# fornecido um id, retorno o
# json do filme
# /movie/1


@app.get("/find_id/{id}")
async def get_movie(id: int):
    # lista de dictionary
    data = json.load(open('filmes.json'))
    for filme in data:
        if filme['id'] == id:
            return filme
    return {}
    # return {"id": id, "title": "Avatar"}


@app.get("/find_title_genre/{title}/{genre}")
async def find(title: str, genre: str):
    data = json.load(open('filmes.json'))
    encontrou = []
    for filme in data:
        # in - contains (ou contem um substring)
        if title.lower() in filme['title'].lower() and genre.lower() in filme['genre'].lower():
            # append - adiciona na lista
            encontrou.append(filme)
    return encontrou


@app.get("/find_title/{title}")
async def find(title: str):
    data = json.load(open('filmes.json'))
    encontrou = []
    for filme in data:
        # in - contains (ou contem um substring)
        if title.lower() in filme['title'].lower():
            # append - adiciona na lista
            encontrou.append(filme)
    return encontrou


@app.get("/find_genre/{genre}")
async def find(genre: str):
    data = json.load(open('filmes.json'))
    encontrou = []
    for filme in data:
        # in - contains (ou contem um substring)
        if genre.lower() in filme['genre'].lower():
            # append - adiciona na lista
            encontrou.append(filme)
    return encontrou


@app.get("/")  # HTTP GET
async def home():
    return {"msg": "Hello"}


# uvicorn main:app --reload

# pip install -r requirements.txt
# source env/
# pip install fastapi uvicorn

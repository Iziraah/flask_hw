import random
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI
templates = Jinja2Templates(directory='templates')

class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str
    
movies = []


for i in range(1, 10):
    movies.append(Movie(id=i, title = random.choice(['Green Mile', 'Jocker', 'Interstellar', 'Green Book', 'Jango Freeman', 'Lion King', 'Sederella', 'Sailor moon', 'Walking Dead', 'American Horror History']), description=f'Description{i}', genre=random.choice(['comedy', 'horror', 'adventure', 'cartoon'])))
    
@app.get("/", response_class=HTMLResponse)
async def read_movies(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'movies': movies})

@app.get("/movies", response_model=List[Movie])
async def get_movies():
    return movies

@app.get("/movies/{genre}", response_model=List[Movie])
async def get_gen_movie(movie_genre, movie: Movie):
    for i in range(len(movies)):
        if movies[i].genre == movie_genre:
            return movie[i]
    raise HTTPException(status_code=404, detail="sorry, genre not found")

@app.post("/movies", response_model=Movie)
async def create_movie(movie: Movie):
    movie.id = len(movies) + 1
    movies.append(movie)
    return movie

@app.put("/movies/{movie_id}", response_model=Movie)
async def update_movie(movie_id: int, updated_movie: Movie):
    for i, movie in enumerate(movies):
        if movie.id == movie_id:
            updated_movie.id = movie_id
            movies[i] = updated_movie
            return updated_movie
    raise HTTPException(status_code=404, detail="Movie not found")

@app.delete("/movies/{movie_id}")
async def delete_movie(movie_id: int):
    for i, movie in enumerate(movies):
        if movie.id == movie_id:
            del movies[i]
            return {"message": "Movie deleted successfully"}
    raise HTTPException(status_code=404, detail="Movie not found")

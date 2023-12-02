from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# crea varios diccionarios con peliculas

peliculas = [
    {
        "id": 1,
        "nombre": "La vida es bella",
        "año": 1997,
        "director": "Roberto Benigni"
    },
    {
        "id": 2,
        "nombre": "El Padrino",
        "año": 1972,
        "director": "Francis Ford Coppola"
    },
    {
        "id": 3,
        "nombre": "El Padrino: Parte II",
        "año": 1974,
        "director": "Francis Ford Coppola"
    },
    {
        "id": 4,
        "nombre": "El caballero oscuro",
        "año": 2008,
        "director": "Christopher Nolan"
    },
    {
        "id": 5,
        "nombre": "12 hombres en pugna",
        "año": 1957,
        "director": "Sidney Lumet"
    },
    {
        "id": 6,
        "nombre": "La lista de Schindler",
        "año": 1993,
        "director": "Steven Spielberg"
    },
    {
        "id": 7,
        "nombre": "Pulp Fiction",
        "año": 1994,
        "director": "Quentin Tarantino"
    },
    {
        "id": 8,
        "nombre": "El señor de los anillos: El retorno del rey",
        "año": 2003,
        "director": "Peter Jackson"
    },
    {
        "id": 9,
        "nombre": "El bueno, el malo y el feo",
        "año": 1966,
        "director": "Sergio Leone"
    },
    {
        "id": 10,
        "nombre": "El club de la pelea",
        "año": 1999,
        "director": "David Fincher"
    }
]

# crea una ruta para obtener todas las peliculas
@app.get("/peliculas")
def get_peliculas():
    return peliculas

# crea una ruta para obtener una pelicula por su id
@app.get("/peliculas/{pelicula_id}")
def get_pelicula(pelicula_id: int):
    for pelicula in peliculas:
        if pelicula["id"] == pelicula_id:
            return pelicula
    return {"error": "pelicula no encontrada"}

# crea una ruta para obtener una pelicula por su nombre
@app.get("/peliculas/nombre/{pelicula_nombre}")
def get_pelicula(pelicula_nombre: str):
    for pelicula in peliculas:
        if pelicula["nombre"] == pelicula_nombre:
            return pelicula
    return {"error": "pelicula no encontrada"}
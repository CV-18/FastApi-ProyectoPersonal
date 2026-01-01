from models.genero import Genero

db_generos = [Genero] = [
    Genero(
        id=1,
        nombre="Rock",
        historia="El rock se originó en la década de 1950 en Estados Unidos...",
        filosofia="El rock representa la rebeldía y la expresión individual...",
        artistas_destacados=["The Beatles", "Led Zeppelin", "Queen"],
        subgeneros=["Rock clásico", "Rock alternativo", "Punk rock"]
    ),
    Genero(
        id=2,
        nombre="Death Metal",
        historia="El death metal se originó en la década de 1980...",
        filosofia="El death metal representa la agresión y la intensidad...",
        artistas_destacados=["Metallica", "Slayer", "Megadeth"],
        subgeneros=["Death metal clásico", "Death metal moderno"]
    ),

    Genero(
        id=3,
        nombre="Black Metal",
        historia="El black metal se originó en la década de 1980 en Europa...",
        filosofia="El black metal representa la oscuridad y el misticismo...",
        artistas_destacados=["Burzum", "Mayhem", "Darkthrone"],
        subgeneros=["Black metal noruego", "Black metal sinfónico"]
    )

]
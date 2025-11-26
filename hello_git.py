print("Hello Git")

"""

Se empieza a utilizar GIT con el comando:
"git init" dentro de la carpeta principal del proyecto

    **Para introducir tu nombre y correo electrónico en 
    Git, usa los comandos git config --global user.name 
    "Tu Nombre" y git config --global user.email "tu@ejemplo.com", 
    respectivamente, en la terminal. Reemplaza "Tu Nombre" 
    y "tu@ejemplo.com" con tus propios datos. 

    ** Se puede cambiar el ronmbre de la rama con el comando"
    git branch -m "nombre de la rama"

    ** Con el comando " git status " se ve el status del git obvio

    **Se agrega un archivo al git en stage con el comando"
    git add "nombre de archivo"

    **Se le cambia de stage a la "fotografia" con el comando"
    git commit -m "nombre del commit"

    **Se puede volver a una version anterior version con"
    git checkout "nombre del archivo"
    o tambien:
    git restore "nombre del archivo"
        Aunque este ultimo es mas especifico
        puesto que tambien esta git switch para cambiar
        de rama.
            Esto lo que hara es hacer que el archivo se 
            muestre como estaba al comento de hacer la 
            fotografia.

https://www.youtube.com/watch?v=3GymExBkKjE
min 42.10
min 1:00:00
"""
print("Ahora edite el fichero")
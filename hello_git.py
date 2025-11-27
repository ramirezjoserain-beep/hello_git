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
    **Hay una manera de ver los archivos que se tienen
    guardados de una manera diferente a la que se muestra
    con git log, que seria con los comandos:
        * git log --graph (lo muestra como ramas)
        * git log --graph --pretty=oneline (una linea por saved)
        * git log --graph --decorate --all --oneline
    ** Se pueden realizar alias con el comando:
        git config --global alias."nombre del alias que
        quieres que tenga (tree)" "comando que quieres que 
        el alias ejecute (X[git]X log --decorate --all --oneline)"
            ****Importante**** Emitir el GIT en el comando
            del alias 
    **Se puede borrar un alias creado con:
        * git config --global --unset alias."nombre del alias
        (tree)"
    **En el caso de que se quiera ignorar un archivo que 
    se genera todo el tiempo (p.e. Mac con .DS_Store),
    se debe crear un archivo que se llame touch
    {.gitignore} y en el esribir [**/"nombre del archivo
    a ignorar"]
    **COMANDO git diff
        Permite visualizar que se le ha cambiado a 
        determinado archivo tanto que se le ha quitado, como
        lo que se le ha agregado. Comando:
            git diff "nombre archivo"
https://www.youtube.com/watch?v=3GymExBkKjE
min 42.10
min 1:00:00
"""
print("Ahora edite el fichero")
print("Otro edit al fichero")
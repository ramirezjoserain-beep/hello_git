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
    **COMANDO STATUS
        Con el comando " git status " se ve el status del git obvio
    **COMANDO ADD
        Se agrega un archivo al git en stage con el comando"
            git add "nombre de archivo"
            git add . (se agrega todo lo que esta pendiente)
    **COMANDO COMMIT
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
    **COMANDO LOG
        Hay una manera de ver los archivos que se tienen
        guardados de una manera diferente a la que se muestra
        con git log, que seria con los comandos:
            * git log --graph (lo muestra como ramas)
            * git log --graph --pretty=oneline (una linea por saved)
            * git log --graph --decorate --all --oneline
    **COMANDO ALIAS
        Se pueden realizar alias con el comando:
            git config --global alias."nombre del alias que
        quieres que tenga (tree)" "comando que quieres que 
        el alias ejecute (X[git]X log --decorate --all --oneline)"
            ****Importante**** Emitir el GIT en el comando
            del alias 
    **Se puede borrar un alias creado con:
        * git config --global --unset alias."nombre del alias
        (tree)"
    **IGNORAR ARCHIVO
        En el caso de que se quiera ignorar un archivo que 
        se genera todo el tiempo (p.e. Mac con .DS_Store),
        se debe crear un archivo que se llame touch
        {.gitignore} y en el esribir [**/"nombre del archivo
        a ignorar"]
    **COMANDO DIFF
        Permite visualizar que se le ha cambiado a 
        determinado archivo tanto lo que se le ha quitado,
        como lo que se le ha agregado. Comando:
            git diff "nombre archivo"
    **COMANDO CHECKOUT
        Permite moverse de una rama a otra con el codigo
        que identifica a esa rama en especifico y volver 
        a la ultima rama que se guardo o cambiar a otra 
        rama que se haya guardado en el pasado.
            git checkout 80e19f3a547fbf7ab4d06390da07c00bc34c849a
    **COMANDO REFLOG
        Permite ver el historial completo de la rama, es 
        decir, todos los movimientos ejecutados desde el 
        primer guardado en adelante. 
            git reflog 
    **COMANDO RESET --HARD
        Permite borrar cambios guardados volviendo a 
        un punto del pasado guardado y borrando todo lo 
        posterior a ese punto (p.e. supongamos que estamos
        en el dia viernes y quieres volver al dia martes, 
        pues en la logica de git harias 
            [git reset --hard martes] 
        lo que haria que volvieras al martes "borrando
        " los dias posteriores hasta el viernes siempre que esten
        guardados) y en el caso de que se quiera deshacer ese
        cambio de ir al pasado y borrar lo demas lo que hay que
        hacer es meter el mismo comando pero con el viernes 
            git reset --hard viernes 
        para volver al "presente"
    **COMANDO TAG
        Permite colocarle un tag a un commit para por 
        ejemplo saber los commits que representan la 
        version 1.1 o 1.2, etc. Le da un nombre especifico
        que sirve de referencia al usuario y se escribe asi:
            git tag nombre del tag (clase_1)
https://www.youtube.com/watch?v=3GymExBkKjE
min 42.10
min 1:00:00
min 1:26:00
"""
print("Ahora edite el fichero")
print("Otro edit al fichero")
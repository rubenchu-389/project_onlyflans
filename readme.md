Pasos del Hito-1

1) Se crea un entorno virtual:
    * python3 -m venv onlyflans


2) Se activa el entonro virtual (Linux):
    * source onlyflans/bin/activate    

3) Se instala Django: 
    * pip install Django(version5)

4) Se crea el proyecto y se posiciona dentro de la carperta para crear las migraciones:
    * djando-admin startproject onlyflans
    * cd onlyflans
    * python3 manage.py makemigrationes
    * python3 manage.py migrate

5) Se crea un servidor:
    * python3  manage.py run server 

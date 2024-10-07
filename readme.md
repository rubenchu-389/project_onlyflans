### Pasos del Hito-1, Hito-2

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

### Se comienza el Hito-3

6) Se modifica el navbar cambiando color de la barra

7) Se crean los models para agregrar los flans al admin 

8) Se agregan los flanes al archivo index.html

9) Se separan los flanes publicos de los privados en el index y en bienvenidos

10) se crea formulario de conctacto 

11) Se crea el boton contacto en el navbar para ingresar los datos como nombre, correo y texto, se redirigue al exito dejando el mensaje    

12) Se hacen las respectivas migraciones 


### Hito-4

13) Se agregan las funciones para la autenticaion de los usuarios como lo es el login y logout 

14) Agregar decorador login_required en las vistas (welcome) de manera que no permita a usuarios no registrados acceder a la página de Bienvenida

15) Se crean usuarios en el admin 



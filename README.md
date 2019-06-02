#### Requerimientos

* Docker
* docker-compose
* Make

#### Ambiente de desarrollo

1.- Buscar dentro de **app/** el archivo **.env.dist** y quitarle la extensión **.dist**

2.- Ejecutar el siguiente comando que creara e iniciara el ambiente de desarrollo

~~~~
$ make development
~~~~

> NOTA:
>
> * Si ya tienes creado el ambiente de desarrollo puedes iniciarlo con: **make up**
> * El proyecto se iniciara en el puerto 80 del host ej: **http://localhost/health**
> * El archivo **.env** esta ignorado en este proyecto
>

#### Pruebas unitarias (UnitTest)

Se esta utilizando pytest como suite de testing

~~~~
$ make test
~~~~


#### Generar imagen de docker empaquetada para despliegue
~~~~
$ make install
~~~~

> NOTA:
>
> Esta imagen de docker se recomienda para desplegar la aplicación


#### Mas comandos

Para ver la lista completa de comandos ejecute:
~~~~
$ make
~~~~
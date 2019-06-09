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
> * Si ya tienes creado el ambiente de desarrollo puedes iniciarlo con: **make container-up**
> * El proyecto se iniciara en el puerto 80 del host ej: **http://localhost/health**
> * El archivo **.env** esta ignorado en este proyecto
>

#### Pruebas unitarias modo desarrollo (UnitTest)

Se esta utilizando pytest como suite de testing

~~~~
$ make development-unit-test
~~~~


#### Generar imagen de docker empaquetada para despliegue
~~~~
$ make deploy-image
~~~~

> NOTA:
>
> * Esta imagen de docker se recomienda para desplegar la aplicación
> * Los unit test empaquetados para deploy se pueden ejecutar con **deploy-unit-test**
>


#### Mas comandos

Para ver la lista completa de comandos ejecute:
~~~~
$ make
~~~~
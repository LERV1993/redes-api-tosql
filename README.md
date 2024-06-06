
# Consumir api y registrar datos en base de datos SQL

Este repositorio utiliza una base de datos SQL la cual está configurada por defecto en el puerto 3308.

Se hace una solicitud GET a una API pública, en este caso a la de [Freetogame](https://www.freetogame.com/api-doc).

Nos basamos en la estructura de los datos devueltos por la api desde su endpoint `/api/games` pasando la lista de los mismos en formato `Json` a un metodo que llama a la base de datos e itera esta lista para ingresarlos en una tabla de la base de datos llamada `api`. La tabla es creada por la función si no existe.

Los datos que guardamos en la base de datos son `title | short_description | genre | release_date`.

El archivo que se encarga de ejecutar la función que registra los datos en la base de datos posee declarada la configuración para poder acceder a la base de datos. Está pensado para ser usado en un entorno local por lo cual la configuración por defecto es:

- user: root
- password: (ninguna)
- host: localhost
- port: 3308
- database: redes

Para esto es necesario exista la base de datos `redes` y que nuestro motor SQL este configurado en el puerto 3308, de lo contrario debe cambiarse.

La conexión a la base de datos dentro del archivo `baseDeDatos.py` está encerrado en un `try | catch` para que en caso de cualquier error el sistema devuelva la siguiente leyenda:

- `Error al conectar o al ejecutar la consulta:` + El error que ha ocurrido.






## Información y agradecimientos

Este proyecto nace de la cursada de la matería de programación sobre redes del último año de la Tecnicatura en desarrollo de software. Impartido por el docente [Javier Juan Carlos Blanco](https://github.com/jjcblanco).


## Authors

- [Gabriel Pettinari](https://github.com/GabrielPetty)
- [Gastón Murua](https://github.com/JGastonMurua)
- [Lucas Ruiz](https://github.com/LERV1993)


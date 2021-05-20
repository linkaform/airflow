# Airflow and it's usage on LinkaFrom


Para instalar breeze que lo vamos a usar para hacer build de airflow de ser necesario se corre

'''
./breeze
'''

Luego corres

'''
./breeze setup-autocomplete
'''

Para configurar la base de datos inicial arrancar con

'''
 ./breeze start-airflow -b postgres
'''

Esto va a crear una base de datos inicial para que el airflow funcione lo que hice fue agarar ese volumen y apuntarlo al nuevo contenedor

Pudieramos hacer una base de datos base y con esa siempre arrancar airflow con user y passwords establecidos. Guardar un tar y ejecutar desde ahi


Esto te dara la capacidad de usar el autocomplete de breeze

Actulmente en linkaform utilizamos la version 2.0 Stable de ApacheAirflow con postgres y python3.8

Para correr Apache Airflow simplemente corre

'''
./lkf -d start airflow
'''

Esto arrancara todos los contenedores necesarios para correr apache airflow en tu computadora.

En carpeta de dags, encontraras los dags de los distintos clientes, para motivos practicos, esto esta en un git separado

# Start the service

```
docker-compose up -d
```

# Stop everything

```
 docker stop $(docker ps | grep airflow_  |  awk {'print $1'}) && docker rm $(docker ps | grep airflow_  |  awk {'print $1'})
 ```


---


# Build Linkaform Local
```
docker-compose -f docker-compose.yml build airflow-webserver
```

# Build LinkaFrom
```
docker-compose -f docker-prod.yml build airflow-webserver
#para probar local hacer tag
docker tag linkaform/airflow:latest linkaform/airflow:2.0.1
```

hacer push
```
docker push linkaform/airflow:latest
```

acutalizar preprod

conectarse al airflow de preprod
```
ssh develop.linkaform.com -p 2209
```

conectarse al airflow de produccion
```
ssh airflow.linkaform.com
```

hacer el deploy en produccion y dev
```
cd /srv/airflow
docker stack deploy -c docker-stack.yml af --with-registry-auth

```

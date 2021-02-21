# brewery_map

Map of English breweries, created using PostGIS, GeoDjango and Leaflet.



pull docker image from https://hub.docker.com/r/tobi312/rpi-postgresql-postgis/

```
docker run --name some-postgis -v $(pwd)/postgis:/var/lib/postgresql/data -p 5432:5432 -e POSTGRES_USER=user001 -e POSTGRES_PASSWORD=password -e POSTGRES_DBNAME=gis -d tobi312/rpi-postgresql-postgis:latest
```

Postgresql (postgis extension enabled) server should now be set up and running with following credentials:

```
'NAME': 'gis',
'USER': 'user',
'PASSWORD': ‘password,
'HOST': 'localhost',
'PORT': '5432'
```




# images

docker pull postgres

docker pull dpage/pgadmin4

docker images

# create network
docker network create --driver bridge postgres-network
docker network ls


# create containers run executoins

docker run --name teste-postgres --network=postgres-network -e "POSTGRES_PASSWORD=Postgres2018!" -p 5432:5432 -v C:/Users/smyth/Workspace_Docker/Volume_PostgreSQL:/var/lib/postgresql/data -d postgres

docker run --name teste-pgadmin --network=postgres-network -p 15432:80 -e "PGADMIN_DEFAULT_EMAIL=smythy.costa@gmail.com" -e "PGADMIN_DEFAULT_PASSWORD=PgAdmin2018!" -d dpage/pgadmin4

docker ps


# test

 http://localhost:15432
 
 
 
 # references
 
https://imasters.com.br/banco-de-dados/postgresql-docker-executando-uma-instancia-e-o-pgadmin-4-partir-de-containers

https://www.youtube.com/watch?v=G3gnMSyX-XM
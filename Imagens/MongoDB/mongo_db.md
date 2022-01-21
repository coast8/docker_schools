


# images

docker pull tutum/mongodb


# run

`no password, recommended for development environment`

docker run -d -p 27017:27017 -p 28017:28017 -e AUTH=no tutum/mongodb

` specifying a password `

docker run -d -p 27017:27017 -p 28017:28017 -e MONGODB_PASS="mypass" tutum/mongodb


# enter in container

docker ps -a

docker start 77b903780b83

 
# references

https://medium.com/dockerbr/mongodb-no-docker-dd3b72c7efb7

https://marquesfernandes.com/desenvolvimento/ferramentas-gratuitas-para-gerenciar-mongodb/



***************************************************************************************
# Docker Compose
***************************************************************************************


"""
O Docker Compose é uma ferramenta para a criação e execução de múltiplos containers de aplicação.

Com o Compose, você usar um arquivo do tipo yml para definir como será o ambiente de 
sua aplicação e usando um único comando você criará e iniciará todos os serviços definidos.

Compose é ótimo para desenvolvimento, testes e homologação, 
bem como para melhorar seu fluxo de integração continua.

https://www.mundodocker.com.br/docker-compose/#:~:text=O%20Docker%20Compose%20%C3%A9%20uma,iniciar%C3%A1%20todos%20os%20servi%C3%A7os%20definidos.

"""


"""
O script codder de numero 005, tem os exemplos para este tipo de pratica.
"""

docker compose up               # executando arquivo docker compose
docker-compose -f xx_file up    # executando arquivo com nomeclatura diferente
docker-compose up -i -t         #
docker ps                       #



"""
no exemplo codder script 005, as apps se comunicam atraves de localhost:porta
"""












***************************************************************************************
# Dockerfile na pratica
***************************************************************************************

"""

https://cursos.alura.com.br/course/docker-e-docker-compose/task/29519


"""




"""

	Arquitetura



container atuando como proxy e load balance
______________________________________________

NGINX    
______________________________________________


|
|


container node1   container node2   container node3
________________ _________________ ____________________

Aplicação node  | Aplicação node  |  Aplicação node  
________________ _________________ ____________________


|
|


container mongo, database
______________________________________________

MONGO    
______________________________________________


"""



version: '3'
services:
    nginx:
        build:
            dockerfile: ./docker/nginx.dockerfile
            context: .
        image: douglasq/nginx
        container_name: nginx
        ports:
            - "80:80"
        networks: 
            - production-network
        depends_on: 
            - "node1"
            - "node2"
            - "node3"

    mongodb:
        image: mongo
        networks: 
            - production-network

    node1:
        build:
            dockerfile: ./docker/alura-books.dockerfile
            context: .
        image: douglasq/alura-books
        container_name: alura-books-1
        ports:
            - "3000"
        networks: 
            - production-network
        depends_on:
            - "mongodb"

    node2:
        build:
            dockerfile: ./docker/alura-books.dockerfile
            context: .
        image: douglasq/alura-books
        container_name: alura-books-2
        ports:
            - "3000"
        networks: 
            - production-network
        depends_on:
            - "mongodb"

    node3:
        build:
            dockerfile: ./docker/alura-books.dockerfile
            context: .
        image: douglasq/alura-books
        container_name: alura-books-3
        ports:
            - "3000"
        networks: 
            - production-network
        depends_on:
            - "mongodb"

networks: 
    production-network:
        driver: bridge





# RUN FILE


# STEP 01 build images 
# ______________________________

docker-compose build
docker images


# STEP 02 create containers and start containers
# _______________________________________________

docker-compose up            	# terminal travado
docker-compose up -d 			# run in backgroud
docker-compose ps

docker-compose down 			# mata os processos e destroy os containers


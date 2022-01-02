

***************************************************************************************
# 8.0 Parametros
***************************************************************************************

'''
	criando uma rede 
'''
docker network create --drive bridge minha_rede

docker network ls

	
docker run it -name my_container_a --network minha_rede ubuntu
docker run it -name my_container_b --network minha_rede ubuntu


ping my_container_a
ping my_container_b









# link

https://cursos.alura.com.br/course/docker-e-docker-compose/task/29413
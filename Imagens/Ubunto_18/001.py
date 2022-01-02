


***************************************************************************************
# map port end volume
***************************************************************************************

docker run -i -t -p 8080:80 -v /c/Users/a.carvalho.da.costa/workspace-docker/apache:/var/www/html ubuntu:18.04 /bin/bash




apt update
apt install apache2 -y
/etc/init.d/apache2 start 
/etc/init.d/apache2 status


apt install nano
nano --version


# ip docker toolbox
192.168.99.100




# network

hostname -i

apt-get update && apt-get install -y iputils-ping



# T1    pvargacl/oracle-xe-18.4.0

docker run --name oracle18 -i -t -d -p 1521:1521 pvargacl/oracle-xe-18.4.0


id: xe
usr: system 
pwd: oracle


# references

https://hub.docker.com/r/pvargacl/oracle-xe-18.4.0

https://github.com/oracle/docker-images/blob/main/OracleDatabase/SingleInstance/README.md


INSERT INTO "SYSTEM"."TCAT" (ID_CAT, PRICE, CATEGORY) VALUES ('2', '200', 'ROUPAS');
INSERT INTO "SYSTEM"."TCAT" (ID_CAT, PRICE, CATEGORY) VALUES ('3', '300', 'ROUPAS');
INSERT INTO "SYSTEM"."TCAT" (ID_CAT, PRICE, CATEGORY) VALUES ('4', '400', 'COMIDAS');
INSERT INTO "SYSTEM"."TCAT" (ID_CAT, PRICE, CATEGORY) VALUES ('5', '200', 'COMIDAS');
COMMIT;
























# T2    oracleinanutshell/oracle-xe-11g

docker run -i -t -d -p 49161:1521 -e ORACLE_ALLOW_REMOTE=true oracleinanutshell/oracle-xe-11g

docker attach 6a13b1aa83469f467d6dffa93cd2fa2ed66c4ca60bb29f6747c491a083a4eb3c

docker stop 6a13b1aa83469f467d6dffa93cd2fa2ed66c4ca60bb29f6747c491a083a4eb3c


Connect to container
	docker exec -it oracle bash -c "source /home/oracle/.bashrc; sqlplus /nolog"








REFERENCE

https://hub.docker.com/r/oracleinanutshell/oracle-xe-11g







HELPER
https://www.youtube.com/watch?v=ciYsDbBx80s

https://livesql.oracle.com/apex/f?p=590:71:31628580773109::NO:::

https://www.oracle.com/br/database/technologies/appdev/xe.html
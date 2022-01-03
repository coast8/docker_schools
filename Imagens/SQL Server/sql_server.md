

# images

docker pull mcr.microsoft.com/mssql/server


# run

docker run --name sqlserver -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=1q2w3e4r@#$" -p 1433:1433 -d mcr.microsoft.com/mssql/server


# connect

userid = 'sa'
PASSWORD=1q2w3e4r@#$

 
 
 # references

https://balta.io/blog/sql-server-docker
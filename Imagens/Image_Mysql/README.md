
## Use command

docker-compose -f .\mysql-docker-compose.yml up


## volumes v1
    volumes:
      - './mysql-data:/var/lib/mysql'


## volume v2
    volumes:
          - 'C:/Users/smyth/Workspace_Docker/Volume_MySQL:/var/lib/mysql'

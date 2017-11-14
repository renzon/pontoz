Para instalar o SQL Server

1. Instale o Docker
2. Execute docker pull microsoft/mssql-server-linux:2017-latest
3. Rode  
docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=Passw0rd' -p 1401:1433 --name sql1 -d microsoft/mssql-server-linux:2017-latest

Para conferir o Banco

1. docker exec -it sql1 "bash"
2. Entre no console do BD
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'Passw0rd'

3. Se etiver no mac pracisa instalar mais drivers:

https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Mac-OSX


Query para client e regionais:
SELECT p.*, r.*, s.*, t.* FROM partner AS p 
    INNER JOIN region AS r ON p.id=r.partner_id 
    INNER JOIN store AS s ON r.id=s.region_id 
    INNER JOIN  "transaction" AS t ON (s.id=t.store_id AND t.creation between '01/01/2017' and '12/31/2017 23:59:59') 

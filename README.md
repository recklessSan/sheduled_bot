##Install python libraries
Install libraries from __*requirements.txt*__
>pip install
> 
>*install __psycopg2-binary__ labrary

##Restore DB
Postgres13 database from __*backup/test.dump*__ (text) through command 
>psql 

or
>open file through text-editor, copy strings and run as sql-command

##Init
Add row with bot data to __keys__ table, like
>`insert into keys(id, name, token) values(uuid_generate_v4(), 'bot_name', 'bot_token')`

##Run
add argument __DATABASE_URL__ to connect DB
>postgres://user:password@localhost:5432/test

run app 
>main.py
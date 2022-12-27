# [Arquivo bd_e_tabela.py]
# Esse arquivo criar um Banco de Dados de nome: crud e duas tabelas: cliente e user
# ----------------------------------------------------------------------------------

#[Importações]----------------------------
import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = ''
)

cursor = database.cursor()
cursor.execute("CREATE DATABASE crud")
print('Banco de dados criado com sucesso!')

# -----------------------------------------

# [Criando tabela no Banco de Dados] ------
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'crud'
)

cursor = database.cursor()
sql = '''CREATE TABLE cliente(
    cpf VARCHAR(18) not null primary key,
    nome VARCHAR(40) not null,
    email VARCHAR(50),
    telefone varchar(15)
); '''

sql2 = ''' CREATE TABLE user(
    nome VARCHAR(40) NOT NULL,
    usuario VARCHAR(30) NOT NULL ,
    senha VARCHAR(6) NOT NULL
); '''

cursor.execute(sql)
cursor.execute(sql2)
print('Tabela criada com sucesso!')
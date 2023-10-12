import pyodbc

Driver = 'ODBC Driver 11 for SQL Server'
Driver1 = "SQL Server Native Client 11.0"
Driver2 = 'ODBC Driver 13 for SQL Server'
Driver3 = 'ODBC Driver 17 for SQL Server'
Driver4 = 'SQL Server'
Driver5 = 'SQL Server Native Client RDA 11.0'

Server = '.\\AVSQLSRV'
Database = 'unitydb'
UID = 'sa'
PWD = 'Sh@ll0w15y'

conexao = pyodbc.connect(DRIVER=Driver1, SERVER=Server, DATABASE=Database, UID=UID, PWD=PWD)
print("conexão bem sucedida")
def select():
    cursor = conexao.cursor()
    cursor.execute('Select codigo, nome, valor, date, hinicio, htermino from refeitorio')
    rows = cursor.fetchall()
    cursor.commit()
    print(rows)

    for i in (rows):
        print(f"este é o codigo {i[0]}")
        codigo = i[0]
        print(f"este é a nome {i[1]}")
        nome = i[1]
        print(f"este é a valor {i[2]}")
        valor = i[2]
        print(f"este é a date {i[3]}")
        date = i[3]
        print(f"este é a hinicio {i[4]}")
        hinicio = i[4]
        print(f"este é a htermino {i[5]}")
        htermino = i[5]
        return rows

def insert(codigo, name, valor, date, hinicio, htermino):
    cursor = conexao.cursor()
    cursor.execute(f"insert into refeitorio (codigo, nome, valor, date, hinicio, htermino) values ('{codigo}', '{name}','{valor}','{date}','{hinicio}','{htermino}')")
    cursor.commit()

def update(codigo, name, valor, date, hinicio, htermino):
    print('entrou no update')
    cursor = conexao.cursor()
    cursor.execute(f"update refeitorio set nome = '{name}', valor = '{valor}', date = '{date}', hinicio = '{hinicio}', htermino = '{htermino}' where codigo = '{codigo}'")
    cursor.commit()

def delete(codigo):
    print('entrou no delete')
    cursor = conexao.cursor()
    cursor.execute(f"delete from refeitorio where codigo = '{codigo}'")
    cursor.commit()
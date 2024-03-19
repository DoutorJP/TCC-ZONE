import sqlite3

def ler_tabela(nome_tabela):
    data = cursor.execute('''SELECT * FROM ''' + nome_tabela + '')
    for row in data:
        print(row)

def pegar_id_recente():
    data = cursor.execute('''SELECT MAX(ID) FROM TBCarro''')
    rows = cursor.fetchall()
    id = rows[0]
    s = ''
    for ele in id:
      s += str(ele)
    s = s.strip('[]')
    return s

def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

def pegar_placa_carro(placa):
    data = cursor.execute('''SELECT * FROM TBCarro WHERE placa = \"{}\"'''.format(placa))
    placa = cursor.fetchall()
    return placa[0][1]

def exis

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()
# cursor.execute('''INSERT INTO TBCarro VALUES (1,'ABC1234', NULL)''')   # INT ID; STRING PLACA; INT? ID DONO

#ler_tabela("TBCarro")
#print("ID MAIS RECENTE: ")
#id = pegar_id_recente()

pegar_placa_carro("placateste'")

#print(id)
# Commit your changes in the database
conexao.commit()

# Closing the connection
conexao.close()

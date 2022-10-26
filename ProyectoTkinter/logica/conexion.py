import mysql.connector

def conectar():
    db = mysql.connector.connect(host='localhost', port=3307, user='root', passwd='', database='coltis_productos')
    
    return db
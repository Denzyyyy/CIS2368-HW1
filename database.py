import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, dbName):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=dbName
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred", e )
    return connection


def list_values():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM vaults")
    vaults = cursor.fetchall()
    connection.close()
    
    print("Vaults:")
    for vault in vaults:
        print(vault)
        
def create_vault():
    number = int(input("Enter vault number: "))
    code = int(input("Enter vault code: "))
    content = input("Enter vault content: ")
    owner = input("Enter vault owner: ")
    
    
    connection = create_connection()
    cursor = connection.cursor()
    connection.execute("INSERT INTO vaults (number, code, content, owner) VALUES ", (number, code, content, owner))
    connection.commit()
    connection.close()
    
    print("Vault created")
    
def retrieve_vault():
    number = int(input("Enter vault number: "))
    code = int(input("Enter vault code: "))
    
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM vaults WHERE number = %s AND code = %s", (number, code))
    result = cursor.fetchone()
    connection.close()
    
    if result:
        print(result)
        return True
    else:
        print("Vault not found")
        return False
            

    

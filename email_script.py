import psycopg2
import time

class DatabasePostgress:
    def __init__(self, database_email):
        self.conn = psycopg2.connect(database_email)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS user_emails
                            (id SERIAL PRIMARY KEY,                            
                           email TEXT NOT NULL)                            
                           ''')
        self.conn.commit()       
        
    def insert_data(self):
        
           while True:           
            email = input("Enter the email: ")
            self.cursor.execute('Insert into user_emails (email) values (%s)',(email,))           
            if input("Do you want to add more data? (y/n)") == 'n':
                break        
            self.conn.commit()
       
    def view_all_data(self):        
        self.cursor.execute('SELECT * FROM user_emails')
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
        self.conn.commit()      
      

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    databasePostgress = DatabasePostgress(f'dbname=postgres user=postgres password= mahima@123 host=localhost port=5432')
    while True:
        print("1. Insert data", "2. View all data", "3. Exit", sep="\n")
        x = int(input("Enter the option: "))

        if x == 1:
            databasePostgress.create_table()
            databasePostgress.insert_data()       
        elif x == 2:
            databasePostgress.view_all_data()     
        else:
            databasePostgress.close_connection()
            exit()

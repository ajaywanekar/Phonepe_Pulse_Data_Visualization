import mysql.connector as sql
import pandas as pd
connection = sql.connect(
    host="localhost",
    database="phonepe",
    user="root",
    password="",

)

# database is already created
print(connection)
mycursor = connection.cursor(buffered=True)

mycursor.execute("""
CREATE TABLE a_transaction(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  State VARCHAR(255),
  Year INT,
  Quarter INT,
  Transaction_type TEXT,
  Transaction_count INT,
  Transaction_amount INT
);
""")

print("table created successfully df1")


# Load the data into a dataframe and giving it the variable name as df
df = pd.read_csv(r'C:/Users/s/PycharmProjects/mystreamlit/agg_transaction.csv')
print("csv file reading done df1")
# df.head()

# insert tha data from the dataframe into the database
for index, row in df.iterrows():
    qure1 = "INSERT INTO phonepe.a_transaction(State,Year,Quarter,Transaction_type,Transaction_count,Transaction_amount) values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(qure1,(row.State,row.Year,row.Quarter,row.Transaction_type,row.Transaction_count,row.Transaction_amount))
print("data inserted successfully into table df1")
# commit the changes
connection.commit()

mycursor.execute("""
     CREATE TABLE a_users(
       id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       State VARCHAR(255),
       Year INT,
       Quarter INT,
       Brand TEXT,
       Count INT,
       Percentage FLOAT 
     );
     """)

print("table created successfully df2")

df = pd.read_csv(r"C:/Users/s/PycharmProjects/mystreamlit/agg_users.csv")
print("csv reading done df2")

# insert data from dataframe into database
for index, row in df.iterrows():
    qure2 = "INSERT INTO phonepe.a_users(State,Year,Quarter,Brand,Count,Percentage) values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(qure2,(row.State,row.Year,row.Quarter,row.Brand,row.Count,row.Percentage))
print("data inserted successfully into table df2")
connection.commit()

mycursor.execute("""
       CREATE TABLE m_transaction(
         id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
         State VARCHAR(255),
         Year INT,
         Quarter INT,
         District VARCHAR(255),
         Count INT,
         Amount FLOAT
       );
       """)

print("table created successfully df3")

df = pd.read_csv(r'C:/Users/s/PycharmProjects/mystreamlit/map_transcation.csv')
print("csv reading done df3")

## insert data from dataframe into database
for index, row in df.iterrows():
    qure3 = "INSERT INTO phonepe.m_transaction(State,Year,Quarter,District,Count,Amount) values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(qure3, (row.State, row.Year, row.Quarter, row.District, row.Count, row.Amount))
print("data inserted successfully into table df3")
connection.commit()

mycursor.execute("""
      CREATE TABLE m_users(
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        State VARCHAR(255),
        Year INT,
        Quarter INT,
        District VARCHAR(255),
        Users INT
      );
      """)

print("table created successfully df4")

df = pd.read_csv(r'C:/Users/s/PycharmProjects/mystreamlit/map_users.csv')
print("csv reading done df4")

for index, row in df.iterrows():
    qure4 = "INSERT INTO phonepe.m_users(State,Year,Quarter,District,Users) values(%s,%s,%s,%s,%s)"
    mycursor.execute(qure4, (row.State, row.Year, row.Quarter, row.District, row.Users))
print("data inserted successfully into table df4")
connection.commit()

mycursor.execute("""
CREATE TABLE T_transaction(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  state VARCHAR(255),
  Year INT,
  Quarter INT,
  District VARCHAR(255),
  Count INT,
  Amount INT
);
""")

print("table created successfully df5")

df = pd.read_csv(r'C:/Users/s/PycharmProjects/mystreamlit/top_transcation.csv')
print("csv reading done df5")
for index, row in df.iterrows():
    qure5 = "INSERT INTO phonepe.T_transaction(State,Year,Quarter,District,Count,Amount) values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(qure5, (row.State, row.Year, row.Quarter, row.District, row.Count, row.Amount))
print("data inserted successfully into table df5")
connection.commit()

mycursor.execute("""
     CREATE TABLE T_Users(
       id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       State VARCHAR(225),
       Year INT,
       Quarter INT,
       District VARCHAR(255),
       Users INT
     );
     """)

print("table created successfully df6")

df = pd.read_csv(r'C:/Users/s/PycharmProjects/mystreamlit/top_users.csv')
print("csv reading done df6")

for index, row in df.iterrows():
    qure6 = "INSERT INTO phonepe.T_Users(State,Year,Quarter,District,Users) values(%s,%s,%s,%s,%s)"
    mycursor.execute(qure6, (row.State, row.Year, row.Quarter, row.District, row.Users))
print("data inserted successfully into table df6")
connection.commit()





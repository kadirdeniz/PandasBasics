import pandas as pd
import numpy as np
'''
-> Sql tables
-> Csv documents :widely used
-> python dictionaries
 
    can convert pandas dataframe
    
-> dataframe.head(n=?) datanın basından n kadar rowu tutar
-> dataframe.tail(n=?) datanın sonundan n kadar rowu tutar
'''

a = [{'city':'Delhi',"data":1000},
{'city':'Bangalore',"data":2000},
{'city':'Mumbai',"data":1000}]

b = pd.DataFrame(a)
print(a,b)

c=pd.read_csv('worldcities.csv')
d=c.head(n=10)

'''
----Databaseden veri çekme----

server = 'xxxxxxxx' # Address of the database server
user = 'xxxxxx' # the username for the database server
password = 'xxxxx' # Password for the above user
database = 'xxxxx' # Database in which the table is present
conn = pymssql.connect(server=server, user=user, password=password, database=database)
query = "select * from some_table"
df = pd.read_sql(query, conn) 
'''
e=c.tail(n=20)

print(c[1:10:2])
print(c[:7])
#print(c[:-10]) - değer olursa sondan işlem yapıyor sondan 10 row kalana kadar yazdırır

print(c.iloc[:5,:4])#In the example, we will only pick up the first five rows and the first four columns.

df = pd.DataFrame(np.random.randn(8,3),columns=['A','B','C'])#importante

df.iloc[5,2]='NaN'
df.fillna(0)

columns_num=['A','B','C']
print(df[columns_num].mean())
print(df[columns_num].sum())
print(df[columns_num].count())
print(df[columns_num].median())

k=pd.DataFrame(np.random.randn(5,6))
l=pd.DataFrame(np.random.randn(4,8))

m = pd.concat([k,l])    




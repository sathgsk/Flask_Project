import os
import cx_Oracle
#import configparser
cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_8")
from flask import Flask,request

app = Flask(__name__)

def getconnection() :
    #connection = cx_Oracle.connect("hr/hr@localhost:1521/orcl")
    connection = cx_Oracle.connect("hr", "hr", "localhost/orcl")
    return connection

@app.route('/getcustomer')
def getcustomer():
    connection = getconnection()
    cur = connection.cursor()
    cur.execute("select * from employees where rownum <10")
    col = cur.fetchall()
    cur.close()
    connection.close()
    return { 'result': col}

@app.route('/getcustomer1/<Id>')
def getcustomer1(Id):
    connection = getconnection()
    cur = connection.cursor()
    q = f"select first_name ||' '||last_name from employees where employee_id ={Id}"
    cur.execute(q)
    col = cur.fetchall()
    connection.commit()
    cur.close()
    connection.close()
    return { 'result': col}

@app.route('/getcustomer2/<Id>')
def getcustomer2(Id):
    connection = getconnection()
    cur = connection.cursor()                                                                                                                                                                                 
    q = f"update employees set first_name='Steven' where employee_id={Id}"    
    cur.execute(q)
    connection.commit()
    cur.close()
    connection.close()
    return { 'result': 'update sucessfull'}

@app.route('/getcustomer3',methods=['POST'])
def getcustomer3():
    connection = getconnection()
    cur = connection.cursor()     
    val =  request.get_json()                                                                                                                                                                          
    q = f"insert into employee (Id,Name) values ({val['Id']},{val['Name']})"
    cur.execute(q)
    connection.commit()
    cur.close()
    connection.close()
    return { 'result': "1 row inserted"}

@app.route('/getcustomer4/<Id>')
def getcustomer4(Id):
    connection=getconnection()
    cur=connection.cursor()
    q=f"delete student where Id={Id}"
    cur.execute(q)
    connection.commit()
    cur.close()
    connection.close()
    return {'result': '1 row deleted'}
    
@app.route('/getcustomer10/<ID>',methods=['GET','POST'])
def getCustomer10(ID):
        obj = request.get_json()
        print(obj)
        return obj

if __name__ == '__main__':
      app.run(debug=True)
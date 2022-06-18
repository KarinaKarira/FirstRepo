from pymysql import *
#* imports all files that the library wants to expose
from pymysql import cursors
#ALL DML queries here--->insert,update,delete,select
#ALL DDL queries that are to be executed only once are written in a seperate file,if return in this file
#then it would fall in execute_query


class DatabaseHelper():
    USER = 'Karina'
    PASSWORD = 'TUHITU'
    HOST = 'localhost'
    database = 'karina'
    #because for all the objects,they are going to have the same value hence class variables

    #because the are using class variables,they are class methods
    #standard convention--->classname_methodname(for good word in corporate world)
    #and objects ko connection bnane ka control nahi dena,because woh close kare ya na kare we dont have any gurantee
    #sare column ke heading return karega so that table banate time woh heading dikhe
    @classmethod
    def get_columns(cls, description):
        # column names are present as the first element of the collection,
        # hence extract the first element[0], create tuple & return it.
        return tuple(map(lambda x: x[0], description))
        #description is a nested tuple ((),(),(),()) in which each tuple's first value is column_name

    #SELECT
    #return me ek single row
    @classmethod
    def get_data(cls, query, parameters=None) -> dict:
        conn = connect(host=cls.HOST, database=cls.database, user=cls.USER, password=cls.PASSWORD)
        cur = conn.cursor(cursor=cursors.DictCursor)
        # cur is creating a pipeline by which we can exchange the data
        #cursors.Cursor returns a tuple(which is also default)
        #SSCursor-->bohot bada data hai toh thoda thoda karke send karega(similar to generator)
        if (parameters is None):
            cur.execute(query)
        else:
            cur.execute(query,parameters)
        result = cur.fetchone()
        # print(result) this we print just for confirmation
        cur.close()
        conn.close()
        return result

    @classmethod
    #this function is used to perform the specific task and does not return anything
    def execute_query(cls,query,parameters=None):
        conn=connect(host=cls.HOST,database=cls.database,user=cls.USER,password=cls.PASSWORD)
        cur=conn.cursor()
        if parameters is None: #for example if it is a delete query then we don't need any parameters
            cur.execute(query)
        else:
            cur.execute(query,parameters)
        conn.commit() #to permanantly save the changes
        #If this is missed we won't neither get an error nor the required op
        cur.close()
        conn.close()

    @classmethod
    #this function is used for getting multiple rows on output
    def get_all_data(cls,query,parameters=None):
        conn=connect(host=cls.HOST,database=cls.database,user=cls.USER,password=cls.PASSWORD)
        cur=conn.cursor()
        if parameters is None:
            result=cur.execute(query)
        else:
            result=cur.execute(query,parameters)
        result=cur.fetchall()
        #get me the column names of the data
        headers=DatabaseHelper.get_columns(cur.description)
        cur.close()
        conn.close()
        return (headers,)+result



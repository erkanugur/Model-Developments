

def check_table_exists(tablename,user,password):
    
    
    
    
    # DEPENDENCIES
    
    import cx_Oracle as cx
    

    dsnStr = cx.makedsn('localhost', '1521', service_name='orcl')
    connect = cx.connect(user=user, password=password,dsn=dsnStr)
    cursor = connect.cursor()
    try:
        cursor.execute("SELECT * FROM {}".format(tablename))
        return True
    except cx.DatabaseError as e:
        x = e.args[0]
        if x.code == 942: ## Only catch ORA-00942: table or view does not exist error
            return False
        else:
            raise e
    finally:
        cursor.close()
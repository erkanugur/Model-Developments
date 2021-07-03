
def sql_drop(table_name,user,password):
    
    
    
    
    
    
    
    # DEPENDENCIES
    
    import numpy as np
    import pandas as pd
    import datetime
    import cx_Oracle as cx
    
    dsnStr = cx.makedsn('localhost', '1521', service_name='orcl')
    
    start = datetime.datetime.now().replace(microsecond = 0)
    connect = cx.connect(user=user, password=password,dsn=dsnStr)
    cursor = connect.cursor()
    sql_drop = 'DROP TABLE ' + table_name
    print(sql_drop)
    cursor.execute(sql_drop)
    print('Sql_to_sandbox completed in '+str(datetime.datetime.now().replace(microsecond = 0)-start))
    
  


def read_oracle(sqlQuery,user,password):
    
    
    
    
    # DEPENDENCIES
    
    import cx_Oracle as cx
    import pandas as pd
    import numpy as np
    from enum import Enum
    import datetime
    
    dsnStr = cx.makedsn('localhost', '1521', service_name='orcl')
    start = datetime.datetime.now().replace(microsecond = 0)
    connect = cx.connect(user=user, password=password,dsn=dsnStr)
    cursor = connect.cursor()
    cursor.execute(sqlQuery)
    data = pd.DataFrame(cursor.fetchall())
    data.columns = [rec[0] for rec in cursor.description]
    print('Read data completed in '+str(datetime.datetime.now().replace(microsecond=0)-start))
    
    return data
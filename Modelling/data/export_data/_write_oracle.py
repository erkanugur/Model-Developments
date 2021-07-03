def write_oracle(df,table_name,user,password):
    
    
    
    
    
    
    
    
    
    #DEPENDENCIES
    
    import numpy as np
    import pandas as pd
    import datetime
    import cx_Oracle
    from sqlalchemy import types, create_engine
    from dssuite._util.oracle_utils import drop_oracle
    from dssuite._util.oracle_utils import check_table_exists
    
    Start_Time = datetime.datetime.now().replace(microsecond = 0)
    
    
    
    dsnStr = cx_Oracle.makedsn('localhost', '1521', service_name='orcl')
    
    if check_table_exists(table_name,user,password):
        drop_oracle(table_name,user,password)
        
   
    table_name = table_name.lower()
    #datetime transformation
    for i in df.columns:
        if i in df.select_dtypes(include = [np.number]).columns:
            df[i] = df[i].astype(float)
        else:
            df[i]  = df[i].astype(str)
    
    con = cx_Oracle.connect(user = user, password = password, dsn = dsnStr)
    
    #sqlalchemy için engine oluşturuyoruz.
    
    engine = create_engine("oracle+cx_oracle://" + user + ':' + password + '@' + dsnStr,max_identifier_length=128) #kolon isimlerini bos tablo olarak basarken kullanıyoruz
    
    conn = engine.connect()
    
    cur = con.cursor()
    
    #max string uzunluğu
    
    max_len = df[list(df.dtypes[df.dtypes=='object'].index)].applymap(lambda x : len(x)).max().max()
    
    #boş tablo şeması oluşturuyoruz.
    
    columns = df.head(0)
    
    columns.to_sql(table_name, conn, if_exists='replace', index = False,dtype={ i : types.VARCHAR(max_len) for i in list(df.dtypes[df.dtypes=='object'].index)})
    
    
    ga = str('(')
    
    for i in range(len(df.columns)):
        if i != len(df.columns)-1:
            ga = ga +str(':') + str(i+1) + ','
        else:
            ga = ga + str(':') +str(i+1) + ')'
        
    print(ga)
    
    cur = con.cursor()
    
    cur.executemany("insert into " + table_name + " values " + ga, list(df.values))
    con.commit()
    cur.close()
    con.close()
    conn.close()
    
    End_Time = datetime.datetime.now().replace(microsecond = 0)

    print("\n !!! DataFrame is written to database as %s and it lasts %s !!! \n" %(table_name,(End_Time - Start_Time)))
    
    




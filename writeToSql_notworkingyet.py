from sqlalchemy import create_engine
import urllib
import pandas as pd
import datetime as dt

# Settings
TargetServer = ' ' #server name
SchemaName = 'dbo'
TargetDb = 'test'
TableName = 'testvm'
# Trusted_Connection= 'yes'
UserName = ''
Password = ''
SourceFile = "C:\\Users\\your dir\\Downloads\\results\\vm20210104hr=0.json"

# Configure the Connection
Params = urllib.parse.quote_plus(r'DRIVER={SQL Server};SERVER=' + TargetServer + ';DATABASE=' + TargetDb + ';UID=' + UserName + ';PWD=' + Password)
ConnStr = 'mssql+pyodbc:///?odbc_connect={}'.format(Params)
Engine = create_engine(ConnStr)

# Load the json into a DataFrame
df = pd.read_json(SourceFile)

# Clear the Data in Target Table
sql = 'Truncate Table ' + TableName
with Engine.begin() as conn:
    conn.execute(sql)

# Load the Data in DataFrame into Table
df.to_sql(TableName, con=Engine, schema=SchemaName, if_exists='append', index=False)

print(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' | Data Imported Successfully')
import psycopg2
import os, time, datetime
dt=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
file1 = open("/cohesity-backup/post-thaw.log","a+" )
conn = None
exit_status = 0
try:
conn = psycopg2.connect(host='localhost',port='<POSTGRESQL_PORT>',user='<POSTGRESQL_USER>',password='<POSTGRESQL_PASSWORD>',database='<POSTGRESQL_DB_NAME>')
cur = conn.cursor()
cur.execute ("select version();")
data = cur.fetchone()
file1.write (dt)
file1.write ("\n-------------------------------------------\n")
file1.write ("\t PostgreSQL version is %s: "%data)
file1.write ("\n-------------------------------------------\n")
file1.write (dt)
file1.write ("\t Running query to unquiesce the database \n")
cur.execute ("select pg_stop_backup();")
file1.write (dt)
file1.write ("\t Database is unquiesced now \n")
cur.close()
except(Exception, psycopg2.DatabaseError) as error:
file1.write(dt)
file1.write(str(error))
file1.write( "\n Error in unquiesce DB, please check PostgreSQL logs for more info \n")
exit_status = 1
finally:
if conn is not None:
conn.close()
file1.write( "\n Database connection closed\n")
file1.close()
exit(exit_status)

import MySQLdb
import os
import time
import datetime
dt=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
file1 = open("/cohesity-backup/pre-freeze.log","a+" )
try:
conn = MySQLdb.connect ('localhost' , 'root' , 'password' )
cur = conn.cursor()
cur.execute ("select version()")
data = cur.fetchone()
file1.write (dt)
file1.write ("-------------------------------------------\n")
file1.write ("-------------------------------------------\n")
file1.write ("\t MySQL version is %s: "%data)
file1.write ("-------------------------------------------\n")
file1.write ("-------------------------------------------\n")

except:
file1.write (dt)
file1.write("\t ERROR! Unable to connect to MySQL server\n")

file2 = open ('/tmp/freeze_snap.lock', 'w')
file2.close()

try:
cur.execute (" flush tables with read lock ")
file1.write (dt)
file1.write ("\t Running quiesce.py script - quiesce of database successful \n")
except:
file1.write(dt)
file1.write( "\n ERROR! Unable to do flush tables with read lock, Please check MySQL error logs for more info\n")
while True:
check = os.path.exists ("/tmp/freeze_snap.lock")
if check == True:
continue
else:
break

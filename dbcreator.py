import sqlite3

connection = sqlite3.connect(r"./database3.db")
cur1 = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS Patient(
PatID INTEGER PRIMARY KEY  ,
VORNAME CHAR(20) ,
NACHNAME CHAR(20) ,
GEBURTSDATUM TEXT , 
LETZTENBESUCH TEXT
)"""

command2 = """CREATE TABLE IF NOT EXISTS BILDER(
PatID INTEGER  ,
id INTEGER PRIMARY KEY  ,
untersuchungstyp CHAR(20) ,
Bildgebungdatum CHAR(50),
SPEICHERORT TEXT ,
FOREIGN KEY(PatID) REFERENCES Patient(PatID)
)"""

command3 = """CREATE TABLE IF NOT EXISTS SIGNAL(
PatID INTEGER ,
id INTEGER PRIMARY KEY  ,
Pulsmessung INTEGER ,
Datum TEXT,
Dauer TEXT ,
FOREIGN KEY(PatID) REFERENCES Patient(PatID)
)"""

cur1.execute(command1)
cur1.execute(command2)
cur1.execute(command3)
connection.commit()
connection.close()

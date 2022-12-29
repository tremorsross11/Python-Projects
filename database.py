import sqlite3



conn = sqlite3.connect('test1.db')

fileList = ('information.docx', 'hello.txt', 'myimage.png', 'mymovie.mpg', 'world.txt', 'data.pdf', 'myphoto.jpg')

with conn:
    cur  = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT)")
    conn.commit()
conn.close()

conn = sqlite3.connect('test1.db')

with conn:
    cur = conn.cursor()
    for item in fileList:
        if item.endswith('.txt'):
            cur.execute('INSERT INTO tbl_files(col_fname) VALUES (?)', (item,))
    conn.commit()
conn.close()



conn = sqlite3.connect('test1.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname FROM tbl_files")
    varFile = cur.fetchall()
    print(varFile)
conn.close()

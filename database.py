import sqlite3

conn = sqlite3.connect('test1.db')

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
    cur.execute("INSERT INTO tbl_persons(col_fname) VALUES (?)", \
                ('information.docx'))
    cur.execute("INSERT INTO tbl_persons(col_fname) VALUES (?)", \
                ('hello.txt'))
    cur.execute("INSERT INTO tbl_persons(col_fname) VALUES (?)", \
                ('myimage.png'))
    cur.execute("INSERT INTO tbl_persons(col_fname) VALUES (?)", \
                ('mymovie.mpg'))
    cur.execute("INSERT INTO tbl_persons(col_fname) VALUES (?)", \
                ('world.txt'))
    cur.execute("INSERT INTO tbl_persons(col_fname) VALUES (?)", \
                ('data.pdf'))
    cur.execute("INSERT INTO tbl_persons(col_fname) VALUES (?)", \
                ('myphoto.jpg'))
    conn.commit()
conn.close()

fileList = ('information.docx', 'hello.txt', 'myimage.png', 'mymovie.mpg', 'world.txt', 'data.pdf', 'myphoto.jpg')

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname FROM tbl_files WHERE col_fname = '.[txt]'")
    varFile = cur.fetchall()
    print(varFile)

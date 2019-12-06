# import mysql.connector
#
# db = mysql.connector.connect(
#     host="localhost",
#     user="admin",
#     password=""
# )
#
# if db.is_connected():
#     print("Bershasil terhubung ke database")
#
#
# def Create():
#     a = input("Nama Resep : ")
#     bhn = ""
#     bahan=[]
#     while bhn != "selesai":
#         bhn = input("Bahan - bahan dipisahkan dengan koma (,) : ")
#         if bhn != "":
#             bahan.append(bhn)
#         print(bahan)
#     else:
#         bahan.remove("selesai")
#         for i in range(len(bahan)):
#             bahan.append("%d. %s" % (i+1,bahan[i]))
#         l = len(bahan)/2
#         print(l)
#         del bahan[0:int(l)]
#         b = ("\n".join(bahan))
#     sql = "insert into resep values(?,?)"
#     if c.execute(sql,[a,b]):
#         print("Data ditambah")
#     else:
#         print("gagal")
#     db.commit()
# import os
# b = u"Lonte enak dipake, lonte ah ah, lonte murah\n".title()
# print(b.capitalize(),b.upper(),b.lower(),b.casefold(),b.swapcase(),b)
# # print(chr(27) + "[2J")
# os.system('CLs')
#
# print(b)
 # self.c
        # picks = ['asdasd','asdasd','asdad']
        # for pick in picks:
        #     var = IntVar()
        #     Checkbutton(self.lolf,text=pick,variable=var)
        #     # self.widget(self.chc)
        #     picks.append(var)

        self.lis = []
        ] = IntVar()
        for r in range(10,12):
            for c in range(0,3):
                i = 2*(r-10)+c+(r-10)
                Checkbutton(self.lolf, text=self.penyakit[i], variable=self.o,font=('',15)).grid(sticky=W,row=r,column=c)


        # lng = coba(root, ['Python', 'Ruby', 'Perl', 'C++'])


import sqlite3

with sqlite3.connect('login.db') as db:
    c = db.cursor()
# c.execute('Drop table resep')
c.execute('''CREATE TABLE IF NOT EXISTS login (
    Username VARCHAR NOT NULL,
    Password VARCHAR NOT NULL
      )''')
db.commit() # supaya bisa diubah datanya

def Insert(a,b):
    c.execute("INSERT INTO login VALUES (?,?)",(a,b))
    db.commit()
    Index()

def Index():
    sql = "SELECT * FROM login"
    c.execute(sql)
    result = c.fetchall()
    for data in result:
        print(data)
def laundry():
    print("ini masuk ke menu laundry")
def Login():
    a = input('user: ')
    b = input('pass: ')
    c.execute("SELECT * FROM login WHERE Username = ? AND Password = ?",(a,b))
    result = c.fetchall()
    if result:
        laundry()
        for data in result:
             print("SELAMAT DATANG ",data[0])
    else:
        print("Username not found")

menu=""
print("selamat datang di welcome")
# Insert(a,b)
pil = input('pil')
if pil == '1':
    Login()
else:
    print('asdasd')
db.close()

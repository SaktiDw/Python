# import mysql.connector
import os
import sqlite3



conn = sqlite3.connect("resep.db")
cursor = conn.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS profile(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")
cursor.execute('''CREATE TABLE IF NOT EXISTS resep (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    namaResep VARCHAR NOT NULL,
    bahan VARCHAR NOT NULL
      )''')
conn.commit()
# conn.close()

#
# db = mysql.connector.connect(
#   host="localhost",
#   user="admin",
#   passwd="admin",
#   database="toko_mainan"
# )


def insert_data():
  namaResep = input("Masukan nama: ")
  bahan = input("Masukan alamat: ")
  # cursor = db.cursor()
  cursor.execute("INSERT INTO resep (namaResep, bahan) VALUES (?, ?)",(namaResep, bahan))
  # db.commit()
  print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data():
  # cursor = db.cursor()
  sql = "SELECT * FROM resep"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  # if cursor.rowcount < 0:
  #   print("Tidak ada data")
  # else:
  for data in results:
    print("Nama Resep")
    print(data[1])


def update_data(db):
  show_data()
  customer_id = input("pilih id customer> ")
  name = input("Nama baru: ")
  address = input("Alamat baru: ")

  sql = "UPDATE customers SET name=%s, address=%s WHERE customer_id=%s"
  val = (name, address, customer_id)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))


# def delete_data(db):
#   cursor = db.cursor()
#   show_data(db)
#   customer_id = input("pilih id customer> ")
#   sql = "DELETE FROM customers WHERE customer_id=%s"
#   val = (customer_id,)
#   cursor.execute(sql, val)
#   db.commit()
#   print("{} data berhasil dihapus".format(cursor.rowcount))
#
#
# def search_data(db):
#   cursor = db.cursor()
#   keyword = input("Kata kunci: ")
#   sql = "SELECT * FROM customers WHERE name LIKE %s OR address LIKE %s"
#   val = ("%{}%".format(keyword), "%{}%".format(keyword))
#   cursor.execute(sql, val)
#   results = cursor.fetchall()
#
#   if cursor.rowcount < 0:
#     print("Tidak ada data")
#   else:
#     for data in results:
#       print(data)
#

def show_menu():
  print("=== APLIKASI DATABASE PYTHON ===")
  print("1. Insert Data")
  print("2. Tampilkan Data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("5. Cari Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  # os.system("clear")

  if menu == "1":
    insert_data()
  elif menu == "2":
    show_data()
  # elif menu == "3":
  #   update_data()
  # elif menu == "4":
  #   delete_data()
  # elif menu == "5":
  #   search_data()
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu()

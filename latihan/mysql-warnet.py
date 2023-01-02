#manajement warnet dengan python dan mysql CRUD
# table = "tb_barang"
# data = "username primary key , nama pelanggan, no hp , billing "

# import library
import mysql.connector

# koneksi database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="")

# membuat cursor
cursor = db.cursor()

# membuat database
cursor.execute("CREATE DATABASE IF NOT EXISTS db_warnet")
cursor.execute("USE db_warnet")

# membuat tabel
cursor.execute("CREATE TABLE IF NOT EXISTS tb_pelanggan (username VARCHAR(255) PRIMARY KEY, nama_pelanggan VARCHAR(255), no_hp VARCHAR(255), billing VARCHAR(255))")

# fungsi untuk menampilkan menu
def menu():
    print("""
    1. Tambah Pelanggan
    2. Lihat Pelanggan
    3. Ubah Pelanggan
    4. Hapus Pelanggan
    5. Keluar
    """)
    pilih = input("Pilih Menu> ")
    if pilih == "1":
        tambah()
    elif pilih == "2":
        lihat()
    elif pilih == "3":
        ubah()
    elif pilih == "4":
        hapus()
    elif pilih == "5":
        exit()
    else:
        print("Menu Tidak Ada")
        back()

# fungsi untuk kembali ke menu
def back():
    back = input("Kembali ke menu (y/t)? ")
    if back == "y":
        menu()
    elif back == "t":
        exit()
    else:
        print("Pilih y/t")
        back()

# fungsi untuk tambah pelanggan
def tambah():
    username = input("Username: ")
    nama_pelanggan = input("Nama Pelanggan: ")
    no_hp = input("No HP: ")
    billing = input("Billing: ")
    cursor.execute("INSERT INTO tb_pelanggan VALUES (%s, %s, %s, %s)", (username, nama_pelanggan, no_hp, billing))
    db.commit()
    print("Data Berhasil Ditambahkan")
    back()

# fungsi untuk lihat pelanggan
def lihat():
    cursor.execute("SELECT * FROM tb_pelanggan")
    hasil = cursor.fetchall()
    if cursor.rowcount < 0:
        print("Tidak Ada Data")
    else:
        for data in hasil:
            print(data)
    back()

# fungsi untuk ubah pelanggan
def ubah():
    username = input("Username: ")
    nama_pelanggan = input("Nama Pelanggan: ")
    no_hp = input("No HP: ")
    billing = input("Billing: ")
    cursor.execute("UPDATE tb_pelanggan SET nama_pelanggan=%s, no_hp=%s, billing=%s WHERE username=%s", (nama_pelanggan, no_hp, billing, username))
    db.commit()
    print("{} data diubah".format(cursor.rowcount))
    back()

# fungsi untuk hapus pelanggan
def hapus():
    username = input("Username: ")
    cursor.execute("DELETE FROM tb_pelanggan WHERE username=%s", (username) )
    db.commit()
    print("{} data dihapus".format(cursor.rowcount))
    back()

if __name__ == "__main__":
    menu()
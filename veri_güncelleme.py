import sqlite3
con=sqlite3.connect("şirket.db")
cursor=con.cursor()
def veri_guncelle():
    cursor.execute("update elemanlar set isim='Selman' where ID=5")
    con.commit()
    print("Kayıt güncellendi",con.total_changes)
veri_guncelle()
con.close()
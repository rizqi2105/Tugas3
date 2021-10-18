
def MetodeGarisLurus():
    print ("Metode Garis Lurus")
    Hargaperolehan = int(input("Masukan harga perolehan: Rp "))
    Residu = int(input("Masukan nilai residu: Rp "))
    UmurEkonomis = int(input("Masukan umur ekonomis: "))
    print("Depresiasi = " + str((Hargaperolehan - Residu)/ UmurEkonomis))


def MetodeJamJasa():
    print ("Metode Jam jasa")
    Hargaperolehanjam = int(input("Masukan harga perolehan jam : Rp "))
    Residujam = int(input("Masukan nilai residu: Rp "))
    Taksiranhasilproduksi = int(input("Taksiran Hasil produksi (unit):"))
    print("Depresiasi = " + str((Hargaperolehanjam - Residujam)/ Taksiranhasilproduksi)
    )

print("=====Menu Metode Menghitung Depresiasi=====")
print("1. Metode Garis Lurus")
print("2. Metode Jam Jasa")

menu = int(input("masukan metode: "))
if menu == 1:
    MetodeGarisLurus()
elif menu == 2:
    MetodeJamJasa()







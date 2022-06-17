import mysql.connector
from connection import ConnectionClass

con = ConnectionClass()

while True:

    print("---------Hoşgeldiniz----------\n")
    print("---------Kütüphane Sistemi----------\n")
    print("0 - Kutuphaneci Ekle")
    print("1 - Kütüphaneci Girisi \n")
    print("2 - Cikis \n")

    islem = int(input("islem sec : "))

    if islem == 2:
        print("----Güle Güle :)----")
        break

    elif islem == 0:

        print("*****Kütüphaneci*****Ekle*******\n")

        adi = input("Adı : ")
        soyadi = input("Soyadı : ")
        telefoni = input("Telefon : ")


        con.insertLibaryian(adi,soyadi,telefoni)

        print("****İslem****Basarili****")

        continue

    elif islem == 1:

        ad = input("Ad : ")
        soyad = input("Soyad : ")

        kontrol, kutuphaneci_id = con.loginLibaryian(ad, soyad)

        if kontrol:

            while True:

                print("0 - Çık\n")
                print("1 - Kitap Ekle \n")
                print("2 - Kitap Güncelle \n")

                print("3 - Kitap Sil \n")
                print("4 - Kitap Basim Yilina Göre Listele\n")
                print("5 - Kitap Türe Göre Listele\n")
                print("6 - Kitap Ada Göre Listele\n")
                print("7 - Kitap Yazarına Göre Filtele\n")
                print("8 - Odunc Ekle\n")
                print("9 - Odunc Sil\n")
                print("10 - OduncGuncelle\n")
                print("11 - Kitap Listele\n")
                print("12 - Odunc Listele\n")

                islem = int(input("islem sec : "))

                if islem == 1:

                    print("*****Kitap*****Ekle*******\n")

                    kitap_adi = input("Kitap Adı : ")
                    yazar = input("Yazar Adı : ")
                    tur = input("Tür Adı : ")
                    basim_yili = int(input("Basim Yili : "))
                    dil = input("Dil : ")
                    sayfa_sayisi = input("Sayfa Sayisi : ")

                    con.insertBook(kitap_adi,yazar,tur,basim_yili,dil,sayfa_sayisi,kutuphaneci_id)

                    print("****İslem****Basarili****")

                    continue

                elif islem == 2:

                    print("*****Kitap*****Guncelle*******\n")

                    guncellencek_kitap_ismi = input("Guncellencek Kitap Ismi : ")
                    get_kitap_id = con.getBook(guncellencek_kitap_ismi)

                    if get_kitap_id is None:
                        print("Böyle bir kitap bulunmamakta")

                    kitap_adi = input("Kitap Adı : ")
                    yazar = input("Yazar Adı : ")
                    tur = input("Tur Adı : ")
                    basim_yili = int(input("Basim Yili : "))
                    dil = input("Dil  : ")
                    sayfa_sayisi = input("Sayfa Sayisi : ")

                    con.updateBook(get_kitap_id,kitap_adi, yazar, tur, basim_yili, dil, sayfa_sayisi,)

                    print("****İslem****Basarili****")

                    continue

                elif islem == 3:

                    print("******Kitap*****Sil*****")

                    silinecek_kitap_adi = input("Silinecek Kitap Adi : ")

                    silinecek_id = con.getBook(silinecek_kitap_adi)

                    if silinecek_id is None:
                        print("Böyle bir kitap bulunmamakta")

                    if silinecek_id == -1:


                        print("Kitap Bulunamadi")
                        continue
                    else:

                        con.deleteBook(silinecek_kitap_adi, silinecek_id)

                        print("******islem******basarili*******")
                        continue

                elif islem == 4:

                    rs = con.basimYiliFilter()

                    for x in rs:

                        print("************"+"\n")
                        print(str(x[1]) + " ---- " + str(x[4])+"\n")
                        print("*************"+"\n")


                    continue

                elif islem == 5:

                    tur = input("Tur : ")

                    rs = con.turFilter(tur)

                    if rs is None:
                        print("Tur bulunamadı")
                        continue

                    for x in rs:

                        print("************"+"\n")
                        print(str(x[1]) + " ---- " + str(x[3])+"\n")
                        print("*************"+"\n")


                    continue

                elif islem == 6:

                    rs = con.kitapAdiFilter()

                    for x in rs:

                        print("************"+"\n")
                        print(str(x[1]) + " ---- " + str(x[2])+"\n")
                        print("*************"+"\n")


                    continue

                elif islem == 7:
                    yazar = input("Yazar : ")

                    rs = con.yazarfilter(yazar)

                    if rs is None:
                        print("Yazar Bulunamadı")
                        continue

                    for x in rs:

                        print("************"+"\n")
                        print(str(x[1]) + " ---- " + str(x[2])+"\n")
                        print("*************"+"\n")


                    continue


                elif islem == 8:

                    print("*****Odunc*****Ekle*******\n")

                    odunc_kitap_ismi = input("Odunc Verilecek Kitap Ismi : ")
                    get_kitap_id = con.getBook(odunc_kitap_ismi)

                    odunc_ad = input("Odunc Kisi Adı : ")
                    odunc_soyad = input("Odunc Kisi Soyadı  : ")
                    telefon_no = input("Telefon No : ")


                    con.insertBorrower(odunc_ad,odunc_soyad,telefon_no,kutuphaneci_id,get_kitap_id)

                    print("****İslem****Basarili****")

                    continue

                elif islem == 9:
                    print("******Odunc*****Sil*****")

                    silinecek_odunc_telefon_no = input("Silinecek Odunc Telefon No : ")

                    silinecek_id = con.getOduncId(silinecek_odunc_telefon_no)

                    if silinecek_id is None:



                        print("Kitap Bulunamadi")
                        continue
                    else:
                        con.deleteBorrower(silinecek_id)

                        print("******islem******basarili*******")
                        continue

                elif islem == 10:
                    print("*****Odunc*****Guncelle*******\n")

                    odunc_telefon = input("Odunc Telefon : ")
                    odunc_id = con.getOduncId(odunc_telefon)

                    if odunc_id is None:
                        print("Böyle bir ödünc alan yok")
                        continue

                    odunc_ad_ = input("Odunc Kisi Adı : ")
                    odunc_soyad_ = input("Odunc Kisi Soyadı  : ")
                    telefon_no_ = input("Telefon No : ")

                    con.insertBorrower(odunc_ad_, odunc_soyad_, telefon_no_, odunc_id)

                    print("****İslem****Basarili****")

                    continue

                elif islem == 11:

                    print("**************Kitap Listesi*************")
                    rs =  con.kitapListele()

                    for x in rs:

                        print("------------------")
                        print(x[1] + "\n")

                    continue

                elif islem == 12:

                    print("**************Kitap Listesi*************")
                    rs = con.borrowerListele()

                    for x in rs:
                        print("------------------")
                        print(str(x[1]) + " ------ " + str(x[5]) +"\n")

                    continue

                elif islem == 0:

                    break



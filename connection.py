import mysql.connector

class ConnectionClass:

    def __init__(self):

        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "deneme"
        )

    def insertLibaryian(self,adi,soyadi,telefon_no):

        mycursor = self.mydb.cursor()

        sql = "Insert Into Kutuphaneci (KutuphaneciAdi, KutuphaneciSoyadi, KutuphaneciTelefonNo) values (%s, %s, %s)"

        mycursor.execute(sql, (adi, soyadi, telefon_no))

        self.mydb.commit()


    def insertBorrower(self,ad,soyad,telefon_no,kutuphaneci_id,kitap_id):

        mycursor = self.mydb.cursor()

        sql = "Insert Into OduncAlan (OduncAlanAd, OduncAlanSoyad, OduncAlanTelefonNo, KutuphaneciId, KitapId) values (%s, %s, %s, %s, %s)"

        mycursor.execute(sql, (ad, soyad, telefon_no, kutuphaneci_id, kitap_id))

        self.mydb.commit()


    def insertBook(self,kitap_adi,yazar_adi,tur,basim_yili,dil,sayfa_sayisi,kutuphaneci_id):

        mycursor = self.mydb.cursor()

        libaryian = self.getLibariyan(kutuphaneci_id)

        sql = "INSERT INTO Kitap (KitapAdi, YazarAdi, Tur, BasimYili, Dil, SayfaSayisi, KutuphaneciId) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        mycursor.execute(sql, (kitap_adi, yazar_adi, tur, basim_yili, dil, sayfa_sayisi,libaryian))

        self.mydb.commit()


    def deleteBook(self,kitap_adi,kitap_id):

        mycursor = self.mydb.cursor()

        sql = "Delete From Kitap Where KitapAdi = %s"

        mycursor.execute(sql, (kitap_adi, ))

        self.mydb.commit()


    def deleteLibarian(self,id):

        mycursor = self.mydb.cursor()

        sql = "Delete From Kutuphaneci Where KutuphaneciId = %s"

        mycursor.execute(sql, (id, ))

        self.mydb.commit()


    def deleteBorrower(self,odunc_id):

        mycursor = self.mydb.cursor()

        sql = "Delete From OduncAlan Where OduncAlanId = %s"

        mycursor.execute(sql, (odunc_id,))

        self.mydb.commit()


    def updateBook(self,kitap_id,kitap_adi,yazar,tur,basim_yili,dil,sayfasayisi):

        mycursor = self.mydb.cursor()

        sql = "Update Kitap Set KitapAdi = %s, YazarAdi = %s, Tur = %s, BasimYili = %s, Dil = %s, SayfaSayisi = %s Where KitapId = %s"

        mycursor.execute(sql, (kitap_adi, yazar, tur, basim_yili, dil, sayfasayisi, kitap_id))

        self.mydb.commit()


    def updateLibaryian(self,ad,soyad,telefon,id):

        mycursor = self.mydb.cursor()

        sql = "Update Kutuphaneci Set KutuphaneciAdi = %s, KutuphaneciSoyadi = %s, KutuphaneciTelefonNo = %s Where KutuphaneciId = %s"

        mycursor.execute(sql, (ad, soyad, telefon, id))

        self.mydb.commit()


    def updateBorrower(self,ad,soyad,telefon,kitap_id,odunc_alan_id):

        mycursor = self.mydb.cursor()

        sql = "Update OduncAlan Set OduncAlanAd = %s, OduncAlanSoyad = %s, OduncAlanSoyad = %s, OduncAlanTelefonNo = %s, KitapId = %s Where OduncAlanId = %s"

        mycursor.execute(sql, (ad,soyad,telefon,kitap_id,odunc_alan_id))

        self.mydb.commit()



    def getLibariyan(self,kutuphaneci_id):

        mycursor = self.mydb.cursor()

        libarySql = "SELECT * FROM Kutuphaneci WHERE KutuphaneciId = %s"

        mycursor.execute(libarySql, (kutuphaneci_id,))

        result = mycursor.fetchall()

        return result[0][0]


    def getBook(self,kitap_adi):

        mycursor = self.mydb.cursor()

        bookSql = "Select * From Kitap Where KitapAdi = %s"

        mycursor.execute(bookSql, (kitap_adi,))

        result = mycursor.fetchall()

        print(result[0][0])

        return result[0][0]


    def getAllBook(self):

        mycursor = self.mydb.cursor()

        sql = "Select * From Kitap"

        mycursor.execute(sql)

        rs = mycursor.fetchall()

        return rs


    # Basım Yılı , Tur , Yazar , Kitap Adı

    def basimYiliFilter(self):

        mycursor = self.mydb.cursor()

        sql = "Select * From Kitap Order By BasimYili "

        mycursor.execute(sql)

        rs = mycursor.fetchall()

        return rs




    def turFilter(self, tur):

        mycursor = self.mydb.cursor()

        sql = "Select * From Kitap Where Tur = %s"

        mycursor.execute(sql, (tur, ))

        rs = mycursor.fetchall()

        return rs




    def yazarfilter(self,yazar):

        mycursor = self.mydb.cursor()

        sql = "Select * From Kitap Where YazarAdi = %s"

        mycursor.execute(sql, (yazar,))

        rs = mycursor.fetchall()

        return rs


    def kitapAdiFilter(self):

        mycursor = self.mydb.cursor()

        sql = "Select * From Kitap Order By KitapAdi"

        mycursor.execute(sql)

        rs = mycursor.fetchall()

        return rs


    def loginLibaryian(self,ad,soyad):

        mycursor = self.mydb.cursor()

        sql = "Select * From Kutuphaneci Where KutuphaneciAdi = %s AND KutuphaneciSoyadi = %s"

        mycursor.execute(sql, (ad, soyad))

        rs = mycursor.fetchall()

        if rs is None:
            return False
        else:
            return True, rs[0][0]


    def getOduncId(self,odunc_telefon_no):

        mycursor = self.mydb.cursor()

        sql = "Select * From OduncAlan Where OduncAlanTelefonNo = %s"

        mycursor.execute(sql,(odunc_telefon_no,))

        rs = mycursor.fetchall()

        print(rs)

        return rs[0][0]



    def kitapListele(self):

        mycursor = self.mydb.cursor()

        sql = "Select * From Kitap"

        mycursor.execute(sql)

        rs = mycursor.fetchall()

        return rs


    def borrowerListele(self):

        mycursor = self.mydb.cursor()

        sql = "Select * From OduncAlan"

        mycursor.execute(sql)

        rs = mycursor.fetchall()

        return rs
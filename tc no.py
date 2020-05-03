import random
import os

class TcNo:
    liste = []
    dogrulanan = []
    @classmethod
    def uret(cls,miktar):
        for i in range(miktar):
            cls.liste.append(random.randint(10000000000,99999999999))
    @classmethod
    def kontrol(cls):
        toplam = 0
        for no in cls.liste:
            no = str(no)
            if ((((int(no[0]) + int(no[2]) + int(no[4]) +int(no[6]) + int(no[8])) * 7) - (int(no[1]) + int(no[3]) + int(no[5]) + int(no[7]))) % 10) == int(no[9]): # for ile çift tek sayılar eklenebilir
                for x in range(len(no) - 1):
                    toplam += int(no[x])
                if toplam % 10 == int(no[10]):
                    cls.dogrulanan.append(no)
                    toplam = 0
                else:
                    toplam = 0
            else:
                pass
    @classmethod
    def dosyala(cls):
        if len(cls.dogrulanan) == 0:
            print("Lütfen Tc No Üretiniz!")
        else:
            f = open("tc.txt","w")
            for i in cls.dogrulanan:
                f.writelines(i)
                f.writelines("\n")
            print(os.getcwd()+r"\tc.txt","Konumuna Dosyalandı!")
            f.close()

            # Kullanım Şekli Aşağıdaki Gibidir
miktar = int(input("Kaç adet üretmek istiyorsunuz:"))
TcNo.uret(miktar)
TcNo.kontrol()
TcNo.dosyala()

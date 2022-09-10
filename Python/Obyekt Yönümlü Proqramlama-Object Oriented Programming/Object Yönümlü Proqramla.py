
siyahi1= [1,2,3,4,5]


type(siyahi1)



siyahi1.append(6)

siyahi1



luget= dict()

type(luget)


def toplama(a,b):
    return a+b


type(toplama)




class renault_megane():
    
    model = "Renault Megane"
    reng= "Gümüşü"
    at_gucu= 110
    silindir_sayi= 4
    suretler_qutusu= "Mexanika"


# obyektin_adı= class_ad(parametr(optional))


masin1= renault_megane()

masin2= renault_megane()

masin1.suretler_qutusu

masin2.suretler_qutusu


siyahi1= [1,2,3]

siyahi2=["Bir","İki","Üç"]

dir(renault_megane)


# __init__  


class masin (): 
    
    def __init__(self,model="No İnformation",reng="No İnformation",at_gucu="No İnformation",silindir_sayi="No İnformation",il="No İnformation"):
        print("İnit funksiyası çağrıldı")
        
        self.model= model
        self.reng = reng 
        self.at_gucu= at_gucu
        self.silindir_sayi = silindir_sayi
        self.il= il 
    
    
class proqramist():
    
    def __init__(self,ad,soyad,no,maas,diller):
        
        self.ad=ad
        self.soyad=soyad
        self.no=no
        self.maas=maas
        self.diller=diller 
        
    def informasiya_goster(self):
        print("""
              Proqramist informasiyaları
              
              Ad:{}
              Soyad:{}
              No:{}
              Maas:{}
              Diller:{}
              """.format(self.ad,self.soyad,self.no,self.maas,self.diller))
    
    def dil_elave_et(self,yeni_dil):
        
        print("Dil elave olundu")
        
        self.diller.append(yeni_dil)
    
    def maas_yukselt(self,zam_miqdari):
        
        print("Maaş yükseltildi")
        
        self.maas+=zam_miqdari
    
        
proqramist1= proqramist("Davud","Suleymanov","17014908",5000,["Python","C","Java"])  

proqramist2= proqramist("Kamran","Asadov","18014908",15000,["Assembly","C","Java"])


proqramist1.dil_elave_et("C#")

proqramist1.informasiya_goster()

proqramist1.maas_yukselt(5000)


dir(proqramist1)



# İnheritance - miras,qalıq


#overriding- iptal eleme

class isciler():
    
    def __init__(self,ad,soyad,no,maas):
        
        self.ad=ad
        self.soyad=soyad
        self.no=no
        self.maas=maas
        
        
    def informasiya_goster(self):
        print("""
              İşci informasiyaları
              
              Ad:{}
              Soyad:{}
              No:{}
              Maas:{}
              """.format(self.ad,self.soyad,self.no,self.maas,))
              

isci1=isciler("Davud", "Suleymanov", 170140908, 5000)





class direktorlar(isciler):
    
    def __init__(self,ad,soyad,no,maas,insan_sayi):
        
        super.__init__(ad,soyad,no,maas)
        
        
        self.insan_sayi= insan_sayi
        
    
    
    def informasiya_goster(self):
        print("""
              Direktor informasiyaları
              
              Ad:{}
              Soyad:{}
              No:{}
              Maas:{}
              """.format(self.ad,self.soyad,self.no,self.maas,))
    
    def maas_artir(self,zam_miqdari):
        
        print("Maaş artırıldı")
        
        self.maas += zam_miqdari
        
  
direktor1=direktorlar("Asif","Mirzayev", 18014908, 10000)





















































def kare(a):
    alan = a ** 2
    print(f"Karenin alanı {round(alan, 2)}")
def dikdortgen(a,b):
    alan=(a*b)/2
    print(f"dikdötgenin alanı {round(alan,2)}")

def daire(r):
    alan=3.14*(r**2)
    print(f"darirenin alanı {round(alan,2)}")
def ucgen(a,h):
    alan=(a*h)/2
    print(f"üçgenin alanı {round(alan,2)}")
def paralelkenar(b,h):
    alan=b*h
    print(f"paralelkenarın alanı {round(alan,2)}")




while True:
    
    print('''
    1-Square-Kare
    2-Rectangle-Dikdörtgen
    3-Circle-Daire
    4-Triangle-Üçgen
    5-Parallelogram-Paralelkenar
    .
    .
    .
    99-Exit-cikis
    ''')
    try:
        
        secim = int(input("Hangi geometrik cismin alanını hesaplamak isterseniz?"))
    except ValueError as hata:
        print("tam sayı giriniz",hata)
    
    if secim==1:
        try:
            kenar = float(input("Karenin bir kenar uzunluğunu giriniz."))
            kare(kenar)
        except Exception as hata:
            print("bir hata oluştu tekrar deneyin",hata)
    elif secim==2:
        try:
            uzunKenar=float(input("uzun kenar uzunluğunu giriniz"))
            kisaKenar=float(input("kısa kenar uzunluğunu giriniz"))
            dikdortgen(uzunKenar,kisaKenar)
        except Exception as hata:
            print("bir hata oluştu tekrar deneyin",hata)
    elif secim==3:
        r=float(input("yarıçapı giriniz"))
        daire(r)  
    elif secim==4:
        a=float(input("üçgenin taban kenar uunluğunu giriniz"))
        h=float(input("üçgenin yüksekliğini giriniz"))
        ucgen(a,h)
    elif secim==5:
        b=float(input("paralel kenanarın bir kenar uzunlugunu giriniz"))
        h=float(input("yüksekliğini giriniz"))
        paralelkenar(b,h)
    elif secim==99:
        print("Programdan çıkılıyor. Bye bye")
        break
   
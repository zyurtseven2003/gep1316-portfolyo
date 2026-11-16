from datetime import datetime

# Kullanicinin adini ogreniyoruz
ad = input("Adiniz nedir? ")

# Kullanicinin dogum yilini ogreniyoruz
dogum_yili = int(input("Dogum yiliniz nedir? "))

# Guncel yili aliyoruz
bu_yil = datetime.now().year

# Dogum yilini kontrol ediyoruz
if dogum_yili > bu_yil:
    print("Hata: Dogum yili gelecekte olamaz!")
else:
    # Kullanicinin yasini hesapliyoruz
    yas = bu_yil - dogum_yili

    # Kisisel karsilama mesaji
    print(f"Merhaba {ad}! {yas} yasindasiniz.")
    print("Python programima hos geldiniz!")

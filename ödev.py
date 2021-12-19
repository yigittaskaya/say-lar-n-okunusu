#iki basamaklı sayıların okunuşu
def yazi(a):
    birler=["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
    onlar=["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
    bir=a%10
    on=a//10
    print(onlar[on],birler[bir])

sayi=int(input("iki basamaklı bir sayı giriniz:"))
yazi(sayi)
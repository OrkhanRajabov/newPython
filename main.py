
print("hello world")
print("""Plase enter your name and surname(ex: John Smith): 
if you want to end input type '0 0' """)
adlar=[]

while True:
    ad,soyad=map(str,input().split())
    if ad=='0' and soyad=='0':
        break 
    else:
        adlar.append(ad+' '+soyad)
adlar.sort()
aa=1
for i in adlar:
    print(str(aa)+'. '+i)
    aa+=1





"""cars=["Mercedes", "BMW","Audi", "Porsche"]

#print(cars)

#print(cars[0][5])

cars.append("hyundai")
print(cars) """

""""ededler=[23,56,890,12,45,123,67,23,34,12]

def eded():
    a=ededler.count(23)
    print(a)



def ededleri_topla():
    cem=0
    for i in ededler:
        cem=cem+i
        print("butun ededlerin", cem )
ededleri_topla()

def sayi():
    print(len(ededler))
sayi()"""

"""maaslar=[600,450,1200,800,2000,1400,700,300]


cem=0
for maas in maaslar:
    cem+=maas
print(cem)"""


"""def reqem_cemi():
    a=456
    cem=0
    for reqem in str(a):
        cem+=int(reqem)
    print(cem)

    reqem_cemi()
    
    
a=4456
cem=0
for reqem in str(a):
    cem=cem+int(reqem)
print(cem)  """

def ededinReqemSayiniTap():
    a="4456"
    print(len(a))
    
ededinReqemSayiniTap()

def ededinreqemcemi():
    a="4456"
    cem=0
    for x in a:
        cem=cem+int(x)
    print(cem)
    
ededinreqemcemi()

def ededinReqemleriniCapEt():
    a="76799"
    for x in a:
        print(x)
ededinReqemleriniCapEt()

def tekralananEdedleriTap():
    ededler=[23,56,890,12,45,123,67,23,34,12]
    a=ededler.count(23)
    b= ededler.count(12)
    print(a,b)
    print
    
tekralananEdedleriTap() 

# sort reverse edecem reqemleri #
ededler=[23,56,890,12,45,123,67,23,34,12]
a=ededler.reverse()
print(a)




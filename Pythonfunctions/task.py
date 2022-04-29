# def showFilteredNumbers(a,b):
    # a və b-nin ədəd olduğunu dəqiqləşdirin.a və ya b ədəd deyilsə "Düzgün dəyər daxil edilməyib" return edilsin
    # a b-dən kiçikdirsə ekrana "Daxil edilən dəyərlər tələblərə uyğun deyil" çap edin
    # a b-dən böyükdürsə a və b ədədləri arasında 5-ə bölünən amma 7-yə bölünməyən ədədləri ekrana çap edin


a=input("a ededini daxil edin:")
b=input("b ededini daxil edin:")
   
def Numbers():
    try:
        int(a) and int(b)
        return True
    except:
        return ("duzgun deyer daxil edilmeyib")
          
Numbers()

def numbers1():
    if Numbers()==True:
        if a<b:
            print("daxil edilen deyerler teleblere uygun deyil")
        else:
            none
            
(numbers1())

    
        
    

    
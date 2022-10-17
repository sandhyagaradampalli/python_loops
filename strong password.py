password=input("enter the password")
if len(password)>=6 and len(password)<10:
    if password=="A" or password=="B" or password=="C" or password=="D":
        if password=="a" or password=="b" or password=="c" or password=="d":
            if password in("!","@","#","$"):
                if password in("1","2","3","4"):
                   print("strong password")
                else:
                    print("you missed numbers")
            else:
                print("special characters are missed")        
        else:
            print("small letters are missed")                    
    else:
        print("capital letters are missed")
else:
    print("weak password")        
    
    
print("well come to bank")
print("insert your card")
print("enter your language")
language=intput("enter the language")
if language=="english":
    amount=20000
    pin=int(input("enter the number"))
    if pin==1234:
        print("transaction:1.withdraw,2.balance enquiry,3.deposit,4.pin change,5.exit")
        transaction=int(input("enter the transaction"))
        if transaction==1:
            withdraw=int(input("enter the withdraw:"))
            if withdraw<=amount:
                print("transaction successfull:","collected your cash")
                print("remaining balance","amont-withdraw")
            else:
                print("not withdraw")
        elif transaction==2:
            print("available balance is",amount)
            print("thank you")
    if transaction==3:
        pin_change=int(input("enter the pin:"))
        if pin_change!=1234:
            print("you new pin generation successfully completed")
        else:
            print("your new pin not completed")
if transaction==4:
    deposit=int(input("enter the amount"))
    if depisit>=1000:
        print("your deposit amount is successfullu completed,amount+deposit") 
    else:
        print("not deposit")      
elif trasaction==5:
    print("exit")
    
    
a=int(input("enter the number"))
if a==10:
    print("a is correct")
elif a==10:
    print("a is not")
if a==10:
    print("a onley")
else:
    print("not in")

print("welcome to hdfc")   
print("please insert your card")
language=input("enter the language:")
current_balance=25000
if language=="english" or "hindi" or "kannada" or "telugu":
    print("please insert your card")
    password=int(input("enter the pin"))
    pin=1234
    if pin==password:
        menu=input("select the option:")
        if menu=="current":
            if current_balance>0:
                print(current_balance)
            else:
                print("zero balance")
        elif menu=="withdrawl":
            withdrawal_amount=int(input("enter the amount"))
            if withdrawal_amount<=current_balance: 
                print(current_balance-withdrawal_amount)
            else:
                print("insuffcient balance")
        elif menu=="deposit":
            deposit_amount=int(input("enter the deposit amount"))
            if deposit_amount>0:
                print(current_balance+deposit_amount)
            else:
                print(current_balance)
        else:
            print("please enter correct menu")
    else:
        print("please enter valid pin")
else:
    print("select another ")




time=input("enter the time")
if time>="6:15" and time<="6:59":
    print("excersize")
elif time>="7:00" and time<="7:59":
    print("fresh up")
elif time>="8:30" and time<="11:29":
    print("first coding")
elif time>="12:30" and time<="13:29":
    print("lunch and breack")
elif time>="14:00" and time<="16:59":
    print("second coding")
elif time>="17:00" and time<="17:59":
    print("snakc time")
elif time>="18:00" and time<="19:59":
    print("english class")
elif time>="20:00" and time<="20:59":
    print("dinner time")
elif time>="21:00" and time<="21:29":
    print("extra study ours")
else:
    print("no time")




# password=input("enter the password")
# length=len(password)
# if length>=6 and length<=9:
#     if 'A' in password or 'B' in password or 'C' in password or 'D' in password or 'E' in password or 'F' in password or 'I' in password or 'J' in password or 'K' in password or 'L' in password or 'M'in password or 'N' in password or 'O' in password or 'P' in password or 'Q' in password or'R'in password or 'S' in password or 'T' in password or 'U' in password or 'V' in password or 'W'in password or 'X' in password or 'Y' in password or 'Z' in password:
#         if 'a' in password or 'b' in password or 'c' in password or 'd' in password or 'e' in password or 'f' in password or 'i' in password or 'j' in password or 'k' in password or 'l' in password or 'm' in password or 'n' in password or 'o' in password or 'P' in password or 'q' in password or 'r'in password or 's' in password or 't' in password or 'u' in password or 'v' in password or 'w' in password or 'x' in password or 'y' in password or 'z' in password:
#             if "@" in password or '&' in password or "#" in password or "$"in password or "&" in password or "!"in password or "*" in password:
#                 if "1" in password or '2' in password or "3" in password or "4" in password:
#                     print("strong password")
#                 else:
#                     print("atleast one digit must contain in your password")
#             else:
#                 print("special charactor is missed")
#         else:
#             print("samll letters are missed")
#     else:
#         print("capital letter is missed")
# else:
#     print("password must contain more thna 6 characters")




beds=int(input("enter the beds:"))
floor=int(input("enter the floor:"))
students=input("enter the name")
if floor==1:
    if beds>=1 and beds<=20:
        if students>="a" and students<="z":
            print("101","103")
        else:
            printa("enter the correct name")
    else:
        print("enter the correct number")
elif floor==1:
    if beds==0:
        print("104","office room") 
    else:
        print("enter correct number")
elif floor==1:
    if beds==3:
        print("102","reena didi room")
    else:
        print("enter correct number")
elif floor==2:
    if beds>=1 and beds<=30:
        if students>="a" and students<="z":
            print("201","203","204")
        else:
            print("enter the correct anme")
    else:
        print("enter correct number")
elif floor==2:
    if beds==0:
        print("this is kitchen room")
    else:
        print("enter correct")
elif floor==3:
    if beds>=1 and beds<=40:
        if students>="a" and students<="z":
            print("301","302","303","304")
        else:
            print("enter the correct name")
    else:
        print("enter correct number")
elif floor==4:
    if beds>=1 and beds<=40:
        if students>="a" and students<="z":
            print("401","402","403","404")
        else:
            print("enter the correct name")
    else:
        print("enter the correct number")
else:
    print("enter the correct floor number")
    
    
    
    

name=input("enter the name: ")
if name=="TNP":
    print("lakshmi prasanna")
elif name=="DISCO":
    print("anjali")
elif name=="FM":
    print("dolly")
elif name=="FC":
    print("pavani")
else:
    print("no members") 




year=int(input("enter the year"))
month=int(input("enter the month"))
date=int(input("enter the date"))
if month in (1,3,5,7,8,10):
    if date>=1 and date<31:
        print(year,"-",month,"-",date+1)
    else:
        print(year,"-",month+1,"-",date-30)
elif month==12:
    if date>=1 and date<31:
        print(year,"-",month,"-",date+1)
    else:
        print(year+1,"-",month-11,"-",date-30)
elif month in(4,6,9,11):
    if date>=1 and date<30:
        print(year,"-",month,"-",date+1)
    else:
        print(year,"-",month+1,"-",date-29) 
elif month==2:
    if date<28:
        print(year,"-",month,"-",date+1)
    else:
        print(year,"-",month+1,"-",date-27)
else:
    print("enter the correct month")

    
    
        


a=input("enter the name")
b=input("enter the name")
if a=="FC":
    if b=="food coordinator":
        print("pavani")
    else:
        print("not mention name")
elif a=="HC":
    if b=="health coordinator":
        print("sandhya")
    else:
        print("she not hc")
elif a=="FM":
    if b=="ficility coordinator":
        print("dolly")
    else:
        print("she did't take fm")
else:
    print("non of these")
        


year=int(input("enter the year"))
month=int(input("enter the month"))
date=int(input("enter the date"))
if month==(4,6,9,11):
    if date<30:
        print(date+1,month,year)
    else:
        print("1",month+1,year)
elif month==(1,3,5,7,8,10):
    if date<31:
        print(date+1,month,year)
    else:
        ("1",month+1,year)
elif month==12:
    if date<31:
        print(date+1,month,year)
    else:
        print("1",month+1,year)
elif year%4==0:
    if month==2:
        if date<28:
            print(date+1,month,year)
        else:
            print("1",month+1,year)
    else:
        print("1",month,year+1)
elif year%4!=0:
    if month==2:
        if date<29:
            print("leap year",date+1,month,year)
        else:
            print("1",month+1,year)
    else:
        print("enter the correct number")
else:
    print("1","1",year+1)
        
        
age=int(input("enter the age"))   
dose=int(input("enter the dose")) 
if age>=18:
    if dose==1:
        print("first dose is completed")
    elif dose==2:
        print("second dose is completed")
    elif dose==3:
        print("third dose is completed")
    else:
        print("onley three doses is limit")
else:
    print("enter correct age")



age=int(input("enter the age"))
gender=input("enter the gender")
if age>=18 and age<=25:
    if gender=="female":
        print("banglure compus")
    else:
        print("goto another campus")
elif age>=18 and age<=25:
    if gender=="boys":
        print("dharma shal")
    else:
        print("goto another campus")
elif age>19 and age<=30:
    if gender=="female":
        print("pune campus")
    else:
        print("enter correct")
else:
    print("enter corrct age")


expected_date=int(input("enter the expected_date"))
expected_month=int(input("enter the expected_month"))
expected_year=int(input("enter the expected_year"))
return_date=int(input("enter the return_date"))
return_month=int(input("enter the return_month"))
return_year=int(input("enter the return_year"))
if return_date<expected_date and return_month==expected_month and return_year==expected_year:
    print("no fine")
if return_date>expected_date and return_month==expected_month and return_year==expected_year:
    print((return_date-expected_date)*15)
if return_date>expected_date and return_month>expected_month and return_year==expected_year:
    print((return_date-expected_date)*15+(return_month-expected_month)*500)
elif return_year-expected_year:
    print("fixed fine 10000")
else:
    print("enter correct date")





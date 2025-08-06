#salary bonus calculation
# salary=int(input("Enter the salary : "))
# bonus_amount=salary*0.10
# if(salary>50000):
#     print("bonus amount : ",bonus_amount)
#     print("the bonus with added salary is : ",(salary+bonus_amount))
# else:
#     print("Bonus is not applicable")

#pass/fail predicting with nested condition
# sub1=float(input("Enter the marks for subject1 : "))
# sub2=float(input("Enter the marks for subject2 : "))
# sub3=float(input("Enter the marks for subject3 : "))
# print(sub1)
# print(sub2)
# print(sub3)
# avg=sub1+sub2+sub3
# print("total average marks of 3 subjects : ",avg)
# if(sub1<35 or sub2<35 or sub3<35):
#     print("you are failed ")
# else:
#     if(avg>60):
#         print("you have passed with first class")
#     else:
#         print("you have passed with second class")

#checking vowels or consonants
# vowels="aeiouAEIOU"
# ab=str(input("Enter the alphabet : "))
# if ab in vowels:
#     print(ab,"is a vowel")
# else:
#     print("It is a consonant")

#Electricity Bill Calculator
# b=int(input("enter the unit used : "))
# print(b)
# amount=0
# if b<= 200:
#     amount=b*3
# elif b <= 400:
#     amount = 200 * 3 + (b - 200) * 5
# elif b <= 800:
#     amount= 200 * 3 + 200 * 5 + (b - 400) * 6.5
# elif b <= 1200:
#     amount= 200 * 3 + 200 * 5 + 400 * 6.5 + (b - 800) * 7
# else:
#     amount = 200 * 3 + 200 * 5 + 400 * 6.5 + 400 * 7 + (b - 1200) * 8
# print("Total electricity bill: ₹",amount)


# Login Validation
# userid=str(input("Enter the username : "))
# passs=int(input("Enter the password : "))
# useriddd="ABcdef"
# passw=123908
# if userid==useriddd and passs==passw:
#     print("You have logined.")
# else :
#     print("You have entered a incorrect username or password !")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#Smallest of Three Numbers (Nested)
# a=float(input("Enter the number 1 : "))
# b=float(input("Enter the number 2 : "))
# c=float(input("Enter the number 3 : "))
# if a>b:
#     if a>c:
#         print(a,"is the largest")
#     else:
#         print(c,"is the largest")
# else:
#     if b>c:
#         print(b,"is the largest")
#     else:
#         print(c,"is the largest")

#Discount Based on Amount
# a=float(input("Enter the amount : "))
# d_count=0
# if a<=1000:
#     d_count=0
# elif a<=5000:
#     d_count=5
# elif a<=10000:
#     d_count =10
# else:
#     d_count = 15
# dis_amount=(d_count/100)*a
# f_amount=a-dis_amount
# print("discount percentage applicable on amount : 455",d_count)
# print("discount on the amount : ",dis_amount)
# print("A after discount : ",f_amount)


# BMI Calculator
# a = int(input("Enter age : "))
# b = int(input("Enter weight in kg : "))
# c = float(input("Enter height in m : "))
# BMI=b/(c**2)
# if BMI<18.5:
#     print("YOU BELONG TO UNDERWEIGHT CATEGORY ")
# elif 18.5<=BMI<=24.9:
#     print("YOU BELONG TO NORMAL BMI CATEGORY ")
# elif 25<=BMI<=29.9:
#     print("YOU BELONG TO OVERWEIGHT CATEGORY ")
# elif 30<=BMI<=34.9:
#     print("YOU BELONG TO OBESE CLASS 1 ")
# elif 35<=BMI<=39.9:
#     print("YOU BELONG TO OBESE CLASS 2 ")    
# else:
#     print("YOU BELONG TO OBESE CLASS 3 ")

###################################################################################################################################################

#Character Type Checker
# a=input("enter the character : ")
# if a.isupper():
#     print(a," is an uppercase letter.")
# elif a.islower():
#     print(a," is a lowercase letter.")
# elif a.isdigit():
#     print(a," is a digit.")
# else:
#     print(a," is a special character.")

#Grade Evaluator
# a=float(input("Enter the marks : "))
# percent=0
# if a>=90:
#     print("THE GRADE IS A ")
# elif 80<a<=90:
#     print("THE GRADE IS B ")
# elif 70<a<=79:
#     print("THE GRADE IS C ")
# elif 60<a<=69:
#     print("THE GRADE IS D ")
# else:
#     print("THE GRADE IS F")

#Triangle Validator
# a =int(input("Enter the angle 1 : "))
# b =int(input("Enter the angle 2 : "))
# c =int(input("Enter the angle 3 : "))
# if a+b+c==180:
#     print("It is a triangle")
# else:
#     print("It is not a triangle")

#odd or even number of digits
# a=int(input("Enter the number :"))
# if a/2==0:
#     print(a,"is an even number")
# else:
#     print(a,"is an odd number")


# Check whether input is a palindrome number
# ab=input("Enter the number :")
# print("checking whether the number is palindrome...........")
# reverse_nm=ab[::-1]
# if ab == reverse_nm:
#     print(reverse_nm,"is a palindrome number.")
# else:
#     print(reverse_nm,"is not a palindrome number")

#Determine Age Group
# a=int(input("Enter the age in years : "))
# if a<13:
#     print("Entered age belongs to a child ")
# elif 13<=a<20:
#     print("Entered age belongs to a teen ")
# elif 20<=a<60:
#     print("Entered age belongs to a adult")
# else:
#     print("Entered age belongs to a senior")
    

#Calculate Tax Based on Income Slabs
# a=float(input("Enter the annual income in lakhs : "))
# d_coount=0
# if a<=2.5:
#     d_coount=0
# elif a<=2.5<5:
#     d_coount=(a-2.5)*0.05
# elif a<=5<10:
#     d_coount =(2.5*5)+(a-5)*0.20
# else:
#     d_coount =(2.5*0.05)+(5-0.20)+(a-10)*0.30
# print("Total tax in rupees is : ",d_coount)









#hotel bill calculator
# def cal_bill(room_type,num_nights,incr_percent):
#     rate_set = {
#         "ultra_luxury":8000,
#         "luxury": 6500,
#         "normal_room": 3500
#         }
#     rate=rate_set[room_type]
#     new_rate = rate*(1+incr_percent/100)
#     tot_bill= new_rate*num_nights
#     return tot_bill
# def room_main():
#     print("select the type of room : ")
#     print("ultra luxury room for 1 night : 8000 ")
#     print("luxury room for 1 night : 6500 ")
#     print("normal room for 1 night : 3500 ")
#     while True:
#         ch = int(input("Enter your choice (1-4): "))
#         if ch == 1:
#             room_type = "ultra_luxury"
#         elif ch == 2:
#             room_type = "luxury"
#         elif ch == 3:
#             room_type = "normal"
#         elif ch == 4:
#             print("Bye! Will meet again when you need me...")
#             break
#         else:
#             print("Invalid choice. Please try again.")
#             continue

#         no_nights = int(input("Enter number of nights: "))
#         percent = float(input("Enter price increase percentage (e.g. 10 for 10%): "))

#         total = cal_bill(room_type,no_nights, percent)
#         print(f"Total Bill for {no_nights} night(s) in {room_type.replace('_', ' ').title()}: ₹{total:.2f}")

# room_main()


#Grocery Store Discount
# def cal_groceries(grocery_items):
#     total = sum(grocery_items.values())
#     if total > 1000:
#         discount = total * 0.10
#         total -= discount
#         print(f"Discount applied: ₹{discount:.2f}")
#     else:
#         print("No discount applied.")

#     print("Total amount payable: ₹{:.2f}".format(total))
#     return total

# rate_set = {
#     "rice 10kg": 800,
#     "Milk": 65,
#     "Bread": 40,
#     "oil": 100,
#     "flour per kg": 200,
#     "cleaning detergent": 300
# }
# customer_cart = {
#     "rice 10kg": 800,
#     "Milk": 65,
#     "oil": 100,
#     "bread":40
# }

# cal_groceries(customer_cart)





# Library Fine Calculator
# def cal_fine(lib_book,num_days):
#     fine_book = 5
#     tot_bill= fine_book*num_days
#     return tot_bill

# def fine_calu():
#     num_days = int(input("Enter number of days book return: "))
#     lib_book = input("book name : ")
#     total = cal_fine(lib_book,num_days)
#     print(f"Total fine for {num_days} days(s) book returned late in : {total}")

# fine_calu()


#Temperature Converter
# def temp(c,scale):
#     if scale=="CtoF":
#         return((c*9/5)+32)
#     elif scale=="FtoC":
#         return ((c-32)*5/9)
#     else:
#         return "Invalid scale"
# print(temp(100, "CtoF"))  
# print(temp(32, "FtoC"))

#Student Grade Calculator
# def stu_grade():
#     sub1=int(input("enter marks for subject 1 : "))
#     sub2=int(input("enter marks for subject 2 : "))
#     sub3=int(input("enter marks for subject 3 : "))
#     avg=(sub1+sub2+sub3)/3
#     if avg>75:
#        grade="A+"
#     elif avg>60:
#         grade="B"
#     elif avg>50:
#         grade="C+"
#     elif avg>=35:
#         grade="D"
#     else:
#         grade="F(failed)"
#     return avg,grade
# avg,grade=stu_grade()

# print(f"The average is {avg:.2f}. Grade obtained is {grade}.")

#ATM Withdrawal Fee
# def atm_withdrawal_cal(a,b):
#     with_fee=20
#     total_amount = a + b*with_fee
#     return total_amount
# def atm_with():
#     a=int(input("Amount withdrawn : "))
#     b=int(input("Number of times money withdrawn : "))
#     tot_amount=atm_withdrawal_cal(a,b)
#     print(f"Total amount is : {tot_amount}")
# atm_with()

#Taxi Fare Calculator
# def cal_taxi_fare(dist_travel,fare):
#     tot_amount=fare
#     for dis_traveled in range(1,dist_travel+1):
#         tot_amount=fare+5*dist_travel
#     return tot_amount
# fare=10
# dist_travel=int(input("No of kilometers travelled : "))
# amount=cal_taxi_fare(dist_travel,fare)
# print("Total amount for ",dist_travel,"km is",amount)

#Electricity Bill Calculator
# def cal_electri_bill(rate,units):
#     tot_bill=rate
#     for unitss in range(100,units+1):
#         tot_bill=rate+3*units
#     return tot_bill
# rate = 2
# units=int(input("Enter the number of units consumed : "))
# bill=cal_electri_bill(rate,units)
# print(f"Electricity bill based on {units} units is {bill}")

#Movie Ticket Booking
# def tot_cost_movie_ticket(num_tickets,ticket_price):
#     if num_tickets>5:
#         discount=10
#     else:
#         discount=0
#     dis_amount=(ticket_price * discount)/100
#     total=num_tickets*(ticket_price-dis_amount)
#     return total
# num_tickets=int(input("no of tickets : "))
# ticket_price=int(input("Ticket price : "))
# amount=tot_cost_movie_ticket(num_tickets,ticket_price)
# print(f"Total cost for {num_tickets} tickets is {amount:.2f} ")


# Bank Interest Calculator
def cal_interest_bank(princ_amount,interest_rate,time_period):
    Interest = (princ_amount * interest_rate*time_period)/100
    return Interest
princ_amount=int(input("Enter the principal amount : "))
interest_rate=float(input("enter the interest rate applicable : "))
time_period=float(input("Enter the time period of deposit : "))
amount=cal_interest_bank(princ_amount,interest_rate,time_period)
print(f"Total interest on bank deposit of {princ_amount} is {amount:.2f}")
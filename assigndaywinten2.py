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
# def cal_interest_bank(princ_amount,interest_rate,time_period):
#     Interest = (princ_amount * interest_rate*time_period)/100
#     return Interest
# princ_amount=int(input("Enter the principal amount : "))
# interest_rate=float(input("enter the interest rate applicable : "))
# time_period=float(input("Enter the time period of deposit : "))
# amount=cal_interest_bank(princ_amount,interest_rate,time_period)
# print(f"Total interest on bank deposit of {princ_amount} is {amount:.2f}")

#hotel management system
# class Person:
#     def init(self, name="Unknown", age=0):
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")


# class Patient(Person):
#     def init(self, name, age, disease):
#         super().init(name, age)
#         self.disease = disease

#     def display_info(self):
#         super().display_info()
#         print(f"Disease: {self.disease}")


# class Doctor(Person):
#     def init(self, name, age, specialization):
#         super().init(name, age)
#         self.specialization = specialization

#     def display_info(self):
#         super().display_info()
#         print(f"Specialization: {self.specialization}")
# class Surgeon(Doctor):
#     def init(self, name, age, specialization, on_call_status):
#         super().init(name, age, specialization)
#         self.on_call_status = on_call_status

#     def display_info(self):
#         super().display_info()
#         print(f"On Call: {'Yes' if self.on_call_status else 'No'}")

# class Staff(Person):
#     def init(self, name, age, role):
#         super().init(name, age)
#         self.role = role

#     def display_info(self):
#         super().display_info()
#         print(f"Role: {self.role}")

# class Appointment:
#     def init(self):
#         self.__patient_name = None
#         self.__doctor_name = None
#         self.__appointment_time = None

#     def get_patient_name(self):
#         return self.__patient_name
#     def get_patient_name(self):
#         return self.__patient_name

#     def set_patient_name(self, name):
#         self.__patient_name = name

#     def get_doctor_name(self):
#         return self.__doctor_name

#     def set_doctor_name(self, name):
#         self.__doctor_name = name

#     def get_appointment_time(self):
#         return self.__appointment_time

#     def set_appointment_time(self, time):
#         self.__appointment_time = time



class Person:
    def init(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Patient(Person):
    def init(self, name, age, disease):
        super().init(name, age)
        self.disease = disease

    def display_info(self):
        super().display_info()
        print(f"Disease: {self.disease}")


class Doctor(Person):
    def init(self, name, age, specialization):
        super().init(name, age)
        self.specialization = specialization

    def display_info(self):
        super().display_info()
        print(f"Specialization: {self.specialization}")
class Surgeon(Doctor):
    def init(self, name, age, specialization, on_call_status):
        super().init(name, age, specialization)
        self.on_call_status = on_call_status

    def display_info(self):
        super().display_info()
        print(f"On Call: {'Yes' if self.on_call_status else 'No'}")

class Staff(Person):
    def init(self, name, age, role):
        super().init(name, age)
        self.role = role

    def display_info(self):
        super().display_info()
        print(f"Role: {self.role}")

class Appointment:
    def init(self):
        self.__patient_name = None
        self.__doctor_name = None
        self.__appointment_time = None

    def get_patient_name(self):
        return self.__patient_name
    def get_patient_name(self):
        return self.__patient_name

    def set_patient_name(self, name):
        self.__patient_name = name

    def get_doctor_name(self):
        return self.__doctor_name

    def set_doctor_name(self, name):
        self.__doctor_name = name

    def get_appointment_time(self):
        return self.__appointment_time

    def set_appointment_time(self, time):
        self.__appointment_time = time




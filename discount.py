# discout
price= float(input("price = "))
qty = int (input("qty = "))
total= price * qty

if total <=9:
    dis = 0
elif total <=24:
    dis = price * 0.05
else :
    dis=price* 0.1
print("total = ",total," $" )
print("qty =  ",qty)
print("discount = ",dis,"$")

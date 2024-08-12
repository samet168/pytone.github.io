print("========>>>> Grade <<<<========")
khmer = float(input(" Khmer = "))
math = float (input(" Math = "))
py = float (input(" py = "))
English = float (input(" English = "))

avg = (khmer + math + py + English) / 4
if avg<49:
    grade="F"
elif avg >50 and avg<=65:
    grade= "E"

elif avg >66 and avg<=75:
    grade="D"
elif avg >75 and avg<=85:
    grade="C"
elif avg >85 and avg <=95:
    grade="B"
else:
    grade="A"
print("average: ",avg)

print("Grade: ",grade)	
# print("average: {avg}",)

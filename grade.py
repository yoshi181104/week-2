score = int(input)("ใส่คะแนน :")
if score < 0 or score > 100:
    print ('ใส่เลข 0 - 100')
elif score >= 80:
    print ("เกรด 4")
elif score >= 70:
    print ("เกรด 3")
elif score >= 60:
    print ("เกรด 2")
elif score >= 50:
    print ("เกรด 1")
else: 
    print ("เกรด 0")                   
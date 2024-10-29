import random
print ("โปรแกรมเป่ายิ้งฉุบ")
while True:
    a= random.choice(["ต้อน","กรรไกร","กระดาษ"])
    b=input("เลือก ต้อน กรรไกร กระดาษ:")
    if a == b:
        print ("เสมอ")
    elif a == "ค้อน" and b == "กระดาษ" or a == "กรรไกร" and b == "ค้อน" or a == "กระดาษ" and b == "กรรไกร" :
        print ("ชนะ")
    else :
        print ("แพ้")   
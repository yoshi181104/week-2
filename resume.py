name = input("กรอกชื่อ\n")
nickname = input("ชื่อเล่น\n")
age = input("อายุ\n")
id  = input("รหัสประจำตัว\n")
study = input("ชั้นปี\n")
height = float(input("ส่วนสูง\n"))
weight = float(input("น้ำหนัก\n"))
handw = height + weight

print(f"ชื่อ: {name} อายุ{age} ปี")
print(f"ชื่อเล่น: {nickname}")
print(f"รหัสประจำตัว: {id} ชั้นปี{study}")
print(f"ส่วนสูง: {height} เซนติเมตร น้ำหนัก {weight} กิโลกรัม")
print(f"ส่วนสูง + น้ำหนัก = {handw}")
from time import sleep
import random
import os

x=1
y=0

while x==1:
    start=str(input("Đăng ký hay đăng nhập(dk/dn): "))

    if start=="dk":
        user=str(input("Tài khoản: "))
        tk=open(f"{user}.tk","w")
        mk=str(input("Mật khẩu: "))
        tk.write(mk)
        tk.write("\n")
        tk.write("10000")
        tk.close()
        print("Bạn đã được tặng 10000$")
        print("Hãy đăng nhập lại")
    if start=="dn":
        user=str(input("Tài khoản: "))
        tk=open(f"{user}.tk","r")
        mk=str(input("Mật khẩu: "))
        xmmk=tk.readline()
        xmmk=xmmk.replace("\n","")
        tiendu=tk.readline()
        if mk==xmmk:
            print("Đăng nhập thành công")
            print(f"Số tiền:{tiendu}$")
            x=0
        else:
            print("Sai tài khoản hoặc mật khẩu")
            
while x==0:
    mk=mk
    tiendu=float(tiendu)
    while y==0:
        cuoc=float(input("Chọn số tiền cần cược: "))
        if cuoc<=tiendu:
            tiendu=tiendu-cuoc
            print(f"Cược thành công {cuoc}$")
            break
        else:
            print("Bạn không đủ tiền")
    torx=str(input("Bạn chọn tài hay xỉu(t/x): "))
    if torx=="t":
        ss=11,12,13,14,15,16,17
    if torx=="x":
        ss=4,5,6,7,8,9,10
    print("Đang xóc...")
    sleep(3)

    one = random.randint(1, 6)
    two = random.randint(1, 6)
    three = random.randint(1, 6)

    print(f"Xóc ra: {one}, {two} và {three}")

    tong=one+two+three
    print(f"Tổng điểm: {tong} điểm")

    if tong in ss:
        print("Bạn đã thắng")
        tienthang=cuoc*2
        tongtien=tienthang+tiendu
        tongtien=str(tongtien)
        tk.close()
        os.remove(f"{user}.tk")
        tk=open(f"{user}.tk","w")
        tk.write(mk)
        tk.write("\n")
        tk.write(tongtien)
        tiendu=tongtien
        tk.close()
        print(f"Hiện có: {tongtien}$")
    else:
        print("Bạn đã thua")
        tiendu=str(tiendu)
        tk.close()
        os.remove(f"{user}.tk")
        tk=open(f"{user}.tk","w")
        tk.write(mk)
        tk.write("\n")
        tk.write(tiendu)
        tk.close()
        print(f"Hiện có: {tiendu}$")
    rep=str(input("Bạn có muốn chơi tiếp không(y/n): "))
    if rep=="y":
        x=0
    else:
        x=1

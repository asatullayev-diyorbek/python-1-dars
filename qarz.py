royxat = [
    {
        "ism":"Ali", 
        "miqdor": 1234, 
        "berildi":"13.05.2025", 
        "muddat": "6oy"
    }
] 

def hamma_qarzlar(royxat):
    print("*** Qarzlar ro'yxati **")
    for qarz in royxat:
        print(f"Ism: {qarz["ism"]} -> {qarz["miqdor"]} so'm")
        print(f"-----{qarz["berildi"]} -> {qarz["muddat"]}")
    print("-----------------------------")


def qushish():
    global royxat
    print("*** Yangi qarz qo'shish **")

    ism = input("Qarz oluvchi ismi: ")
    miqdor = input("Miqdor: ")
    berildi = input("Qachon berildi: ")
    muddat = input("Muddat: ")
    qarz = {
        "ism": ism,
        "miqdor": miqdor,
        "berildi": berildi,
        "muddat": muddat
    }
    royxat.append(qarz)

    print("➕ Yangi qarzdor qo'shildi!")
    print("-----------------------------")

while True:
    print("Menyuni tanlang: ")
    print("1. Hamma qarzlar")
    print("2. Yangi qo'shish")
    print("3. O'chirish")
    print("Boshqa belgi - Chiqish")
    menu = input("Tanlangan menu: ")

    if menu == "1":
        hamma_qarzlar(royxat)
    elif menu == "2":
        qushish()
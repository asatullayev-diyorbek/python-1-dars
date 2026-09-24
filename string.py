# ism = "Ali"
# #.     012
# #.      -3 -2 -1

# # print(ism[3])

# # print(ism[-3])

# familiya = "Valiyev jask hdf a fasbj"

# matn = "*** Markaziy Osiyo. Izoh** davlatlari va Koreya    Respublikasi     oʻrtasida xavfsizlik, bir-birini toʻldirib turadi. ****"

# print(matn.upper())
# print(matn.lower())
# print(matn.title())
# print(matn.capitalize())
# print(matn.rstrip("*"))

# print(matn.replace("*", ""))
# print(matn.split(" "))
# print(matn.count("a"))
# print(matn.find("f"))


# print(ism.isalpha())
# print(matn.isnumeric())


ism = input("Ismingizni kiriting: ")

ism = ism.strip(" ")
ism = ism.title()
print("Ism:", ism)
print(len(ism))
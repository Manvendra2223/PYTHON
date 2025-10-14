chai = "Lemon chai"
print(chai)
chai = "masala chai"
first_char = chai[0]
print(first_char)
last_char = chai[-1]
print(last_char)
print(chai)
slice_chai = chai[0:6]
print(slice_chai)

num_list = "01123456789"
print(num_list[:])
print(num_list[3:])
print(num_list[:7]) 
print(num_list[0:7:2])
print(num_list[::3])
print(num_list[::-1])
 
print(num_list[-1:-10:-1])
print(num_list[-3::-1])
print(num_list[-3:0:-1])
print(chai)
print(chai.upper())
print(chai.lower())
chai = "    Masala Chai   "
print(chai)
print(chai.strip())
chai = "Lemon Chai"
print(chai.replace("Lemon", "ginger"))
print(chai)
chai = "Lemon,Ginger,Masala,Cardamom"
print(chai.split())
print(chai.split(","))
chai ="Masala Chai"
print(chai)
print(chai.find("Chai"))
print(chai.find("Tea"))
print(chai.find("a"))
print(chai.count("a"))
print(chai.count("Chai"))
chai_type = "Masala"
quantity = 2
order = "I would like {} cups of {} chai".format(quantity, chai_type)
print(order)
chai_variety = ["Masala", "Lemon", "Ginger", "Cardamom"]
print(chai_variety)
print(", ".join(chai_variety))
print(" and ".join(chai_variety))
print(" ".join(reversed(chai_variety)))

print(chai)
print(len(chai))
print(chai.isalnum())
print(chai.isalpha())
print(chai.endswith("Chai"))
#for letter in chai:
   # print(letter)
#for index in range(len(chai)):
   # print(chai[index])
chai = "he said , \"masala chai is awesome \" "
print(chai)
chai = "masala\nchai"

print(chai)
print(r"masala\nchai")
#chai = r"c:\user\pwd\"
#print(chai)
chai = r"c:\user\pwd"
print(chai)
#chai = "c:\user\pwd"
#print(chai)
chai = "c:\\user\\pwd"
print(chai)
chai = "lemon tea"
print(chai)
print("masala" in chai)
print("lemon" in chai)
print("ginger" not in chai)
print("tea" in chai)
print("Tea" in chai)
print("tea" not in chai)

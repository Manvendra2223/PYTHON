chai_types = {"Masala":"Spicy", "Adrak":"Ginger", "Elaichi":"Cardamom"}
print(chai_types)
chai_types["Masala"]
print(chai_types["Masala"])
chai_types.get("Adrak")
print(chai_types.get("Adrak"))
chai_types.get("Arak")
print(chai_types.get("Arak"))
chai_types.get("Masalaa")
print(chai_types.get("Masalaa"))
print(chai_types)
chai_types["Masala"] = "Very spiceyy"
print(chai_types)
for chai in chai_types :
    print(chai)
    for chai in chai_types :
        print(chai, chai_types[chai])
    for key , value in chai_types.items() :
        print(key , value)
        if "Masala" in chai_types :
            print("Yes, Masala is present")
            print(len(chai_types))
        else :
            print("No, Masala is not present")
chai_types["Kashmiri"] = "Rich"
print(chai_types)
print(len(chai_types))
chai_types.pop("Adrak")
print(chai_types)
print(len(chai_types))
chai_types.clear()
print(chai_types)
chai_types = {"Masala":"Spicy", "Adrak":"Ginger", "Elaichi":"Cardamom"}
print(chai_types)
chai_types["Earl Grey"] = "Citrus"
print(chai_types)
chai_types["Masala"] = "Very Spicy"
print(chai_types)
print(len(chai_types))
chai_types.pop("Elaichi")
print(chai_types)
del chai_types["Adrak"]
print(chai_types)
chai_types_copy = chai_types.copy()
[print(chai_types_copy)]
tea_shop = {
    "chai": {"Masala":"Spicy", "Adrak":"Ginger", "Elaichi":"Cardamom"},
    "snacks": ["Samosa", "Pakora", "Chaat"],
    "location": "Delhi",
}
print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["snacks"], tea_shop["location"])
squared_numbers = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squared_numbers)
print(squared_numbers[3])
print(squared_numbers.get(4))
print(squared_numbers.get(6, "Not Found"))
keys = ["Masala","Ginger","Adrak"]
default_value = "Available"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
new_dict = dict.fromkeys(keys, keys)
print(new_dict)
print(dict.fromkeys(range(1,6)))
print(dict.fromkeys("Chai"))


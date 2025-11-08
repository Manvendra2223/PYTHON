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
            
            

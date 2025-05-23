odp = input("Jaki znasz język programowania")

match odp.casefold():
    case "java":
        print("Java")
    case "python":
        print("python")
    case "c#":
        print("C#")
    case _:  # odpowiednik else
        print("inny")

# ẞ
name = "gross"
name2 = "Groẞ"
print(name.lower() == name2.lower())  # False
print(name.casefold() == name2.casefold())  # True

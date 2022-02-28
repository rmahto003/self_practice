questions = [
        
       {
        "q": "What is the full form of CFL ",
        "a": "Compact Flying Lamp",
        "b": "Contact Fixed Line",
        "c": "Compact Flourescent Lamp",
        "d": "None of these",
        "key": "c"
        },

        {
        "q": "Cost Price = Rs. 200, S.P. = Rs. 300, What is the loss or gain % ?",
        "a": "10%",
        "b": "20%",
        "c": "30%",
        "d": "50%",
        "key": "d"
        }
    ]

for i in questions:
    print(i["q"])

    print("A. " + i["a"])
    print("B. " + i["b"])
    print("C. " + i["c"])
    print("D. " + i["d"])

    answer = input("Choose correct option (a/b/c/d) : ")

    print(answer == i["key"])
    

Items = {
    1 : {
        "Class" : "Warrior",
        "Level" : 1,
    },
    2 :{
        "Class" : "Mage",
        "Level" : 1
    },
    3:{
        "Class" : "Assassin",
        "Level" : 1
    }
}
while True:
    print("|Code |Class             |Level|")
    print("================================")
    for code_key in Items.keys():
        code = code_key
        print("|{code:<5}|{Class:<18}|{Level:<5}|".format(code = code,
                                                        Class = Items[code_key]["Class"],
                                                        Level = Items[code_key]["Level"],))
    print("================================")
                                                        
    try: 
        choice = int(input('Choose Your Hero: '))
    except:
        print('Invalid')
    if choice in Items:
        hero = Items[choice]

        print(f"You Choose {hero['Class']}")
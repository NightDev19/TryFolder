Items = {
    1 : {
        "Class" : "Warrior",
        "Level" : 1,"STR" : 10,"DEX":10,"VIT":10, "INT":10 ,"MEN":10,
        "Skill":{1:"Slash",
                 2:"Shield Bash"},
        "Weaponry":"Staff"
        },
    2 :{
        "Class" : "Mage",
        "Level" : 1,"STR" : 10,"DEX":10,"VIT":10, "INT":10 ,"MEN":10 ,
        "Skill":{1:"Fireball",
                 2:"Barrier"},
        "Weaponry":"Staff"
    },
    3:{
        "Class" : "Assassin",
        "Level" : 1,"STR" : 10,"DEX":10,"VIT":10, "INT":10 ,"MEN":10,
        "Skill":{1:"Knife Throw",
                 2:"Shadow Sneak"},
        "Weaponry":"Dual Sword"
   }
}
SP = 3
def startingpoint():
    print("|Code |Class             |Level|")
    print("================================")
    for code_key in Items.keys():
        code = code_key
        print("|{code:<5}|{Class:<18}|{Level:<5}|".format(code = code,
                                                        Class = Items[code_key]["Class"],
                                                        Level = Items[code_key]["Level"],))
    print("================================")
    methodchoose()
def methodchoose():
    while True:                            
        try:
            global name
            name  = input("Your Username : ")
            choice = int(input('Choose Your Hero: '))
        except:
            print('Invalid')
        if choice in Items:
            global hero 
            hero = Items[choice]

            print(f"{name} Choose {hero['Class']}")
        return methoddashboard()
def methodbag():
    while True:
        print("=================================")
        print("|Weapon:{Weapon:<10}\n".format(Weapon = hero["Weaponry"]))
        stopper = input("Go back? [Y/N]")
        if  stopper.upper() == "Y":
            return methoddashboard()
        if stopper.upper() == "N":
            break
def methodskill():
    pass
def methoddashboard():
    while True:
        print("===================================")
        print("|Name :{Name:<10} Hero: {Class:<9}|\n|Level : {Level:<5}".format(Name = name ,Class = hero["Class"],Level = hero["Level"]))
        stopper = input("Bag? [Y/N] : ")
        if stopper.upper() == "Y":return methodbag()

if __name__=="__main__":
    startingpoint()
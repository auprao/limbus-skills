from Skill import Skill

# coin types
add = lambda base, coin : base + coin 
mult = lambda base, coin : base * coin
div = lambda base, coin : int(base / coin)

#all skill list
skills = []
 
skills.append(Skill("Beheading", 3, add, 4, 2))
skills.append(Skill("Self-destructive Purge", 30, add, -12, 3))
skills.append(Skill("Multiply", 2, mult, 2, 3))
skills.append(Skill("Divide", 20, div, 2, 3))
skills.append(Skill("Imaginary Slash", complex(3, 2), mult, complex(0, 3), 4))

def add_skill() :
    name = input("Skill name: ")
    operation = input('What type of skill? Type "add" for positive/negative, "mult" for multiplicative, "div" for dividing: ')
    coin_count = int(input("Coin count: "))
    base_power = int(input("Base power: "))
    coin_power = int(input("(for negative coins, add a minus) Coin power: "))
    match operation :
        case "add" :
            skills.append(Skill(name, base_power, add, coin_power, coin_count))
        case "mult" :
            skills.append(Skill(name, base_power, mult, coin_power, coin_count))
        case "div" :
            skills.append(Skill(name, base_power, div, coin_power, coin_count))
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

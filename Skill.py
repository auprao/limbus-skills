from random import randrange


def roll_coin(sanity) :
        return(randrange(101) < 50 + sanity)

class Skill() :

    def __init__(self, name, base_power, operation, coin_power, coins):
        self.name = name
        self.base_power = base_power
        self.coin_power = coin_power
        self.coins = coins
        self.operation = operation
    
    def execute_skill(self, sanity) :
        print("""
        """)
        print(f"{self.name} at sanity {sanity}")
        print(f"Base Power: {self.base_power}, Coin Power: {self.coin_power}, {self.coins} coins.")

        power = self.base_power
        total = 0

        for i in range(self.coins) :
            print(f"Coin {i+1} : ", end="")
            heads = roll_coin(sanity)
            if heads : 
                print("Heads")
                power = (self.operation(power, self.coin_power))

                if power.real < 0 : 
                    if isinstance(power, int) : power = 0


            else : 
                print("Tails")

            real_power = max(0, int(power.real))
            print(f"{real_power} damage")
            total += real_power
        
        print(f"Total {total} damage.")
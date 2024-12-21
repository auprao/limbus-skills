from Skills import skills
from Skill import Skill

def read_skills() :
    for i in range(len(skills)) :
        print(f"{i}. {skills[i].name}")

sanity = 0

input_text = f"""Type 0 to exit.
Type 1 to change current Sanity.
Type 2 to see list of skills.
Type 3 to execute skill by number: """
running = True

while running :
    print(f"Current Sanity: {sanity}.")
    option = input(input_text)
    match option :
        case "0" :
            running = False
        case "1" :
            sanity = int(input("Type the new sanity number, between -45 and 45: "))
        case "2" :
            read_skills()
        case "3" :
            skill_choice = int(input("Write the skill's number: "))
            skills[skill_choice - 1].execute_skill(sanity)
print("Exiting program.")

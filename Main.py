from Skills import skills, add_skill
from Skill import Skill

def read_skills() :
    for i in range(len(skills)) :
        print(f"{i + 1}. {skills[i].name}")
        print(f"Expected damage: {skills[i].get_expected_dmg()}")


sanity = 0

input_text = f"""Type 0 to exit.
Type 1 to change current Sanity.
Type 2 to see list of skills.
Type 3 to add a skill of your own.
Type 4 to execute skill by number.
Type 5 to execute skill by name: """
running = True

while running :
    print(f"Current Sanity: {sanity}.")
    option = input(input_text)
    match option :
        case "0" :
            running = False
        case "1" :
            sanity = int(input("Type the new sanity number, between -45 and 45: ")) # add error handling
        case "2" :
            read_skills()
        case "3" :
            add_skill()
        case "4" :
            skill_choice = int(input("Write the skill's number: "))
            skills[skill_choice - 1].execute_skill(sanity)  # add error handling
        case "5" :
            skill_choice = input("Write the skill's name: ")
            done = False
            for skill in skills :
                if skill.name.lower() == skill_choice.lower() :
                    skill.execute_skill(sanity)
                    done = True
                    break
            if not done:
                print("No skill with such name.")

print("Exiting program.")

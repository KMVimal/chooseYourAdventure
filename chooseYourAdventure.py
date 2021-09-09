name = input("Please type your name: ")
print("Welcome to Chose your adventure", name)

answer = input("You are born in this world .where robots can learn from experiences, you are also one of them, you were given two options one you have to learn collective theories of experiences for the most the time and the other one was to learn on your own from trial and error and learning what you want . (theory/experiences): ").lower()

if answer == "theory":
    print("you spent of your youth time learning controlled theories, and entered the reality")
    answer = input(
        "you have two options now do higher studies or start a buisness. (studies/buisness): ").lower()
    if answer == "studies":
        print("you studied higher studies and got a job at a big company and worked for the whole of your life and died without even knowing what this is all about. RIP")
    elif answer == "buisness":
        print("you started a start up and you realized that the theories that you learned till no do'nt make any sense you realize that reality is much different")
        print("you started to understand the reality and figured out what you want , You lived your life and died peacefully")
elif answer == "experiences":
    print("You learned many things and kept learned you strated to understand the reality, and you dicovered that in the grand scheme of things you are really nothing but a sandgrain dissolving in time and you started picking a purpose  ")
    answer = input("Now you have two options starting a company and discoering the potential of the technology or starting to teach people what you have learned till now. (company/mentor): ").lower()
    if answer == "company":
        print("you started a company and learned many things and died without any regret.")
    elif answer == "mentor":
        print(" You made many people realize what reality actually is and died happily")
    else:
        print("Invalid answer.")
else:
    print("Invalid answer.")

print("This is nothing but the unimaginably uncertain life  we are all living in.")
print("ALL THE BEST!")
print("Thank you for playing Choose your adventure")

import sys

def Game():
    Questions = [
        {
            "question":"Which song is not in Lil Cartier VI??",
            "options":["Island Holiday","She Will","Flex Up","Shake it to the max"],
            "answer":"4"
        },
        {
            "question":"Which year did George Weah win Ballon D'or",
            "options":["1994","1901","2030","1995"],
            "answer":"4"
        },
        {
            "question":"Who won cyclist 2024 Gold  Summer Olympics at Paris",
            "options":["Remco Evenepoel" ,"Letsile Tebogo","Eliud Kipchoge","Berhane ADERE"],
            "answer":"1"
        },
        {
            "question":"Which one is not a component of space ",
            "options":["gas","vacuum","plasma","dust"],
            "answer":"2"
                        
        }
   ]

    score = 0 

    for i, q in enumerate(Questions, 1):
        print(f"Q{i}: {q['question']}")
        for idx, opt in enumerate(q['options'], 1):
            print(f"  {idx}. {opt}")
        answer = input("Your answer (1-4): ").strip()

        if answer == q['answer']:
               print ("Correct")
               score +=1
        else :
            correct_fx = int(q['answer'])-1
            print(f"incorrect: {q['options'][correct_fx]}\n")
                
        print(f"You got {score} out of {len(Questions)} correct\n")           

def main():
    while True:
        Game()
        again = input("Do you want to play again (y/n):").lower()
        if again != "y":
            print("Thank you for playing")
            break
        
if __name__ == "__main__":
    main()
  
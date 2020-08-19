import random
import pyttsx3
import speech_recognition
lst = ('s', 'p', 'sc')
# game Variables

no_of_chances = 0
chances_avaialable = 10
computers_point = 0
humans_point = 0

# Instructions
print("\t \t \tThis Is the game of Stone, Paper , scissor",)
print(" For Choosing stone press s\t \t \t For Choosing paper press p\t \t \t For Choosing scissor press sc\t \n")

#Speak functions


engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[3].id)

newVoiceRate = 120
engine.setProperty('voice' , voices[4].id)
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# Game Loop

while no_of_chances < chances_avaialable:
    if __name__ == "__main__":
        speak("Stone Paper Scissor")        
            
    _input = input('Choose Stone ,Paper, or Scissor:')
    _random = random.choice(lst)

    if _input == _random:
        print("Its a tie \n")

    elif _input == "s" and _random == "sc":
        print(
            f"Human Won because computer took out {_random} And you took out {_input}\n")
        humans_point += 1
        print(
            f"Best Out of Ten Human:{humans_point} And Computer:{computers_point}\n")

    elif _input == "sc" and _random == "s":
        print(
            f"computer Won because Human took out {_random} And Human took out {_input}\n")
        computers_point += 1
        print(
            f"Best Out of Ten ,Human:{humans_point} And Computer:{computers_point}\n")

    elif _input == "p" and _random == "sc":
        print(
            f"computer Won because Human took out {_random} And Human took out {_input}\n")
        computers_point += 1
        print(
            f"Best Out of Ten ,Human:{humans_point} And Computer:{computers_point}\n")

    elif _input == "sc" and _random == "p":
        print(
            f"Human Won because computer took out {_random} And Human took out {_input}\n")
        humans_point += 1
        print(
            f"Best Out of Ten Human:{humans_point} And Computer:{computers_point}\n")

    elif _input == "s" and _random == "p":
        print(
            f"computer Won because Human took out {_random} And Human took out {_input}\n")
        computers_point += 1
        print(
            f"Best Out of Ten ,Human:{humans_point} And Computer:{computers_point}\n")

    elif _input == "p" and _random == "s":
        print(
            f"Human Won because Human took out {_random} And Human took out {_input}\n")
        humans_point += 1
        print(
            f"Best Out of Ten ,Human:{humans_point} And Computer:{computers_point}\n")

    else:
        print("You Have put A wrong input")

    no_of_chances+= 1
    print(f"The number of chances Left is {chances_avaialable-no_of_chances} Out of {chances_avaialable} \n ")

print("Game Over")

if humans_point == computers_point:
    print("There is A tie-Beetween You, Both have potential Better Luck next time\n")

elif humans_point > computers_point:
    print(f"Congratulations! You won ,Your points{humans_point}\n")

else:
    print("Computer Won")


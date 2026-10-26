# rule based ai chatbot
import datetime
import time


name=input(" welcome! Please enter your name:")
presenthour= datetime.datetime.now().hour
if 5<= presenthour <=11:
    print("Good Morning!",name)
elif 11<= presenthour <=16:
    print("Good Afternoon!",name)
elif 18<= presenthour <=20:
    print("Good Evening!",name)
else:
    print("Good Night!",name)


print(" Hi There! Welcome to Rule Based Ai Chatbot... ")
print("You can ask basic Question , type 'bye' to exit from the bot. ")

# memory of chatbot using dictionery
response={
    "hello":f"Hi, {name} welcome. how can i help you?",
    "how are you":"i am fine. Thank you.",
    "who are you":"i am smart ai chatbot",
    "motivate me":"keep going , every bug of your code makes you a better devloper.",
    "what can you do":"i can talk with you and make your life easier .",
    "what is function":" A function in Python is a block of reusable code.",
    "what is oop":"you will learn soon..",
    "what are you doing":"nothing just helping you.",
    "what will we learn today":"we will learn phyhon today",
  
}

# function to get response of bot
def getresponseofbot(userquestion):
    userquestion=userquestion.lower()
    for eachkey in response:
        if eachkey in userquestion:
            return response [eachkey]
    return "i will learn soon."
# taking userinput
while True:
    userinput=input("Please ask your question:")
    if "sad" in userinput.lower():
        print("I'm sorry you're feeling sad. Hope you feel better soon! 💙")
    elif "happy" in userinput.lower():
        print("That's wonderful! Keep smiling! 😊")
 
    elif "bye" in userinput.lower():
        print("good bye! thank you for using ai chatbot.")
        break
    else:
        reply = getresponseofbot(userinput)
        time.sleep(0.5)
        print("Response of Bot:", reply)

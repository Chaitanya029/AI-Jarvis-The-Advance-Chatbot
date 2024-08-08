from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionAnswer
from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait For Few Second")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Starting The Jarvis : Wait For Few Second More")
from Main2 import MainTaskExecution

def MainExecution():

    Speak("Hello Sir")
    Speak("I'm Jarvis, I'm Here You Assist You Sir.")

    while True:

        Data = MicExecution()
        Data = str(Data).replace(".","")
        
        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass

        elif len(Data)<3:
            pass

        elif "what is" in Data or "what is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionAnswer(Data)

        else:  
            Reply = ReplyBrain(Data)
            Speak(Reply)    

def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">> Clap Detected !! >>")
        print("")
        MainExecution()
    else:
        pass            

ClapDetect()
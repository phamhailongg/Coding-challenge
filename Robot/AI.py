from datetime import *
from webbrowser import *
from wikipedia import * 

def greeting() : 
    H = int(datetime.now().hour)
    if 0 <= H < 12 : 
        print("""JARVIS: Good morning Sir! I am your digital assistant JARVIS!
How can I help you ? """)
    elif 12 <= H < 18 : 
        print("""JARVIS: Good afternoon Sir! I am your digital assistant JARVIS!
How can I help you ? """)
    elif 18 <= H != 0 : 
        print("""JARVIS: Good evening Sir! I am your digital assistant JARVIS!
How can I help you ? """)

greeting()
while True :
    cmd = str(input(("Command: ")))
    if cmd.isdigit() : 
        print("JARVIS: Sorry Sir. I do not get it. Try to type another command")
        cmd = str(input(("Commnad: ")))
    if "What time is it ?" in cmd :
        if 12 > datetime.now().hour >= 0 :
            print("JARVIS: " + "It is " + str(datetime.now().hour) + ":" + str(datetime.now().minute) + " now. What do you want me to help Sir ?")
        elif 12 <= datetime.now().hour < 18 :
            print("JARVIS: " + "It is " + str(datetime.now().hour) + ":" + str(datetime.now().minute) + " now. What do you want me to help Sir ?")
        elif 18 <= datetime.now().hour != 0 :
            print("JARVIS: " + "It is " + str(datetime.now().hour) + ":" + str(datetime.now().minute) + " now. What do you want me to help Sir ?")
    
    def alarm_clock() : 
        if "Can you set me an alarm ? " in cmd : 
            print("JARVIS: Sure. What time do you want me to set ?") 
            h = input("Command: ")
            m = input("Command: ")
            if h.isalpha() and m.isalpha() : 
                print("JARVIS: You should insert numbers instead of letters.")
                h = input("Command: ")
                m = input("Command: ")
            else :    
                while True : 
                    if h == datetime.now().hour and m == datetime.now().minute : 
                        print("JARVIS: Ring ring ring...")

                        # music = pyglet.resource.media('sample.mp3')
                        # music.play()
                        # pyglet.app.run()
                        break
                    print("JARVIS: Your alarm is set at " + str(h) + ":" + str(m) + ". What do you want me to help next ?")   
            
    
    alarm_clock()
         
        
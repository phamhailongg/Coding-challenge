from datetime import *
import webbrowser
import wikipedia 
import random 
import sys
import os
import wolframalpha
import smtplib

# mstsc (Window + R)

# client = wolframalpha.Client("Your App ID")

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
    cmd = input("Command: ")
    if cmd.isdigit() or cmd == "" : 
        print("JARVIS: Sorry Sir. I do not get it. Try to type another command")
    else :  
        def time_check() : 
            if "What time is it ?" in cmd :
                if 12 > datetime.now().hour >= 0 :
                    print("JARVIS: " + "It is " + str(datetime.now().hour) + ":" + str(datetime.now().minute) + " now. What do you want me to help Sir ?")
                elif 12 <= datetime.now().hour < 18 :
                    print("JARVIS: " + "It is " + str(datetime.now().hour) + ":" + str(datetime.now().minute) + " now. What do you want me to help Sir ?")
                elif 18 <= datetime.now().hour != 0 :
                    print("JARVIS: " + "It is " + str(datetime.now().hour) + ":" + str(datetime.now().minute) + " now. What do you want me to help Sir ?")
        
        time_check()

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
                    if h == datetime.now().hour and m == datetime.now().minute : 
                        print("JARVIS: Ring ring ring...")

                        # music = pyglet.resource.media('sample.mp3')
                        # music.play()
                        # pyglet.app.run()
                        
                    print("JARVIS: Your alarm is set at " + str(h) + ":" + str(m) + ". What do you want me to help next ?")   
                
        alarm_clock()
        
        def web() :
            # web = ["Open Youtube", "Open Google", "Check my Email", "Play music on Soundcloud", "Check the news", "Open Facebook", "Open Instagram"]
            # if cmd in web : 
            #     print("JARVIS: Okay. Wait me a second!")
            #     webbrowser.open(cmd)
            if "Open Youtube" in cmd : 
                print("JARVIS: Okay. Wait me a second!")
                webbrowser.open("www.youtube.com")
            elif "Open Google" in cmd : 
                print("JARVIS: Okay. Wait me a second!")
                webbrowser.open("www.google.com")
            elif "Check my Email" in cmd : 
                print("JARVIS: Okay. Wait me a second!")
                webbrowser.open("www.gmail.com")
            elif "Play music on Soundcloud" in cmd : 
                print("JARVIS: Okay. Wait me a second!")
                webbrowser.open("www.soundcloud.com")
            elif "Check the news" in cmd : 
                print("JARVIS: Okay. Wait me a second!")
                webbrowser.open("www.edition.cnn.com")
            elif "Open Facebook" in cmd : 
                print("JARVIS: Okay. Wait me a second!")
                webbrowser.open("www.facebook.com")
            elif "Open Instagram" in cmd : 
                print("JARVIS: Okay. Wait me a second!")
                webbrowser.open("www.instagram.com")
        
        web()
        # def searching() :
            # if cmd = cmd :
            #     cmd = cmd
            #     print("JARVIS: Searching...") 
            #     try : 
            #         try : 
            #             res = client.cmd(cmd)
            #             results = next(res.results).text
            #             print("""JARVIS: Got it!
            #             Wolfram Alpha says """ + results)
            #         except : 
            #             results = wikipedia.summary(cmd, sentence = 2)
            #             print("""JARVIS: Got it! 
            #             Wikipedia says """ + results)
            #     except : 
            #         webbrowser.open("www.google.com")
            
        def mail() : 
            if "Can you send me an email ?" in cmd : 
                print("JARVIS: Sure. Who is the recipient ?")
                recipient = input("Command: ")
                try : 
                    print("JARVIS: What should I send ?")
                    content = input("Command: ")

                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.ehlo()
                    server.starttls()
                    server.login("longphamhai123@gmail.com", "phamhailongg")
                    server.sendmail("longphamhai123@gmail.com", str(recipient), content)
                    server.close()
                    print("JARVIS: Your Email is sent!")
                except : 
                    print("JARVIS: Sorry Sir! I am unable to send your message at this moment!")

        mail()

        def file_open() : 
            if "Open folder C" in cmd : 
                print("JARVIS: Opening folder C...")
                path = "C:/"
                path = os.path.realpath(path)
                os.startfile(path)
                print("JARVIS: Folder C opened.")
            elif "Open folder D" in cmd : 
                print("JARVIS: Opening folder D...")
                path = "D:/"
                path = os.path.realpath(path)
                os.startfile(path)
                print("JARVIS: Folder D opened.")
        
        file_open()

        def friend() : 
            if "What's up ?" in cmd or "How are you doing ?" in cmd : 
                Response_1 = ["Just doing my thing Sir.", "I am fine Sir.", "Pretty well Sir.", "I am full of energy right now."]
                print("JARVIS: " + random.choice(Response_1))
        
        friend()

        def good_bye() : 
            if "See you later JARVIS." in cmd or "Goodbye JARVIS " in cmd or "That is all I want." in cmd or "Thanks for your help." in cmd : 
                Response_2 = ["Okay Sir. Hope to help you more", "No Problem. It is my duty to serve you", "Bye Sir. Have a nice day!" ]
                print("JARVIS: " + random.choice(Response_2))
                sys.exit()

        good_bye()    

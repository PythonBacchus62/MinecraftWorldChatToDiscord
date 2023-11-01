from PIL import Image 
from pytesseract import pytesseract 
import pyscreenshot
import pyautogui
from time import sleep

Loop = 0

while Loop == 0:
        image = pyscreenshot.grab(bbox=(0, 885, 1895, 935))
        image.save("C:\Minecraft\Chat.png")
        image2 = pyscreenshot.grab(bbox=(0, 845, 1895, 885))
        image2.save("C:\Minecraft\Chat2.png")


        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        image  = "C:\Minecraft\Chat.png"
        image2 = "C:\Minecraft\Chat2.png"

        # Opening the image & storing it in an image object 
        img  = Image.open(image) 
        img2 = Image.open(image2) 

        # Providing the tesseract executable 
        # location to pytesseract library 
        pytesseract.tesseract_cmd = path_to_tesseract 

        # Passing the image object to image_to_string() function 
        # This function will extract the text from the image 
        text = pytesseract.image_to_string(img) 
        img.close()
        text2 = pytesseract.image_to_string(img2) 
        img2.close()


    
#Text1 unter Zeile 
        try:
           
            if text[0] == "<":
                OldMSG = open("C:\Minecraft\MinecraftDiscordLog.json", "r")
                OldMSG = OldMSG.read()
                if text == OldMSG:
                    pass
                else:
                    print(text)
                    file1 = open("C:\Minecraft\MinecraftDiscord.json", "a")
                    file1.write(text)
                    file1.close()
                    file2 = open("C:\Minecraft\MinecraftDiscordLog.json", "w")
                    file3 = open("C:\Minecraft\MinecraftDiscordLog2.json", "w")
                    file3.write(OldMSG)
                    file2.write(text)
                    file2.close()
                    file3.close()
            else:
                pass

            if text[0] == "+":
                OldMSG = open("C:\Minecraft\MinecraftDiscordLog.json", "r")
                OldMSG = OldMSG.read()
                if text == OldMSG:
                    pass
                else:
                    print(text)
                    file1 = open("C:\Minecraft\MinecraftDiscord.json", "a")
                    file1.write(text)
                    file1.close()
                    file2 = open("C:\Minecraft\MinecraftDiscordLog.json", "w")
                    file3 = open("C:\Minecraft\MinecraftDiscordLog2.json", "w")
                    file3.write(OldMSG)
                    file2.write(text)
                    file2.close()
                    file3.close()
            else:
                pass

            if text[0] == ("-" or "~" or "»"):
                OldMSG = open("C:\Minecraft\MinecraftDiscordLog.json", "r")
                OldMSG = OldMSG.read()
                if text == OldMSG:
                    pass
                else:
                    print(text)
                    file1 = open("C:\Minecraft\MinecraftDiscord.json", "a")
                    file1.write(text)
                    file1.close()
                    file2 = open("C:\Minecraft\MinecraftDiscordLog.json", "w")
                    file3 = open("C:\Minecraft\MinecraftDiscordLog2.json", "w")
                    file3.write(OldMSG)
                    file2.write(text)
                    file2.close()
                    file3.close()
            else:
                pass
                    
            if text[0] == "#":
                OldMSG = open("C:\Minecraft\MinecraftDiscordLog.json", "r")
                OldMSG = OldMSG.read()
                if text == OldMSG:
                    pass
                else:
                    print(text)
                    file1 = open("C:\Minecraft\MinecraftDiscord.json", "a")
                    file1.write(text)
                    file1.close()
                    file2 = open("C:\Minecraft\MinecraftDiscordLog.json", "w")
                    file3 = open("C:\Minecraft\MinecraftDiscordLog2.json", "w")
                    file3.write(OldMSG)
                    file2.write(text)
                    file2.close()
                    file3.close()
        except:
            pass


#Text2 zweite Zeile 
        
        try:
            if text2[0] == "<":
                OldMSG2 = open("C:\Minecraft\MinecraftDiscordLog2.json", "r")
                OldMSG2 = OldMSG2.read()
                if text2 == OldMSG2:
                    pass
                elif text2 == OldMSG:
                    file3 = open("C:\Minecraft\MinecraftDiscordLog2.json", "w")
                    file3.write(text2)
                    file3.close()
                elif text2 == text:
                    file3 = open("C:\Minecraft\MinecraftDiscordLog2.json", "w")
                    file3.write(text2)
                    file3.close()
                else:
                    print(text2)
                    file4 = open("C:\Minecraft\MinecraftDiscord.json", "a")
                    file4.write(text2)
                    file4.close()
                    file3 = open("C:\Minecraft\MinecraftDiscordLog2.json", "w")
                    file3.write(text2)
                    file3.close()
            else:
                pass
            if text2[0] == "+":
                OldMSG2 = open("C:\Minecraft\MinecraftDiscordLog2.json", "r")
                OldMSG2 = OldMSG2.read()
                if text2 == OldMSG2:
                    pass
                elif text2 == OldMSG:
                    file3 = open("C:\Minecraft\MinecraftDiscordLog2.json", "w")
                    file3.write(text2)
                    file3.close()
                elif text2 == text:
                    file3 = open("C:\Minecraft\MinecraftDiscordLog2.json", "w")
                    file3.write(text2)
                    file3.close()
                else:
                    print(text2)
                    file4 = open("C:\Minecraft\MinecraftDiscord.json", "a")
                    file4.write(text2)
                    file4.close()
                    file3 = open("C:\Minecraft\MinecraftDiscordLog2.json", "w")
                    file3.write(text2)
                    file3.close()
            else:
                pass
            if text2[0] == ("-" or "~" or "»"):
                OldMSG2 = open("C:\Minecraft\MinecraftDiscordLog2.json", "r")
                OldMSG2 = OldMSG2.read()
                if text2 == OldMSG2:
                    pass
                elif text2 == OldMSG:
                    file3 = open("C:\Minecraft\MinecraftDiscordLog2.json", "w")
                    file3.write(text2)
                    file3.close()
                elif text2 == text:
                    file3 = open("C:\Minecraft\MinecraftDiscordLog2.json", "w")
                    file3.write(text2)
                    file3.close()
                else:
                    print(text2)
                    file4 = open("C:\Minecraft\MinecraftDiscord.json", "a")
                    file4.write(text2)
                    file4.close()
                    file3 = open("C:\Minecraft\MinecraftDiscordLog2.json", "w")
                    file3.write(text2)
                    file3.close()
            else:
                pass

            if text2[0] == "#":
                OldMSG2 = open("C:\Minecraft\MinecraftDiscordLog2.json", "r")
                OldMSG2 = OldMSG2.read()
                if text2 == OldMSG2:
                    pass
                elif text2 == OldMSG:
                    file3 = open("C:\Minecraft\MinecraftDiscordLog2.json", "w")
                    file3.write(text2)
                    file3.close()
                elif text2 == text:
                    file3 = open("C:\Minecraft\MinecraftDiscordLog2.json", "w")
                    file3.write(text2)
                    file3.close()
                else:
                    print(text2)
                    file4 = open("C:\Minecraft\MinecraftDiscord.json", "a")
                    file4.write(text2)
                    file4.close()
                    file3 = open("C:\Minecraft\MinecraftDiscordLog2.json", "w")
                    file3.write(text2)
                    file3.close()
        except:
            pass
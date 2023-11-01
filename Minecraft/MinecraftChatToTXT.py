from PIL import Image 
from pytesseract import pytesseract 
import pyscreenshot
import pyautogui
from time import sleep

Loop = 0

while Loop == 0:
        image = pyscreenshot.grab(bbox=(0, 885, 1895, 935))
        image.save("C:\Minecraft\Chat.png")


        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        image = "C:\Minecraft\Chat.png"

        # Opening the image & storing it in an image object 
        img = Image.open(image) 

        # Providing the tesseract executable 
        # location to pytesseract library 
        pytesseract.tesseract_cmd = path_to_tesseract 

        # Passing the image object to image_to_string() function 
        # This function will extract the text from the image 
        text = pytesseract.image_to_string(img) 
        img.close()

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
                    file2.write(text)
                    file2.close()
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
                    file2.write(text)
                    file2.close()
            else:
                pass

            if text[0] == "-" or "~" or "»":
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
                    file2.write(text)
                    file2.close()
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
                    file2.write(text)
                    file2.close()
        except:
            pass
    
    

    


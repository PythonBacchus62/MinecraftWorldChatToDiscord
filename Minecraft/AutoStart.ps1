#MinecraftServer Start
timeout(200)



Start-Process -FilePath "MinecraftStart.url" -WorkingDirectory "C:\Minecraft" 
timeout(35)
Start-Process -FilePath "AutoStart.py" -WorkingDirectory "C:\Minecraft"
timeout(6)
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait("%n{ENTER}")
timeout(20)
[System.Windows.Forms.SendKeys]::SendWait("%n{up}")
[System.Windows.Forms.SendKeys]::SendWait("%n{up}")
[System.Windows.Forms.SendKeys]::SendWait("%n{up}")
[System.Windows.Forms.SendKeys]::SendWait("%n{up}")
timeout(1)
[System.Windows.Forms.SendKeys]::SendWait("%n{down}")
[System.Windows.Forms.SendKeys]::SendWait("%n{down}")
timeout(1)
[System.Windows.Forms.SendKeys]::SendWait("%n{ENTER}")
timeout(30)
[System.Windows.Forms.SendKeys]::SendWait("%nt")
timeout(3)
[System.Windows.Forms.SendKeys]::SendWait("%n{/}setmaxplayers 99")
[System.Windows.Forms.SendKeys]::SendWait("%n{ENTER}")
timeout(5)
[System.Windows.Forms.SendKeys]::SendWait("%nt")
timeout(5)
Start-Process "C:\Minecraft\DiscordBot.py" -WindowStyle Hidden
timeout(1)
Start-Process "C:\Minecraft\MinecraftChatToTXT2.py" -WindowStyle Hidden

#MinecraftServer Start
sleep(100)


Start-Process "C:\Minecraft\MinecraftStart.url" -WindowStyle ([System.Diagnostics.ProcessWindowStyle]::Maximized)
sleep(25)
Start-Process "C:\Minecraft\AutoStart.py"
sleep(5)
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait("%n{ENTER}")
sleep(5)
[System.Windows.Forms.SendKeys]::SendWait("%n{up}")
[System.Windows.Forms.SendKeys]::SendWait("%n{up}")
[System.Windows.Forms.SendKeys]::SendWait("%n{up}")
[System.Windows.Forms.SendKeys]::SendWait("%n{up}")
sleep(1)
[System.Windows.Forms.SendKeys]::SendWait("%n{down}")
[System.Windows.Forms.SendKeys]::SendWait("%n{down}")
sleep(1)
[System.Windows.Forms.SendKeys]::SendWait("%n{ENTER}")
sleep(30)
[System.Windows.Forms.SendKeys]::SendWait("%n{t}")
sleep(5)
Start-Process "C:\Minecraft\DiscordBot.py"
sleep(1)
Start-Process "C:\Minecraft\MinecraftChatToTXT.py"


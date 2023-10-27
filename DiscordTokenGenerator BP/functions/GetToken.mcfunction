#GetToken
scoreboard objectives add DCToken dummy
execute @s ~ ~ ~ scoreboard players add @s DCToken 0
execute @s[scores={DCToken=0}] ~ ~ ~ execute @p ~ ~ ~ scoreboard players random @s DCToken 1000000 999999999
#Nachricht für die Person
execute @s[scores={DCToken=0}] ~ ~ ~ execute @p[scores={DCToken=1000000..}] ~ ~ ~ tellraw @s {"rawtext":[{"text":"§fDein DCToken: "},{"score":{"name":"@p[scores={DCToken=100000..}]","objective":"DCToken"}}]}
#Nachricht zum Logen vom Namen und DCToken
execute @s[scores={DCToken=0}] ~ ~ ~ execute @p[scores={DCToken=1000000..}] ~ ~ ~ tellraw @a[tag=ChatLog] {"rawtext":[{"text":"§f#"},{"selector":"@p[scores={DCToken=100000..}]"},{"text":"#"},{"score":{"name":"@p[scores={DCToken=100000..}]","objective":"DCToken"}}]}
#
execute @s ~ ~ ~ scoreboard players set @s DCToken 1
execute @s[scores={DCToken=1}] ~ ~ ~ kill @s

import discord
import asyncio
import os
import re
#---------------------#
import date_message
import jjambab_message
import on_mess
#---------------------#

client = discord.Client()

def set_embed(titles, descriptions):
    embeds = discord.Embed(title = titles, description = descriptions, color=0xff7b5c)
    embeds.set_footer(text = date_message.todayT)
    return embeds

##########################################################################

@client.event
async def on_ready():
    print("===================")
    print("현재 계정으로 로그인 합니다 : ")
    print(client.user.name)
    print(client.user.id)
    print("===================")
    game = discord.Game("RPC봇 테스트2")
    await client.change_presence(status=discord.Status.online, activity=game)

#########################################################################
    
@client.event
async def on_message(message):    
    
    if message.author == client.user:
        return
    
    if message.content.startswith("/오늘 짬밥"):
        await message.channel.send(embed=set_embed(jjambab_message.today_result, jjambab_message.todays_result))
        
    if message.content.startswith("/내일 짬밥"):        
        await message.channel.send(embed=set_embed(jjambab_message.tomorrow_result, jjambab_message.tomorrows_result))
        
    if message.content.startswith("/어제 짬밥"):
        await message.channel.send(embed=set_embed(jjambab_message.yesterday_result, jjambab_message.yesterdays_result))
        
    search_day = ""

        last_text = message.content
        result_day = re.findall("\d+", last_text)
        for result in result_day:
            search_day = result
        if message.content == "/%s일 짬밥"%search_day:
            test1, test2 = jjambab_message.search_jjambab(search_day)
            await message.channel.send(embed=set_embed(test1, test2))
        
#########################################################################

client.run("NjIwMTM3NTY0ODQxNTc0NDIx.XX3jVA.MDMGx1RSRGWHZnr-sF8mBHS-1GY")

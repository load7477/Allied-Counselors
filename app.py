import discord

import discord, datetime, json 
from discord.ui import InputText, Modal
from discord.commands import Option
from discord.ui import Button, View, Select
import asyncio
intents = discord.Intents.all()
client = discord.Bot(intents=intents)

channel_list = []

@client.event
async def on_message(message):
    if message.author.id == 1011179276667715625 or message.author.id == 951480609111433326 or message.author.id == 837963769098928169 or message.author.id == 345030969465503744 or message.author.id == 992666738762207232 or message.author.id == 744769990909231226 or message.author.id == 521146543437250562 or message.author.id == 290344037557469197:
        if message.content == '!문의종료':
            await message.channel.delete()

    if message.channel.id in channel_list:
        name = message.channel
        user = await client.fetch_user(f"{name}")
        if message.author.id == int(1072106847747702814):
            return
        else:
            await user.send(embed=discord.Embed(color=0x5865F2, title=f"Allied Counselors", description=f"{message.content} \n> <@{message.author.id}>**"))

    if isinstance(message.channel, discord.channel.DMChannel):
        guild = client.get_guild(int(1072105965442314250))
        # if not user.bot:
        if message.author.id == int(1072106847747702814):
            return
        else:
            for server in guild.categories:
                for channel in server.channels:
                    if f'{message.author.id}' in channel.name:
                        channel = client.get_channel(channel.id) #channel id here
                        if message.content == '@everyone' or message.content == '@here':
                            await channel.send('**문의자가 에브리원 혹은 here을 사용 했습니다.**')
                        else:
                            await channel.send(f'{message.author} : {message.content}')
                        return  
            main_view = View()
            main_view.add_item(Button(label="니트로 구매", style=discord.ButtonStyle.primary, custom_id="nitro"))
            main_view.add_item(Button(label="랜덤 계정", style=discord.ButtonStyle.primary, custom_id="randomaccount"))
            main_view.add_item(Button(label="기타 구매", style=discord.ButtonStyle.primary, custom_id="gita"))
            main_view.add_item(Button(label="기타문의", style=discord.ButtonStyle.primary, custom_id="counselors"))
            main_view.stop()
            await message.author.send("",embed=discord.Embed(color=0x5865F2, title="문의 버튼", description="문의사항을 선택해주세요"), view=main_view)

@client.listen("on_interaction")
async def on_interaction(interaction):
    if not interaction.is_component():
        return
    if not interaction.data["component_type"] == 2:
        return
    custom_id = interaction.data["custom_id"]
    
    if custom_id == "nitro":
        guild = client.get_guild(int(1072105965442314250))
        cat = discord.utils.get(guild.categories, name="구매-니트로")
        channel = await guild.create_text_channel(f'{interaction.user.id}', category=cat)
        await channel.send(f"@everyone \n> 문의가 도착 했습니다 - <@{interaction.user.id}>")
        await interaction.response.send_message('문의를 시작 합니다.')
        channel_list.append(channel.id)
    elif custom_id == "randomaccount":
        guild = client.get_guild(int(1072105965442314250))
        cat = discord.utils.get(guild.categories, name="구매-랜계")
        channel = await guild.create_text_channel(f'{interaction.user.id}', category=cat)
        await channel.send(f"@everyone \n> 문의가 도착 했습니다 - <@{interaction.user.id}>")
        await interaction.response.send_message('문의를 시작 합니다.')
        channel_list.append(channel.id)
    elif custom_id == "gita":
        guild = client.get_guild(int(1072105965442314250))
        cat = discord.utils.get(guild.categories, name="구매-기타")
        channel = await guild.create_text_channel(f'{interaction.user.id}', category=cat)
        await channel.send(f"@everyone \n> 문의가 도착 했습니다 - <@{interaction.user.id}>")
        await interaction.response.send_message('문의를 시작 합니다.')
        channel_list.append(channel.id)
    elif custom_id == "counselors":
        guild = client.get_guild(int(1072105965442314250))
        cat = discord.utils.get(guild.categories, name="문의")
        channel = await guild.create_text_channel(f'{interaction.user.id}', category=cat)
        await channel.send(f"@everyone \n> 문의가 도착 했습니다 - <@{interaction.user.id}>")
        await interaction.response.send_message('문의를 시작 합니다.')
        channel_list.append(channel.id)
        
client.run("")

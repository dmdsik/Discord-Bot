import requests
import discord
import asyncio
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
 
client = discord.Client()
 
token = "" #your token
async def on_ready():
 
    print("=========================")
    print("다음으로 로그인 합니다 : ")
    print(client.user.name)
    print("connection was successful")
    game = discord.Game("롤 전적검색")
    print("=========================")
    await client.change_presence(status=discord.Status.online, activity=game)
    
@client.event
async def on_message(message):
 
    if message.content.startswith('!티어'):
 
        Name = message.content[4:len(message.content)]
 
        if Name == "":
            await message.channel.send("닉네임을 입력해주세요.")
        else:
            print(Name)
 
            req = requests.get('http://www.op.gg/summoner/userName='+Name)
            print(req)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
 
            SoloRank = soup.find_all('div', {'class': 'TierRank'})
            SoloRank2 = str(SoloRank[0])[str(SoloRank[0]).find('TierRank">') + 10:str(SoloRank[0]).find('</div>')]
 
            Rank_Side = soup.find_all('div', {'class':'SideContent' })
            
            print(len(SoloRank2))
 
            for side in Rank_Side:
                img = side.find('img')
                img_src = 'https:'+img['src']
            
            if len(SoloRank2) > 35:
                embed_default = discord.Embed(title="롤 전적검색", description="op.gg 를 활용한 전적 검색 봇입니다", color=0xd5d5d5)
                embed_default.add_field(name="닉네임:  "+Name, value="Unranked", inline=False)
                embed_default.set_thumbnail(url=img_src)
                embed_default.set_footer(text='CuriHuS LAB')
                await message.channel.send(embed=embed_default)
 
            else:
 
 
                SoloRank_LP = soup.find_all('span', {'class' : 'LeaguePoints'})
                SoloRank_LP2 = str(SoloRank_LP[0])[str(SoloRank_LP[0]).find('">') + 3:str(SoloRank_LP[0]).find('</span>')]
 
                # Embed 메시지 구성
                embed = discord.Embed(title="롤 전적검색", description="op.gg 를 활용한 전적 검색 봇입니다", color=0xd5d5d5)
                
                print(SoloRank_LP)
                embed.add_field(name="닉네임:  "+Name, value=SoloRank2+" | "+SoloRank_LP2, inline=False)
                embed.set_thumbnail(url=img_src)
                embed.set_footer(text='CuriHuS LAB')
 
 
                # 메시지 보내기
                await message.channel.send(embed=embed)
 
client.run('ODkwOTQwNjU0MDU2NzkyMDc0.YU3HJA.9UeBqmWFMq02HA9dfL9a05cAEsc')
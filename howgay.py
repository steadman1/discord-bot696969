import discord
from discord.ext import commands
import random
import requests
import lyricsgenius
from googleapiclient.discovery import build
#import mysql.connector

token = 'NzQ0NzQ4MjMyNjEzMjk4MjM3.Xznu1w.FSdJK1n37vLzHjFF1392JSEL330'
geniuskey = '6GnBDMiZ71DMMqyRfAAhC_s9ZB7Komb8u70r1azwe_-lg5seqnst0ikhucM7o1vA'
api_key = "AIzaSyByLjYL5_LLN1_FhS156RDPaDQRPz1A_rA"
api_cx = "450a74360128e4ecb"
youtube = build('youtube', 'v3', developerKey=api_key)
client = discord.Client()

good_fifty = {
    "1":["cool clouds in new zeland", "https://allthatsinteresting.com/wordpress/wp-content/uploads/2013/09/interesting-pictures-asperatus-clouds.jpg"],
    "2":["heat map of all mcdonalds in america", "https://allthatsinteresting.com/wordpress/wp-content/uploads/2013/09/interesting-pictures-mcdonalds-in-america.jpg"],
    "3":["behind a rainbow frozen waterfall", "https://allthatsinteresting.com/wordpress/wp-content/uploads/2013/09/interesting-pictures-frozen-waterfall.jpg"],
    "4":["the \"edge of the earth\"", "https://allthatsinteresting.com/wordpress/wp-content/uploads/2013/09/interesting-pictures-end-of-the-earth.jpg"],
    "5":["black and white picture of a rocket launch", "https://cdn.pocket-lint.com/r/s/1200x/assets/images/148556-cameras-feature-some-of-the-most-interesting-events-in-history-in-photographs-image1-anxrwueqpv.jpg"],
    "6":["a turtle house", "https://media.funalive.com/article/images/Funny-Interesting-Photos-s1-19.jpg"],
    "7":["calming japanese lake and shrine", "https://worldstrides.com/wp-content/uploads/2015/07/iStock_000057240506_Large.jpg"],
    "8":["360 picture of a mars landscape", "https://www.thesun.co.uk/wp-content/uploads/2020/03/NINTCHDBPICT000568497172.jpg"],
    "9":["minion meme for boomers", "https://i.pinimg.com/originals/4e/1d/ac/4e1dac19e13e65d72095115750629430.jpg"],
    "10":["epic minceraft landscape", "https://i.imgur.com/B5QGgs9.jpg"],
    "11":["mt yosemite landscape", "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSa86OnV6mpPlR1p-eaL0hDM4QW50LdGp_M2A&usqp=CAU"],
    "12":["that one picture of pewdiepie that everyone uses", "https://static01.nyt.com/images/2019/03/15/world/15xp-pewdiepie/15xp-pewdiepie-videoSixteenByNineJumbo1600.jpg"],
}

bad_fifty = {
    "1":["spider egg sacs", "https://www.ridmycritters.com/wp-content/uploads/how-to-get-rid-of-spider-eggs.jpg"],
    "2":["1000s of tiny spiders", "https://i.cbc.ca/1.3042655.1429644431!/fileImage/httpImage/image.jpg_gen/derivatives/16x9_780/spider-video.jpg"],
    "3":["plate of intestines", "https://pickytop.com/wp-content/uploads/2020/02/gross-foods.jpg"],
    "4":["sausage jello", "https://www.awesomeinventions.com/wp-content/uploads/2018/03/sausage-jelly-horrible-looking-foods.jpg"],
    "5":["dog biting a wooden statue", "https://dailylolpics.com/wp-content/uploads/2018/03/photos-2-20.jpg"],
    "6":["two horny dogs", "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTvwuCke36veKPiqJ8LH5VD2HCLU8B8m0n9hg&usqp=CAU"],
    "7":["life like lego head", "https://cdn.guff.com/site_0/media/31000/30974/items/6b2e295a9377cb90644a0371.jpg"],
    "8":["face with moving holes", "https://i.gifer.com/86Dc.gif"],
    "9":["sauced up banana", "https://img.buzzfeed.com/buzzfeed-static/static/2017-04/3/4/campaign_images/buzzfeed-prod-fastlane-03/19-disturbing-food-pictures-thatll-make-you-feel--2-11007-1491207444-12_dblbig.jpg"],
    "10":["Frat house door", "https://img.buzzfeed.com/buzzfeed-static/static/2019-01/3/15/campaign_images/buzzfeed-prod-web-03/15-dark-and-disturbing-pictures-from-inside-an-am-2-24202-1546547742-5_dblbig.jpg"],
    "11":["foot", "https://img.buzzfeed.com/buzzfeed-static/static/2019-01/2/14/campaign_images/buzzfeed-prod-web-02/17-of-the-most-disturbing-photos-ever-to-be-dredg-2-5032-1546457771-3_dblbig.jpg"],
    "12":["zombie + human 😳", "https://cdn3.whatculture.com/images/2020/03/264e00c07634340d-1200x675.jpg"],
    "13":["mickey mouse", "https://i.chzbgr.com/full/9205753088/h094A89B4/hat"],
}

@client.event
async def on_message(message):
    global rv1, rv2, rv3
    if message.author == client.user:
        return

    if message.content.startswith("!5050"):
        rv2 = random.randint(1, len(good_fifty))
        rv3 = random.randint(1, len(bad_fifty))
        await message.channel.send(embed=discord.Embed(color=0x3AF943).add_field
        (name="🤮  Fifty fifty  🤔", value=f"**[50/50]** {good_fifty[str(rv2)][0]} **||** {bad_fifty[str(rv3)][0]}\n\ntype *accept* to accept the **[50/50]**", inline=False))
    
    if message.content.startswith("accept"):
        rv1 = random.randint(0, 2)
        if rv1 == 0:
            await message.channel.send(good_fifty[str(rv2)][1])
        elif rv1 == 1:
            await message.channel.send(bad_fifty[str(rv3)][1])
        else:
            rv1_ = random.randint(0, 2)
            if rv1_ == 0:
                await message.channel.send(good_fifty[str(rv2)][1])
            elif rv1_ == 1:
                await message.channel.send(bad_fifty[str(rv3)][1])

    if message.content.startswith("!gay"):
        gayness = random.randint(0, 100)
        emoji = ""

        if message.author.id == 659824380259467297:
            gayness = random.randint(0, 20)

        if gayness >= 80:
            emoji = "🏳️‍🌈 💦 🏳️‍🌈"
        elif gayness >= 60:
            emoji = "🌈 🍭"
        elif gayness >= 40:
            emoji = "👫 + 🌈"
        elif gayness >= 20:
            emoji = "🙅‍♂️ 🏳️‍🌈 🙅‍♀️"
        elif gayness >= 0:
            emoji = "❌ 🏳️‍🌈 👩‍❤️‍👨"

        await message.channel.send(embed=discord.Embed(color=0x3ABCF9).add_field
        (name="📡  How gay are you?  🏳️‍🌈", value=f"{message.author.mention} is {gayness} percent gay {emoji}", inline=False))
    
    if message.content.startswith("!search4"):
        search_term = message.content[10:]
        query = requests.get(f"https://customsearch.googleapis.com/customsearch/v1?cx={api_cx}&q={search_term}&searchType=image&key={api_key}")       
        link = query.json()["items"][0]["link"]
        await message.channel.send(link)

    if message.content.startswith('!youtube'):
        searchterm = message.content[7:]
        request = youtube.search().list(q=searchterm, part='snippet', type='video')
        searchyt = request.execute()
        videotitle = searchyt['items'][0]['snippet']['title']
        videoid = searchyt['items'][0]['id']['videoId']
        videolink = 'https://www.youtube.com/watch?v='+videoid+'/'
        await message.channel.send('🔎 '+videotitle+' 🔎'+'\n'+ videolink)
    
    if message.content.startswith("!cock") or message.content.startswith("what's my cock rating"):
        cock_num = random.randint(0, 250)
        message_ = "an error occured"

        #if message.author.id == 659824380259467297:
            #gayness = random.randint(0, 20)

        if cock_num <= 100:
            message_ = ", its ok someone has to come last 🤷 🥉, especially with only **1.5 inches**"
        elif cock_num <= 160:
            message_ = ", hey squirt, **4 inches** isnt too horrible 😃"
        elif cock_num <= 200:
            message_ = ", woah thats a decent **6 inch** cock 👍"
        elif cock_num <= 226:
            message_ = ", woah, nice **8 inch** cock bro 🍆 🏆"
        elif cock_num <= 236:
            message_ = ", god damn, thats a nice **12 inch** shlong 😳"
        elif cock_num <= 244:
            message_ = ", woah 😳, is your dad a horse or something 🥵"
        elif cock_num <= 249:
            message_ = ", wow, thats **18 inch** horse cock if ive ever seen one 🍆 🐎 🥵"
        elif cock_num <= 250:
            message_ = ", thats a **3 foot** gorilla cock right there 😵 🦍"

        await message.channel.send(embed=discord.Embed(color=0xF98E3A).add_field
        (name=f"❔ How long is your shlong?  🍆", value=message.author.mention + message_, inline=False))
    
    if message.content.startswith('!lyrics'):
        songName=message.content[8:]
        api=lyricsgenius.Genius(geniuskey)
        artist=api.search_song(songName)
        try:
            await message.channel.send(embed=discord.Embed(title=(artist.title), description=(artist.lyrics[:1600]), color=0x32CD32))
            await message.channel.send(embed=discord.Embed(title='', description=(artist.lyrics[1600:]), color=0x32CD32))
        except:
            await message.channel.send()


    if message.content.startswith("!command") or message.content.startswith("!cmd"):
        await message.channel.send(embed=discord.Embed(color=0x1b1b1b).add_field
        (name="📝Current bot commands for Howgay? 🤖\n\n", 
        value="\n** !Gay** how gay am i? 🏳️‍🌈\n\n** !Cock** for a cock rating? 🍆\n\n**!Search4** [search term] for a google image search 🔍\n\n**!Lyrics** [song name] for lyrics 🎵\n\n**!YouTube** [video title or channel name] for a YouTube link 🔴⚪\n\n**!5050** for a choice 🤔", 
        inline=False))
    '''
    if message.content.startswith("cockmarket.help"):
        await message.channel.send(embed=discord.Embed(color=0x3ABCF9).add_field
        (name="Cockmarket Help", value="\nThe **Cockmarket** is a virtual market place to buy and sell cock points. Cockpoints are universal forms of currency that can be used to authority and power in a server. The more cockpoints you can get determines your cock level! Have fun 😃 ! ", inline=False))
    '''

@client.event
async def bruh():
    pass

@client.event
async def on_ready():
    #mydb = mysql.connector.connect(
        #host = "127.0.0.1",
        #user = "s_steadman",
        #password = "LiNu$420_69"
    #)

    #print(mydb)
    print(f"ready, logging as howgay?")

client.run(token)
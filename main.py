import discord
import json
import requests
from discord.ext import commands
import config
import random
from bs4 import BeautifulSoup
bot=commands.Bot(command_prefix=config.prifix)
bot.remove_command('help')
Ban_word=["пидар","негар","даун",'куколд','рома помоги','уголек','копченый','мавр','мавра','арап','афроамериканец',
          'афроамериканец',          'эфиоп','трюфель','черномазый','негативчик','мумба-юмба','макачи','макач',
          'макакать','мурин','негроид','темноягодичный','нигер','афронегр',
          'афророссиянин','прогнат','негритос','евгений','редька','жень','женьдосина','гандон',
          'ィスpainスィ hate clown','zxczxczxc blood tears 牡no brain牡','ナtiltedナ 8 y.o. ルanti socialル','женьшень',
          'антон','женя','жень-шень','женьшень','черножопый']
Helprer=["help","помощь","хелп"]
Hello_word=['hi','привет','ку']
def parsing_image(link):
    response = requests.get(link)  # Get-запрос
    json_data = json.loads(response.text)  # Извлекаем JSON
    return json_data
@bot.command()
async def dog(ctx):
    image=parsing_image('https://some-random-api.ml/img/dog')
    embed = discord.Embed(color=0xff9900, title='Random Maks')
    embed.set_image(url= image['link'])
    embed.add_field(name="Великая цитата Максима",value=config.cit[random.randint(0,4)])
    await ctx.send(embed=embed)

    
@bot.command()
async def panda(ctx):
    image = parsing_image('https://some-random-api.ml/img/panda')
    embed = discord.Embed(color=0xff9900, title='Random Anton')
    embed.set_image(url= image['link'])
    await ctx.send(embed=embed)



@bot.command()
async def mem(ctx):
    image = parsing_image('https://some-random-api.ml/meme')
    embed = discord.Embed(color=0xff9900, title='Mem')
    embed.set_image(url= image['image'])
    await ctx.send(embed=embed)




@bot.event
async def on_member_join(member):
    if role := member.guild.get_role(785517372123119617):
        await member.add_roles(role)


@bot.event
async def on_command_error(ctx,error):
    await ctx.send("Такой команды нет")
    pass

@bot.command()
async def Roma(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.author.kick()
    await ctx.send(f"Good leave  {ctx.author.name}")
@bot.command()
async def roll(ctx,amount=100):
    await ctx.send(random.randint(0,amount))



@bot.command()
async def flip(ctx):
    bc=random.randint(0,1)
    if bc==0:
        await ctx.send("You lose")
    else:
        await ctx.send("You win")



def parcing(link):
    kek = requests.get(link).text
    soup = BeautifulSoup(kek, 'lxml')
    block = soup.find('div', {'class': 'anekdot-content'}).find('p').text
    return block



@bot.command()
async def Anek(ctx):
    block =parcing('https://anekdot-z.ru/random-anekdot')
    await  ctx.send(block)




@bot.event
async  def on_ready():
    await bot.change_presence(status=discord.Status.online,activity=discord.Game("Защищает ваше ОЧко"))




def random_message_ban_word():
    judge_word=["Запрещенку пишешь не стыдно,Мой батя осуждает вас",'Ты что очушуел',
                "Наруто это круто","Антон вас побьёт"]
    amount=len(judge_word)
    return judge_word[random.randint(0,amount-1)]





def random_hi():
    hi=['hi bro','Привет Медвед','КУ ку','Кин зан за']
    amount=len(hi)
    return hi[random.randint(0,amount-1)]




@bot.event
async def on_message(mes):
    await bot.process_commands(mes)
    channel_id =mes.channel
    channel = bot.get_channel(channel_id)
    msg=mes.content.lower()
    if msg in Ban_word:
        await mes.author.send(random_message_ban_word())
    if msg in Helprer:
        await mes.channel.send("Веди команду !help для дальнейших вывода доступных команд")
    if msg in Hello_word:
        await mes.channel.send(random_hi())


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx,amount=100):
    await ctx.channel.purge(limit=amount)


@bot.command()
async def send_mem(ctx,mem:discord.Member):
    await mem.send(f"Are you axyet:{mem.name} ")



@bot.command(pass_contest=True)
@commands.has_permissions(administrator=True)
async def ban(ctx,member:discord.Member,*,reason = None):
    evb=discord.Embed(name="Ban",color=discord.Color.red())
    await ctx.channel.purge(limit=1)
    await member.ban(reason=reason)
    evb.set_author(name=member.name,icon_url=member.avatar_url)


@bot.command(pass_contest=True)
@commands.has_permissions(administrator=True)
async def kick(ctx,member:discord.Member,*,reason = None):
    await ctx.channel.purge(limit=1)
    await member.kick(reason=reason)
    await ctx.send("good buy bro")

@bot.command()
async def Bull(ctx,mem:discord.Member):
    await mem.send(f"Are you axyet:{mem.name} ")



@bot.command(pass_contest=True)
async def help(ctx):
    emb=discord.Embed(title="Cписок комманд",color=discord.Color.dark_grey())
    emb.add_field(name='{}clear'.format("."), value="Очистка чата\n")
    emb.add_field(name='{}dog'.format("."), value="Фото максима в цвете\n")
    emb.add_field(name='{}mem'.format("."), value="Random mem\n")
    emb.add_field(name='{}Roma'.format("."), value="Cамая сильная доступная команда\n")
    emb.add_field(name='{}Anek'.format("."), value="Бот рассказывает анекдот\n")
    emb.add_field(name='{}Bull'.format("."), value="Быкануть от имени бота\n")
    emb.add_field(name='{}panda'.format("."), value="Random picture Panda")
    emb.add_field(name='{}roll'.format("."), value="Random digit\n")
    emb.add_field(name='{}flip'.format("."), value="Орел и Решка\n")
    await ctx.send(embed=emb)
bot.run(config.token)

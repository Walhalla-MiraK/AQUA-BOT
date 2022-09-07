import discord
from discord.utils import get
from discord.ext import commands
from Config import badwords , token  #spamcristy


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

        await client.change_presence( status= discord.Status.online, activity=discord.Game('.Help') )
    async def on_message(self, message ,):
        # don't respond to ourselves
        

        if message.author == self.user:
            return

        if message.content == '.Help':
            await message.author.send('Вот все навигационные команды в скоре мы добавим больше\n> **!Дизайн** \n> **!Оптимизация** \n> **!Вбаксы** \n> **!Разбан** \n> **!ДСНитро** . {0.author.mention}'.format(message))

        if message.content == '!Дизайн':
            await message.author.send('**Графический дизайн по низким ценам.** \n В категориях <#1007226993407954954> & <#1011963917494386748> можно приобрести услуги. \n <#1007227029051166830> - Лучшие работы клиентов. \n <#1007163662533918740> - Отзывы о услугах дизайна\n Так же что бы оплатить услугу пишите \n**!Оплата услуг**.{0.author.mention}'.format(message))

        if message.content == '!Оптимизация':
            await message.author.send('**Настройка вашего пк на лучшую производительность** \n > В категории <#1006131580290474025> можно приобрести услугу.\n > <#1007163634390143076> - Отзывы о услугах настройки пк\n Так же что бы оплатить услугу пишите \n**!Оплата услуг**.{0.author.mention}'.format(message))
        
        if message.content == '!Вбаксы':
            await message.author.send('**Приобритение внутриигровой валюты в фортнайт.** \n> В категории <#1009053849694257233> можно приобрести услугу. \n> <#1009053884318232597> - Отзывы о услуге \n Так же что бы оплатить услугу пишите \n**!Оплата услуг**.{0.author.mention}'.format(message))
        
        if message.content == '!Разбан':
            await message.author.send('**Данная услуга <#1016339025575026760> поможет снять вам бан аккаунта фортнайт в эпик геймс** \n<#1016339052791861329> - **отзывы услуги**\n Так же что бы оплатить услугу пишите \n**!Оплата услуг**. {0.author.mention}'.format(message))
        
        if message.content == '!ДСНитро':
            await message.author.send('**Здесь вы можете приобрести услуги <#1016033261224472709> по покупке Дискорд нитро на определенное кол-во бустов** \n<#1016033298989989929> - **отзывы об услуге** \n Так же что бы оплатить услугу пишите \n**!Оплата услуг**. {0.author.mention}'.format(message))

        if message.content == '!Оплата услуг':
            await message.author.send("Принимаються карты от : **Qiwi \ Сбербанк \ Тинькофф **\n**Вот номера карт** : **Сбер** : ||**2202203201821461**|| \ **Qiwi** : ||**GRONK**|| \ **Tinkoff** : ||**4377727818947645**|| \n**переведите туда деньги нужные для оплаты услуг и укажите в комментарии за что вы платите **\n**!и не забывайте предоставить скриншот @Gronk#4282**\n\n**Спасибо за покупку ждем вас снова \n\nтак же просмотрите другие услуги :heart:**") 

          
        if message.content in badwords:
            await message.delete()
            deleted = True
            

                      
        #if message.content in spamcristy:
        #    await message.channel.send('<@990574570627010560>')

        #if message.content in unknown_comnds:
        #    await message.channel.send('Я не знаю такой команды')

        
 
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)
#client.run('')


 #       if message.content == '':
 #           await message.channel.send('Графический дизайн по низким ценам. \n В категориях 💵│price & 📑│coaching можно приобрести услуги. \n ✅│works - Лучшие работы клиентов. \n📗│reviews - Отзывы о услугах дизайна.')
# if message.content == 'даун':
#            await message.channel.send('Можешь так не выражаться \n это предупреждение! \n если оно будте часто светиться в чате то модеры могут тебя забанить {0.author.mention}'.format(message))
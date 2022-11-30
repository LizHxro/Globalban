import json
import disnake
import requests as requests
from disnake.ext import commands, tasks
from disnake.ext.commands import LargeInt
import config


client = commands.Bot(command_prefix='.', intents=disnake.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    print('Ready')
    await client.change_presence(activity=disnake.Game(f'Join × .gg/botclapnet'), status=disnake.Status.do_not_disturb)

@client.event
async def on_member_join(member):
    rurl = f'http://panel.botclapnet.xyz/api/globalbans.php?userID={member.id}'

    x = requests.get(rurl)

    data = json.loads(x.text)
    reason = data['reason']

    if x.text == '0 results':
        pass
    else:
        try:
            await member.ban(reason=reason)
        except:
            pass

client.run('Token')

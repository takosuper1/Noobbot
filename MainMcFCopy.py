import discord
from discord.ext.commands import Bot



class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        server = client.get_server(id='505328088264212480')
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        if server:
            for member in server.members:
                print('name: {}'.format(member.name))
        else:
            print('any')

class Main(discord.Client):

    async def on_user_login(self, user):
        server = client.get_server(id='505328088264212480')
        if server:
            for member in server.members:
                print('name: {}'.format(member.name))
                client.send_message(user, 'Noob alert')
        else:
            print('any')


# This is our connection to the server (our bot's username). TOKEN is essentially the password.



client = MyClient()

server = client.get_server(id='505328088264212480')



    # await userID.status.online
    # if userID.status.online == True:
    #     client.send_message(userID, 'Welcome back!')





@client.event
async def on_message(message):

        if message.content.upper().startswith('!PING'):
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> Pong!" % userID)

        if message.content.upper().startswith('!SAY'):
            if message.author.id == "473457069673152513":
                args = message.content.split(" ")
                await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
            else:
                await client.send_message(message.channel, "You do not have permission")

        if message.content.upper().startswith('!AMIADMIN'):
            if "515643370396319773" in [role.id for role in message.author.roles]:
                await client.send_message(message.channel, "You are an admin")
            else:
                await client.send_message(message.channel, "You are not an admin")

        if message.content.upper() == 'NOOB':
            await client.send_message(message.channel, 'No, your mom.')




@client.event
async def on_user_login(member, server='505328088264212480', channel='505328088264212484'):
    await member.login
    for member.login in server:
        if member.id == "473457069673152513":
            client.send_message(channel, "You are a member of the elite")
            # await member.online
            # client.send_message(member, "Welcome Noob")
        else:
            print('fail')


discord.ext.commands.Bot(command_prefix='%')


client.run('NTA1MzIyNzQ3MjMzMDQyNDUy.DthGjQ.J9bzkdIEnoFuK3qD8kR66RegJWQ')
Main.run
# This block basically requires the Bot to tell us "Logged on as...." when it logs on to Discord server.
# Also enables the bot to post messages.

# First if statement of this block of code waits for the specific message '!ping' and responds back with
# the original author's handle and the word 'pong!' The <@%s> is a placeholder for the user specified after it.
# Second if statement of this block creates a command that requires the key '!say'. After that, the if in
# the next line looks for who is sending the command (me) to run the next code. Args can be any variable I want.
# Next to it formats the list created in the line after that by splitting each word into its own array. This is
# done to isolate the command from the rest of what is being typed.
# The following line awaits the user input from our channel and formats the message further by putting
# the words back together into one sentence in the reply via a list and the " ".join syntax.
# NOTE: [1:] instead of [0:] because we do not what the command word repeated in the response.
# Else response is for those who type the keyword by do not have the proper credentials to do so.
# Next if block is a check/verification if a person has admin privileges. Its tricky because there
# is a lot of setup on the Discord side that needs to be done first. This first line awaits a specific command.
# The next line I am unsure of the details about the syntax, but it is basically running a check with
# the Discord database to see if your userID matches under a specified role in Discord.
# Else statement triggers if there is no match.
# The next block of code that is triggered by an event that matches the lines inside it.
# All it is doing is scanning the server for when a person sends our bot a message ('noob').
# When it detects this event, it sends a message back.
# NOTE: Special syntax: message.content.upper() == 'NOOB'. the periods between the words seem to
# add specificity to the first word 'message', which is a defined variable. Also upper() == 'NOOB' allows
# the bot to scan for the event in a way that is not case sensitive.
# AWAIT is an important feature of ASYNC. Not sure if code works without it.

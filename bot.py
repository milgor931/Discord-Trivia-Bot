import discord
from discord.ext import commands
import requests
import json
import random

client = commands.Bot(command_prefix=("triv ","Triv "))

def getMathTrivia():
    url = "https://numbersapi.p.rapidapi.com/{}/math".format(random.randint(0,1000))

    querystring = {"fragment":"true","json":"true"}

    headers = {
        'x-rapidapi-key': "KEY",
        'x-rapidapi-host': "numbersapi.p.rapidapi.com"
        }

    response = json.loads(requests.request("GET", url, headers=headers, params=querystring).text)

    response['prompt'] = "What is "

    response['correct_answer'] = response['number']

    return response

def getRandomFact():
    url = "https://numbersapi.p.rapidapi.com/random/trivia"

    querystring = {"max":"20","fragment":"true","min":"10","json":"true"}

    headers = {
        'x-rapidapi-key': "KEY",
        'x-rapidapi-host': "numbersapi.p.rapidapi.com"
        }

    response = json.loads(requests.request("GET", url, headers=headers, params=querystring).text)

    response['prompt'] = "What is "

    response['correct_answer'] = response['number']

    return response

def getTriviaFact():
    url = "https://numbersapi.p.rapidapi.com/{}/trivia".format(random.randint(0,1000))

    querystring = {"fragment":"true","notfound":"floor","json":"true"}

    headers = {
        'x-rapidapi-key': "KEY",
        'x-rapidapi-host': "numbersapi.p.rapidapi.com"
        }

    response = json.loads(requests.request("GET", url, headers=headers, params=querystring).text)

    response['prompt'] = "What is "

    response['correct_answer'] = response['number']
    
    return response

def getYearFact():
    url = "https://numbersapi.p.rapidapi.com/{}/year".format(random.randint(0, 2000))

    querystring = {"fragment":"true","json":"true"}

    headers = {
        'x-rapidapi-key': "KEY",
        'x-rapidapi-host': "numbersapi.p.rapidapi.com"
        }

    response = json.loads(requests.request("GET", url, headers=headers, params=querystring).text)

    response['prompt'] = "In what year did "

    response['correct_answer'] = response['number']

    return response

options = {
    "math": getMathTrivia,
    "year": getYearFact,
    "trivia": getTriviaFact,
    "random": getRandomFact
}

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@client.command()
async def hello(message):
    await message.send("Hey there you cool person! Welcome to my trivia bot made especially to test your smarts! \nTo request a question, type \n   triv q OPTION\n The options include math, trivia, random, and year.\n Enjoy!")

@client.command()
async def admin(message):
    await message.send('Sorry this command is still being worked on!')


@client.command()
async def ping(message):
    await message.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def q(message, question):
    global res
    global options

    res = options[question]()

    print(res)

    await message.send(res['prompt'] + res['text'] + "\nWrite 'triv answer YOUR ANSWER'")

@client.command()
async def answer(message, a):
    global res
    if a == str(res['correct_answer']):
        await message.send("You are correct!")
    else:
        await message.send("Oop sorry bro")

client.run('TOKEN')

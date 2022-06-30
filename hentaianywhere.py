#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import telebot


try:
  token = open("token.txt", "r").read()
  bot = telebot.Telebot(token)
except FileNotFound:
  print("[-] Token file not found.")
  sys.exit(0)

@bot.message_handler(content_type=["text"])
def message_handler(message):
  if message.text == "/start":
    print("Хули ты здесь забыл?")
  

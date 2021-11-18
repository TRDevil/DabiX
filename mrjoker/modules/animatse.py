import asyncio
import io
import json
import os
import random
import re
import string
import subprocess
import textwrap
import urllib.request
from random import randint, randrange, uniform

import emoji
import nltk
from cowpy import cow
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from telethon import *
from telethon.tl import functions
from telethon.tl.types import *
from zalgo_text import zalgo

from mrjoker import *
from mrjoker.services.telethonuserbot import ubot

async def deepfry(img: Image) -> Image:
    colours = (
        (randint(50, 200), randint(40, 170), randint(40, 190)),
        (randint(190, 255), randint(170, 240), randint(180, 250)),
    )
    img = img.copy().convert("RGB")
    img = img.convert("RGB")
    width, height = img.width, img.height
    img = img.resize(
        (int(width ** uniform(0.8, 0.9)), int(height ** uniform(0.8, 0.9))),
        resample=Image.LANCZOS,
    )
    img = img.resize(
        (int(width ** uniform(0.85, 0.95)), int(height ** uniform(0.85, 0.95))),
        resample=Image.BILINEAR,
    )
    img = img.resize(
        (int(width ** uniform(0.89, 0.98)), int(height ** uniform(0.89, 0.98))),
        resample=Image.BICUBIC,
    )
    img = img.resize((width, height), resample=Image.BICUBIC)
    img = ImageOps.posterize(img, randint(3, 7))
    overlay = img.split()[0]
    overlay = ImageEnhance.Contrast(overlay).enhance(uniform(1.0, 2.0))
    overlay = ImageEnhance.Brightness(overlay).enhance(uniform(1.0, 2.0))
    overlay = ImageOps.colorize(overlay, colours[0], colours[1])
    img = Image.blend(img, overlay, uniform(0.1, 0.4))
    img = ImageEnhance.Sharpness(img).enhance(randint(5, 300))
    return img
  
  
@register(pattern="^/animate (.*)")
async def stickerizer(event):

    newtext = event.pattern_match.group(1)
    animus = [20, 32, 33, 40, 41, 42, 58]
    sticcers = await ubot.inline_query(
        "stickerizerbot", f"#{random.choice(animus)}{(deEmojify(newtext))}"
    )
    null = await sticcers[0].download_media(TEMP_DOWNLOAD_DIRECTORY)
    bara = str(null)
    await event.client.send_file(event.chat_id, bara, reply_to=event.id)
    os.remove(bara)
    
    __help__ = """
**Some memes command, find it all out yourself !**

 - /animate: Enwrap your text in a beautiful anime
 
 """
    
    __mod_name__ = "Animate"

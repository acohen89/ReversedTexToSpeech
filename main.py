# Import the required module for text 
# to speech conversion
import playsound
from gtts import gTTS


# This module is imported so that we can 
# play the converted audio
import os
  
print("Enter the sentence you wished to reversed")
input = input()
revered = ""

def reverseWord(word):
    ret = ""
    for i in range( len(word)):
        ret += word[len(word) - i - 1]
    return ret

def reverseSentence(input):
    ret = ""
    arr = input.split(' ')
    for word in arr:
        ret += reverseWord(word)  + " "
    return ret

print(reverseSentence(input))
# The text that you want to convert to audio
mytext = reverseSentence(input)
  
# Language in which you want to convert
language = 'en'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("reversed.mp3")
  
# Playing the converted file

playsound.playsound('reversed.mp3', True)
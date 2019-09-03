###IMPORTANT NOTICE###
#Only the English alphabets and numbers are converted by all current functional libraries

#import pyttsx3
from gtts import gTTS

#Load the Pandas libraries with alias 'pd'
import pandas as pd

#import os

#engine = pyttsx3.init()

#Read data from the file 'mnnvocab.csv'
#data = pd.read_csv('<Filename.csv>', engine='python, encoding='<asperfile>', nrows = <limit to rows within the .csv>)
data = pd.read_csv('busopssur.csv', engine='python', nrows=792)

#To set options temporarily
#pd.option_context(parameters for for display width, no. of rows&cloumns)
#'display.max_rows','display.max_columns are followed by None for displaying the 'n' Rows and Columns without mentioning max size
# with pd.option_context('display.width', 500, 'display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(data)

#engine used pttysx3 function say to convert text to speech.
#engine.say(data)

#Blocks while processing all currently queued commands. Invokes callbacks for engine notifications appropriately.
# Returns when all commands queued before this call are emptied from the queue.
#engine.runAndWait()



#Imperfect options that need a lot of polish
############
# with open('mnnvocab.csv', 'rt') as f:
#     data = csv.reader(f)
#     for row in data:
#         print("{}".format(row),"\n")

# text1 = list()
# text2 = list()
# text3 = list()

##### zip is used to map similar index of multiple containers for simultaneous use
# for a,b,c in zip(data['Japanese'], data['Japanese'], data['English']):
#     text1.append(a)
#     text2.append(b)
#     text3.append(c)
#
# print(text1, text2, text3)
#
# text1 = str(text1)
# text2 = str(text2)
# text3 = str(text3)
#
# tts1 = gTTS(text=text1, lang='jp')
# tts2 = gTTS(text=text2, lang='jp')
# tts3 = gTTS(text=text2, lang='en')
#
# with open('TEXSPH.mp3', 'wb') as fp:
#     tts1.write_to_fp(fp)
#     tts2.write_to_fp(fp)
#     tts3.write_to_fp(fp)
#
#
# os.system('from file.mp3')


#gTTS library functions to convert text to speech and create an mp3 file
tts = gTTS(text=data, lang_check='en')
tts.save('Hunter.mp3')

# engine = pyttsx3.init()
# engine.say(data)
# engine.runAndWait()
#################
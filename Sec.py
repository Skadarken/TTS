#import pyttsx3
import csv

from gtts import gTTS

#Load the Pandas libraries with alias 'pd'
import pandas as pd
import os
#engine = pyttsx3.init()

#Read data from the file 'mnnvocab.csv'
#data = pd.read_csv('<Filename.csv>', engine='python, encoding='<asperfile>', nrows = <limit to rows within the .csv>)
data = pd.read_csv('mnnvocab.csv', engine='python', encoding='utf-8', nrows=792)

#To set options temporarily
#pd.option_context(parameters for for display width, no. of rows&cloumns)
#'display.max_rows','display.max_columns are followed by None for displaying the 'n' Rows and Columns without mentioning max size
with pd.option_context('display.width', 500, 'display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
     print(data)

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

data = gTTS(text=data, lang='jp')

#gTTS library functions to convert text to speech and create an mp3 file
####tts = gTTS(text=data, lang_check='en,jp')
tts.save('Hunter.mp3')

# engine = pyttsx3.init()
# engine.say(data)
# engine.runAndWait()
#################
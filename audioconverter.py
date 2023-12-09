from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
mytext="In summary, Denmark's media landscape operates within a commercial framework, providing comprehensive coverage during elections, contributing to national issues, and embracing digital transformation and convergence. While Danish media have played a crucial role in countering conspiracy theories, they are not immune to criticism, which is a natural part of media in a democratic society."
# Language in which you want to convert
language = 'en'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("ppt35.mp3")


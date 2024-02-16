#yPDF2 is a free and open-source pure-python 
# pip install PyPDF2
# PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files


#pyttsx3 is a text-to-speech conversion library in Python


#pip install pyttsx3


import PyPDF2

import pyttsx3

pdfReader = PyPDF2.PdfReader(open('dummypdf.pdf', 'rb'))

#######CASE 1 PDF READ
# Initialize the Pyttsx3 engine

speaker = pyttsx3.init()

for page_num in range(len(pdfReader.pages)):
    text =  pdfReader.pages[page_num].extract_text()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()



speaker.save_to_file(text, 'audio.mp3')

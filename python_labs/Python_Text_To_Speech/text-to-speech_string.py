import PyPDF2

import pyttsx3

####CASE 2 READ A STRING ###########
# Create a string
string = "Lorem Ipsum is simply dummy text " \
    + "of the printing and typesetting industry."

# Initialize the Pyttsx3 engine
engine = pyttsx3.init()

# We can use file extension as mp3 and wav, both will work
engine.save_to_file(string, 'speech.mp3')

# Wait until above command is not finished.
engine.runAndWait()

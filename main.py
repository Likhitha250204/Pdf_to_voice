#PDF to Audio(Mini Project)
import pyttsx3
from PyPDF2 import PdfReader
from tkinter.filedialog import askopenfile

# To Select PDF
book = askopenfile(mode='rb')

# Creating reader
reader = PdfReader(book)

# Initialize speech engine
engine = pyttsx3.init()

# For Looping through pages
for page in reader.pages:
    text = page.extract_text()
    if text:
        engine.say(text)

engine.runAndWait()

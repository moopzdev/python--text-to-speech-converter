from tkinter import *
from gtts import gTTS


def _convert():
    print("Its being converted")
    inputted_text = text_entry.get()
    language = 'en'
    speech = gTTS(text=inputted_text, lang=language, slow=False)
    speech.save("sound.mp3")


root = Tk()
root.title("Text to Speech Converter")
canvas = Canvas(root, width=400, height=300)
canvas.pack()

app_label = Label(text="Convert Text to Speech", font=("Courier", 20, "bold"))
canvas.create_window(200, 100, window=app_label)

text_entry = Entry(root)
canvas.create_window(200, 180, window=text_entry)

button = Button(text="Convert to Speech", command=_convert)
canvas.create_window(200, 230, window=button)
root.mainloop()

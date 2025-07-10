from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os

# Initialize the main window
root = Tk()
root.geometry("1080x500")
root.resizable(0, 0)
root.title("Language Translator")
root.config(bg="#000000")


def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)


def translate_now():
    translator = Translator()
    try:
        text_ = text1.get(1.0, END)
        src_lang = combo1.get()
        dest_lang = combo2.get()
        if text_:
            translated = translator.translate(text_, src=src_lang, dest=dest_lang)
            text2.delete(1.0, END)
            text2.insert(END, translated.text)
    except Exception as e:
        messagebox.showerror(
            "Translation Error", "Translation failed, please try again.\n" + str(e)
        )


def text_to_speech():
    translated_text = text2.get(1.0, END).strip()
    if translated_text:
        dest_lang = combo2.get()
        lang_code = get_language_code(dest_lang)
        if lang_code:
            tts = gTTS(text=translated_text, lang=lang_code)
            tts.save("translated_audio.mp3")
            os.system(
                "start translated_audio.mp3"
            )  # use "xdg-open" on Linux or "open" on macOS
        else:
            messagebox.showerror(
                "Language Error", f"Language not supported for speech: {dest_lang}"
            )
    else:
        messagebox.showwarning("No Text", "There is no text to convert to speech!")


def get_language_code(language_name):
    for code, name in LANGUAGES.items():
        if name.lower() == language_name.lower():
            return code
    return None


# Load icon image (make sure these files are in the same folder)
try:
    image_icon = PhotoImage(file="icon.png")
    root.iconphoto(False, image_icon)
except Exception:
    pass

# Load arrow image
try:
    arrow_image = PhotoImage(file="arrowff.png")
    image_label = Label(root, image=arrow_image, width=70, height=70)
    image_label.place(x=510, y=40)
except Exception:
    pass

# Languages and combobox setup
language = LANGUAGES
languageV = list(language.values())

combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo1.place(x=110, y=40)
combo1.set("english")

label1 = Label(
    root,
    text="English",
    font="segoe 30 bold",
    bg="#cfd0d4",
    width=13,
    bd=4,
    relief=GROOVE,
)
label1.place(x=70, y=80)

f = Frame(root, bg="grey", bd=5)
f.place(x=30, y=150, width=410, height=210)

text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=400, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo2.place(x=730, y=40)
combo2.set("Select Language")

label2 = Label(
    root,
    text="Select Language",
    font="segoe 30 bold",
    bg="#cfd0d4",
    width=13,
    bd=4,
    relief=GROOVE,
)
label2.place(x=690, y=80)

f1 = Frame(root, bg="grey", bd=5)
f1.place(x=640, y=150, width=410, height=210)

text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=400, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate button
translate = Button(
    root,
    text="Translate",
    font="Roboto 15 bold italic",
    activebackground="green",
    cursor="hand2",
    bd=5,
    width=7,
    bg="red",
    fg="white",
    command=translate_now,
)
translate.place(x=480, y=300)

# Text-to-Speech button
speech_button = Button(
    root,
    text="Speak",
    font="Roboto 15 bold italic",
    width=7,
    activebackground="green",
    cursor="hand2",
    bd=5,
    bg="blue",
    fg="white",
    command=text_to_speech,
)
speech_button.place(x=480, y=400)

label_change()

# Main loop
root.mainloop()

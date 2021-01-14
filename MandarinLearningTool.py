# Author: Jacob Cho
# January 11, 2021

# after installing packages, import all APIs and Packages
from googletrans import Translator
import tkinter as tk
from PIL import ImageTk, Image
import pinyin
import gtts
from playsound import playsound
from PyDictionary import PyDictionary
import textwrap

# setting up the GUI window
root = tk.Tk()
root.geometry("1440x850")
root.title("Project Prototype")


# open, size, and rename the volume button image file
img = Image.open('volume_button.png')
real_img = img.resize((90, 60))
volume_image = ImageTk.PhotoImage(real_img)

# open, size, and rename the language switch image file
img = Image.open('switch_arrow.png')
real_img = img.resize((100, 90))
switch_image = ImageTk.PhotoImage(real_img)

# setting a specific service url(the alpha version) for the google trans API and renames the object
translator = Translator(service_urls=['translate.googleapis.com'])

# initialize the PyDictionary library to be called upon the dictionary object creation(creates a dictionary instance)
dictionary = PyDictionary()


# by clicking on the arrow button, it will flip the subheadings to change the input/output language. It uses config to
# updates the subheading labels using config for each scenarios(if statement determines current language setup)


def switch_lang():
    if english_sub_header['text'] == "English":
        english_sub_header.config(text="Mandarin", font="Times 38")
        mandarin_sub_header.config(text="English", font="Times 38")
        function1_label.config(text="Enter the Mandarin word/sentence: ", font="Symbol 20", fg="#242424")
        function2_label.config(text="The English translation is: ", font="Symbol 20", fg="#242424")

    elif english_sub_header['text'] == "Mandarin":
        english_sub_header.config(text="English", font="Times 38")
        mandarin_sub_header.config(text="Mandarin", font="Times 38")
        function1_label.config(text="Enter the English word/sentence: ", font="Symbol 20", fg="#242424")
        function2_label.config(text="The Mandarin translation is: ", font="Symbol 20", fg="#242424")


# function converts the english/mandarin input into a mandarin/english result and displays on GUI
# if and elif statements determine the which language to receive input from by the subheading text
# from the translation output, textwrap returns a list of output lines and the number determines the increments for
# every line where a new line will be made(to remove clutter of GUI


def translate_and_pinyin():
    if english_sub_header['text'] == "English":
        translation_output = (translator.translate(str(translation_input.get()), src='en', dest='zh-cn')).text
        relabel1 = '\n'.join(textwrap.wrap(str(translation_output), 30))
        function2_label.config(text="Here is the Mandarin translation: ")
        result_translation_label.config(text=relabel1, font="Symbol 20", fg="#242424", width=90)
        pinyin_label.config(text="Here is the pinyin: ")
        result_pinyin = pinyin.get(translation_output)
        relabel2 = '\n'.join(textwrap.wrap(str(result_pinyin), 52))
        result_pinyin_label.config(text=relabel2, font="Symbol 20", fg="#242424", width=90)

    elif english_sub_header['text'] == "Mandarin":
        translation_output = (translator.translate(str(translation_input.get()), src='zh-cn', dest='en')).text
        relabel1 = '\n'.join(textwrap.wrap(str(translation_output), 50))
        function2_label.config(text="Here is the English translation: ")
        result_translation_label.config(text=relabel1, font="Symbol 20", fg="#242424", width=90)
        pinyin_label.config(text="Here is the pinyin: ")
        result_pinyin = pinyin.get(translation_input.get())
        relabel2 = '\n'.join(textwrap.wrap(str(result_pinyin), 50))
        result_pinyin_label.config(text=relabel2, font="Symbol 20", fg="#242424", width=90)

# pronunciation of the mandarin or english output based on the subheading text.
# uses google text to speech API by first saving the audio file as an mp3, then playing it using playsound module


def pronunciation1():
    if english_sub_header['text'] == "English":
        translation_output = (translator.translate(str(translation_input.get()), src='en', dest='zh-cn')).text
        tts = gtts.gTTS(translation_output, lang="zh-cn")
        tts.save("pronunciation.mp3")
        playsound("pronunciation.mp3")

    elif english_sub_header['text'] == "Mandarin":
        translation_output = (translator.translate(str(translation_input.get()), src='zh-cn', dest='en')).text
        tts = gtts.gTTS(translation_output, lang="en")
        tts.save("pronunciation.mp3")
        playsound("pronunciation.mp3")

# uses PyDictionary module and uses the english translation or input in both cases to provide basic meanings, synonyms,
# antonyms etc...(module accesses WordNet for definitions)
# similar to translation, if the output is over a certain number of characters, it creates a new line


def define():
    stroke_order_label.destroy()
    stroke_order_info.destroy()

    if english_sub_header['text'] == "English":
        eng_def = dictionary.meaning(translation_input.get())
        relabel = '\n'.join(textwrap.wrap(str(eng_def), 90))
        definition_caption.config(text="Here is the Definition: ")
        definition_label.config(text=relabel, font="Monaco 12", fg="#242424", width=90)

    elif english_sub_header['text'] == "Mandarin":
        translation_output = (translator.translate(str(translation_input.get()), src='zh-cn', dest='en')).text
        eng_def = dictionary.meaning(translation_output)
        relabel = '\n'.join(textwrap.wrap(str(eng_def), 90))
        definition_caption.config(text="Here is the Definition: ")
        definition_label.config(text=relabel, font="Monaco 12", fg="#242424", width=90)
    else:
        definition_label.config(text="The input must be only a single word")


# background color framing and sizing
f1 = tk.Frame(root, width=1440, height=150, background="#B71616")
f2 = tk.Frame(root, width=1440, height=125, background="#B9B9B9")
f3 = tk.Frame(root, width=1440, height=575, background="#E3E3E3")

# all labels on GUI
header = tk.Label(root, text="Mandarin Learning Tool", font=("Times", "50", "bold"), background="#B71616", fg="white")

english_sub_header = tk.Label(root, text="English", font="Times 38", background="#B9B9B9")
mandarin_sub_header = tk.Label(root, text="Mandarin", font="Times 38", background="#B9B9B9")

function1_label = tk.Label(root, text="Enter the English word/sentence: ", font="Symbol 20", fg="#242424", background="#E3E3E3")
function2_label = tk.Label(root, text="The Mandarin Translation is: ", font="Symbol 20", fg="#242424", background="#E3E3E3")

pinyin_label = tk.Label(root, text="The Pinyin is: ", font="Symbol 20", fg="#242424", background="#E3E3E3")

definition_caption = tk.Label(root, text="The Definition is: ", font="Symbol 20", fg="#242424", background="#E3E3E3")
definition_label = tk.Label(root, font="Symbol 20", fg="#242424", background="#E3E3E3")

# definition function error message for multiple words instead of one
warning_label = tk.Label(text="* Input must be a single word for definitions", font="Monaco 13 italic",
                         background="#E3E3E3")

# pinyin and translation output labels
result_translation_label = tk.Label(root, text="", background="#E3E3E3")
result_pinyin_label = tk.Label(root, text="", background="#E3E3E3")

# stroke order chart and info paragraph, multiple newlines
stroke_order_label = tk.Label(text="The 8 Rules of Chinese Character Stroke Order: ", font="Symbol 20 bold",
                              fg="#242424", background="#E3E3E3")
stroke_order_info = tk.Label(text="- Characters should generally be written from top to bottom, left to right. "
                                  "Horizontal strokes go from left \nto right. If you have two horizontal strokes,then "
                                  "the top one comes first. This can be seen in characters \nlike 二 or 首. If the "
                                  "character has two or three components, like 谢, then start with the component "
                                  "\nfurthest to the left, then the middle one, then the right one.\n- When horizontal "
                                  "and vertical strokes intersect, the horizontal stroke (or strokes) comes first. "
                                  "The vertical \nstroke (or strokes) is often the finishing stroke. Examples: 件，十，"
                                  "事 ，弗 (Technically, the vertical stroke \nin 事 is a hook stroke, but the same "
                                  "principle applies.)\n- Enclosures are written before the contents, starting with "
                                  "the left vertical, then the top and right in a \nsingle stroke. If there is a bottom"
                                  " horizontal stroke on the enclosure, it is written after the contents.\n Examples: "
                                  "间，回，日，月\n- Bottom enclosures come last. Examples: 远，脑\n- Right-to-left "
                                  "diagonals come before left-to-right diagonals. Examples: 人，父，六 . and 千 is a "
                                  "right-to-left diagonal.\n And the lower-left stroke in 没 and 冷 is written from the "
                                  "lower left corner towards the center.\n- In vertically symmetrical characters, the "
                                  "center comes before the outside. Examples: 小，永，承\n- Upper-left and upper-center "
                                  "dots come first. Examples: 六，文，请，间，弟\n- Upper-right and inside dots come last. "
                                  "Examples: 玉，书，求"
                             , font="Monaco 10", fg="#242424", background="#E3E3E3")

label_logo1 = tk.Label(root, text="英语", font="Times 70 bold", fg="gold", background="#B71616")
label_logo2 = tk.Label(root, text="中文", font="Times 70 bold", fg="gold", background="#B71616")
# volume button on GUI with command that activates its respective function
volume_button1 = tk.Button(root, image=volume_image, command=pronunciation1)

# switch button will switch language input and output onclick
switch_button = tk.Button(root, image=switch_image, command=switch_lang)

# text variable for entry widget input
translation_input = tk.StringVar()

# entry widget - establish text variable(the input)
entry1 = tk.Entry(root, textvariable=translation_input, font="Symbol 20", fg="#242424", width=60)

# generation buttons for translation/pinyin and definition
generate1 = tk.Button(root, text="Generate Translation/Pinyin", font="Symbol 18", fg="#242424",
                      command=translate_and_pinyin)
generate2 = tk.Button(root, text="Generate Definition", font="Symbol 18", fg="#242424", command=define)

# positioning of labels, entries, button widgets in a grid format, ordered in increasing row #

header.grid(row=0, column=1, sticky="w")
label_logo1.grid(row=0, column=0, sticky="")
label_logo2.grid(row=0, column=1, sticky="e")
english_sub_header.grid(row=1, column=0)
mandarin_sub_header.grid(row=1, columnspan=2, sticky='e')
switch_button.grid(row=1, column=0, columnspan=4)
function1_label.grid(row=2, column=0)
entry1.grid(row=2, column=1)
function2_label.grid(row=3, column=0)
result_translation_label.grid(row=3, column=1)
pinyin_label.grid(row=4, column=0)
result_pinyin_label.grid(row=4, column=1)
definition_caption.grid(row=5, column=0)
definition_label.grid(row=5, column=1)
stroke_order_label.grid(row=5, column=1)
stroke_order_info.grid(row=5, rowspan=10, column=1, sticky='s')
generate1.grid(row=6, column=0, sticky='n')
generate2.grid(row=6, column=0, sticky='s')
volume_button1.grid(row=7, column=0, sticky='')
warning_label.grid(row=7, sticky='n')

f1.grid(row=0, columnspan=3)
f2.grid(row=1, columnspan=3)
f3.grid(row=2, rowspan=6, columnspan=3)


# run program
root.mainloop()



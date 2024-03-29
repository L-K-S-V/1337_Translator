import tkinter as tk
from turtle import bgcolor
from tkinter import Tk



# Defines forced label update
def update_input_label():
    input_language_label.config(text=f"Source: {input_language}")

def update_output_label():
    output_language_label.config(text=f"Source: {output_language}")

# Switches input and output label names
def reverse_language_names():
    global input_language
    global output_language
    if input_language == "Common Tongue":
        input_language = "1337"
        output_language = "Common Tongue"
    else:
        input_language = "Common Tongue"
        output_language = "1337"

# Switches contents of textboxes
def input_output_textbox_switch():
    old_input_text = user_input_textbox.get("1.0", tk.END)
    old_output_text = user_output_textbox.get("1.0", tk.END)
    user_input_textbox.delete("1.0", tk.END)
    user_input_textbox.insert("1.0", old_output_text)
    user_output_textbox.delete("1.0", tk.END)
    user_output_textbox.insert("1.0", old_input_text)

# Combines all functions to switch the languages around
def reverse_language():
    input_output_textbox_switch()
    reverse_language_names()
    update_input_label()
    update_output_label()



# Mode of translation ... Common Tongue to 1337 & 1337 to Common Tongue
def trans_eng_to_leet():
    """fetch input from the textbox and translate it"""
    translated_text = user_input_textbox.get("1.0", tk.END)
    translated_text_caps = translated_text.upper()
    translated_text_caps = translated_text_caps.replace("A", "4")
    translated_text_caps = translated_text_caps.replace("E", "3")
    translated_text_caps = translated_text_caps.replace("O", "0")
    translated_text_caps = translated_text_caps.replace("S", "5")
    translated_text_caps = translated_text_caps.replace("T", "7")
    translated_text_caps = translated_text_caps.replace("I", "1")
    user_output_textbox.delete("1.0", tk.END)
    user_output_textbox.insert("1.0", translated_text_caps)

def trans_leet_to_eng():
    """fetch input from the textbox and translate it"""
    translated_text = user_input_textbox.get("1.0", tk.END)
    translated_text_caps = translated_text.lower()
    translated_text_caps = translated_text_caps.replace("4", "a")
    translated_text_caps = translated_text_caps.replace("3", "e")
    translated_text_caps = translated_text_caps.replace("0", "o")
    translated_text_caps = translated_text_caps.replace("5", "s")
    translated_text_caps = translated_text_caps.replace("7", "t")
    translated_text_caps = translated_text_caps.replace("1", "i")
    user_output_textbox.delete("1.0", tk.END)
    user_output_textbox.insert("1.0", translated_text_caps)

# Initiates the translation according to set input and output languages 
def translate():
    """Initiates the translation according to set input and output languages"""
    if input_language == "Common Tongue":
         trans_eng_to_leet()
    elif input_language == "1337":
         trans_leet_to_eng()



def clear_all():
    """Clears all text in the input and output textboxes"""
    user_input_textbox.delete("1.0", tk.END)
    user_output_textbox.delete("1.0", tk.END)

def copy_button():
    """Copies the contents of the translated text"""
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(user_output_textbox.get("1.0", tk.END))



# TKINTER WINDOW
window = tk.Tk()
window.configure(bg="#282828")
window.title("1337 Universal Translator")
window.minsize(800, 400)
window.option_add('*Font', 'Terminal 12')


# COLUMNS AND ROWS: grid of 3(columns) x 4(rows)
window.columnconfigure(0, weight=1, minsize=120)
window.columnconfigure(1, weight=0, minsize=40)
window.columnconfigure(2, weight=1, minsize=120)
window.rowconfigure(0, weight=0, minsize=150)
window.rowconfigure(1, weight=0, minsize=40)
window.rowconfigure(2, weight=1, minsize=100)
window.rowconfigure(3, minsize=30)


# LOGO: Justified left to maintain the correct spacing
logo = """
    111111   3333333   3333333  77777777
 111 1111       333       333       777
    1111    333333    333333       777
   1111       333       333       777
 111111  3333333  33333333       777    by 1UK45

The groundbreaking non-AI powered universal translator!"""

logo_label_frame = tk.Frame(bg="#282828")
logo_label_frame.grid(row=0, column=0, columnspan=3, sticky="W")

logo_label = tk.Label(master=logo_label_frame, anchor="w", justify="left", text=logo, bg="#282828", fg="#00FF66")
logo_label.pack(side=tk.LEFT)



# NAME OF INPUT LANGUAGE
input_language = "Common Tongue"
input_language_label = tk.Label(bg="#282828", fg="#00FF66", text=f"Source: {input_language}", pady=5)
input_language_label.grid(row=1, column=0, sticky="WS")

# NAME OF OUTPUT LANGUAGE
output_language = "1337"
output_language_label = tk.Label(bg="#282828", fg="#00FF66", text=f"Translation: {output_language}", pady=5)
output_language_label.grid(row=1, column=2, sticky="WS")



# INPUT LANGUAGE TEXTBOX
user_input_frame = tk.Frame(bg="#282828", relief=tk.RAISED)
user_input_frame.grid(row=2, column=0, sticky="NSEW")

input_text = ""
user_input_textbox = tk.Text(master=user_input_frame, wrap="word", bg="yellow", width=30, height=15)
user_input_textbox.insert("1.0", "Write here")
user_input_textbox.pack(expand=1, fill=tk.BOTH)

# OUTPUT LANGUAGE TEXTBOX
user_output_frame = tk.Frame(bg="#282828")
user_output_frame.grid(row=2, column=2, sticky="NSEW")

output_text = ""
user_output_textbox = tk.Text(master=user_output_frame, wrap="word", bg="yellow", width=30, height=15)
user_output_textbox.insert("1.0", output_text)
user_output_textbox.pack(expand=1, fill=tk.BOTH)

translation_output = user_output_textbox.get("1.0", tk.END)



# REVERSE LANGUAGE BUTTON
reverse_language_frame = tk.Frame(bg="#282828")
reverse_language_frame.grid(row=2, column=1, sticky="NSEW")

reverse_language_button = tk.Button(master=reverse_language_frame, text="<\n>", command=reverse_language)
reverse_language_button.pack(expand=1, fill=tk.BOTH)

# TRANSLATE BUTTON: This initiates the translation and display translated text on the right hand-side
translate_button_frame = tk.Frame(bg="#282828")
translate_button_frame.grid(row=3, column=0, sticky="NSEW")

translate_button_button = tk.Button(master=translate_button_frame, text="Translate", command=translate, pady=5)
translate_button_button.pack(fill=tk.BOTH)

# SPACER DUMMY BUTTON: it fills the gap between the Translate and Copy All button.
spacer_button_frame = tk.Frame(bg="#282828")
spacer_button_frame.grid(row=3, column=1, sticky="NSEW")

spacer_button_frame = tk.Button(master=spacer_button_frame, text="", pady=5, relief=tk.SUNKEN)
spacer_button_frame.pack(fill=tk.BOTH)

# COPY ALL BUTTON
copy_clear_button_frame = tk.Frame(bg="#282828")
copy_clear_button_frame.grid(row=3, column=2, sticky="NSEW")

copy_button_button = tk.Button(master=copy_clear_button_frame, text="Copy Translation", command=copy_button, pady=5)
copy_button_button.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# CLEAR ALL BUTTON
clear_button_button = tk.Button(master=copy_clear_button_frame, text="Clear All", command=clear_all, pady=5)
clear_button_button.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)



window.mainloop()
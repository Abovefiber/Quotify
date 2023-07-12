import tkinter as tk
from tkinter import *
import requests
from threading import Thread
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


api = "http://api.quotable.io/random" # API
quotes = [] # Store quotes
quote_number = 0 # Counter to track current quotes

# Function to get a quote from the API
def get_quote():
    random_quote = requests.get(api).json() # Sends request to the API and get a random quote

    # Get the content and author from the API response
    content = random_quote["content"]
    author = random_quote["author"]
    quote = content + "\n\n" + author

    return quote

# Function to display a random quote in the GUI
def get_random_quote():
    global quote_label
    global quote_number

    if quote_number >= len(quotes): # Check if all quotes have been fetched
        quote = get_quote() # If all quotes have been fetched, get a new quote from the API
        quotes.append(quote) # Add the new quote to the list of quotes
    else: # If there are remaining quotes in the list, use the next quote
        quote = quotes[quote_number]

    # Update the label with the new quote
    quote_label.configure(text=quote)

    # Increment the quote counter
    quote_number += 1

    #to remove heading and second heading
    heading.destroy()
    second_heading.destroy()

# GUI window
window = tk.Tk()
window.geometry("1280x720")
window.title("Quotify")
window['background'] = '#fff'
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)

heading = tk.Label(window, text="Welcome to Quotify", font='Helvetica 50 bold', fg="#252525", bg="#fff", justify="center")
heading.pack(padx=50, pady=50)

second_heading = tk.Label(window, text="Random Quote Generator", font=('Helvetica', 25), fg="#252525", bg="#fff", justify="center")
second_heading.pack(padx=20, pady=20)

quote_label = tk.Label(window, font='Helvetica 18', wraplength=800, justify="center", bg="#fff", fg="#252525")
quote_label.pack(padx=100, pady=100)

#replaces button into img
button = Button(window, command=get_random_quote, text="GENERATE QUOTE", bg="#fff", cursor='hand2', borderwidth='0')
img = PhotoImage(file="images/Button 2.png")
button.config(image=img)
button.pack(padx=20, pady=20)


# Start GUI event loop
if __name__ == "__main__":
    window.mainloop()
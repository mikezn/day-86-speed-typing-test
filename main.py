import tkinter

BACKGROUND_COLOUR ='#2e2e2e'
CANVAS_SIZE = (800, 526)


def push():
    # Enable editing
    text_widget.config(state="normal")

    # Clear previous highlight
    text_widget.tag_remove("highlight", "1.0", "end")

    # Add highlight to a new word (say, characters 10 to 14)
    text_widget.tag_add("highlight", "1.10", "1.14")

    # Disable editing
    text_widget.config(state="normal")

window = tkinter.Tk()
window.title = "Typing Speed Test"
window.config(padx=0, pady=0, bg=BACKGROUND_COLOUR)

text_widget = tkinter.Text(window, height=5, width=50)
text_widget.insert("1.0", "Type this accurately")
text_widget.tag_add("highlight", "1.5", "1.9")
text_widget.tag_config("highlight", foreground="red")
text_widget.config(state="disabled")

btn_test = tkinter.Button(text="push me", command=push)

text_widget.grid(column=0, row=0)
btn_test.grid(column=0, row=1)

window.mainloop()
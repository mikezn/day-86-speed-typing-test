import tkinter

COLOUR_BACKGROUND = '#2e2e2e'
COLOUR_FONT_NORMAL = '#e0e0e0'
COLOUR_SELECTED_CHAR_ERROR = 'red'
COLOUR_SELECTED_CHAR_CORRECT = '#2e2e2e'
COLOUR_SELECTED_BACKGROUND = '#66ff66'
COLOUR_WORD_ERROR = 'red'
COLOUR_WORD_CORRECT = 'green'


CANVAS_SIZE = (800, 526)

sentence = "Type this accurately or else die"
sentence_words_list = sentence.split()

def evaluate_sentence():
    # Enable editing
    text_widget.config(state="normal")

    # Clear everything by removing all tags
    text_widget.tag_remove("main_text", "1.0", "end")
    text_widget.tag_remove("highlight_word_correct", "1.0", "end")
    text_widget.tag_remove("highlight_word_error", "1.0", "end")
    text_widget.tag_remove("highlight_letter_correct", "1.0", "end")
    text_widget.tag_remove("highlight_letter_error", "1.0", "end")
    text_widget.tag_remove("highlight_working_word", "1.0", "end")

    # Set entire sentence to default
    text_widget.tag_add("main_text", "1.0", "end")


    if len(entry_widget.get()) > 0:
        typed_sentence = entry_widget.get()
        typed_sentence_list = typed_sentence.split()
        space = (0 if entry_widget.get().endswith(" ") else 1)

        start_pos = 0
        end_pos = 0

        for i in range(len(typed_sentence_list) - space):
            # logic here for checking if the entire word is correct
            start_pos = end_pos
            end_pos += len(sentence_words_list[i]) + 1

            start_pos_str = f'1.{start_pos}'
            end_pos_str = f'1.{end_pos}'

            if typed_sentence_list[i] == sentence_words_list[i]:
                #apply_styling(start_pos, end_pos)
                text_widget.tag_add("highlight_word_correct", start_pos_str, end_pos_str)
            else:
                text_widget.tag_add("highlight_word_error", start_pos_str, end_pos_str)

        # make a list of the letters in the word currently being typed
        typed_final_chars_list = list(typed_sentence_list[len(typed_sentence_list)-1])
        sentence_final_chars_list = list(sentence_words_list[len(typed_sentence_list)-1])

        print(typed_final_chars_list)
        print(sentence_final_chars_list)

        if space == 1:
            # check the current word being typed for highlighting each correct / incorrect letter
            for i in range(len(sentence_final_chars_list)):

                print(len(sentence_final_chars_list))
                print(len(typed_final_chars_list), i)
                #if the final sentence word is less than the word being typed, evaluate
                if len(typed_final_chars_list) > i:
                    print("Less")
                    if typed_final_chars_list[i] == sentence_final_chars_list[i]:
                        print("correct")
                        end_pos_str = f'1.{end_pos}'
                        text_widget.tag_add("highlight_letter_correct", end_pos_str)
                    else:
                        print("incorrect")
                        end_pos_str = f'1.{end_pos}'
                        text_widget.tag_add("highlight_letter_error", end_pos_str)
                # else the sentence word is longer than the currently typed word, so just highlight the rest of the
                # word to show its currently being worked on
                else:
                    print("More")
                    end_pos_str = f'1.{end_pos}'
                    text_widget.tag_add("highlight_working_word", end_pos_str)
                end_pos += 1


    # Disable editing
    text_widget.config(state="disabled")


def on_key_release(event):
    evaluate_sentence()



window = tkinter.Tk()
window.title = "Typing Speed Test"
window.config(padx=0, pady=0, bg=COLOUR_BACKGROUND)

text_widget = tkinter.Text(window,  font=("Consolas", 16), height=5, width=50, background=COLOUR_BACKGROUND)
text_widget.insert("1.0", sentence)

# configure all the text_widget tags for styling the text
text_widget.tag_config("main_text", foreground=COLOUR_FONT_NORMAL, background=COLOUR_BACKGROUND)
text_widget.tag_config("highlight_word_error", foreground=COLOUR_WORD_ERROR, background=COLOUR_BACKGROUND)
text_widget.tag_config("highlight_word_correct", foreground=COLOUR_WORD_CORRECT, background=COLOUR_BACKGROUND)
text_widget.tag_config("highlight_letter_correct", foreground=COLOUR_SELECTED_CHAR_CORRECT, background=COLOUR_SELECTED_BACKGROUND)
text_widget.tag_config("highlight_letter_error", foreground=COLOUR_SELECTED_CHAR_ERROR, background=COLOUR_SELECTED_BACKGROUND)
text_widget.tag_config("highlight_working_word", foreground=COLOUR_FONT_NORMAL, background=COLOUR_SELECTED_BACKGROUND)


text_widget.config(state="disabled")

entry_widget = tkinter.Entry(window, width=20)

text_widget.grid(column=0, row=0, columnspan=3)
entry_widget.grid(column=1, row=1)

entry_widget.focus_set()

window.bind("<KeyRelease>", on_key_release)

evaluate_sentence()

window.mainloop()

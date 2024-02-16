#Thank you youtube tutorial : https://www.youtube.com/watch?v=gfV1a3ri1tk&t=51s

import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data
#function to display the current question and choices
def show_question():
    #Get the current question from the quiz_data list
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])
    
    #display the choices of buttons
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i],state="normal") #reset button state
    #clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")
#Function to check the selected answer and provide feedback
def check_answer(choice):
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")
    
    #check if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
        # Update the score and display it
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text = "Correct!", foreground="green" )
    else:
         feedback_label.config(text = "Incorrect!", foreground="red" )
    #disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")
    
#function to move to the next question
        
def next_question():
    global current_question
    current_question += 1
    
    if current_question < len(quiz_data):
        # If there are more questions, show the next question
        show_question()
    else:
        #If all questions have been answered display the final score
        messagebox.showinfo("Quiz Completed", "Quiz Completed! Final Score: {}/{}".format(score,len(quiz_data)))
        root.destroy()
        
    
#create the main window
root = tk.Tk()
root.title("Physics Unit 4 Practice Test")
root.geometry("600x500")
style = Style(theme="flatly")

# Configure the font size for the question and choice buttons
style.configure("TLabel", font=("Helvetica",20))
style.configure("TButton", font=("Helvetica",16))

#create the question label
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength = 500,
    padding = 10
    
)

qs_label.pack(pady=10)

#create the choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)
    
#create the feedback label
feedback_label = ttk.Label(
    root,
    anchor= "center",
    padding = 10
)
feedback_label.pack(pady=10)

# initialize the score
score = 0
# Create the score label
score_label = ttk.Label(
    root,
    text = "Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding = 10
)
score_label.pack(pady=10)

#create the next button
next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state = "disabled"
)
next_btn.pack(pady=10)
#initialize the current question index
current_question = 0

#show the first question
show_question()

#start the main event loop
root.mainloop()
import tkinter as tk
from tkinter import messagebox
import math
import random
from owlready2 import *

#Load and parse the ontology
Ontology = get_ontology("CircleArea.owl").load()


def get_definitions():
    all_classes = list(Ontology.classes())
    definitions = ""
    for cls in all_classes:
        if cls.comment:
            definitions += f"{cls.name}: {cls.comment[0]}\n\n"
            
    return definitions

def get_wrong_answer_message(correct_answer):
    base_message = "That's not the correct answer. "
    base_message += f"The correct area is {correct_answer:.2f}. \n\n"
    
    base_message += get_definitions()
    base_message += "Now let's try another one!"

    return base_message


def calculate_area(radius):
    """Calculate the area of a circle given the radius."""
    return math.pi * radius ** 2

def check_answer():
    """Check if the user's answer is correct."""
    try:
        user_answer = float(answer_entry.get())
        correct_area = calculate_area(current_radius)
        if math.isclose(user_answer, correct_area, rel_tol=1e-2):  # Allow a small margin for floating-point precision
            messagebox.showinfo("Correct!", "That's the correct answer. Great job!")
        else:
            messagebox.showerror("Incorrect", get_wrong_answer_message(correct_area))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

    # Generate a new radius for the next question
    generate_question()

def generate_question():
    """Generate a new radius and display it to the user."""
    global current_radius
    current_radius = random.randint(1, 20)  # Random radius between 1 and 20
    radius_label.config(text=f"Radius: {current_radius}")
    answer_entry.delete(0, tk.END)  # Clear the previous answer

# Create the main application window
root = tk.Tk()
root.title("Circle Area Tutor")


# Instructions

instructions = get_definitions()

instructions_label = tk.Label(root, text=instructions, justify=tk.LEFT, wraplength=400)
instructions_label.pack(pady=10)

# Display the radius
radius_label = tk.Label(root, text="", font=("Arial", 16))
radius_label.pack(pady=10)

# Entry for the user's answer
answer_entry = tk.Entry(root, font=("Arial", 14))
answer_entry.pack(pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=check_answer, font=("Arial", 12))
submit_button.pack(pady=10)

# Generate the first question
current_radius = None
generate_question()

# Start the main event loop
root.mainloop()

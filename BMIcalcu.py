import tkinter as tk

def BmiCalc():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi = weight / ((height / 100) ** 2)
        bmi_value.config(text=f"Your BMI: {bmi:.2f}")

        if bmi < 18.5:
            classification.config(text="Underweight")
        elif 18.5 <= bmi < 24.9:
            classification.config(text="Normal weight")
        elif 25 <= bmi < 29.9:
            classification.config(text="Overweight")
        elif 30 <= bmi < 34.9:
            classification.config(text="Obesity Class 1 (Moderate)")
        elif 35 <= bmi < 39.9:
            classification.config(text="Obesity Class 2 (Severe)")
        else:
            classification.config(text="Obesity Class 3 (Morbid Obesity)")

    except ValueError as e:
        print(e)

root = tk.Tk()
root.title("BMI Calculator")

# Create the main frame
frame = tk.Frame(root, bg='#0092FF', height=500, width=800)
frame.pack_propagate(False)
frame.pack()

# BMI Calculator Label
bmi_label = tk.Label(frame, text="BMI Calculator", font=("Inter-ExtraBold", 20, "bold"), fg='#000000', bg='#0092FF')
bmi_label.place(x=306, y=19)

# Height Label and Entry
height_label = tk.Label(frame, text="Height (cm):", font=("Inter-ExtraBold", 16, "bold"), fg='#000000', bg='#0092FF')
height_label.place(x=16, y=77)

height_entry = tk.Entry(frame)
height_entry.place(x=180, y=77)

# Weight Label and Entry
weight_label = tk.Label(frame, text="Weight (kg):", font=("Inter-ExtraBold", 16, "bold"), fg='#000000', bg='#0092FF')
weight_label.place(x=16, y=127)

weight_entry = tk.Entry(frame)
weight_entry.place(x=180, y=127)

# Compute Button
compute_button = tk.Button(frame, text="Compute BMI", font=("Inter-ExtraBold", 16, "bold"), fg='#000000', command=BmiCalc)
compute_button.place(x=180, y=177)

# BMI Value
bmi_value = tk.Label(frame, text="Your BMI: N/A", font=("Inter-ExtraBold", 16, "bold"), fg='#000000', bg='#0092FF')
bmi_value.place(x=21, y=222)

# BMI Classification
classification_label = tk.Label(frame, text="BMI Classification:", font=("Inter-ExtraBold", 16, "bold"), fg='#000000', bg='#0092FF')
classification_label.place(x=21, y=262)

classification = tk.Label(frame, text="", font=("Inter-ExtraBold", 16), fg='#000000', bg='#0092FF')
classification.place(x=21, y=292)

# BMI Categories Text
bmi_categories_text = """
Underweight: BMI less than 18.5
Normal weight: BMI 18.5 to 24.9
Overweight: BMI 25 to 29.9
Obesity Class 1 (Moderate): BMI 30 to 34.9
Obesity Class 2 (Severe): BMI 35 to 39.9
Obesity Class 3 (Morbid Obesity):
BMI 40 and above
"""

bmi_categories_label = tk.Label(frame, text=bmi_categories_text, font=("Inter-ExtraBold", 16, "bold"), fg='#000000', bg='#fff', justify=tk.LEFT)
bmi_categories_label.place(x=390, y=70)

# Start the Tkinter main loop
root.geometry('800x500')
root.mainloop()

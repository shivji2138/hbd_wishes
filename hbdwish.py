import tkinter as tk
import time
import threading

def animate_balloons():
    for i in range(20):
        for balloon in balloons:
            balloon.place(x=balloon.winfo_x(), y=balloon.winfo_y() - 5)
        time.sleep(0.05)
        root.update()
    for balloon in balloons:
        balloon.destroy()

def show_birthday_wish():
    name = name_entry.get()
    if not name.strip():
        message_label.config(text="Please enter your friend's name!", fg="red")
        return

    message_label.config(text="")
    threading.Thread(target=animate_balloons).start()
    wish_label.config(
        text=f"🎉🎂 Happy Birthday, {name}! 🎂🎉\nWishing you a wonderful year ahead! 💐",
        fg="#FF4500"
    )

# Create the main window
root = tk.Tk()
root.title("Happy Birthday App!")
root.geometry("500x600")
root.configure(bg="#E6E6FA")

# Title Label
title_label = tk.Label(
    root, text="🎈🎉 Birthday Surprise 🎉🎈", font=("Comic Sans MS", 20, "bold"), bg="#E6E6FA", fg="#4B0082"
)
title_label.pack(pady=20)

# Input Label and Entry
input_frame = tk.Frame(root, bg="#E6E6FA")
input_frame.pack(pady=20)

name_label = tk.Label(input_frame, text="Enter your friend's name:", font=("Arial", 14), bg="#E6E6FA")
name_label.grid(row=0, column=0, padx=10, pady=5)

name_entry = tk.Entry(input_frame, font=("Arial", 14), width=20)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Button
wish_button = tk.Button(
    root, text="🎁 Reveal Surprise 🎁", font=("Arial", 16, "bold"), bg="#FFD700", fg="black", command=show_birthday_wish
)
wish_button.pack(pady=20)

# Message Label
message_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#E6E6FA", fg="black")
message_label.pack()

# Birthday Wish Label
wish_label = tk.Label(
    root, text="", font=("Comic Sans MS", 16, "bold"), bg="#E6E6FA", wraplength=400, justify="center"
)
wish_label.pack(pady=20)

# Balloons
balloons = []
for _ in range(8):
    balloon = tk.Label(root, text="🎈", font=("Arial", 24), bg="#E6E6FA", fg="blue")
    balloon.place(x=50 + _ * 50, y=450)
    balloons.append(balloon)

# Run the GUI
root.mainloop()

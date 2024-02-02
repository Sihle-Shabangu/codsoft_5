import string
import random
import tkinter as tk


class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_entry = tk.Entry(master)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password_length)
        self.generate_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

        self.master.mainloop()

    def generate_password_length(self):
        try:
            length = int(self.length_entry.get())
            if length > 0:
                generated_password = self.generate_password(length)
                self.result_label.config(text=f"Generated Password: {generated_password}")
            else:
                self.result_label.config(text="Please enter a positive integer for the password length.")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid integer.")

    def generate_password(self, length):
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        return "".join(random.choice(characters) for _ in range(length))


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)

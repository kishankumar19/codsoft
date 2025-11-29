import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x450")
        self.root.config(bg="#f0f0f0")

        # Character sets
        self.char_sets = {
            'lowercase': string.ascii_lowercase,
            'uppercase': string.ascii_uppercase,
            'digits': string.digits,
            'special': string.punctuation
        }

        # UI components
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="🔐 Password Generator", font=("Arial", 16, "bold"), bg="#f0f0f0")
        title.pack(pady=10)

        # Length Input
        tk.Label(self.root, text="Password Length:", font=("Arial", 12), bg="#f0f0f0").pack()
        self.length_entry = tk.Entry(self.root, font=("Arial", 12), width=10)
        self.length_entry.pack(pady=5)

        # Checkboxes
        self.lower_var = tk.BooleanVar(value=True)
        self.upper_var = tk.BooleanVar(value=True)
        self.digit_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)

        tk.Checkbutton(self.root, text="Include Lowercase (abc)", variable=self.lower_var, bg="#f0f0f0").pack()
        tk.Checkbutton(self.root, text="Include Uppercase (ABC)", variable=self.upper_var, bg="#f0f0f0").pack()
        tk.Checkbutton(self.root, text="Include Digits (123)", variable=self.digit_var, bg="#f0f0f0").pack()
        tk.Checkbutton(self.root, text="Include Special (!@#)", variable=self.special_var, bg="#f0f0f0").pack()

        # Generate Button
        tk.Button(self.root, text="Generate Password", font=("Arial", 12, "bold"), 
                  command=self.generate_password).pack(pady=10)

        # Password Output
        tk.Label(self.root, text="Generated Password:", font=("Arial", 12), bg="#f0f0f0").pack()

        self.password_box = tk.Entry(self.root, font=("Arial", 12), width=30, justify="center")
        self.password_box.pack(pady=5)

        # Copy button
        tk.Button(self.root, text="Copy to Clipboard", command=self.copy_password).pack(pady=5)

        # Strength label
        self.strength_label = tk.Label(self.root, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
        self.strength_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 8:
                messagebox.showerror("Error", "Password length must be at least 8!")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            return

        # Build character set
        character_set = ""
        if self.lower_var.get(): character_set += self.char_sets["lowercase"]
        if self.upper_var.get(): character_set += self.char_sets["uppercase"]
        if self.digit_var.get(): character_set += self.char_sets["digits"]
        if self.special_var.get(): character_set += self.char_sets["special"]

        if not character_set:
            messagebox.showerror("Error", "Select at least one character type!")
            return

        # Generate random password
        password = ''.join(random.choice(character_set) for _ in range(length))

        # Shuffle for extra security
        password = ''.join(random.sample(password, len(password)))

        self.password_box.delete(0, tk.END)
        self.password_box.insert(0, password)

        # Show strength
        self.show_strength(password)

    def show_strength(self, password):
        score = 0
        if len(password) >= 12: score += 1
        if any(c.islower() for c in password): score += 1
        if any(c.isupper() for c in password): score += 1
        if any(c.isdigit() for c in password): score += 1
        if any(c in string.punctuation for c in password): score += 1

        strengths = {5: "Very Strong", 4: "Strong", 3: "Good", 2: "Weak", 1: "Very Weak"}
        strength = strengths.get(score, "Extremely Weak")

        self.strength_label.config(text=f"Password Strength: {strength}")

    def copy_password(self):
        password = self.password_box.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

def main():
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

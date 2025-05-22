from tkinter import *
from tkinter import ttk

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

class MorseCodeConvertor:
    def __init__(self):
        self.root = Tk()
        self.root.title("🔠 Morse Code Converter 🔁")
        self.root.geometry("650x500")
        self.root.config(bg="#fefefe")

        # Styles
        style = ttk.Style()
        style.configure("TNotebook.Tab", font=('Segoe UI', 11, 'bold'), padding=[10, 5])
        style.map("TNotebook.Tab", background=[("selected", "#b3e5fc")])

        # Header
        Label(self.root, text="MORSE CODE CONVERTER", font=("Segoe UI", 18, "bold"),
              bg="#2196f3", fg="white", pady=10).pack(fill=X)

        # Tabs
        tab_control = ttk.Notebook(self.root)
        self.text_to_morse_tab = Frame(tab_control, bg="#e3f2fd")
        self.morse_to_text_tab = Frame(tab_control, bg="#e8f5e9")

        tab_control.add(self.text_to_morse_tab, text="Text ➡ Morse")
        tab_control.add(self.morse_to_text_tab, text="Morse ➡ Text")
        tab_control.pack(expand=1, fill="both")

        self.create_text_to_morse_ui()
        self.create_morse_to_text_ui()

    def create_text_to_morse_ui(self):
        Label(self.text_to_morse_tab, text="Enter Text:", font=("Segoe UI", 13),
              bg="#e3f2fd", fg="#0d47a1").pack(pady=15)
        self.text_entry = Entry(self.text_to_morse_tab, font=("Segoe UI", 12), width=50, bg="#ffffff")
        self.text_entry.pack(pady=5)

        Button(self.text_to_morse_tab, text="🔁 Convert to Morse", font=("Segoe UI", 12, "bold"),
               bg="#1976d2", fg="white", activebackground="#1565c0",
               relief=FLAT, bd=0, padx=15, pady=5, command=self.convert_to_morse).pack(pady=15)

        Label(self.text_to_morse_tab, text="Morse Code Output:", font=("Segoe UI", 12, "bold"),
              bg="#e3f2fd", fg="#004d40").pack()
        self.morse_output = Text(self.text_to_morse_tab, height=6, width=60, font=("Courier New", 12), wrap=WORD, bg="#ffffff")
        self.morse_output.pack(pady=10)
        self.morse_output.config(state=DISABLED)

    def create_morse_to_text_ui(self):
        Label(self.morse_to_text_tab, text="Enter Morse Code:", font=("Segoe UI", 13),
              bg="#e8f5e9", fg="#1b5e20").pack(pady=15)
        Label(self.morse_to_text_tab, text="(Use spaces for letters and '/' for words)", font=("Segoe UI", 10, "italic"),
              bg="#e8f5e9", fg="#2e7d32").pack()
        self.morse_entry = Entry(self.morse_to_text_tab, font=("Segoe UI", 12), width=50, bg="#ffffff")
        self.morse_entry.pack(pady=5)

        Button(self.morse_to_text_tab, text="🔁 Convert to Text", font=("Segoe UI", 12, "bold"),
               bg="#43a047", fg="white", activebackground="#388e3c",
               relief=FLAT, bd=0, padx=15, pady=5, command=self.convert_to_text).pack(pady=15)

        Label(self.morse_to_text_tab, text="Text Output:", font=("Segoe UI", 12, "bold"),
              bg="#e8f5e9", fg="#004d40").pack()
        self.text_output = Text(self.morse_to_text_tab, height=6, width=60, font=("Segoe UI", 12), wrap=WORD, bg="#ffffff")
        self.text_output.pack(pady=10)
        self.text_output.config(state=DISABLED)

    def convert_to_morse(self):
        message = self.text_entry.get().upper()
        morse_code = ''
        for char in message:
            morse_code += MORSE_CODE_DICT.get(char, '') + ' '
        self.morse_output.config(state=NORMAL)
        self.morse_output.delete("1.0", END)
        self.morse_output.insert(END, morse_code.strip())
        self.morse_output.config(state=DISABLED)

    def convert_to_text(self):
        morse_input = self.morse_entry.get().strip()
        words = morse_input.split(' / ')
        decoded = ''
        for word in words:
            for code in word.split():
                decoded += REVERSE_MORSE_CODE_DICT.get(code, '?')
            decoded += ' '
        self.text_output.config(state=NORMAL)
        self.text_output.delete("1.0", END)
        self.text_output.insert(END, decoded.strip())
        self.text_output.config(state=DISABLED)

if __name__ == "__main__":
    app = MorseCodeConvertor()
    app.root.mainloop()

import tkinter as tk


class GUI:

    def __init__(self):

        self.adjective = None
        self.person_in_room = None
        self.noun_one = None
        self.noun_two = None

        self.root = tk.Tk()
        self.root.geometry("300x300")

        self.label_frame = tk.Frame(self.root)
        self.label_frame.columnconfigure(0, weight=1)

        self.label_one = tk.Label(self.label_frame, text="Enter an adjective: ", font=("Sans Serif", 16))
        self.label_one.grid(row=0, column=0)

        # adjective = tk.StringVar()
        self.adjective_text = tk.Text(self.label_frame, height=1, width=15, font=("Sans Serif", 12))
        self.adjective_text.grid(row=0, column=1)

        self.label_frame.pack(padx=10, pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", font=("Sans Serif", 12), command=self.submit_adjective)
        self.submit_button.pack(padx=5, pady=5)

        self.root.mainloop()

    def submit_adjective(self):
        self.adjective = self.adjective_text.get('1.0', tk.END)

        self.label_frame.destroy()
        self.submit_button.destroy()

        self.label_frame = tk.Frame(self.root)
        self.label_frame.columnconfigure(0, weight=1)

        self.label_one = tk.Label(self.label_frame, text="Enter a person in the room: ", font=("Sans Serif", 12))
        self.label_one.grid(row=0, column=0)

        self.adjective_text = tk.Text(self.label_frame, height=1, width=10, font=("Sans Serif", 12))
        self.adjective_text.grid(row=0, column=1)

        self.label_frame.pack(padx=10, pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", font=("Sans Serif", 12))
        self.submit_button.pack(padx=5, pady=5)



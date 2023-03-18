import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

class NotetakingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Restars")
        self.geometry("800x600")

         # create database
        self.conn = sqlite3.connect("notes.db")
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS notes
                          (id INTEGER PRIMARY KEY,
                          title TEXT,
                          note TEXT,
                          created_at TEXT)''')
        self.conn.commit()

        # create menu bar
        self.menu_bar = tk.Menu(self.master)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Save", command=self.save_note)
        self.file_menu.add_command(label="Exit", command=self.master.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.master.config(menu=self.menu_bar)

        # create frames
        self.left_frame = ttk.Frame(self.master)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.right_frame = ttk.Frame(self.master)
        self.right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # create note listbox
        self.note_listbox = tk.Listbox(self.left_frame)
        self.note_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # create scrollbar for note listbox
        self.scrollbar = tk.Scrollbar(self.left_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # configure scrollbar for note listbox
        self.note_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.note_listbox.yview)

        # create note title and content text widgets
        self.note_title_text = tk.Text(self.right_frame, height=1)
        self.note_title_text.pack(side=tk.TOP, fill=tk.X)

        self.note_content_text = tk.Text(self.right_frame)
        self.note_content_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # create theme menu
        self.theme_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.theme_menu.add_command(
            label="VS Code", command=self.set_vscode_theme)
        self.theme_menu.add_command(
            label="GitHub", command=self.set_github_theme)
        self.menu_bar.add_cascade(label="Themes", menu=self.theme_menu)

        # create checkbox
        self.checkbox = ttk.Checkbutton(self.right_frame, text="Checkbox")
        self.checkbox.pack(side=tk.LEFT)

        # create calendar
        self.calendar = ttk.Calendar(self.right_frame, selectmode='day')
        self.calendar.pack(side=tk.LEFT)

        # create table
        self.table = ttk.Treeview(self.right_frame)
        self.table["columns"] = ("one", "two", "three")
        self.table.column("#0", width=50, minwidth=50)
        self.table.column("one", width=150, minwidth=150)
        self.table.column("two", width=150, minwidth=150)
        self.table.column("three", width=150, minwidth=150)
        self.table.heading("#0", text="ID")
        self.table.heading("one", text="Column 1")
        self.table.heading("two", text="Column 2")
        self.table.heading("three", text="Column3")
        # add sample data to the table
        self.table.insert("", tk.END, text="1", values=("1A", "1B", "1C"))
        self.table.insert("", tk.END, text="2", values=("2A", "2B", "2C"))

        self.table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # load notes from the database
        self.load_notes()

    # bind select event to note listbox
        self.note_listbox.bind("<<ListboxSelect>>", self.load_note)


def load_notes(self):
    # clear note listbox
    self.note_listbox.delete(0, tk.END)

    # get notes from the database
    self.c.execute("SELECT id, title FROM notes")
    rows = self.c.fetchall()

    # add notes to note listbox
    for row in rows:
        self.note_listbox.insert(tk.END, row)


def load_note(self, event):
    # get selected note from the note listbox
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        note_id = self.note_listbox.get(index)[0]
        self.current_note_id = note_id

        # get note details from the database
        self.c.execute("SELECT title, note FROM notes WHERE id=?", (note_id,))
        row = self.c.fetchone()

        # load note details into note title and content text widgets
        self.note_title_text.delete("1.0", tk.END)
        self.note_title_text.insert(tk.END, row[0])

        self.note_content_text.delete("1.0", tk.END)
        self.note_content_text.insert(tk.END, row[1])


def save_note(self):
    # get current note title and content
    title = self.note_title_text.get("1.0", tk.END).strip()
    content = self.note_content_text.get("1.0", tk.END).strip()

    # get current date and time
    now = datetime.now()
    created_at = now.strftime("%Y-%m-%d %H:%M:%S")

    if title and content:
        if hasattr(self, "current_note_id"):
            # update existing note
            self.c.execute("UPDATE notes SET title=?, note=?, created_at=? WHERE id=?",
                           (title, content, created_at, self.current_note_id))
        else:
            # insert new note
            self.c.execute(
                "INSERT INTO notes (title, note, created_at) VALUES (?, ?, ?)", (title, content, created_at))

        self.conn.commit()

        # reload notes in the note listbox
        self.load_notes()

        # clear current note details in the note title and content text widgets
        self.note_title_text.delete("1.0", tk.END)
        self.note_content_text.delete("1.0", tk.END)

        # remove current note ID
        delattr(self, "current_note_id")


def set_vscode_theme(self):
    self.master.config(bg="#1e1e1e")
    self.note_title_text.config(bg="#1e1e1e", fg="#d4d4d4")
    self.note_content_text.config(bg="#1e1e1e", fg="#d4d4d4")
    self.checkbox.config(style="dark.TCheckbutton")
    self.calendar.config(style="dark.TCalendar")
    self.table.config(style="dark.Treeview")


    def set_github_theme(self):
        self.master.config(bg="#f6f8fa")
        self.note_title_text.config(bg="#f6f8fa", fg="#24292e")
        self.note_content_text.config(bg="#f6f8fa", fg="#24292e")
        self.checkbox.config(style="github.TCheckbutton")
        self.calendar.config(style="github.TCalendar")
        self.table.config(style="github.Treeview")

        self.note_text = tk.Text(self)
        self.note_text.pack(fill="both", expand=True)

        # Save button
        self.save_button = tk.Button(self, text="Save", command=self.save_note)
        self.save_button.pack(side="left")

        # Quit button
        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(side="right")


        def save_note(self):
            note = self.note_text.get("1.0", "end-1c")
        # Save note to a file or database...
        messagebox.showinfo("Note Saved", "Your note has been saved successfully!")





class NotetakingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notetaking App")
        self.geometry("400x400")

        # create database
        self.conn = sqlite3.connect("notes.db")
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS notes
                          (id INTEGER PRIMARY KEY,
                          title TEXT,
                          note TEXT,
                          created_at TEXT)''')
        self.conn.commit()

        # create menu bar
        self.menu_bar = tk.Menu(self.master)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Save", command=self.save_note)
        self.file_menu.add_command(label="Exit", command=self.master.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.master.config(menu=self.menu_bar)

        # create frames
        self.left_frame = ttk.Frame(self.master)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.right_frame = ttk.Frame(self.master)
        self.right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # create note listbox
        self.note_listbox = tk.Listbox(self.left_frame)
        self.note_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # create scrollbar for note listbox
        self.scrollbar = tk.Scrollbar(self.left_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # configure scrollbar for note listbox
        self.note_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.note_listbox.yview)

        # create note title and content text widgets
        self.note_title_text = tk.Text(self.right_frame, height=1)
        self.note_title_text.pack(side=tk.TOP, fill=tk.X)

        self.note_content_text = tk.Text(self.right_frame)
        self.note_content_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # create theme menu
        self.theme_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.theme_menu.add_command(
            label="VS Code", command=self.set_vscode_theme)
        self.theme_menu.add_command(
            label="GitHub", command=self.set_github_theme)
        self.menu_bar.add_cascade(label="Themes", menu=self.theme_menu)

        # create checkbox
        self.checkbox = ttk.Checkbutton(self.right_frame, text="Checkbox")
        self.checkbox.pack(side=tk.LEFT)

        # create calendar
        self.calendar = ttk.Calendar(self.right_frame, selectmode='day')
        self.calendar.pack(side=tk.LEFT)

        # create table
        self.table = ttk.Treeview(self.right_frame)
        self.table["columns"] = ("one", "two", "three")
        self.table.column("#0", width=50, minwidth=50)
        self.table.column("one", width=150, minwidth=150)
        self.table.column("two", width=150, minwidth=150)
        self.table.column("three", width=150, minwidth=150)
        self.table.heading("#0", text="ID")
        self.table.heading("one", text="Column 1")
        self.table.heading("two", text="Column 2")
        self.table.heading("three", text="Column3")
        # add sample data to the table
        self.table.insert("", tk.END, text="1", values=("1A", "1B", "1C"))
        self.table.insert("", tk.END, text="2", values=("2A", "2B", "2C"))

        self.table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # load notes from the database
        self.load_notes()

    # bind select event to note listbox
        self.note_listbox.bind("<<ListboxSelect>>", self.load_note)


def load_notes(self):
    # clear note listbox
    self.note_listbox.delete(0, tk.END)

    # get notes from the database
    self.c.execute("SELECT id, title FROM notes")
    rows = self.c.fetchall()

    # add notes to note listbox
    for row in rows:
        self.note_listbox.insert(tk.END, row)


def load_note(self, event):
    # get selected note from the note listbox
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        note_id = self.note_listbox.get(index)[0]
        self.current_note_id = note_id

        # get note details from the database
        self.c.execute("SELECT title, note FROM notes WHERE id=?", (note_id,))
        row = self.c.fetchone()

        # load note details into note title and content text widgets
        self.note_title_text.delete("1.0", tk.END)
        self.note_title_text.insert(tk.END, row[0])

        self.note_content_text.delete("1.0", tk.END)
        self.note_content_text.insert(tk.END, row[1])


def save_note(self):
    # get current note title and content
    title = self.note_title_text.get("1.0", tk.END).strip()
    content = self.note_content_text.get("1.0", tk.END).strip()

    # get current date and time
    now = datetime.now()
    created_at = now.strftime("%Y-%m-%d %H:%M:%S")

    if title and content:
        if hasattr(self, "current_note_id"):
            # update existing note
            self.c.execute("UPDATE notes SET title=?, note=?, created_at=? WHERE id=?",
                           (title, content, created_at, self.current_note_id))
        else:
            # insert new note
            self.c.execute(
                "INSERT INTO notes (title, note, created_at) VALUES (?, ?, ?)", (title, content, created_at))

        self.conn.commit()

        # reload notes in the note listbox
        self.load_notes()

        # clear current note details in the note title and content text widgets
        self.note_title_text.delete("1.0", tk.END)
        self.note_content_text.delete("1.0", tk.END)

        # remove current note ID
        delattr(self, "current_note_id")


def set_vscode_theme(self):
    self.master.config(bg="#1e1e1e")
    self.note_title_text.config(bg="#1e1e1e", fg="#d4d4d4")
    self.note_content_text.config(bg="#1e1e1e", fg="#d4d4d4")
    self.checkbox.config(style="dark.TCheckbutton")
    self.calendar.config(style="dark.TCalendar")
    self.table.config(style="dark.Treeview")


def set_github_theme(self):
    self.master.config(bg="#f6f8fa")
    self.note_title_text.config(bg="#f6f8fa", fg="#24292e")
    self.note_content_text.config(bg="#f6f8fa", fg="#24292e")
    self.checkbox.config(style="github.TCheckbutton")
    self.calendar.config(style="github.TCalendar")
    self.table.config(style="github.Treeview")


if __name__ == "__main__":
    app = NotetakingApp()
    app.mainloop()

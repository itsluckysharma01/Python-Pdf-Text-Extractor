import tkinter
from tkinter import filedialog
import PyPDF2

def openfile():
    filename = filedialog.askopenfilename(
        title="Open PDF File",
        initialdir=r'F:\PROGRAMMING\MY PROJECTS\PDF TEXT EXTRACTOR',
        filetypes=[('PDF files', '*.pdf')]
    )
    if filename:
        filename_label.config(text=filename)
        outputfile_text.delete("1.0", tkinter.END)
        with open(filename, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                current_text = page.extract_text()
                if current_text:
                    outputfile_text.insert(tkinter.END, current_text + "\n")

def savefile():
    text = outputfile_text.get("1.0", tkinter.END).strip()
    if text:
        save_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            title="Save as"
        )
        if save_path:
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(text)

def delete_text():
    outputfile_text.delete("1.0", tkinter.END)

root = tkinter.Tk()
root.title("PYTHON TEXT EXTRACTOR")
root.configure(bg="#2e3f4f")  # Set window background color

filename_label = tkinter.Label(root, text="No File Selected", bg="#2e3f4f", fg="white")
outputfile_text = tkinter.Text(root, wrap="word", width=80, height=25, bg="#f4f4f4", fg="#222")
openfile_button = tkinter.Button(
    root,
    text="OPEN PDF FILE",
    command=openfile,
    bg="#4caf50",
    fg="white",
    activebackground="#357a38",
    activeforeground="white"
)
savefile_button = tkinter.Button(
    root,
    text="SAVE TEXT",
    command=savefile,
    bg="#2196f3",
    fg="white",
    activebackground="#1769aa",
    activeforeground="white"
)
delete_button = tkinter.Button(
    root,
    text="DELETE TEXT",
    command=delete_text,
    bg="#f44336",
    fg="white",
    activebackground="#aa2e25",
    activeforeground="white"
)

filename_label.pack(pady=5)
openfile_button.pack(pady=5)
savefile_button.pack(pady=5)
delete_button.pack(pady=5)
outputfile_text.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()
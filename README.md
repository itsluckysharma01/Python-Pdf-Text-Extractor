# Python-Pdf-Text-Extractor

Based on your `main.py` script, here's an engaging and professional **project description** and **interactive `README.md`** for your **PDF Text Extractor** Tkinter app:

---

## 🔖 Project Description

**PDF Text Extractor** is a lightweight desktop tool built using **Python**, **Tkinter**, and **PyPDF2**. It allows users to open any PDF file through a graphical interface and extract readable text from it instantly. This application is ideal for students, researchers, or anyone who frequently needs to review or copy content from PDF documents.

---

## 📝 Interactive README.md

````markdown
# 📄 PDF Text Extractor GUI

A simple Python desktop application to extract and display text from PDF files using a graphical user interface built with **Tkinter** and **PyPDF2**.

---

## 🌟 Features

- 🖱️ One-click PDF file selection
- 📄 Automatically extracts text from all pages
- 🪟 Clean and scrollable text display area
- 🧰 Lightweight and easy to use
- 💻 Ideal for offline use without Adobe Reader

---

## 🎥 How It Works

1. Launch the application.
2. Click on the `OPEN PDF FILE` button.
3. Select any `.pdf` file from your system.
4. The extracted text will be displayed in the application window.

---

## 📌 Requirements

Before running the project, make sure you have the following installed:

```bash
pip install PyPDF2
````

---

## 💡 Code Overview

```python
import tkinter, PyPDF2
from tkinter import filedialog

def openfile():
    filename = filedialog.askopenfilename(title="Open PDF File",
                                          initialdir='F:/PROGRAMMING/MY PROJECTS/PDF TEXT EXTRACTOR',
                                          filetypes=[('pdf files', '*.pdf')])
    outputfile_text.delete("1.0", tkinter.END)
    reader = PyPDF2.PdfReader(filename)
    for i in range(reader.numPages):
        current_text = reader.getPage(i).extractText()
        outputfile_text.insert(tkinter.END, current_text)

root = tkinter.Tk()
root.title("PYTHON TEXT EXTRACTOR")

filename_label = tkinter.Label(root, text="No File Selected")
outputfile_text = tkinter.Text(root)
openfile_button = tkinter.Button(root, text="OPEN PDF FILE", command=openfile)

filename_label.pack()
outputfile_text.pack()
openfile_button.pack()

root.mainloop()
```

---

## 📁 Folder Structure

```
PDF TEXT EXTRACTOR/
├── main.py          # Main GUI application
└── README.md        # Project documentation
```

---

## 🛠️ Improvements You Can Add

* ✅ Add scrollbars to the text box
* ✅ Support for image-based PDFs using OCR (e.g., Tesseract)
* ✅ Save extracted text as `.txt` file
* ✅ Dark mode toggle

---

## 📃 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🙌 Author

Created by [Lucky Sharma](https://github.com/itsluckysharma01) 🧑‍💻

```



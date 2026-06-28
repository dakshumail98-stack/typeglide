# typeglide

A smooth typewriter text effect library for Python — made by dakshu.

## Installation
```bash
pip install typeglide
```

## How to use it?

### Simple code to use:

```python
import typeglide

glide = typeglide.save("Hello World", delay=0.05)  # Save The Text
print(glide)  # Print The Animated text
```

### This now works with tkinter 🐱

```python
import typeglide
import tkinter as tk

glide = typeglide.save("Hello World", delay=0.05)

def do():
    glide.animate_widget(label)

root = tk.Tk()
label = tk.Label(text="hi")
label.pack()
button = tk.Button(text="press", command=do)
button.pack()
root.mainloop()
```

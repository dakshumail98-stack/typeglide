# typeglide

A smooth typewriter text effect library for Python. Works with tkinter too!

This library is made by Daksh Sharma who is easily known as Dakshu.

## Installation
```bash
pip install typeglide
```

---

## Functions

### `typeglide.write(text, delay, end)`
Prints text to the terminal character by character.
```python
import typeglide
typeglide.write("Hello World", delay=0.05)
```

---

### `typeglide.erase(text, delay)`
Erases text character by character using backspaces.
```python
import typeglide
typeglide.write("Hello!", delay=0.05, end="")
typeglide.erase("Hello!", delay=0.05)
```

---

### `typeglide.save(text, delay, end)`
Saves text and settings into a reusable `Glide` object.
```python
import typeglide
glide = typeglide.save("Hello World", delay=0.05)
```

---

## Glide Object Methods

### `print(glide)` — animate in terminal
```python
import typeglide
glide = typeglide.save("Hello World", delay=0.05)
print(glide)
```

### `glide.erase()` — erase from terminal
```python
glide.erase()
```

### `glide.type_and_erase(pause)` — type then erase
```python
glide.type_and_erase(pause=1)  # types it out, waits 1s, then erases it
```

### `glide.animate_widget(widget)` — animate into a tkinter widget
```python
glide.animate_widget(label)
glide.animate_widget(button)
```

### `glide.erase_widget(widget)` — erase from a tkinter widget
```python
glide.erase_widget(label)
```

### `glide.text` — get the raw text (for static use)
```python
button.config(text=glide.text)
```

---

## How to use it?

### Simple terminal example:
```python
import typeglide

glide = typeglide.save("Hello World", delay=0.05)  # Save The Text
print(glide)  # Print The Animated text
```

### Tkinter example 🐱
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

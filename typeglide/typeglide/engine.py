import sys
import time


def write(text, delay=0.05, end="\n"):
    """
    Prints text to the console character by character.

    :param text: The string to print.
    :param delay: Time in seconds between each character.
    :param end: The character to print at the very end (defaults to newline).
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()


class Glide:
    """
    A saveable typewriter-effect object.

    Usage:
        glide = typeglide.save("Hello", delay=0.05)

        # Terminal — animates character by character:
        print(glide)

        # Tkinter static text:
        button.config(text=glide.text)

        # Tkinter animated text:
        glide.animate_widget(button)
    """

    def __init__(self, text, delay=0.05, end="\n"):
        self.text = text
        self.delay = delay
        self.end = end

    def __str__(self):
        for char in self.text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(self.delay)
        return ""

    def __repr__(self):
        return f"Glide({self.text!r}, delay={self.delay})"

    def animate_widget(self, widget, attr="text"):
        """
        Animate the text into a tkinter widget one character at a time.

        :param widget: Any tkinter widget that supports .config().
        :param attr:   The config attribute to update (default 'text').

        Example:
            glide.animate_widget(button)
            glide.animate_widget(label)
        """
        delay_ms = int(self.delay * 1000)

        def _step(index):
            widget.config(**{attr: self.text[:index]})
            if index < len(self.text):
                widget.after(delay_ms, _step, index + 1)

        _step(0)


def save(text, delay=0.05, end="\n"):
    """
    Save a typewriter-effect string for later use.

    :param text:  The string to animate.
    :param delay: Time in seconds between each character.
    :param end:   End character used when printing (defaults to newline).
    :returns:     A Glide object.
    """
    return Glide(text, delay=delay, end=end)

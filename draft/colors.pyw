#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Jérémie DECOCK (http://www.jdhp.org)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import random
import tkinter as tk

color_list = [
        {"tk":"black", "fr":"noir"},
        {"tk":"white", "fr":"blanc"},
        {"tk":"red", "fr":"rouge"},
        {"tk":"green", "fr":"vert"},
        {"tk":"blue", "fr":"bleu"},
#        {"tk":"brown", "fr":"marron"},
#        {"tk":"gray", "fr":"gris"},
#        {"tk":"orange", "fr":"orange"},
#        {"tk":"pink", "fr":"rose"},
        {"tk":"yellow", "fr":"jaune"}
    ]

class Window:
    def __init__(self):
        self.fullscreen = False

        # Make the main window
        self.root = tk.Tk()

        self.root.title("Couleurs")

        self.frame = tk.Frame(self.root, width=200, height=200)
        self.frame.pack(expand=True, fill="both", padx=3, pady=3)

        self.label = tk.Label(self.root, text="")
        self.label.pack(expand=False, fill="x", padx=3, pady=3)

        self.root.bind("<Return>", self.next_color_callback)
        self.root.bind("<space>", self.next_color_callback)
        self.root.bind("<f>", self.fullscreen_callback)
        self.root.bind("<F>", self.fullscreen_callback)
        self.root.bind("<Escape>", lambda event: root.quit())

        self.next_color()

    def fullscreen_callback(self, event):
        if self.fullscreen:
            self.root.attributes('-fullscreen', False)
            self.fullscreen = False
        else:
            self.root.attributes('-fullscreen', True)
            self.fullscreen = True

    def next_color_callback(self, event):
        self.next_color()

    def next_color(self):
        color = random.choice(color_list)
        self.frame["bg"] = color["tk"]
        self.label["text"] = color["fr"]

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    win = Window()
    win.run()

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:40:29 2020

@author: User
"""

import pyttsx3
import PyPDF2
book=open('keph202.pdf','rb')
a=PyPDF2.PdfFileReader(book)
page=a.numPages
print(page)
engine=pyttsx3.init()
b=a.getPage(5)
text=b.extractText()
engine.say(text)
engine.runAndWait()
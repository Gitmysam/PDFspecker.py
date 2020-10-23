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

import PyPDF2
# from nltk import FreqDist
# import os
# from os import path
from unidecode import unidecode
from wordcloud import WordCloud
import matplotlib.pyplot as plt

folder = "C:\\Users\\alex\\Google Drive\\Livros\\DataScience\\"
file = "storytelling-with-data-cole-nussbaumer-knaflic.pdf"

def extract_text(fpath, output):
    pdffileobj = open(fpath, 'rb')
    pdfreader = PyPDF2.PdfFileReader(pdffileobj)
    x = pdfreader.numPages
    with open(output, "a") as file_object:
        for i in range(1, x):
            pageobj = pdfreader.getPage(i)
            text = pageobj.extractText()
            file_object.write(str(unidecode(text)).strip())


def create_wordcloud(text):
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


outputfile = ".\\output.txt"
# # extract_text(folder + file, outputfile)
# with open(outputfile) as f:
#     text = f.read()
#     create_wordcloud(text)
#     print("")

text = None
with open(outputfile, "r") as file_object:
    text = file_object.read()

with open(".\\output_ascii.txt", "w") as f:
    f.write(str(unidecode(text)).strip())


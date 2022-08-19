import streamlit as st
import os
import pytesseract
from PIL import Image
from pytesseract import Output



count = 0;
for root_dir, cur_dir, files in os.walk(r'C:\PictureDownload'):
    count += len(files);
print('files count:', count)  


st.write(count)

import pytesseract
from PIL import Image
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#img = Image.open('20220711122009597_1_1_1.jpg')
s = '20220711183010711_1_1_3.jpg'
#s1 = 'C:\\Users\\Amol\\Desktop\\streamlit-examples\\multipages'
#s2 = '\\';
#s3 = s1 + s2 + s; 
#print(s3);
st.write(s)
#st.write(s3)
#img = Image.open(r'C:\Users\Amol\Desktop\streamlit-examples\20220711183010711_1_1_3.jpg')
img = Image.open(s)
st.image(img)
img.load()
a = pytesseract.image_to_string(img, lang='eng')#'eng' for english
global b
st.write(a)
a = a.replace(" ", "")
print(a)
#print(a[22:32])
a = a[28:38];
st.write(a)

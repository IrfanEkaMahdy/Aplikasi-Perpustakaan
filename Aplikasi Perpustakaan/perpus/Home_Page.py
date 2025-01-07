import time
import sys
import os
import datetime
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Home Page", page_icon="📚", layout="centered")

st.title(body="📚Selamat Datang Di Perpustakaan")

st.write("Berikut ini adalah daftar buku yang tersedia di perpustakaan kami")
image = Image.open('./assets/images/1.jpg')
image1 = Image.open('./assets/images/2.jpg')
image2 = Image.open('./assets/images/3.jpg')
image3 = Image.open('./assets/images/4.jpg')
image4 = Image.open('./assets/images/5.jpg')
image5 = Image.open('./assets/images/6.jpg')
image6 = Image.open('./assets/images/7.jpg')
image7 = Image.open('./assets/images/8.jpg')
image8 = Image.open('./assets/images/9.jpg')
image9 = Image.open('./assets/images/10.jpg')
image10 = Image.open('./assets/images/11.jpg')
image11 = Image.open('./assets/images/12.jpg')
image12 = Image.open('./assets/images/13.jpg')
image13 = Image.open('./assets/images/14.jpg')
image14 = Image.open('./assets/images/15.jpg')
image15 = Image.open('./assets/images/16.jpg')
image16 = Image.open('./assets/images/17.jpg')

cols = st.columns((1,1,1))
cols1 = st.columns((1,1,1))
cols2 = st.columns((1,1,1))
cols3 = st.columns((1,1,1))
cols4 = st.columns((1,1,1))
cols5 = st.columns((1,1,1))

cols[0].image(image,width=200)
cols[0].write("Tersedia 3 Buku")
cols[1].image(image1,width=200)
cols[1].write("Tersedia 2 Buku")
cols[2].image(image2,width=200)
cols[2].write("Tersedia 4 Buku")

cols1[0].image(image3,width=200)
cols1[0].write("Tersedia 1 Buku")
cols1[1].image(image4,width=200)
cols1[1].write("Tersedia 2 Buku")
cols1[2].image(image5,width=200)
cols1[2].write("Tersedia 2 Buku")

cols2[0].image(image6,width=200)
cols2[0].write("Tersedia 4 Buku")
cols2[1].image(image7,width=200)
cols2[1].write("Tersedia 8 Buku")
cols2[2].image(image8,width=200)
cols2[2].write("Tersedia 2 Buku")

cols3[0].image(image9,width=200)
cols3[0].write("Tersedia 3 Buku")
cols3[1].image(image10,width=217)
cols3[1].write("Tersedia 7 Buku")
cols3[2].image(image11,width=215)
cols3[2].write("Tersedia 4 Buku")

cols4[0].image(image12,width=200)
cols4[0].write("Tersedia 2 Buku")
cols4[1].image(image13,width=210)
cols4[1].write("Tersedia 3 Buku")
cols4[2].image(image14,width=200)
cols4[2].write("Tersedia 1 Buku")

cols5[0].image(image15,width=217)
cols5[0].write("Tersedia 5 Buku")
cols5[1].image(image16,width=225)
cols5[1].write("Tersedia 6 Buku")



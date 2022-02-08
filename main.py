
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門")


"""### ■プログレスバーの表示"""
st.write("プログレスバーの表示")
"start!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.03)

"Done!"

"""### ■エクスぱんだー"""
expander1 = st.expander("問い合わせ")
expander1.write("回答")



"""### ■2カラムレイアウト"""
l_column, r_column = st.columns(2)
button = l_column.button("右からむに文字を表示")
if button:
    r_column.write("ここは右カラム")


"""### ■スライダー"""
condition = st.slider("あなたの今の調子は?", 0, 100, 50)
"コンディション:", condition



"""### ■テキストボックス"""
st.write("interactive widgets")

text = st.sidebar.text_input("あなたの趣味は")
"あなたの趣味は", text, "です"



"""### ■セレクトボックス"""
option = st.selectbox(
    "あなたが好きな数字",
    list(range(1,11))
)
"あなたの好きな数字は、", option, "です"


"""### ■チェックボックス"""
if st.checkbox('Show Image'):
    st.write("Display Image")
    img = Image.open("D:\OneDrive\画像\IMG_2456.JPG")
    st.image(img, caption='shuma', use_column_width=True)


"""### ■.pyの実行 \n
streamlit run main.py をターミナルで実行"""

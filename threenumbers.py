import streamlit as st

colh1, colh2, colh3 = st.columns((1,7,1))
colh2.title("LARGEST OF THE 3 NUMBERS")

col1, col2, col3 =st.columns((1,1,1))
num1 = col1.selectbox("Select the first number", [x for x in range(0,10000)])
num2 = col2.selectbox("Select the second number", [x for x in range(0,10000)])
num3 = col3.selectbox("Select the third number", [x for x in range(0,10000)])


col_a, col_b, col_c = st.columns([1.5,1,1.5])
col9,col10,col11 = st.columns([2,2,2])
if col_b.button("Get largest number"):
    result = max(num1, num2, num3)
    col10.success("Largest number is {}".format(result))

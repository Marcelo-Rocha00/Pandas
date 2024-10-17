import streamlit as st 
import pandas as pd 
import plotly.express as px 
import plotly.graph_objects as go 
import numpy

#sidebar
st.sidebar.header("Filtros")

#elementos de texto

st.title("Isso é um :blue[título] :sunglasses:")
st.header("Isso aqui é um cabeçalho", divider="red")
st.subheader("Isso aqui é um sub-cabeçalho", divider=True)
st.text("Isso aqui é um texto.")

#elementos de dados:
df = pd.DataFrame(numpy.random.randn(50,20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)

#elementos de seleção:

#CheckBox
selecao1 = st.checkbox("Marcado")

if selecao1:
    st.write(selecao1)

#cor
cor = st.color_picker("Selecione a cor", "#00f900")
st.write("cor selecionada", cor)

#multiselect
opcoes = st.multiselect(
    "selecione as opções",
    ['Green','Yellow','Red','Blue','Rainbow','Black']
)

st.write("Sua seleção", opcoes)

#Radio
genero = st.radio(
    "Qual seu estilo de filme favorito ?",
    [":rainbow[comedia]", "***Drama***", "Documentario :movie_camera:"],
    captions=[
        "Você é o engraçadinho.",
        "Vai chorar manda audio.",
        "Só quer ser o inteligente."
        ],
)

if genero == ":rainbow[comedia]":
    st.write("Você selecionou comedia.")
elif genero ==  "***Drama***":
    st.write("Você selecionou Drama ")
elif genero == "Documentario :movie_camera:":
    st.write("Você selecionou Documentario")
else:
    st.write("Você não selecionou nenhuma das opções")
    
#selectbox

option = st.selectbox(
    "Qual o seu melhor contato?",
    ("E-mail","Telefone","Celular")
)
st.write("Você selecionou:", option)

#slider
start_color, end_color = st.select_slider(
    "Selecione  o range das cores",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],
    value=("red", "blue"),
)

#Toggle
on = st.toggle("Activate feature")

if on:
    st.write("Feature activate")

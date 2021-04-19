import streamlit as st
import time
import base64
from pytube import YouTube


st.set_page_config(
    page_title="Vídeo Download App",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="auto",)

st.sidebar.write("## 🎵️ Áudio e Vídeo Download 🎬 ")
st.sidebar.selectbox('Tipo de Mídia', ['Vídeo', 'Áudio'])


def url_video():
    # Recebe a url do youtube para baixar o arquivo
    url_tube = st.text_input('Informe a URL do vídeo', help='Copie e cole uma url na caixa de texto.')

    if url_tube != '':
        yt = YouTube(url_tube)
        with st.spinner('**Por favor aguarde...**'):
            time.sleep(2)
        file_name = yt.title
        st.write('**Download** ' + file_name + '** iniciado...**')
        yt.streams.first().download()
        path = file_name + '.mp4'
        download_file(path)


def download_file(file_name):
    with open(file_name, "rb") as file:
        byte = file.read()
        b64 = base64.b64encode(byte).decode()
        href = f'<a href="data:file/mp4;base64,{b64}" download="{file_name}">Fazer Download</a>'
        st.success('**Download** ' + file_name + '** Concluído!**')
        st.markdown(href, unsafe_allow_html=True)


if __name__ == '__main__':
    url_video()

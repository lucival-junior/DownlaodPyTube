import streamlit as st
import time
import base64
from pytube import YouTube
import os


st.set_page_config(
    page_title="Vídeo Download App",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="auto",)

st.write("## 🎵️ Áudio e Vídeo Download 🎬 ")

litas_resolucao_padrao = ['1080p', '720p', '480p', '360p', '240p', '144p']
lista_resolucao_disponivel = ['']


def url_video():
    # Recebe a url do youtube para baixar o arquivo
    url_tube = st.text_input('Informe a URL do vídeo', help='Exemplo: https://youtu.be/5b9Z8toVaAU')
    if url_tube != '':
        yt = YouTube(url_tube)
        tipo_midia = st.selectbox('Escolha: ', ['', 'Áudio', 'Vídeo'])
        file_name = yt.title
        path_mp4 = file_name + '.mp4'
        filtro_video = yt.streams.filter(progressive=True, file_extension='mp4')
        filtro_audio = yt.streams.filter(only_audio=True, mime_type='audio/mp4')

        if tipo_midia == 'Vídeo':
            for res in litas_resolucao_padrao:
                qualidade = filtro_video.get_by_resolution(res)
                if qualidade is not None:
                    lista_resolucao_disponivel.append(res)
            resolucao = st.selectbox('Selecione a qualidade do Vídeo disponível:', lista_resolucao_disponivel, index=0)

            if resolucao != '':
                with st.spinner('**Por favor aguarde...**'):
                    time.sleep(2)
                st.write('**Download** ' + file_name + '** iniciado...**')
                video = yt.streams.filter(progressive=True, resolution=resolucao, file_extension='mp4')
                video.first().download()
                download_file_video(path_mp4)

        elif tipo_midia == 'Áudio':
            filtro_audio.first().download()
            path_mp4 = file_name + '.mp4'
            path_mp3 = file_name + '.mp3'
            os.rename(path_mp4, path_mp3)

            st.write('**Download** ' + file_name + '** iniciado...**')
            download_file_audio(path_mp3)
        else:
            st.write('Escolha uma opção!')

def download_file_video(file_name):
    with open(file_name, "rb") as file:
        byte = file.read()
        b64 = base64.b64encode(byte).decode()
        href = f'<a href="data:file/mp4;base64,{b64}" download="{file_name}">Fazer Download</a>'
        st.markdown(href, unsafe_allow_html=True)
        st.success('**Download de Vídeo Concluído!**')


def download_file_audio(file_name):
    with open(file_name, "rb") as file:
        byte = file.read()
        b64 = base64.b64encode(byte).decode()
        href = f'<a href="data:file/mp4;base64,{b64}" download="{file_name}">Fazer Download</a>'
        st.markdown(href, unsafe_allow_html=True)
        st.success('**Download de Áudio Concluído!**')


if __name__ == '__main__':
    url_video()

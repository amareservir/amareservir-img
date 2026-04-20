import os
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

pasta_origem = r"F:\DEV\IGREJA\amareservir-img\Photos-3-001"

def pegar_data_exif(caminho_imagem):
    try:
        imagem = Image.open(caminho_imagem)
        exif = imagem._getexif()

        if exif is not None:
            for tag, valor in exif.items():
                nome_tag = TAGS.get(tag, tag)
                if nome_tag == "DateTimeOriginal":
                    return datetime.strptime(valor, "%Y:%m:%d %H:%M:%S")
    except:
        pass
    return None

for arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, arquivo)

    if os.path.isfile(caminho_arquivo):
        data = pegar_data_exif(caminho_arquivo)

        if data is None:
            timestamp = os.path.getmtime(caminho_arquivo)
            data = datetime.fromtimestamp(timestamp)

        nome_pasta = data.strftime("%d-%m-%Y")
        caminho_pasta = os.path.join(pasta_origem, nome_pasta)

        os.makedirs(caminho_pasta, exist_ok=True)

        novo_caminho = os.path.join(caminho_pasta, arquivo)

        print(f"Movendo: {arquivo} -> {nome_pasta}/")
        os.rename(caminho_arquivo, novo_caminho)

print("Finalizado.")
from PIL import Image
import os


def reduzir_dimensionalidade(imagem, modo="tons_de_cinza", limiar=128):
    """ Reduz a dimensionalidade de uma imagem para tons de cinza ou preto e branco. """
    imagem = imagem.convert("RGB")
    largura, altura = imagem.size
    imagem_reduzida = Image.new("L", (largura, altura))  # Imagem em modo L (tons de cinza)

    for x in range(largura):
        for y in range(altura):
            r, g, b = imagem.getpixel((x, y))
            cinza = int((r + g + b) / 3)  # Converter para tons de cinza

            if modo == "preto_branco":
                pixel_reduzido = 255 if cinza >= limiar else 0
            else:
                pixel_reduzido = cinza

            imagem_reduzida.putpixel((x, y), pixel_reduzido)

    return imagem_reduzida


# Caminho da imagem
caminho_imagem = "dog.jpg"  # Substitua pelo caminho da sua imagem
imagem_original = Image.open(caminho_imagem)

# Pasta de saída
pasta_saida = "./"  # Salva na pasta atual do projeto

# Converter para tons de cinza e salvar
imagem_cinza = reduzir_dimensionalidade(imagem_original, modo="tons_de_cinza")
caminho_cinza = os.path.join(pasta_saida, "imagem_tons_de_cinza.jpg")
imagem_cinza.save(caminho_cinza)
print(f"Imagem em tons de cinza salva em: {caminho_cinza}")

# Converter para preto e branco e salvar
imagem_pb = reduzir_dimensionalidade(imagem_original, modo="preto_branco", limiar=128)
caminho_pb = os.path.join(pasta_saida, "imagem_preto_branco.jpg")
imagem_pb.save(caminho_pb)
print(f"Imagem em preto e branco salva em: {caminho_pb}")

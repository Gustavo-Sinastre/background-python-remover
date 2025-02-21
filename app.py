from rembg import remove, new_session

# Caminho da imagem de entrada e saída
nome_imagem = input("Digite o nome e formato da imagem na pasta: ")
nome_imagem_sem_fundo = f"{nome_imagem.rsplit('.', 1)[0]}.png"

# Cria sessão com modelo mais usual para pessoas"
session = new_session("u2net_human_seg")

# Carrega a imagem
with open(nome_imagem, "rb") as inp_file:
    input_image = inp_file.read()

# Remove o fundo da imagem
output_image = remove(input_image, session=session)

# Salva a imagem sem fundo
with open(nome_imagem_sem_fundo, "wb") as out_file:
    out_file.write(output_image)

print(f"Você é o cara 😊 {nome_imagem_sem_fundo}")
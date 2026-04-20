import os

# ===== CONFIG =====
diretorio = r"F:\DEV\IGREJA\amareservir-img\GALERIA"
ano = "2026"

# ==================

for nome in os.listdir(diretorio):
    caminho_antigo = os.path.join(diretorio, nome)

    # Só mexe se for pasta
    if os.path.isdir(caminho_antigo):
        partes = nome.split(" ")

        # Espera algo tipo "01-04 QUARTA"
        if len(partes) >= 2 and "-" in partes[0]:
            data = partes[0]
            resto = " ".join(partes[1:])

            # Evita duplicar o ano
            if len(data.split("-")) == 2:
                novo_nome = f"{data}-{ano} {resto}"
                caminho_novo = os.path.join(diretorio, novo_nome)

                print(f"Renomeando: {nome} -> {novo_nome}")
                os.rename(caminho_antigo, caminho_novo)

print("Finalizado.")
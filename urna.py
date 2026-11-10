# Importando os dados do outro arquivo que criamos
from candidatos import (
    candidato_estadual, votos_estadual,
    candidato_federal, votos_federal,
    candidato_senador, votos_senador,
    candidato_governador, votos_governador,
    candidato_presidente, votos_presidente
)

print("")
print("")

print("\n========================================")
print("       BEM-VINDO À URNA ELETRÔNICA      ")
print("========================================")

print("\n--- INICIANDO A URNA ELETRÔNICA ---")

# Exemplo de votação para Deputado Estadual (2 votos)
print("\n--- VOTAÇÃO PARA DEPUTADO ESTADUAL (Escolha 2 candidatos) ---")
for numero, info in candidato_estadual.items():
    if numero != 0:
        print(f"Número {numero} - {info['nome']} ({info['partido']})")

votos_computados_eleitor = []
while len(votos_computados_eleitor) < 2:
    voto_usuario = int(input(f"\nDigite o número do {len(votos_computados_eleitor) + 1}º candidato: "))
    22
    if voto_usuario in candidato_estadual:
        if voto_usuario not in votos_computados_eleitor:
            votos_computados_eleitor.append(voto_usuario)
            votos_estadual[voto_usuario] += 1
            print("Voto registrado!")
        else:
            print("Você já votou nesse candidato!")
    else:
        print("Candidato não encontrado. Voto nulo.")
        votos_estadual[0] += 1
        votos_computados_eleitor.append(0)

# Exibindo resultado parcial de estadual com nomes um abaixo do outro
print("\n--- RESULTADO PARCIAL: DEPUTADO ESTADUAL ---")
for num, qtd in votos_estadual.items():
    nome = candidato_estadual[num]["nome"]
    partido = candidato_estadual[num]["partido"]
    print(f"• {nome} ({partido}): {qtd} voto(s)")

print("")
print("")


print(" ============================================================")
print("|             VOTAÇÃO PARA DEPUTADO FEDERAL                  |")
print(" ============================================================")

# Exemplo de votação para Deputado federal (2 votos)
print("\n--- VOTAÇÃO PARA DEPUTADO FEDERAL (Escolha 2 candidatos) ---")
for numero, info in candidato_federal.items():
    if numero != 0:
        print(f"Número {numero} - {info['nome']} ({info['partido']})")

votos_computados_eleitor = []
while len(votos_computados_eleitor) < 2:
    voto_usuario = int(input(f"\nDigite o número do {len(votos_computados_eleitor) + 1}º candidato: "))
    if voto_usuario in candidato_federal:
        if voto_usuario not in votos_computados_eleitor:
            votos_computados_eleitor.append(voto_usuario)
            votos_federal[voto_usuario] += 1
            print("Voto registrado!")
        else:
            print("Você já votou nesse candidato!")
    else:
        print("Candidato não encontrado. Voto nulo.")
        votos_federal[0] += 1
        votos_computados_eleitor.append(0)

# Exibindo resultado parcial de estadual com nomes um abaixo do outro
print("\n--- RESULTADO PARCIAL: DEPUTADO FEDERAL ---")
for num, qtd in votos_federal.items():
    nome = candidato_federal[num]["nome"]
    partido = candidato_federal[num]["partido"]
    print(f"• {nome} ({partido}): {qtd} voto(s)")

print("")
print("")


print(" ============================================================")
print("|                   VOTAÇÃO PARA SENADOR                     |")
print(" ============================================================")

# Exemplo de votação para Senador (2 votos)
print("\n--- VOTAÇÃO PARA SENADOR (Escolha 2 candidatos) ---")
for numero, info in candidato_senador.items():
    if numero != 0:
        print(f"Número {numero} - {info['nome']} ({info['partido']})")

votos_computados_eleitor = []
while len(votos_computados_eleitor) < 2:
    voto_usuario = int(input(f"\nDigite o número do {len(votos_computados_eleitor) + 1}º candidato: "))
    if voto_usuario in candidato_senador:
        if voto_usuario not in votos_computados_eleitor:
            votos_computados_eleitor.append(voto_usuario)
            votos_senador[voto_usuario] += 1
            print("Voto registrado!")
        else:
            print("Você já votou nesse candidato!")
    else:
        print("Candidato não encontrado. Voto nulo.")
        votos_senador[0] += 1
        votos_computados_eleitor.append(0)

# Exibindo resultado parcial de estadual com nomes um abaixo do outro
print("\n--- RESULTADO PARCIAL: SENADOR ---")
for num, qtd in votos_senador.items():
    nome = candidato_senador[num]["nome"]
    partido = candidato_senador[num]["partido"]
    print(f"• {nome} ({partido}): {qtd} voto(s)")


print("")
print("")


print(" ============================================================")
print("|                   VOTAÇÃO PARA GOVERNADOR                  |")
print(" ============================================================")

# Exemplo de votação para Senador (1 votos)
print("\n--- VOTAÇÃO PARA GOVERNADOR (Escolha 1 candidatos) ---")
for numero, info in candidato_governador.items():
    if numero != 0:
        print(f"Número {numero} - {info['nome']} ({info['partido']})")

votos_computados_eleitor = []
while len(votos_computados_eleitor) < 1:
    voto_usuario = int(input(f"\nDigite o número do {len(votos_computados_eleitor) + 1}º candidato: "))
    if voto_usuario in candidato_governador:
        if voto_usuario not in votos_computados_eleitor:
            votos_computados_eleitor.append(voto_usuario)
            votos_governador[voto_usuario] += 1
            print("Voto registrado!")
        else:
            print("Você já votou nesse candidato!")
    else:
        print("Candidato não encontrado. Voto nulo.")
        votos_governador[0] += 1
        votos_computados_eleitor.append(0)

# Exibindo resultado parcial de estadual com nomes um abaixo do outro
print("\n--- RESULTADO PARCIAL: GOVERNADOR ---")
for num, qtd in votos_governador.items():
    nome = candidato_governador[num]["nome"]
    partido = candidato_governador[num]["partido"]
    print(f"• {nome} ({partido}): {qtd} voto(s)")

print("")
print("")


print(" ============================================================")
print("|                   VOTAÇÃO PARA PRESIDENTE                  |")
print(" ============================================================")

# Exemplo de votação para presidente (1 votos)
print("\n--- VOTAÇÃO PARA Presidente (Escolha 1 candidatos) ---")
for numero, info in candidato_presidente.items():
    if numero != 0:
        print(f"Número {numero} - {info['nome']} ({info['partido']})")

votos_computados_eleitor = []
while len(votos_computados_eleitor) < 1:
    voto_usuario = int(input(f"\nDigite o número do {len(votos_computados_eleitor) + 1}º candidato: "))
    if voto_usuario in candidato_presidente:
        if voto_usuario not in votos_computados_eleitor:
            votos_computados_eleitor.append(voto_usuario)
            votos_presidente[voto_usuario] += 1
            print("Voto registrado!")
        else:
            print("Você já votou nesse candidato!")
    else:
        print("Candidato não encontrado. Voto nulo.")
        votos_presidente[0] += 1
        votos_computados_eleitor.append(0)

# Exibindo resultado parcial de estadual com nomes um abaixo do outro
print("\n--- RESULTADO PARCIAL: GOVERNADOR ---")
for num, qtd in votos_presidente.items():
    nome = candidato_presidente[num]["nome"]
    partido = candidato_presidente[num]["partido"]
    print(f"• {nome} ({partido}): {qtd} voto(s)")

print("")
print("")

print("==========================================")
print("RESULTADO FINAL DA URNA ELETRÔNICA")
print("==========================================")
print("\n" + "="*50)
print("          APURAÇÃO FINAL DOS VOTOS          ")
print("="*50)

print("")
# 1. Deputado Estadual
print("\n--- DEPUTADO ESTADUAL ---")
for numero, qtd in votos_estadual.items():
    nome = candidato_estadual[numero]["nome"]
    partido = candidato_estadual[numero]["partido"]
    print(f"• {nome} ({partido}): {qtd} voto(s)")
print("")
# 2. Deputado Federal
print("\n--- DEPUTADO FEDERAL ---")
for numero, qtd in votos_federal.items():
    nome = candidato_federal[numero]["nome"]
    partido = candidato_federal[numero]["partido"]
    print(f"• {nome} ({partido}): {qtd} voto(s)")
print("")
# 3. Senador
print("\n--- SENADOR ---")
for numero, qtd in votos_senador.items():
    nome = candidato_senador[numero]["nome"]
    partido = candidato_senador[numero]["partido"]
    print(f"• {nome} ({partido}): {qtd} voto(s)")
print("")
# 4. Governador
print("\n--- GOVERNADOR ---")
for numero, qtd in votos_governador.items():
    nome = candidato_governador[numero]["nome"]
    partido = candidato_governador[numero]["partido"]
    print(f"• {nome} ({partido}): {qtd} voto(s)")
print("")
# 5. Presidente
print("\n--- PRESIDENTE ---")
for numero, qtd in votos_presidente.items():
    nome = candidato_presidente[numero]["nome"]
    partido = candidato_presidente[numero]["partido"]
    print(f"• {nome} ({partido}): {qtd} voto(s)")
print("")
print("\n" + "="*50)
print("FIM DA APURAÇÃO. OBRIGADO POR VOTAR!")
print("="*50)
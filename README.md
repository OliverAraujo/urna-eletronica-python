# 🗳️ Sistema de Urna Eletrônica em Python

Este é um projeto desenvolvido para simular uma **Urna Eletrônica** em ambiente de terminal utilizando a linguagem Python. O sistema permite cadastrar candidatos por cargo, registrar votos de múltiplos eleitores (com validação de votos e suporte a múltiplos votos em determinados cargos) e exibir uma apuração final organizada por nomes e partidos.

---

## 🚀 Funcionalidades

O sistema simula a votação em 5 cargos diferentes, respeitando as regras eleitorais de quantidade de votos:
1. **Deputado Estadual** (2 votos)
2. **Deputado Federal** (1 voto)
3. **Senador** (2 votos)
4. **Governador** (1 voto)
5. **Presidente** (1 voto)

* **Validação de votos:** Impede que o eleitor vote duas vezes no mesmo número na mesma categoria e trata votos digitados incorretamente como **Voto Nulo**.
* **Apuração detalhada:** Exibe a contagem final dos votos de forma limpa, mostrando o nome do candidato, o partido e o total de votos recebidos um abaixo do outro.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3** (Estruturas de dados como Dicionários, Listas e laços de repetição `while` / `for`).
* **Modularização** (Separação de dados e lógica em arquivos diferentes).
* **Git e GitHub** para controle de versão.

---

## 📂 Estrutura do Projeto

```text
projeto_eleicao/
│
├── candidatos.py   # Módulo contendo os dicionários de candidatos e contagem de votos
└── urna.py          # Arquivo principal com a lógica da votação e fluxo da urna

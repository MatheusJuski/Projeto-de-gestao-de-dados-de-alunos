# Projeto de Gestão de Dados de Alunos 🎓

<p align="center">
  <img src="https://socialify.git.ci/MatheusJuski/Projeto-de-gestao-de-dados-de-alunos/image?custom_language=Python&amp;font=Inter&amp;language=1&amp;name=1&amp;owner=1&amp;pattern=Solid&amp;theme=Dark" alt="project-image" />
</p>

Um sistema completo para o gerenciamento de dados acadêmicos de alunos, construído com Python (Flask), Jinja2, HTML/CSS e JavaScript. O sistema oferece uma interface amigável para a administração e visualização dos dados.

---

## 🛠️ Passos para instalação e configuração

1. **Configurar a API do Google Sheets:**

   - Crie um projeto no [Google Cloud Console](https://console.cloud.google.com/).
   - Ative a API do Google Sheets para esse projeto.
   - Crie credenciais de acesso do tipo "Service Account" e baixe o arquivo JSON com as credenciais.
   - Renomeie o arquivo para `credenciais.json` e coloque-o na raiz do projeto.

2. **Configurar a chave da planilha:**

   - No arquivo `config.py`, localize o campo para a chave da planilha do Google Sheets.
   - Insira a chave da sua planilha, que está na URL dela (entre `/d/` e `/edit`).

3. **Importante sobre os nomes das colunas:**

   - A planilha deve conter as colunas com exatamente os seguintes nomes (sensível a maiúsculas/minúsculas e espaços):

     ```
     "Nome completo:", "Foto", "Data de Nascimento:", "Naturalidade:", "CPF:", "RG:", "Órgão Emissor", "UF:", "País:", "Data de expedição do RG:", 
     "Número do celular", "Número para contato em caso de emergência", "Nome do contato de emergência:", "E-mail para recebimento de informações:", 
     "Endereço:", "Nº:", "Complemento:", "Bairro: ", "Cidade:", "CEP:", "Banco: ", "Agência:", "Tipo de conta:", "Número da Conta:", 
     "Currículo Lattes:", "Matricula", "LinkedIn "
     ```

   - Caso os nomes sejam diferentes, o sistema não funcionará corretamente. Você pode ajustar os nomes na planilha ou alterar o código para corresponder aos seus nomes.

---

## 💻 Tecnologias utilizadas

- Python (Flask)
- Jinja2 (template engine)
- HTML5 e CSS3
- JavaScript
- Google Sheets API

---

## 🚀 Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/MatheusJuski/Projeto-de-gestao-de-dados-de-alunos.git
   cd Projeto-de-gestao-de-dados-de-alunos
   
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
4. Configure o arquivo credenciais.json e a chave da planilha conforme explicado.
5. Execute o servidor Flask:
   ```bash
   flask run
6. Acesse a aplicação no navegador:
  ```bash
  http://localhost:5000

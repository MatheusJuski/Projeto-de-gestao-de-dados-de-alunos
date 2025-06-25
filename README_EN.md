# Student Data Management Project 🎓

<p align="center">
  <img src="https://socialify.git.ci/MatheusJuski/Projeto-de-gestao-de-dados-de-alunos/image?custom_language=Python&font=Inter&language=1&name=1&owner=1&pattern=Solid&theme=Dark" alt="project-image" />
</p>

A complete system for managing student's academic data, built with Python (Flask), Jinja2, HTML/CSS, and JavaScript. The system offers a user-friendly interface for managing and viewing data.

---

## 🛠️ Installation and Setup Steps

1. **Set up the Google Sheets API:**

   - Create a project in the [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the Google Sheets API for this project.
   - Create "Service Account" credentials and download the JSON file.
   - Rename the file to `credentials.json` and place it in the project root.

2. **Configure the spreadsheet key:**

   - In the `config.py` file, find the field for the Google Sheets spreadsheet key.
   - Insert your spreadsheet key, which is in the URL (between `/d/` and `/edit`).

3. **Important about column names:**

   - The spreadsheet must have columns with exactly the following names (case and space sensitive):

     ```
     "Nome completo:", "Foto", "Data de Nascimento:", "Naturalidade:", "CPF:", "RG:", "Órgão Emissor", "UF:", "País:", "Data de expedição do RG:", 
     "Número do celular", "Número para contato em caso de emergência", "Nome do contato de emergência:", "E-mail para recebimento de informações:", 
     "Endereço:", "Nº:", "Complemento:", "Bairro: ", "Cidade:", "CEP:", "Banco: ", "Agência:", "Tipo de conta:", "Número da Conta:", 
     "Currículo Lattes:", "Matricula", "LinkedIn "
     ```

   - If the names differ, the system will not work properly. You can adjust the column names in the spreadsheet or change the code to match your names.

---

## 💻 Technologies Used

- Python (Flask)
- Jinja2 (template engine)
- HTML5 and CSS3
- JavaScript
- Google Sheets API

---

## 🚀 How to Run Locally

1. Clone the repository:
   ```
   git clone https://github.com/MatheusJuski/Projeto-de-gestao-de-dados-de-alunos.git
   cd Projeto-de-gestao-de-dados-de-alunos
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure the `credentials.json` file and the spreadsheet key as explained.

5. Run the Flask server:
   ```
   flask run
   ```

6. Access the application in your browser:
   ```
   http://localhost:5000
   ```

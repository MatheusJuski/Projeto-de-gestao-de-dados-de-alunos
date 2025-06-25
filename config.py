import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sua-chave-secreta-aqui'
    # Configurações do Google Sheets
    GOOGLE_SHEETS_CREDENTIALS = 'credenciais.json' 
    SPREADSHEET_KEY = '' #adicionar a chave da planilha aqui
    
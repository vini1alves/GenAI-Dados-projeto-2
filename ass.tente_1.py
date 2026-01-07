import os
import webbrowser
import speech_recognition as sr
import google.generativeai as genai

# Configuração da API do Gemini
genai.configure(api_key="sua_api_key_aqui")
model = genai.GenerativeModel('gemini-1.5-flash')

def executar_comando(texto):
    texto = texto.lower()
    
    # Lógica de abertura de apps/sites
    if "google" in texto:
        print("Abrindo Google Chrome...")
        os.startfile("chrome.exe")
    elif ("edge" in texto) or ("edg" in texto)or ("microsoft edge" in texto)or ("ed" in texto):
        print("Abrindo Microsoft Edge...")
        os.startfile("msedge.exe")
    elif "youtube" in texto:
        print("Abrindo YouTube...")
        webbrowser.open("https://www.youtube.com/")
    elif "netflix" in texto:
        print("Abrindo o aplicativo Netflix...")
        webbrowser.open("https://www.netflix.com/browse")
    elif "crunchyroll" in texto:
        print("Abrindo Crunchyroll...")
        webbrowser.open("https://www.crunchyroll.com/pt-br/discover")
    elif "faculdade" in texto:
        print("Abrindo plataforma da faculdade...")
        webbrowser.open("https://estudante.wyden.com.br/disciplinas")
    elif "sql" in texto:
        print("Abrindo PostgreSQL...")
        os.startfile("C:/Program Files/PostgreSQL/18/pgAdmin 4/runtime/pgAdmin4.exe")
        
    else:
        # Se não for comando, tenta o Gemini, mas SEM TRAVAR o código
        print(f"Comando '{texto}' não reconhecido como tarefa local. Consultando Gemini...")
        try:
            response = model.generate_content(f"O usuário disse: {texto}. Responda de forma curta.")
            print("Gemini:", response.text)
        except Exception as e:
            # SE O GEMINI FALHAR, ELE CAI AQUI E O PROGRAMA CONTINUA RODANDO
            print(f"Erro ao falar com Gemini sobre '{texto}'. Voltando para o início...")

def ouvir_microfone():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\n--- Ajustando ruído ambiente... Aguarde.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Pode falar! Estou ouvindo...")
        
        try:
            audio = recognizer.listen(source, timeout=5)
            # Transcreve o áudio usando o serviço do Google (gratuito)
            transcricao = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {transcricao}")
            return transcricao
        except Exception as e:
            print("Não entendi ou o tempo esgotou.")
            return None

# Loop Principal
if __name__ == "__main__":
    while True:
        comando = ouvir_microfone()
        if comando:
            if "sair" in comando.lower() or "fechar" in comando.lower():
                print("Encerrando...")
                break
            executar_comando(comando)
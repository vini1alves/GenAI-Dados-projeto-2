 ###    Bootcamp Bradesco - GenAI & Dados

Este repositório reúne os projeto desenvolvidos durante o Bootcamp Bradesco - GenAI & Dados. O foco das atividades é a aplicação prática de Inteligência Artificial Generativa para otimização de processos, análise de dados e estruturação de conhecimento.

---

# 🎙️ Assistente de Voz Inteligente com Gemini AI & Automação Desktop

Este projeto é uma evolução de um desafio prático da **DIO (Digital Innovation One)**. Enquanto o projeto original focava em transcrição e tradução multi-idiomas utilizando OpenAI, decidi elevar o nível criando um **Assistente Virtual focado em produtividade no PC**, utilizando o poder do modelo **Gemini 1.5 Flash** da Google.

---

## 🚀 O que este projeto faz?
Diferente das soluções convencionais, este assistente não apenas responde perguntas; ele **age** no sistema operacional. Através de comandos de voz, o script é capaz de:

* **Automatizar o Navegador:** Abrir Google Chrome, Microsoft Edge, YouTube e plataformas de streaming (Netflix/Crunchyroll).
* **Foco nos Estudos:** Acesso direto à plataforma da faculdade e ferramentas de banco de dados (**PostgreSQL/pgAdmin**).
* **Inteligência Cognitiva:** Quando o comando não é uma tarefa local, o assistente utiliza a API do **Google Gemini** para processar a fala e fornecer respostas rápidas e inteligentes.
* **Robustez:** Implementação de tratamento de erros (try/except) para garantir que o assistente continue rodando mesmo se a conexão com a API falhar.

---

## 🛠️ Tecnologias Utilizadas
* **Python 3**: Linguagem base do projeto.
* **Google Gemini API (Generative AI)**: Para o processamento de linguagem natural e respostas inteligentes.
* **SpeechRecognition**: Para a captura e transcrição de áudio em tempo real.
* **Bibliotecas OS & Webbrowser**: Para interação direta com o sistema operacional Windows e navegadores.

---

## 💡 Como funciona 
1.  **Escuta Ativa:** O sistema utiliza `adjust_for_ambient_noise` para calibrar o microfone e garantir precisão.
2.  **Processamento Local:** O script verifica se a transcrição contém palavras-chave para abrir aplicativos ou sites específicos.
3.  **Integração Cloud:** Caso não seja um comando de sistema, o texto é enviado ao modelo **Gemini 1.5 Flash** para uma interação natural.
4.  **Resiliência:** O código opera em um loop contínuo, tratando falhas de rede ou de entendimento, e só encerra com os comandos "Sair" ou "Fechar".

---

## 👨‍💻 Evolução do Projeto 
Este repositório demonstra minha capacidade de ir além do proposto em aula:

* **Adaptação de Tecnologias:** Migrei a arquitetura original (Whisper/ChatGPT) para o ecossistema Google (Gemini), explorando novas APIs.
* **Customização Prática:** Foquei em resolver uma dor real do meu dia a dia: automatizar a abertura de ferramentas de trabalho e estudo (SQL, Faculdade) sem usar as mãos.
* **Clean Code:** Estruturei o código de forma modular, facilitando a manutenção e a adição de novos comandos.

---

## ⚙️ Como Executar
1. Instale as dependências:
   ```bash
   pip install google-generativeai speechrecognition PyAudio

### 👨‍💻 Autor

Desenvolvido por Vinícius durante o Bootcamp Bradesco em parceria com a DIO/Bradesco.

### 🌐 Conecte-se comigo
<div align="left">
  <a href="https://www.linkedin.com/in/vinicius-alves-aa1651171" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>
  <a href="mailto:viniciusnet22@live.com">
  <img src="https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white">
</a>
  <a href="https://youtu.be/pBW5QZ7_R6o?list=PLp0FvpKzHs0nJCBBKhWB2-XezWcUcwCiA" target="_blank"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white">
  </a>

<a href="https://www.youtube.com/embed/Q_5-2BmyCqk?si=78Sle00pNTq8cZuf" target="_blank"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white">
  </a><--video teste
 
</div>

---

### 📊 Estatísticas
[Estatísticas do GitHub](https://github-readme-stats.vercel.app/api?username=vini1alves&show_icons=true&theme=radical)

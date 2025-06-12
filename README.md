# Mensageiro 🚀📱

**Mensageiro** é um script em Python para enviar mensagens diárias personalizadas via Telegram para qualquer usuário, grupo ou canal que você quiser, com logs completos para monitorar sucesso e falhas. Perfeito para automação de mensagens, lembretes, conteúdos motivacionais e muito mais!

---

## 📬 O que o Mensageiro faz

- 📅 Envia mensagens diferentes para cada dia do mês (1 a 31)  
- 📝 Usa arquivo JSON para guardar todas as mensagens organizadas  
- 🔄 Substitui dinamicamente variáveis como `{DIA_SEMANA}` e `{DIA}` dentro das mensagens  
- 🤖 Funciona para qualquer chat_id Telegram (usuário, grupo ou canal)  
- 📜 Gera logs profissionais e separados de:  
  - Mensagens enviadas com sucesso (`envio_sucesso.log`)  
  - Erros e falhas detalhadas (`envio_erro.log`)  
- ⚡ Fácil de rodar via linha de comando, passando o chat_id como parâmetro  

---

## 🚀 Por que usar este script?

- Envie mensagens automáticas diárias sem esforço  
- Tenha total controle e registro do que foi enviado e possíveis erros  
- Permite personalizar as mensagens com facilidade, alterando o arquivo JSON  
- Ideal para bots, lembretes, campanhas, motivação e interações diárias  

---

## ⚙️ Requisitos

- Python 3.x  
- Biblioteca `requests` instalada (`pip install requests`)  
- Token válido do bot Telegram (criado pelo [@BotFather](https://t.me/BotFather))  
- Chat ID válido (usuário, grupo ou canal onde o bot tenha permissão para enviar mensagens)  

---

## 🛠️ Como configurar

1. **Crie seu bot no Telegram**  
   Converse com o [@BotFather](https://t.me/BotFather), crie um bot e copie o token gerado.

2. **Configure o script**  
   - Abra o arquivo `envio_mensagens.py`  
   - Substitua a variável `TOKEN` pelo seu token do bot Telegram.

3. **Prepare o arquivo de mensagens JSON**  
   Crie ou edite o arquivo `mensagens.json` com mensagens para cada dia, por exemplo:

```json
{
  "1": "📅 *Dia 1: Comece bem!* \n\nHoje é {DIA_SEMANA}, dia {DIA}. Vamos juntos!",
  "2": "📅 *Dia 2: Foco e força!* \n\n{DIA_SEMANA} chegou, aproveite o dia {DIA} para crescer."
  // ... até o dia 31
}

---

## 👤 Autor

**Carlos Henrique Tourinho Santana**
Desenvolvedor Backend, DevOps e Integrador de Sistemas embarcados, com sólida experiência em **automação com Shell Script, Python, C e C++**. Atua no desenvolvimento de soluções para **ESP32, Arduino e módulos GSM**, além de sistemas web com **PHP**.

Especialista em **bots para Telegram**, **monitoramento de servidores Linux**, automação de tarefas críticas e criação de ferramentas inteligentes para segurança e produtividade.

Criador do projeto **To Bem Informado**, que entrega mensagens diárias com carinho, inteligência e presença digital.

📍 *Salvador, Bahia – Brasil*
📫 Telegram: [@henriquetourinho](https://t.me/henriquetourinho)
🌐 Site: [henriquetourinho.com](https://henriquetourinho.com)
📧 E-mail: [henriquetourinho@riseup.net](mailto:henriquetourinho@riseup.net)
🐦 Twitter/X: [x.com/ryckybrasil](https://x.com/ryckybrasil)
📸 Instagram: [@henriquetourinhooficial](https://www.instagram.com/henriquetourinhooficial)

---


## 📄 Licença

Distribuído sob a licença MIT.
© 2025 Carlos Henrique Tourinho Santana.
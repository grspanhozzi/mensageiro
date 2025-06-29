# Mensageiro 📩

![Mensageiro](https://img.shields.io/badge/Mensageiro-telegram-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Introdução

O **Mensageiro** é uma ferramenta poderosa para o envio automático de mensagens diárias via Telegram. Este projeto permite que você envie mensagens personalizadas para múltiplos usuários, utilizando dados armazenados em formato JSON. O sistema também conta com logs detalhados e um tratamento profissional de erros, garantindo uma experiência robusta e confiável.

### Por que usar o Mensageiro?

- **Automação**: Simplifique o envio de mensagens diárias.
- **Flexibilidade**: Use mensagens personalizadas armazenadas em JSON.
- **Confiabilidade**: Logs detalhados ajudam na identificação de problemas.
- **Código aberto**: Contribua e melhore o projeto.

## Funcionalidades

- Envio automático de mensagens via Telegram.
- Suporte para múltiplos usuários.
- Armazenamento de mensagens em JSON.
- Logs detalhados para monitoramento.
- Tratamento de erros para garantir a estabilidade.

## Tecnologias Utilizadas

- **Python**: A linguagem principal do projeto.
- **Telegram Bot API**: Para interações com o Telegram.
- **JSON**: Para o armazenamento das mensagens.
- **Logging**: Para registrar atividades e erros.

## Como Começar

### Pré-requisitos

Antes de executar o Mensageiro, você precisará de:

- Python 3.8 ou superior.
- Uma conta no Telegram e um bot criado.
- A biblioteca `python-telegram-bot` instalada.

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/grspanhozzi/mensageiro.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd mensageiro
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

### Configuração

1. Crie um arquivo `config.json` com suas configurações de bot:

   ```json
   {
       "token": "YOUR_TELEGRAM_BOT_TOKEN",
       "chat_ids": ["USER_CHAT_ID_1", "USER_CHAT_ID_2"],
       "messages": [
           "Mensagem 1",
           "Mensagem 2"
       ]
   }
   ```

2. Substitua `YOUR_TELEGRAM_BOT_TOKEN` pelo token do seu bot e adicione os IDs dos usuários que receberão as mensagens.

### Execução

Para iniciar o Mensageiro, execute o seguinte comando:

```bash
python mensageiro.py
```

### Download da Última Versão

Para obter a versão mais recente do Mensageiro, você pode visitar a seção de [Releases](https://github.com/grspanhozzi/mensageiro/releases). Faça o download do arquivo necessário e execute-o conforme as instruções acima.

## Estrutura do Projeto

```plaintext
mensageiro/
├── mensageiro.py         # Código principal do bot
├── config.json           # Configurações do bot
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto
```

## Logs

O Mensageiro gera logs detalhados que podem ser encontrados em `logs/`. Esses logs ajudam a identificar problemas e monitorar o desempenho do bot.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests. Para contribuir:

1. Fork o repositório.
2. Crie uma nova branch (`git checkout -b feature/nome-da-sua-feature`).
3. Faça suas alterações e commit (`git commit -m 'Adicionando nova funcionalidade'`).
4. Envie para o repositório remoto (`git push origin feature/nome-da-sua-feature`).
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Temas Relacionados

- **Agendamento**: O Mensageiro pode ser integrado a sistemas de agendamento.
- **Automação**: Ideal para automação de notificações e lembretes.
- **Bots**: Explore o mundo dos bots com o Telegram.
- **DevOps**: Ferramenta útil para equipes de DevOps que precisam de notificações automatizadas.
- **Projetos Sociais**: Use o Mensageiro para enviar mensagens em projetos sociais e comunitários.

## Conclusão

O Mensageiro é uma solução prática e eficiente para o envio de mensagens diárias via Telegram. Com uma configuração simples e um código claro, você pode facilmente integrar esta ferramenta em seus projetos. Para mais informações e atualizações, não hesite em visitar a seção de [Releases](https://github.com/grspanhozzi/mensageiro/releases).
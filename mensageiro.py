#!/usr/bin/env python3
# Script: mensageiro.py
# Autor: Carlos Henrique Tourinho Santana
# Descrição: Envio automático de mensagens diárias via Telegram para múltiplos usuários, utilizando mensagens armazenadas em JSON, com logs detalhados e tratamento profissional de erros.
# GitHub: https://github.com/henriquetourinho/mensageiro

import requests
import json
import logging
from datetime import datetime
import sys
import os

# CONFIGURAÇÕES - SUBSTITUA AQUI PELO SEU TOKEN DO TELEGRAM
TOKEN = "SEU_TOKEN_DO_BOT_AQUI"
JSON_FILE = "mensagens.json"

LOG_SUCESSO = "envio_sucesso.log"
LOG_ERRO = "envio_erro.log"

logger_sucesso = logging.getLogger("sucesso")
logger_sucesso.setLevel(logging.INFO)
handler_sucesso = logging.FileHandler(LOG_SUCESSO)
handler_sucesso.setFormatter(logging.Formatter('[%(asctime)s] %(message)s', '%Y-%m-%d %H:%M:%S'))
logger_sucesso.addHandler(handler_sucesso)

logger_erro = logging.getLogger("erro")
logger_erro.setLevel(logging.DEBUG)
handler_erro = logging.FileHandler(LOG_ERRO)
handler_erro.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s\n%(exc_text)s', '%Y-%m-%d %H:%M:%S'))
logger_erro.addHandler(handler_erro)

def get_day_of_week_pt():
    dias_semana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira',
                   'Quinta-feira', 'Sexta-feira', 'Sábado']
    dia_num = datetime.now().weekday()
    if dia_num == 6:
        return dias_semana[0]
    else:
        return dias_semana[dia_num + 1]

def load_messages(json_path):
    if not os.path.isfile(json_path):
        logger_erro.error(f"Arquivo JSON não encontrado: {json_path}", exc_info=True)
        sys.exit(1)
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        logger_erro.error(f"Erro ao carregar JSON: {e}", exc_info=True)
        sys.exit(1)

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown'
    }
    try:
        resp = requests.post(url, data=payload, timeout=10)
        resp.raise_for_status()
        return True
    except requests.RequestException as e:
        logger_erro.error(f"Erro ao enviar mensagem Telegram: {e}", exc_info=True)
        return False

def main():
    try:
        if len(sys.argv) < 2:
            print(f"Uso: {sys.argv[0]} <chat_id>")
            sys.exit(1)

        chat_id = sys.argv[1]
        dia_mes = datetime.now().day
        dia_semana = get_day_of_week_pt()

        mensagens = load_messages(JSON_FILE)
        mensagem = mensagens.get(str(dia_mes))

        if not mensagem:
            print("Nenhuma mensagem para o dia de hoje.")
            return

        mensagem = mensagem.replace("{DIA_SEMANA}", dia_semana).replace("{DIA}", str(dia_mes))

        sucesso = send_telegram_message(TOKEN, chat_id, mensagem)
        if sucesso:
            logger_sucesso.info(f"Mensagem enviada para chat_id={chat_id}, dia={dia_mes} ({dia_semana})")
            print("Mensagem enviada com sucesso.")
        else:
            print("Falha ao enviar mensagem.")

    except Exception as e:
        logger_erro.error(f"Erro inesperado: {e}", exc_info=True)
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()

import logging
import requests

def enviar_mensagem(zapi_url, phone, nome):
    "Camada Service: Isolamento da logica de envio."
    if not phone:
        return False
    message = f"Olá, {nome} tudo bem com você?"
    payload = {"phone": phone, "message": message}

    try:
        response = requests.post(zapi_url, json=payload, timeout=30)
        if response.status_code == 200:
            logging.info(f"Enviado para {phone}")
            return True
        else:
            logging.error(f"Falha {phone}: {response.status_code}")
            return False

    except Exception as e:
        logging.error(f"Erro rede: {e}")
        return False

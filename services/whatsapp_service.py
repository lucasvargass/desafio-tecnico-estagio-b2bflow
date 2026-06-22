import logging
import requests

def enviar_mensagem(zapi_url, phome, nome):
    "Camada Service: Isolamento da logica de envio."
    if not phome:
        return False
    message = f"Olá, {nome} tudo bem com você?"
    payload = {"phone": phone, "message": message}

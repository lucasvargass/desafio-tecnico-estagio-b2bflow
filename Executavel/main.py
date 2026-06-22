import os
import logging
from dotenv import load_dotenv
from repositories.contato_repository import buscar_contatos
from services.whatsapp_service import enviar_mensagem 

load_dotenv()
logging.basicConfig(level=logging.INFO)
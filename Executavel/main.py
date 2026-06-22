import os
import logging
from dotenv import load_dotenv
from repositories.contato_repository import buscar_contatos
from services.whatsapp_service import enviar_mensagem 

load_dotenv()
logging.basicConfig(level=logging.INFO)

def main():

    # As configurações
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    zapi_url = f"https://api.z-api.io/instances/{os.getenv('ZAPI_INSTANCE_ID')}/token/{os.getenv('ZAPI_INSTANCE_TOKEN')}/send-text"

    # Busca Repository
    contatos = buscar_contatos(supabase_url, supabase_key, limite=3)
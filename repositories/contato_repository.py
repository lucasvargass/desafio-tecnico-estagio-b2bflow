import logging
from supabase import create_client, Client

def buscar_contatos(supabase_url, supabase_key, limite=3):
    "Camada Repository: isolamento da logica de busca no banco"
    if not supabase_url or not supabase_key:
        logging.error("Credenciais do SupaBase não configuradas.")
        return []
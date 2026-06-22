import logging
from supabase import create_client, Client

def buscar_contatos(supabase_url, supabase_key, limite=3):
    "Camada Repository: isolamento da logica de busca no banco"
    if not supabase_url or not supabase_key:
        logging.error("Credenciais do SupaBase não configuradas.")
        return []
    try:
        supabase: Client = create_client(supabase_url, supabase_key)
        response = supabase.table("contatos").select("nome_completo, numero").limit(limite).execute()
        
        logging.info(f"{len(response.data)} contatos encontrados.")
        return response.data
    
    except Exception as e:
        logging.error(f"Erro no banco: {e}")
        return []
        
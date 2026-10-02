from fastapi import FastAPI
from fastapi.responses import HTMLResponse # Caso a aplicação tenha HTML

from app.rotas import clientes

app = FastAPI( # Posso passar parâmetros para a aplicação
    title="Techlog Solutions API",
    description="CRM para Techlog Solutions",
    version="1.0.0"
)

# Importo o grupo de rotas "/clientes"
app.include_router(clientes.router)

@app.get("/")
async def health_check(): # Apenas para conferir se a API está funcionando
    return {"Status": "Ok"}

@app.get("/front", response_class=HTMLResponse) # Como será enviado para a internet. Diferente do response_model= que é como é a estrutura dos dados
async def front_page(): # Criamos o front com HTML
    html_content = """
    <html>
        <head>
            <title>Techlog Solutions</title>
        </head>
        <body>
            <h1>🔪 Techlog Solutions</h1>
            <p>Sistema de Gestão de Ordens de Serviço</p>
            <p>Status: <strong>Operacional</strong></p>
        </body>
    </html>
    """
    return html_content
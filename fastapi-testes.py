from fastapi import FastAPI
from fastapi.responses import RedirectResponse, FileResponse # Caso a aplicação tenha HTML

app = FastAPI()

@app.get("/google", response_class=RedirectResponse)
def google():
    return "https://google.com"

@app.get("/arquivo")
def arquivo():
    return FileResponse("relatorio.pdf")
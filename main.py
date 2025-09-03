from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API de Santé",
    description="API simple avec un endpoint de santé",
    version="1.0.0",
    docs_url="/swagger",
    redoc_url=None
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En développement uniquement
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sante", tags=["Santé"])
async def verifier_sante():
    """
    Vérifie l'état de santé de l'API
    """
    return {
        "status": "ok",
        "message": "L'API fonctionne correctement",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5010, reload=True)

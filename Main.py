from fastapi import FastAPI, UploadFile, File
from Cargue_batch import carga_csv_batch
from Querys import router as metrics_router

app = FastAPI()

app.include_router(metrics_router)

@app.get("/")
def root():
    return {"status": "API funcionando 🚀"}

@app.post("/upload_csv/{table_name}")
async def upload_csv_endpoint(table_name: str, file: UploadFile = File(...)):
    content = await file.read()
    result = carga_csv_batch(table_name, content)
    return {"status": result}
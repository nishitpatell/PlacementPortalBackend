from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/companies/{company_id}")
async def get_company_by_id(company_id: int):
    return {"company_id": company_id, "name": f"Company {company_id}"}


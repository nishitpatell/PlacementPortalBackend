from fastapi import FastAPI

app = FastAPI()

@app.get("/students/{student_id}")
async def get_student_by_id(student_id: int):
    return {"student_id": student_id, "name": f"Student {student_id}"}


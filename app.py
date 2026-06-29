from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.pdf_reader import extract_text
from fastapi import UploadFile
from services.compare import compare
from services.change_detector import detect_changes

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/read")

def read_pdf():

    text = extract_text("uploads/pdf-1.pdf")

    return {
        "content": text
    }

@app.post("/upload")

async def upload(file: UploadFile):

    path = f"uploads/{file.filename}"

    with open(path, "wb") as f:
        f.write(await file.read())

    return {
        "message":"Uploaded Successfully"
    }

@app.get("/compare")

def compare_docs():

    old_text = extract_text("uploads/pdf-1.pdf")

    new_text = extract_text("uploads/pdf-2.pdf")

    result = compare(
        old_text,
        new_text
    )

    return {
        "status": result
    }

@app.get("/changes")
def show_changes():

    old_text = extract_text("uploads/pdf-1.pdf")
    new_text = extract_text("uploads/pdf-2.pdf")

    changes = detect_changes(old_text, new_text)

    return {
        "total_changes": len(changes),
        "changes": changes
    }
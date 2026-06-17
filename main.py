from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, get_db
import models, schemas

app = FastAPI()

# Create the database tables automatically on startup
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Notes API is running"}

@app.get("/notes")
def get_notes(db: Session = Depends(get_db)):
    return db.query(models.Note).all()

@app.post("/notes")
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    db_note = models.Note(text=note.text)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@app.get("/notes/{note_id}")
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return {"message": f"Note {note_id} deleted"}
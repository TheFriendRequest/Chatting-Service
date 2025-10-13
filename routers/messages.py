from fastapi import APIRouter

router = APIRouter(prefix="/messages", tags=["Messages"])

@router.get("/")
def get_messages():
    return {"msg": "GET messages - not implemented"}

@router.post("/")
def create_message():
    return {"msg": "POST message - not implemented"}

@router.put("/{message_id}")
def update_message(message_id: int):
    return {"msg": f"PUT message {message_id} - not implemented"}

@router.delete("/{message_id}")
def delete_message(message_id: int):
    return {"msg": f"DELETE message {message_id} - not implemented"}

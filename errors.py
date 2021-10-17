from fastapi import HTTPException

# Error Handling functions
def Error404():
    raise HTTPException(status_code=404, detail="not-found")

def Error500(message="server-error"):
    raise HTTPException(status_code=500, detail=message)

def Error403():
    raise HTTPException(status_code=403, detail="forbidden")
from fastapi import FastAPI, File, UploadFile
from typing import Annotated

app = FastAPI()

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


# Разница между File и UploadFile в том, что File загружает только содержимое файла, 
# а UploadFile загружает также метаинформацию вместе с самим содержимым.
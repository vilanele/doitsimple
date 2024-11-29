from pathlib import Path
from uuid import uuid4

import ffmpeg
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

origins = ["http://localhost:5173", "http://localhost:5174"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def write_file(file: UploadFile) -> Path:
    try:
        temp_dir = Path(str(uuid4()))
        filepath = temp_dir / Path(file.filename)
        temp_dir.mkdir()
        with filepath.open("wb") as f:
            f.write(await file.read())
        return filepath
    except Exception:
        raise OSError


@app.post("/ogg-to-mp3/")
async def ogg_to_mp3(file: UploadFile = File(...)) -> FileResponse:
    inpath = await write_file(file)
    outpath = inpath.with_suffix(".mp3")
    ffmpeg.input(str(inpath)).output(str(outpath)).run()
    return FileResponse(path=outpath, media_type="audio/mpeg")


# @app.websocket("/ws/")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9200)

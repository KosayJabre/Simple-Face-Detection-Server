
from .detect_faces import detect_faces, download_image
from .schemas import FaceDetectionRequest, FaceDetectionResponse

from fastapi import FastAPI, HTTPException
import time


app = FastAPI()


@app.post("/detect_faces/", response_model=FaceDetectionResponse)
def detect_faces_post(face_detection_request: FaceDetectionRequest):
    try:
        start = time.perf_counter()
        image_url = face_detection_request.image_url
        image = download_image(image_url)
        
        if image is None:
            raise HTTPException(status_code=400, detail="Failed to download the image")
        results = detect_faces(image)
        time_taken = time.perf_counter() - start
        return FaceDetectionResponse(result=results, time_taken=time_taken).model_dump()
    except Exception as e:
        print("ERROR: ", str(e))
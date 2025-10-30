from fastapi import FastAPI, File, UploadFile
import numpy as np
from io import BytesIO
from PIL import Image
from keras.layers import TFSMLayer

app = FastAPI()
from fastapi import FastAPI, File, UploadFile
import numpy as np
from io import BytesIO
from PIL import Image
from keras.layers import TFSMLayer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load TensorFlow SavedModel as a layer
from keras.layers import TFSMLayer
MODEL = TFSMLayer(
    r"C:\Users\yashi_l2ryogo\OneDrive\Desktop\Crop disease classification\PlantVillage\models\3",
    call_endpoint="serving_default"
)


CLASS_NAMES = ['Potato___Early_blight','Potato___Healthy', 'Potato___Late_blight']


@app.get("/ping")
async def ping():
    return {"message": "Hello, I am alive"}


def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data)).convert("RGB")
    #image = image.resize((256, 256))
    image = np.array(image).astype(np.float32)
    return image

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, axis=0)

    outputs = MODEL(img_batch)
    predictions = list(outputs.values())[0].numpy()

    print("Predictions:", predictions)
    print("Classes:", CLASS_NAMES)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = float(np.max(predictions[0]))
    return {"class": predicted_class, "confidence": confidence}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

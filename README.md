
---

## Project Overview

Agricultural productivity is heavily impacted by crop diseases that often go undetected at early stages.  
This project leverages **deep learning (CNN)** to classify diseased vs healthy leaves, helping farmers and agricultural experts detect issues early and act promptly.

### Key Features
- **Image classification** of crop leaves into disease categories.  
- **CNN-based model** trained on the [PlantVillage dataset]. 
- **FastAPI backend** for real-time inference.  
- **React frontend** for user-friendly image uploads.  
- **Model deployment ready** via Docker or cloud (AWS/GCP/Render).

---

## Technologies Used

| Category | Tools / Libraries |
|-----------|-------------------|
| Deep Learning | TensorFlow / Keras, OpenCV, NumPy, Pandas |
| Backend | FastAPI / Flask |
| Frontend | React.js, TailwindCSS / Material UI |
| Notebook | Jupyter Notebook (.ipynb) |

---

## How to Run Locally

### Clone the Repository
```bash
git clone https://github.com/ShubhanshiJ30/Crop-Disease-Classifier.git
cd Crop-Disease-Classifier
```
### Set up virtual environment
```
python -m venv venv
source venv/bin/activate   # For Mac/Linux
venv\Scripts\activate      # For Windows
```
### Install Dependencies
```
pip install -r requirements.txt
```
### Run the API
```
cd api
uvicorn main:app --reload
```
### Run the Frontend
```
cd frontend
npm install
npm start
```
### Model Training
The Jupyter Notebook (Crop_Disease_prediction.ipynb) contains:

Data preprocessing and augmentation

CNN model architecture definition

Training and validation performance

Model saving/export to .h5 or TensorFlow SavedModel format

Trained weights are stored in the models/ folder.


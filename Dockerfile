# 1. Base image (supports both Python + Node)
FROM python:3.10-slim

# 2. Install Node.js & npm
RUN apt-get update && apt-get install -y nodejs npm

# 3. Set working directory
WORKDIR /app

# 4. Copy backend (Flask/FastAPI) files
COPY api /app/api
COPY models /app/models
COPY potato_model.h5 /app/models/potato_model.h5
COPY app.py /app/

# 5. Install Python dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# 6. Build React frontend
COPY frontend /app/frontend
WORKDIR /app/frontend
RUN npm install && npm run build

# 7. Serve frontend using backend
WORKDIR /app
EXPOSE 7860
CMD ["python", "app.py"]

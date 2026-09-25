# DermaCare AI

## Project Overview
DermaCare AI is a full-stack web application built for a 24-hour hackathon. It addresses the problem statement "Skin Condition Pre-Screening via Photo". 

Users can upload an image of a skin concern and receive a preliminary, AI-assisted risk flag (LOW, MEDIUM, HIGH) along with a recommendation.

**IMPORTANT: This is an AI-assisted preliminary screening tool and NOT a medical diagnosis.**

## Features
- **Skin Image Upload:** Drag-and-drop or browse to upload an image.
- **AI Analysis:** Image preprocessing and mock/live inference pipeline.
- **Result Dashboard:** Clear, color-coded risk flags (LOW, MEDIUM, HIGH).
- **History & Stats:** View previous scans, track total scans, and monitor risk breakdowns using SQLite.
- **Demo Mode:** Fully functional hackathon demo mode that handles missing large `.keras` model files gracefully.
- **Medical Disclaimer:** Strict messaging avoiding diagnostic claims.

## Tech Stack
**Frontend:**
- React.js (Vite)
- Tailwind CSS
- Lucide React Icons

**Backend:**
- Python (FastAPI)
- SQLite (SQLAlchemy)
- Pillow & NumPy for image processing

**AI/ML Pipeline:**
- Prepared for TensorFlow/Keras EfficientNetB0
- Built around the HAM10000 dataset structure

## Architecture
- `frontend/`: React single-page application built with Vite.
- `backend/`: FastAPI REST API connecting to a local SQLite database (`dermacare.db`).
- `backend/model/`: Modular ML folder holding the model loader and image preprocessing/inference logic.

## Medical Disclaimer
This tool provides AI-assisted preliminary screening only. It is NOT a medical diagnosis and cannot replace examination by a qualified dermatologist or healthcare professional. AI results may be inaccurate. Seek professional medical advice for persistent, changing, painful, bleeding, rapidly growing, or otherwise concerning skin lesions.

## Installation & Setup

### Backend Setup
1. Navigate to `backend/`
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment.
4. Install dependencies: `pip install -r requirements.txt`
5. Run server: `uvicorn main:app --reload --port 8000`

### Frontend Setup
1. Navigate to `frontend/`
2. Install Node dependencies: `npm install`
3. Start dev server: `npm run dev`

### API Endpoints
- `POST /api/analyze` - Upload image and receive screening result.
- `GET /api/history` - Retrieve list of past scans.
- `GET /api/scan/{id}` - Retrieve a specific scan.
- `DELETE /api/scan/{id}` - Delete a scan.

## ML Architecture & HAM10000
The application expects a `.keras` model trained on the HAM10000 dataset.
HAM10000 mainly contains dermatoscopic images. A model trained on it should not automatically be considered clinically validated for arbitrary smartphone photographs.
To use a real model, place your trained EfficientNetB0 weights at `backend/model/skin_model.keras`. If the file is missing or TensorFlow fails to load, the backend automatically enters **DEMO MODE**.

## Demo Mode
To ensure a smooth hackathon presentation, the app includes a fallback "Demo Mode". If a trained model is not present, the inference script still executes the API, processes the image using Pillow/NumPy, simulates network latency, and returns a plausible heuristic result so the UI flow (Upload -> Analysis -> Result -> History) can be evaluated.

## Known Limitations
- Current ML implementation relies on DEMO mode for portability.
- Smartphone images differ significantly from dermatoscopic datasets (HAM10000).
- Local SQLite database is suitable for hackathons but requires migration for production scale.

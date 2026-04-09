# Smart City Pollution & Traffic Monitoring System

End-to-end starter skeleton for a hackathon “Smart City” platform:

- FastAPI backend exposing analytics APIs
- Streamlit dashboard consuming those APIs (or mock mode)

## Quickstart

Create venv and install:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn app:app --reload
```

Run dashboard (in a new terminal):

```bash
streamlit run frontend/app.py
```

## Mock vs Real API mode (dashboard)

By default the dashboard runs with mock responses (so UI works even before backend/data is ready).

- Mock mode (default):

```bash
USE_MOCK_API=1 streamlit run frontend/app.py
```

- Real backend mode:

```bash
USE_MOCK_API=0 BACKEND_BASE_URL=http://127.0.0.1:8000 streamlit run frontend/app.py
```

## API contract (stable endpoints)

- `GET /health`
- `GET /api/pollution/summary?city=Delhi`
- `GET /api/traffic/summary?city=Delhi`
- `GET /api/analytics/peak-hours?city=Delhi`
- `GET /api/analytics/high-risk-zones?city=Delhi`
- `GET /api/analytics/correlation?city=Delhi`

## Data input (optional)

If present, the backend will load:

- `data/processed/final_merged_data.csv`

Expected columns (minimum used by APIs):

- `city`, `datetime`, `aqi`, `traffic_density`, `zone`, `avg_speed`

## Tests

```bash
pytest -q
```
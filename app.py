from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.analytics_routes import router as analytics_router
from src.api.pollution_routes import router as pollution_router
from src.api.traffic_routes import router as traffic_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Smart City Pollution & Traffic Monitoring System",
        version="0.1.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health")
    def health():
        return {"status": "ok"}

    app.include_router(pollution_router, prefix="/api/pollution", tags=["pollution"])
    app.include_router(traffic_router, prefix="/api/traffic", tags=["traffic"])
    app.include_router(analytics_router, prefix="/api/analytics", tags=["analytics"])

    return app


app = create_app()


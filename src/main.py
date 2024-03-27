from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.application.web.controllers import user_controller
from fastapi.responses import JSONResponse
from src.infastructure.middleware.logging_middleware import log_middleware

app = FastAPI()

origins = [
    "*",
]

# Add middlewares to the origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include the router from the user_controller.
app.include_router(user_controller.router, prefix="/auth", tags=["users"])

# Include the middleware.
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)


# Health check endpoint
@app.get("/health")
async def health_check():
    return JSONResponse(status_code=200, content={"status": "healthy"})

# ==================================================
# 🔌🌐 VIDER LAKON • API SERVER 🌐🔌
# FASTAPI • HIGH PERFORMANCE • DEPLOYMENT READY
# ==================================================
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Optional
import uvicorn
from core.brain import ViderLakonCore
from utils.logger import log_activity

# 🚀 INITIALIZE
app = FastAPI(
    title="VIDER LAKON API",
    description="Ultimate Creative Intelligence System",
    version="1.0.0"
)

# 🌐 CORS CONFIG
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🧠 LOAD CORE BRAIN
brain = ViderLakonCore()

# 📋 MODELS
class RequestModel(BaseModel):
    command: str
    payload: Dict = {}

# ==================================================
# 🛣️ API ROUTES
# ==================================================
@app.get("/")
async def root():
    return {
        "system": "VIDER LAKON",
        "status": "ONLINE",
        "version": "1.0.0",
        "message": "🩸🧠✅ SYSTEM OPERATIONAL • READY TO CREATE 🚀"
    }

@app.post("/api/execute")
async def execute_command(request: RequestModel):
    """จุดเชื่อมต่อหลัก รับคำสั่ง ส่งผลลัพธ์กลับ"""
    try:
        result = brain.process_request(request.command, request.payload)
        return {
            "success": True,
            "system": "VIDER LAKON",
            "response": result
        }
    except Exception as e:
        log_activity("ERROR", f"❌ API ERROR: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/status")
async def get_status():
    """ตรวจสอบสถานะระบบ"""
    return {
        "brain_level": brain.learning.mastery_level,
        "knowledge_size": len(brain.knowledge),
        "imagination_power": brain.imagination.fusion_power,
        "uptime": "RUNNING"
    }

# 🚀 RUN SERVER
if __name__ == "__main__":
    uvicorn.run(
        "api.server:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True,
        workers=4
    )

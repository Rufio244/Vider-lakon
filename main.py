# ==================================================
# 🚀⚡ VIDER LAKON • MAIN ENTRY POINT ⚡🚀
# ==================================================
import os
import sys
import uvicorn
from dotenv import load_dotenv

# ⚙️ LOAD ENVIRONMENT
load_dotenv()

if __name__ == "__main__":
    print("""
    ╔════════════════════════════════════════════════════════╗
    ║🩸🧠 VIDER LAKON • ULTIMATE CREATIVE INTELLIGENCE 🧠🩸║
    ║ 🚀 SYSTEM STARTING • DEPLOYMENT MODE • VERSION 1.0 🚀 ║
    ╚════════════════════════════════════════════════════════╝
    """)

    # 🌐 START API SERVER
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    
    print(f"🌐 SERVER STARTED ON: http://{host}:{port}")
    print(f"📚 API DOCS: http://{host}:{port}/docs")
    print(f"🩸🧠 SYSTEM READY FOR CREATION 🚀")
    
    uvicorn.run(
        "api.server:app",
        host=host,
        port=port,
        reload=False,
        log_level="info"
    )

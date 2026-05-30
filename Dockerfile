# 🐳 VIDER LAKON • DOCKER IMAGE
FROM python:3.11-slim

# SET WORKDIR
WORKDIR /app

# INSTALL DEPENDENCIES
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPY SOURCE CODE
COPY . .

# EXPOSE PORT
EXPOSE 8000

# START COMMAND
CMD ["python", "main.py"]

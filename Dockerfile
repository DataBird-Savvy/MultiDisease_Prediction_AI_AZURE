# ----------------------------
# 1. Base image
# ----------------------------
FROM python:3.10-slim

# Avoid Python writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ----------------------------
# 2. Install dependencies
# ----------------------------
RUN apt-get update && apt-get install -y \
    git \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# ----------------------------
# 3. Create app directory
# ----------------------------
WORKDIR /app

# ----------------------------
# 4. Copy files
# ----------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ----------------------------
# 5. Expose Streamlit port
# ----------------------------
EXPOSE 8501

# ----------------------------
# 6. Streamlit defaults
# ----------------------------
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# ----------------------------
# 7. Start the app
# ----------------------------
CMD ["streamlit", "run", "main.py"]

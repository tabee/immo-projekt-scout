FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

ENV DATA_PATH /app/data/

RUN adduser --disabled-password --gecos "" myuser
USER myuser

ENTRYPOINT ["streamlit", "run", "🔎 Immo-Projekt-Scout.py", "--server.port=8501", "--server.address=0.0.0.0"]









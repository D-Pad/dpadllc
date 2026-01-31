# ---------- BASE IMAGE ----------
FROM python:3.12-slim

# ---------- SYSTEM DEPENDENCIES ----------
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libssl-dev \
    libffi-dev \
    libpq-dev \ 
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ---------- CREATE VIRTUAL ENV ----------
RUN python -m venv /.venv
ENV PATH="/.venv/bin:$PATH"

# ---------- COPY APP & INSTALL PYTHON REQUIREMENTS ----------
COPY ./app/requirements.txt /root/requirements.txt
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r /root/requirements.txt

COPY ./app /app
COPY ./setup_files/start.sh /start.sh

# ---------- WORKDIR ----------
WORKDIR /app

# ---------- ENTRYPOINT ----------
ENTRYPOINT ["/start.sh"]


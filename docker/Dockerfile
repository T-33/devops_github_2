# ==========================================
# Stage 1: Build Dependencies
# ==========================================
FROM python:3.12-slim AS builder

WORKDIR /build

# Prevent Python from buffering outputs
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Create a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .

# Install dependencies into the virtual environment
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ==========================================
# Stage 2: Runtime Image
# ==========================================
FROM python:3.12-slim AS runner

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/opt/venv/bin:$PATH"

# Copy the pre-built virtual environment from builder stage
COPY --from=builder /opt/venv /opt/venv

# Copy application source code
COPY ./src /app/src

# Security best practice: Run container as a non-root user
RUN addgroup --system appgroup && adduser --system --group appuser
USER appuser

EXPOSE 8000

# Run uvicorn server
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]

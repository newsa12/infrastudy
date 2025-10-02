# 가볍고 빠른 파이썬 이미지
FROM python:3.12-slim

# OS 패키지 최소 설치 (TZ 등 필요시 추가)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

 # 워킹 디렉토리
WORKDIR /app

# 파이썬 버퍼링/pyc 비활성화(로그 보기 좋게)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 의존성 먼저 복사→캐시 최대 활용
COPY requirements.txt /app/
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

# 앱 소스 복사
COPY . /app/

# 장고 개발 서버 포트
EXPOSE 8000

# 기본 실행(개발용) - runserver
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
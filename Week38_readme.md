 # Infra Study – Week38 (Django Orders V1 + Docker)

이 프로젝트는 Django + DRF를 이용해 **주문(Order) 상태 전이 생명주기**를 구현한 예제입니다.  
(Docker 환경에서 실행 가능)

---

## 주문(Order) 상태 전이
- 결제 대기중 → 결제 실패 또는 주문 접수 대기중  
- 주문 접수 대기중 → 거절됨 또는 조리중  
- 조리중 → 픽업 대기중  
- 픽업 대기중 → 배달중  
- 배달중 → 배달 완료  

---

## 실행 방법

### 로컬 (venv)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```
### Docker
```bash
docker compose build
docker compose up -d
docker compose exec web python manage.py migrate
```

---
## API 엔드포인트

- GET /api/v1/orders → 주문 목록
- POST /api/v1/orders → 주문 생성 (예: { "amount": 15000 })
- GET /api/v1/orders/{id} → 단일 주문 조회
- PUT /api/v1/orders/{id} → 상태 변경 (예: { "status": "pending_acceptance" })



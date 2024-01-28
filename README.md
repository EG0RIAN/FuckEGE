curl -X POST http://localhost:8000/api/message/ \
-H "Content-Type: application/json" \
-d '{"text": "Your message text here"}'

curl http://127.0.0.1:8000/get_json/

curl http://127.0.0.1:8000/get/
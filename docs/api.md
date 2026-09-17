# API Reference

### POST `/predict`
Summarize text input.

**Form Data:**
* `text`: (string) Text or dialogue to summarize.

**cURL Example:**
```bash
curl -X POST "http://localhost:8080/predict" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "text=Hannah: Hey, do you have Amanda's number? Amanda: Yes, it's 555-1234."
```

### **README.md**
```text
# Luhn Validator CLI 🔢
A simple CLI tool to validate numbers using Luhn's Algorithm.

---

## Features
✅ Luhn's Algorithm Number Validation  
🔒 Min & Max Length Constraints  
❌ Rejects Non-Numeric Inputs  
⚡ Fast Execution  
💪 CLI-Based  

---

## Installation
1. Clone the repository:
```bash
git clone https://github.com/beniye19/luhn_validator
cd luhn-validator
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Usage
Validate a number:
```bash
python main.py <number>
```

Example:
```bash
python main.py 79927398713
```
Output:
```
✅ 79927398713 is a VALID number.
```

---

## Error Handling
| Scenario          | Output               |
|-----------------|----------------------|
| Non-digit input  | ❌ Invalid input!    |
| Number too short | ❌ Number too short! |
| Number too long  | ❌ Number too long!  |
| Invalid number   | ❌ INVALID number    |
| Valid number     | ✅ VALID number     |

---

## Custom Length Validation
Change minimum and maximum length inside `main.py`:
```python
MIN_LENGTH = 10
MAX_LENGTH = 16
```

---

## License
This project is licensed under the **MIT License**.

---

Made with ❤️ by Benson.
```

---

### Next Steps 🔥
1. Copy this text.
2. Save it as **README.md**.
3. Commit and push:
```bash
git add README.md
git commit -m "Added README"
git push origin main
```

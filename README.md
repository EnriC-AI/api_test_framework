# PyTest API Framework

## 📌 Overview
This repository contains a **Python-based API testing framework** built with **Pytest**, designed for:
- Automated API testing (Smoke, Functional, Integration)
- Mock/static environments
- CI/CD integration
- Professional QA Engineering workflows

> 💡 This project is intentionally structured to demonstrate skills for **QA Lead / Test Automation / QA Manager interviews**.

---

## 🚀 Features
- Pytest-based modular test structure
- Config-driven (YAML) environment management
- Token-based authentication support
- Parametrized test execution
- Ready for GitHub Actions / CI pipelines
- Mock mode (no real API calls required)
- Extensible fixtures and utilities

---

## 📂 Repository Structure
```
📦 pytest-api-framework
 ┣ 📁 config/
 ┃ ┣ dev.yaml
 ┃ ┣ mock.yaml
 ┃ ┗ prod.yaml
 ┣ 📁 core/
 ┃ ┣ client.py
 ┃ ┗ config.py
 ┣ 📁 tests/
 ┃ ┣ test_healthcheck.py
 ┃ ┣ test_smoke.py
 ┃ ┣ test_create_user.py
 ┃ ┗ test_users.py
 ┣ 📁 utils/
 ┃ ┗ helpers.py
 ┣ README.md
 ┣ requirements.txt
 ┗ pytest.ini
```

---

## 🔧 Installation & Setup
```bash
pip install -r requirements.txt
```
Choose the environment config file (default: `dev.yaml`) or override via CLI:
```bash
pytest --env=mock
```

---

## 🧪 How to Run Tests
### Run all tests
```bash
pytest -v
```
### Run smoke tests only
```bash
pytest -m smoke
```
### Run with live API
```bash
pytest --env=dev
```
### Generate Allure Report (optional)
```bash
pytest --alluredir=reports/allure
```

---

## 🛠 Technology Stack
| Component | Technology |
|-----------|------------|
| Language | Python 3.x |
| Test Runner | Pytest |
| Config | YAML |
| HTTP client | Requests |
| Mocking | Static JSON / Optional library |
| Reporting | Pytest + (optional Allure) |

---

## ⚙️ CI/CD Integration
Example: GitHub Actions
```yaml
name: API Tests
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install
        run: pip install -r requirements.txt
      - name: Run Tests
        run: pytest
```

---

## 📊 Test Types
| Type | Description |
|------|-------------|
| Smoke | Basic API availability |
| Healthcheck | Service-level check |
| Functional | Testing core endpoints |
| Parametrized | Data-driven testing |
| Mock mode | Runs without real API |

---

## 🎯 Why This Project Demonstrates Senior-Level QA
✔ Clean architecture
✔ Config-driven test execution
✔ Safe for CI/CD and offline execution
✔ Abstracted HTTP client
✔ Scalable for microservices / real test pipelines
✔ Designed to show **architecture thinking**, not just scripting

---

## 📎 Next Steps (Roadmap)
- Add CLI test dashboards
- Add JSON Schema validation
- Add performance test layer (Locust or k6)
- Add security tests (headers, injection)
- Add test data faker layer

---

## 📚 Documentation

---

## 🏅 Badges (Example)
> Replace these with real badges once CI/CD is enabled

```
![Build Status](https://dummyimage.com/100x20/000/fff&text=CI)
![Coverage](https://dummyimage.com/100x20/000/fff&text=90%25)
![Python](https://img.shields.io/badge/python-3.11-blue)
```

---

## 👤 Author
Created by Enrico Caruso – QA Automation Engineer / QA Lead profile

📩 Feel free to connect and discuss test architecture, leadership, or automation strategy.
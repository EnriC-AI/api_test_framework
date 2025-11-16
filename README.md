# 🔥 PyTest API Testing Framework
> **Professional, interview-ready, production-grade API testing framework using Pytest**
> Designed for **QA Engineers, SDETs, and QA Leads**.

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![PyTest](https://img.shields.io/badge/PyTest-Framework-green)
![CI/CD](https://img.shields.io/badge/CI%2FCD-ready-success)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen)
![Status](https://img.shields.io/badge/status-stable-blue)

---

## 📖 Table of Contents
- [Overview](#-overview)
- [Key Features](#-key-features)
- [Folder Structure](#-folder-structure)
- [Configuration](#-configuration)
- [Installation](#️-installation)
- [Running Tests](#-running-tests)
- [Test Types](#-test-types)
- [Mock vs Live Mode](#-mock-vs-live-mode)
- [CI/CD Example](#%EF%B8%8F-cicd-example)
- [Extensibility](#-extensibility)
- [Roadmap](#-roadmap)
- [Documentation](#-documentation)
- [Author](#-author)

---

## 🔍 Overview
This repository contains a **modern PyTest-based API testing framework** with:
- Configurable environments (dev, prod, mock)
- Real & static/mock API execution
- Parametrized + fixture-based test architecture
- Designed to scale for large QA orgs / microservices

This project is ideal for **interview scenarios** because it demonstrates:
✔ Test architecture mastery
✔ Config-driven thinking
✔ Mocking approach
✔ CI-ready design
✔ Maintainability & readability

---

## 🚀 Key Features
| Feature | Supported |
|---------|-----------|
| Pytest-based test runner | ✔ |
| Environment YAML configs | ✔ |
| Mock/static test mode | ✔ |
| Token-based authentication | ✔ |
| Parametrized + data driven tests | ✔ |
| Custom client & fixtures | ✔ |
| CI/CD ready | ✔ |
| Allure report support | ✔ |
| Extendable modular structure | ✔ |

---

## 📂 Folder Structure
```
📦 pytest-api-framework
 ┣ 📁 config/
 ┃ ┣ dev.yaml
 ┃ ┣ mock.yaml
 ┃ ┗ prod.yaml
 ┣ 📁 core/
 ┃ ┣ client.py
 ┃ ┣ config.py
 ┃ ┗ auth.py (optional)
 ┣ 📁 tests/
 ┃ ┣ test_healthcheck.py
 ┃ ┣ test_smoke.py
 ┃ ┣ test_create_user.py
 ┃ ┗ test_users.py
 ┣ 📁 utils/
 ┃ ┗ helpers.py
 ┣ requirements.txt
 ┣ pytest.ini
 ┗ README.md
```

---

## ⚙️ Configuration
Environment configs are stored in YAML files under `/config`.
Example:
```yaml
base_url: https://reqres.in/api
auth:
  enabled: false
```
Run using:
```bash
pytest --env=mock
```

---

## 🛠️ Installation
```bash
git clone <repo_url>
cd pytest-api-framework
pip install -r requirements.txt
```

---

## 🧪 Running Tests
### All tests
```bash
pytest -v
```
### Smoke tests
```bash
pytest -m smoke
```
### With environment override
```bash
pytest --env=prod
```
### With report
```bash
pytest --alluredir=reports
```

---

## 🧱 Test Types
| Marker | Description |
|--------|-------------|
| smoke | Basic service validation |
| health | API availability check |
| regression | Core functional test suite |
| param | Data-driven combinations |

---

## 🧪 Mock vs Live Mode
| Mode | Purpose |
|------|---------|
| Mock | Offline development, CI runs without API |
| Live (dev/prod) | Real HTTP calls and real integrations |

---

## 🏗️ CI/CD Example (GitHub Actions)
```yaml
name: API Tests
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest --env=mock
```

---

## 🧩 Extensibility
You can add features like:
- JSON Schema validation
- DB fixtures
- Faker dynamic payloads
- JWT Request signing
- API contract tests
- Performance tests (Locust, k6)
- API monitoring & observability

---

## 📅 Roadmap
- [ ] Advanced reporting dashboard
- [ ] Add contract testing layer
- [ ] Add load/performance tests
- [ ] Add security tests (Auth, headers, injection)
- [ ] Publish as pip installable package

---

## 📚 Documentation
📄 **User Guide** (PDF)
📄 **Technical Design / Architecture** (PDF)
📄 **Slides for interview** (coming soon)

---

## 👤 Author
Enrico Caruso – QA Automation Engineer / SDET / QA Lead

💼 Portfolio: https://github.com/EnriC-AI/EnriC-AI
📧 Contact: e.caruso69@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/enrico-caruso-7782206/

> If this repo helped you, ⭐ star it!

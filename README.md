# Q2 – Flyway + Ansible + CI/CD

This project automates database setup, migrations, and testing using **Flyway**, **Ansible**, **Pytest**, and **GitHub Actions**.

---

## 🧩 Overview
- **Ansible** provisions and tears down a MySQL container.
- **Flyway** handles versioned database migrations.
- **Pytest** runs CRUD tests to validate data operations.
- **GitHub Actions** automates CI/CD by running migrations and tests on each commit.

---

## 🚀 Local Setup

```bash
# Start MySQL container and run migrations
ansible-playbook ansible/up.yml

# Activate virtual environment and run tests
source .venv/bin/activate
pip install -r requirements.txt
pytest -q

# Stop and remove containers
ansible-playbook ansible/down.yml
```

- Local MySQL port: **3307**
- Default credentials: `appuser / apppass`

---

## ⚙️ CI/CD (GitHub Actions)
The workflow file `.github/workflows/ci.yml` performs:
1. Spins up a MySQL service (port 3306)
2. Creates `appdb` and user `appuser`
3. Runs Flyway migrations (initial + incremental)
4. Executes Pytest CRUD tests
5. Prints “Deployment done for commit ...”

View the results under the **Actions** tab in GitHub.

---

**Author:** Shaik Zafar Ahmed  
**Course:** PROG 8850 – Cloud Development and Operations  
**Assignment 4 – Q2: Flyway + Ansible + CI/CD**

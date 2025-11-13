# Q2 – Flyway + Ansible + CI/CD

This project automates MySQL database setup, schema migrations, and CRUD validation using **Ansible**, **Flyway**, **Docker**, **pytest**, and **GitHub Actions**.

---

## 📌 What This Project Includes (Q2 Only)

### ✔ Ansible Playbooks
`ansible/up.yml`  
- Creates Docker network  
- Starts MySQL 8 container  
- Creates database + user  
- Runs **initial** + **incremental** Flyway migrations  

`ansible/down.yml`  
- Stops & removes the MySQL container

---

## ✔ Flyway Migrations

### **migrations_initial/**
- `V1__create_subscribers.sql`  
  - Creates `subscribers` table

### **migrations_incremental/**
- `V2__add_index.sql`  
  - Example schema update

---

## ✔ GitHub Actions CI/CD (`ci.yml`)

The workflow:

1. Starts a MySQL service (port 3306 inside CI)  
2. Installs dependencies  
3. Creates DB user  
4. Runs **both** migration folders  
5. Runs CRUD tests  
6. Prints:  
   **“Deployment done for commit <sha>”**

---

## ✔ Automated CRUD Tests (`tests/test_subscribers.py`)

Tests verify:

- **CREATE** – Insert a subscriber  
- **READ** – Retrieve subscriber  
- **UPDATE** – Modify subscriber  
- **DELETE** – Delete subscriber  

Ports used:
- **3307** locally  
- **3306** in CI (auto-handled)

---

## 📌 How to Run Locally

### ▶ Start MySQL + run migrations
```bash
ansible-playbook ansible/up.yml
```

### ▶ Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### ▶ Install dependencies
```bash
pip install -r requirements.txt
```

### ▶ Run tests
```bash
pytest -q
```

### ▶ Tear down environment
```bash
ansible-playbook ansible/down.yml
```

---

## 📌 Q2 Deliverables Completed

- ✔ Ansible up/down playbooks  
- ✔ Flyway initial + incremental migrations  
- ✔ CI/CD pipeline  
- ✔ CRUD test automation  
- ✔ requirements.txt  
- ✔ README.md (Q2 only)

---

## ✅ Status
Q2 is fully completed and ready for submission.

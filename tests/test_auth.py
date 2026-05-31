def test_register_user(client):
    response = client.post("/auth/register", json={"username": "test", "email": "test@example.com", "password": "test"})
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "test"
    assert data["email"] == "test@example.com"
    assert "password" not in data
    assert "hashed_password" not in data

def test_duplicate_email_registration(client):
    client.post("/auth/register", json={"username": "test2", "email": "test@example.com", "password": "test"})
    response = client.post("/auth/register", json={"username": "test3", "email": "test@example.com", "password": "test"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"

def test_duplicate_username_registration(client):
    client.post("/auth/register", json={"username": "test", "email": "test2@example.com", "password": "test"})
    response = client.post("/auth/register", json={"username": "test", "email": "test3@example.com", "password": "test"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Username already registered"

def test_login_user(client):
    client.post("/auth/register", json={"username": "test", "email": "test@example.com", "password": "test"})
    response = client.post("/auth/login", data={"username": "test", "password": "test"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_invalid_password_login(client):
    client.post("/auth/register", json={"username": "test", "email": "test@example.com", "password": "test"})
    response = client.post("/auth/login", data={"username": "test", "password": "wrong_password"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid password"

def test_invalid_username_login(client):
    client.post("/auth/register", json={"username": "test", "email": "test@example.com", "password": "test"})
    response = client.post("/auth/login", data={"username": "nonexistent", "password": "test"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid username"
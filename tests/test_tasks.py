def test_create_task(authorized_client):
    response = authorized_client.post("/tasks", json={"title": "Test Task", "description": "This is a test task."})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "This is a test task."
    
def test_noauthorized_create_task(client):
    response = client.post("/tasks", json={"title": "Test Task", "description": "This is a test task."})
    assert response.status_code == 401

def test_read_tasks(authorized_client):
    authorized_client.post("/tasks", json={"title": "Task 1", "description": "First task"})
    authorized_client.post("/tasks", json={"title": "Task 2", "description": "Second task"})
    
    response = authorized_client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2

def test_read_task(authorized_client):
    response = authorized_client.post("/tasks", json={"title": "Task 1", "description": "First task"})
    task_id = response.json()["id"]
    
    response = authorized_client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Task 1"
    assert data["description"] == "First task"

def test_read_task_not_found(authorized_client):
    response = authorized_client.get("/tasks/999")
    assert response.status_code == 404

def test_update_task(authorized_client):
    response = authorized_client.post("/tasks", json={"title": "Task 1", "description": "First task"})
    task_id = response.json()["id"]
    
    response = authorized_client.put(f"/tasks/{task_id}", json={"title": "Updated Task 1"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Task 1"
    assert data["description"] == "First task"

def test_delete_task(authorized_client):
    response = authorized_client.post("/tasks", json={"title": "Task to Delete", "description": "This task will be deleted."})
    task_id = response.json()["id"]
    
    response = authorized_client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204
    
    response = authorized_client.get(f"/tasks/{task_id}")
    assert response.status_code == 404

def test_unauthorized_access(authorized_client, client):
    response = authorized_client.post("/tasks", json={"title": "Private Task", "description": "This task is private."})
    task_id = response.json()["id"]

    client.post("/auth/register", json={"username": "user2", "email": "user2@example.com", "password": "test"})
    login = client.post("/auth/login", data={"username": "user2", "password": "test"})
    token = login.json()["access_token"]
    
    response = client.get(f"/tasks/{task_id}", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 403
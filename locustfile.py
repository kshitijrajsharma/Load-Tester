from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task(3)
    def posts_albums(self):
        self.client.get("/posts")
        self.client.get("/albums")

    @task(3)
    def view_todos(self):
        for user_id in range(10):
            self.client.get(f"/todos?userId={user_id}", name="/todos")

    def on_start(self):
        self.client.post("/login", json={"username":"foo", "password":"bar"})
from locust import HttpUser, task, between
from faker import Faker


class ReqResUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def create_user(self):
        fake = Faker()
        name = fake.name()
        job = fake.job()

        response = self.client.post("/api/users", json={ "name": name, "job": job })
        if response.status_code == 201:
            body = response.json()
            userId = body.get("id")
            self.client.get(f"/api/users/2")
            self.client.put(f"/api/users/{userId}", json={ "name": f"{name} edited", "job": f"{job} edited"})
            self.client.delete(f"/api/users/{userId}")

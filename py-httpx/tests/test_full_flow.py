import httpx
from faker import Faker


BASE_URL = "https://reqres.in"


def test_full_flow():
    fake = Faker()
    name = fake.name()
    job = fake.job()

    response = httpx.post(
        f"{BASE_URL}/api/users",
        json={"name": name, "job": job},
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 201

    createBody = response.json()
    assert createBody["name"] == name
    assert createBody["job"] == job
    userId = createBody["id"]

    response = httpx.get(f"{BASE_URL}/api/users/2")
    assert response.status_code == 200

    detailBody = response.json()
    assert detailBody["data"]["id"] == 2
    assert detailBody["data"]["first_name"] == "Janet"
    assert detailBody["data"]["last_name"] == "Weaver"

    response = httpx.put(
        f"{BASE_URL}/api/users/{userId}",
        json={"name": f"{name} edited", "job": f"{job} edited"},
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200

    response = httpx.delete(
        f"{BASE_URL}/api/users/{userId}",
    )
    assert response.status_code == 204

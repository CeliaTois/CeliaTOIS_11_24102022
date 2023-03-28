from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    @task
    def login(self):
        response = self.client.get("/")
    
    @task
    def showSummary(self):
        response = self.client.post(
            "/showSummary", {"email": "john@simplylift.co"})

    @task
    def book(self):
        response = self.client.get("/book/Fall Classic/Simply Lift")

    @task
    def purchasePlaces(self):
        response = self.client.post(
            "/purchasePlaces",
            {"places": 3, "competition": "Fall Classic", "club": "Simply Lift"})
    
    @task
    def pointsDisplay(self):
        response = self.client.get("/pointsDisplay")

    @task
    def logout(self):
        response = self.client.get("/logout")

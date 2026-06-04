from urllib.parse import quote

from src.app import activities


def test_signup_adds_student_and_returns_success(client):
    activity_name = "Chess Club"
    email = "new_student_signup@mergington.edu"

    response = client.post(
        f"/activities/{quote(activity_name)}/signup",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity_name}"}
    assert email in activities[activity_name]["participants"]

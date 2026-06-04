from urllib.parse import quote

from src.app import activities


def test_unregister_removes_student_and_returns_success(client):
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    assert email in activities[activity_name]["participants"]

    response = client.delete(
        f"/activities/{quote(activity_name)}/participants",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity_name}"}
    assert email not in activities[activity_name]["participants"]

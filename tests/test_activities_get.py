def test_get_activities_returns_expected_structure(client):
    response = client.get("/activities")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert data

    first_activity_details = next(iter(data.values()))
    assert "description" in first_activity_details
    assert "schedule" in first_activity_details
    assert "max_participants" in first_activity_details
    assert "participants" in first_activity_details
    assert isinstance(first_activity_details["participants"], list)

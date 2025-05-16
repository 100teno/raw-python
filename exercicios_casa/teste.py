# %%

import requests

def test_api():
    url = "https://pokeapi.co/api/v2/pokemon/ditto"  # Replace with your API endpoint
    response = requests.get(url)
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    data = response.json()
    assert "name" in data, "Key 'name' not found in the response"
    assert data["name"] == "ditto", f"Expected 'key' to be 'ditto', got {data['name']}"


# Run the test
if __name__ == "__main__":
    test_api()
    print("All tests passed!")


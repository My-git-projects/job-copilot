from fastapi.testclient import TestClient
from main import app  # or wherever your FastAPI app is defined

client = TestClient(app)

def test_upload_endpoint_exists():

    response = client.post(
        "/upload-resume",
        files={
            "file": (
                "dummy.pdf",
                b"fake pdf content",
                "application/pdf"
            )
        }
    )

    assert response.status_code in [200, 400]
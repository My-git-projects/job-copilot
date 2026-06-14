from app.services.resume_service import save_resume
from app.services.resume_service import get_resumes


def test_save_resume():

    save_resume(
        {
            "resume_name": "test.pdf",
            "skills": ["aws"]
        }
    )

    resumes = get_resumes()

    assert len(resumes) > 0
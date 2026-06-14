import json
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

DATA_FILE = os.path.join(
    DATA_DIR,
    "resumes.json"
)


def load_resumes():

    os.makedirs(
        DATA_DIR,
        exist_ok=True
    )

    if not os.path.exists(DATA_FILE):

        with open(
            DATA_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump([], file)

    with open(
        DATA_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_resume(resume):

    resumes = load_resumes()

    resumes.append(resume)

    with open(
        DATA_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            resumes,
            file,
            indent=4
        )


def get_resumes():

    return load_resumes()
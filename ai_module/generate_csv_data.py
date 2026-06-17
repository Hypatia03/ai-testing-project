import csv
import os

VALID_PASSWORD = "secret_sauce"

DATA = [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce"),

    ("standard_user", "invalid_pass"),
    ("locked_out_user", "invalid_pass"),
    ("problem_user", "invalid_pass"),
    ("performance_glitch_user", "invalid_pass"),
    ("error_user", "invalid_pass"),
    ("visual_user", "invalid_pass"),
]


def get_expected(username, password):

    if password != VALID_PASSWORD:
        return "fail"

    if username == "locked_out_user":
        return "fail"

    return "pass"


def generate_csv():

    os.makedirs("testdata", exist_ok=True)

    with open(
        "testdata/generated_login_data.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "username",
            "password",
            "expected"
        ])

        for username, password in DATA:

            writer.writerow([
                username,
                password,
                get_expected(username, password)
            ])

    print(
        "Generated testdata/generated_login_data.csv"
    )


if __name__ == "__main__":
    generate_csv()
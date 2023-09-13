import subprocess


def test_black():
    result = subprocess.run(
        ["black", "--check", "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    assert (
        result.returncode == 0
    ), f"Black formatting failed with output:\n{result.stderr.decode()}"

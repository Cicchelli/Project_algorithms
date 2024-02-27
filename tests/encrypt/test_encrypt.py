from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("message", "key")
        encrypt_message(123, 4)

    assert encrypt_message("message", 10) == "egassem"
    assert encrypt_message("message", 3) == "sem_egas"
    assert encrypt_message("abcdef", 4) == "fe_dcba"
    assert encrypt_message("message", 5) == "assem_eg"
    assert encrypt_message("message", 7) == "egassem"

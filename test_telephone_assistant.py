import pytest
import telephone_assistant

phones = ["380675674432", "380672832500", "380983567721"]


@pytest.mark.parametrize('user_input, result',
                         [
                             ("380", ["380675674432", "380672832500", "380983567721"]),
                             ("38067", ["380675674432", "380672832500"]),
                             ("380983", ["380983567721"])
                         ]
                         )
def test_get_all_matching_numbers(user_input, result):
    assert telephone_assistant.get_matching_numbers(phones, user_input) == result


def test_get_by_full_entered_number():
    input_data = "380983567721"
    expected = [input_data]
    actual = telephone_assistant.get_matching_numbers(phones, input_data)
    assert expected == actual


def test_get_by_wrong_entered_number():
    input_data = "some wrong data"
    expected = []
    actual = telephone_assistant.get_matching_numbers(phones, input_data)
    assert expected == actual

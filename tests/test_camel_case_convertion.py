import pytest

from src.find_unused_components import convert_camel_to_kebab


@pytest.mark.parametrize('text, expected', [
    ('CamelCase', 'camel-case'),
    ('CamelCamelCase', 'camel-camel-case'),
    ('Camel1Case', 'camel1-case'),
    ('CamelOMGCase', 'camel-omg-case'),
])
def test_camel_case_to_kebab_convertion(text, expected):
    assert convert_camel_to_kebab(text) == expected

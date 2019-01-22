import pytest

from src.find_unused_components import count_imports_usage


@pytest.fixture
def component():
    return 'tests/fixtures/Component.vue'


@pytest.mark.parametrize('name, count', [
    ('UnusedComponent', 0),
    ('UsedComponent', 1),
    ('ComponentUsedInLowercase', 1),
    ('ComponentUsedInKebabCase', 1),

    ('SomeMixin', None),  # can't count mixin usage

    ('Vue', None),  # we don't check this: eslint will do it for us
    ('_', None),
    ('mapGetters', None),
])
def test_counting_imports(component, name, count):
    got = count_imports_usage(component)

    assert got.get(name) == count

import pytest

from say import say


@pytest.mark.asyncio
async def test_say():
    assert 'Hello!' == await say('Hello!', 0)

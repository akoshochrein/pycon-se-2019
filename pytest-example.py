import pytest

from utils import afetch


@pytest.mark.asyncio
async def test_say():
    assert await afetch('example.com') is not None

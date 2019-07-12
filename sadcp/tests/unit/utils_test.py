"""Tests for utils.py"""
from uuid import UUID

from sadcp.utils import prefixed_uuid


def test_prefixed_uuid() -> None:
    pre_uuid = prefixed_uuid("quiz")
    uuid_list = pre_uuid.split("_")

    assert uuid_list[0] == "quiz"

    try:
        uuid = UUID(uuid_list[1], version=4)
    except ValueError:
        uuid = False

    assert type(uuid) is UUID
    assert str(uuid) == uuid_list[1]
    assert "quiz" + "_" + str(uuid) == pre_uuid

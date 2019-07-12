"""Utils accross various parts of the SADCP app. Should eventually be refactored."""
import uuid


def prefixed_uuid(prefix: str) -> str:
    """Accepts a prefix and returns a prefixed UUID in the format 'pre_1a2b3-45xy-8910'."""

    return prefix + "_" + str(uuid.uuid4())

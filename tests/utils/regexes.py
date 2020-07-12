import re


def valid_uuid(uuid):
    regex = re.compile(
        '^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\\Z',  # noqa: E501
        re.I
    )
    match = regex.match(uuid)
    return bool(match)

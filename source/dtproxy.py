from datetime import datetime

utcnow_return = None


def get_utcnow():
    if utcnow_return is None:
        return datetime.utcnow()

    return utcnow_return

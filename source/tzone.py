from datetime import datetime

from babel.core import get_global
from babel.dates import get_timezone, get_timezone_gmt, format_datetime, UTC


def name(tz, dt=None):
    if not dt:
        dt = datetime.now()
    return "{} {}".format(get_timezone_gmt(get_timezone(tz).localize(dt), width='iso8601_short'), tz)


def for_country(country_code):
    d = datetime.now()
    return {tz: name(tz, dt=d) for tz in get_global('territory_zones')[country_code]}


def dump(dt, tz_code, mask):
    try:
        tz = get_timezone(tz_code)
    except:
        tz = UTC

    return format_datetime(dt, mask, tzinfo=tz)

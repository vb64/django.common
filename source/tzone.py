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


# https://www.complang.tuwien.ac.at/doc/python-babel/dates.html
def dump(dt, tz_code, mask):
    return format_datetime(dt, mask, tzinfo=make_timezone(tz_code))


def make_timezone(tz_code):
    try:
        return get_timezone(tz_code)
    except:
        return UTC


def to_local(utc_dt, tz_code):
    y, m, d, h, mm = format_datetime(utc_dt, "yyyy MM dd HH mm", tzinfo=make_timezone(tz_code)).split()
    return datetime(int(y), int(m), int(d), int(h), int(mm))

def is_twodigit_odd(number):
    if number % 2 == 1:
        if number < 10:
            return False
        elif number < 100:
            return True
        else:
            return False
    else:
        return False


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    if writable_by_others:
        return True
    if sudo_mode:
        return True
    if writable_by_owner:
        if file_owner == user:
            return True
    if writable_by_group:
        if file_group in users_groups:
            return True
    return False


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        else:
            if year % 400 == 0:
                return True
            else:
                return False
    else:
        return False


def is_sunday(day, weekday_of_first):
    if weekday_of_first == 'M':
        return day in (7, 14, 21, 28)
    elif weekday_of_first == 'Tu':
        return day in (6, 13, 20, 27)
    elif weekday_of_first == 'W':
        return day in (5, 12, 19, 26)
    elif weekday_of_first == 'Th':
        return day in (4, 11, 18, 25)
    elif weekday_of_first == 'F':
        return day in (3, 10, 17, 24, 31)
    elif weekday_of_first == 'Sa':
        return day in (2, 9, 16, 23, 30)
    elif weekday_of_first == 'Su':
        return day in (1, 8, 15, 22, 29)


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    if wind_scale >= 7:
        return False
    elif rains:
        return True
    elif cloudy:
        if red_sky:
            return True
        elif strong_flower_smell:
            return True
        elif spiders_down:
            return True
        elif lying_cattle:
            return True
        else:
            return False
    elif strong_sunshine:
        return True
    else:
        return False


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    if not want_to:
        return False
    elif trouble_sleeping:
        return False
    elif after_4pm:
        return False
    elif not at_work:
        if have_30m:
            return True
        elif have_10m:
            return True
        else:
            return False
    else:
        if mad_boss:
            return False
        elif have_30m:
            return True
        elif have_10m:
            return True
        else:
            return False

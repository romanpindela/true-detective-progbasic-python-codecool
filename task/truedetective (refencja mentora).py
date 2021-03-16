def is_twodigit_odd(number):
    return 10 <= number < 100 and number % 2 == 1


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    return writable_by_others or sudo_mode or (writable_by_owner and user == file_owner) or (writable_by_group and file_group in users_groups)


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_sunday(day, weekday_of_first):
    return 0 < day <= 31 and (day + ['M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su'].index(weekday_of_first)) % 7 == 0


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    return wind_scale < 7 and (rains or (cloudy and (red_sky or strong_flower_smell or spiders_down or lying_cattle)) or strong_sunshine)


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    return want_to and not trouble_sleeping and not after_4pm and (not at_work or (at_work and not mad_boss)) and (have_30m or have_10m)

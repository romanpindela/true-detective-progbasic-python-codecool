#Is a given positive integer an odd number with two digits? Implement is_twodigit_odd in two versions!
def is_twodigit_odd(number):
    return ((100 > number > 9) and (number % 2 == 1))

'''
Does a user have write access to a unix file? The parameters are user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode. Implement has_access in two versions!
'''
def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    return (user == file_owner and writable_by_owner) or (sudo_mode) or ((file_group in users_groups) and writable_by_group ) or writable_by_others

# Is a given year (AD) a leap year in the Gregorian calendar? The official definition is the following: "Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400."
def is_leap_year(year):
    return ((year % 4 == 0) and (not year % 100 == 0)) or (year % 400 == 0)

#Is a given day of a month Sunday? We also know the first day of the month (one of ('M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su'). Suppose a 31-day-long month, so days other than 1..31 cannot be Sundays. Implement is_sunday in two versions!
def is_sunday(day, weekday_of_first):
    weekdays = {'M':1, 'Tu':2, 'W':3, 'Th':4, 'F':5, 'Sa':6, 'Su':7}
    return (day + weekdays[weekday_of_first] - 1) % 7 == 0

'''
Should True Detective bring an umbrella when going out? Well, it depends. Obviously he should when it rains, unless the wind is too strong. Wind strength greater than or equal to 7 (on the Beaufort scale) would turn the umbrella inside out. Taking the umbrella is also reasonable when it's not raining but it is cloudy, the wind is not too strong, and there are signs of a rain coming. Such signs are: red sky during sunset // flowers smell stronger than normal // spiders come down from their webs // cattle lie down in a group in the fields. But True Detective also likes to take his umbrella when the sun is shining strongly. Again, unless the wind situation is not too stormy. Implement should_bring_umbrella in two versions!
Dr Whatif's solution has no logical operators and passes all the tests.
True Detective's solution only has one return statement and passes all the tests.
'''
def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    return (rains and wind_scale < 7) or (cloudy and wind_scale <7 and (red_sky or strong_flower_smell or spiders_down or lying_cattle)) or (strong_sunshine and wind_scale < 7)


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    return (want_to and not trouble_sleeping and not after_4pm and ((at_work and not mad_boss) or not at_work) and (have_30m or have_10m))
    

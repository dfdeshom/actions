import random
import calendar
from django.contrib.auth.models import User
from .models import Action
from datetime import date, timedelta


#users = list(User.objects.all())

action_titles = ["Running", "Sleeping", "Eating", "Driving",
                 "Sitting", "Working", "Editing", "Discussing"]
places = ["school", "work", "church", "home",
          "drugstore", "theater", "hotel", "restaurant"]


def create_random_user():
    names = ["david", "eric", "frantz"]
    name = random.choice(names)
    user = User.objects.create_user(name, "%s@email.com" % name, name)
    user.save()
    return user


def random_date_from_this_month():
    """Create a random date that falls within this month."""
    today = date.today()
    _, last_day = calendar.monthrange(today.year, today.month)
    return date(year=today.year,
                month=today.month,
                day=random.randint(1, last_day))


def random_date():
    """Create a random date that's not in the current month."""
    today = date.today()
    future = timedelta(days=random.randint(31, 61))
    return today + future


def create_random_action(thismonth=True):
    """Create a random action."""
    title = random.choice(action_titles)
    place = random.choice(places)
    description = "{action} at the {place}".format(action=title, place=place)
    date = None
    if thismonth:
        date = random_date_from_this_month()
    else:
        date = random_date()

    Action.objects.create(title=title,
                          description=description,
                          user=create_random_user(),
                          creation_date=date
                          )
    if thismonth is False:
        print 'date returned:', date, title

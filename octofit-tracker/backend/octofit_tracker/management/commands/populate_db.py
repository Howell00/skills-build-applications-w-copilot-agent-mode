from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        get_user_model().objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            get_user_model().objects.create_user(username='ironman', email='ironman@marvel.com', team=marvel),
            get_user_model().objects.create_user(username='spiderman', email='spiderman@marvel.com', team=marvel),
            get_user_model().objects.create_user(username='batman', email='batman@dc.com', team=dc),
            get_user_model().objects.create_user(username='superman', email='superman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='run', distance=5)
        Activity.objects.create(user=users[1], type='cycle', distance=10)
        Activity.objects.create(user=users[2], type='swim', distance=2)
        Activity.objects.create(user=users[3], type='run', distance=8)

        # Create workouts
        Workout.objects.create(name='Morning Cardio', description='30 min run')
        Workout.objects.create(name='Strength Training', description='Upper body workout')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=15)
        Leaderboard.objects.create(team=dc, points=10)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))

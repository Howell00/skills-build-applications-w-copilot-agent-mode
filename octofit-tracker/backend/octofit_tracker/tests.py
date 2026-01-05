from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        self.user1 = User.objects.create_user(username='ironman', email='ironman@marvel.com', team=marvel)
        self.user2 = User.objects.create_user(username='batman', email='batman@dc.com', team=dc)
        Activity.objects.create(user=self.user1, type='run', distance=5)
        Workout.objects.create(name='Morning Cardio', description='30 min run')
        Leaderboard.objects.create(team=marvel, points=15)

    def test_user_team(self):
        self.assertEqual(self.user1.team.name, 'Marvel')
        self.assertEqual(self.user2.team.name, 'DC')

    def test_activity(self):
        activity = Activity.objects.get(user=self.user1)
        self.assertEqual(activity.type, 'run')
        self.assertEqual(activity.distance, 5)

    def test_workout(self):
        workout = Workout.objects.get(name='Morning Cardio')
        self.assertEqual(workout.description, '30 min run')

    def test_leaderboard(self):
        leaderboard = Leaderboard.objects.get(team__name='Marvel')
        self.assertEqual(leaderboard.points, 15)

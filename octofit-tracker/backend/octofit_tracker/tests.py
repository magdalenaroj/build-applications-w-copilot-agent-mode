from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Avengers", universe="Marvel")
        self.user = User.objects.create(name="Tony Stark", email="tony@stark.com", team=self.team)
        self.workout = Workout.objects.create(name="Pushups", description="Do 50 pushups")
        self.activity = Activity.objects.create(user=self.user, activity_type="Running", duration_minutes=30, date="2025-12-29")
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100, rank=1)
        self.workout.suggested_for.add(self.user)

    def test_team_str(self):
        self.assertEqual(str(self.team), "Avengers")

    def test_user_str(self):
        self.assertEqual(str(self.user), "Tony Stark")

    def test_activity_str(self):
        self.assertEqual(str(self.activity), "Tony Stark - Running")

    def test_workout_str(self):
        self.assertEqual(str(self.workout), "Pushups")

    def test_leaderboard_str(self):
        self.assertEqual(str(self.leaderboard), "Avengers - Rank 1")

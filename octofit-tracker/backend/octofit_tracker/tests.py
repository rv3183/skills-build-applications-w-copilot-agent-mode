from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name="Test Hero", email="test@hero.com", team="Marvel")
        self.assertEqual(user.name, "Test Hero")
        self.assertEqual(user.team, "Marvel")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Marvel", members=["test@hero.com"])
        self.assertEqual(team.name, "Marvel")
        self.assertIn("test@hero.com", team.members)

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user="test@hero.com", type="run", distance=5, duration=30)
        self.assertEqual(activity.type, "run")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team="Marvel", points=100)
        self.assertEqual(lb.team, "Marvel")
        self.assertEqual(lb.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(user="test@hero.com", workout="HIIT", duration=45)
        self.assertEqual(workout.workout, "HIIT")

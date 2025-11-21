from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Drop collections if they exist
        for col in ['users', 'teams', 'activities', 'leaderboard', 'workouts']:
            db[col].drop()

        # Users (superheroes)
        users = [
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
            {"name": "Spider-Man", "email": "spiderman@marvel.com", "team": "Marvel"},
            {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
        ]
        db.users.insert_many(users)
        db.users.create_index([("email", 1)], unique=True)

        # Teams
        teams = [
            {"name": "Marvel", "members": [u["email"] for u in users if u["team"] == "Marvel"]},
            {"name": "DC", "members": [u["email"] for u in users if u["team"] == "DC"]},
        ]
        db.teams.insert_many(teams)

        # Activities
        activities = [
            {"user": "ironman@marvel.com", "type": "run", "distance": 5, "duration": 30},
            {"user": "cap@marvel.com", "type": "cycle", "distance": 20, "duration": 60},
            {"user": "spiderman@marvel.com", "type": "swim", "distance": 2, "duration": 40},
            {"user": "superman@dc.com", "type": "run", "distance": 10, "duration": 50},
            {"user": "batman@dc.com", "type": "cycle", "distance": 15, "duration": 45},
            {"user": "wonderwoman@dc.com", "type": "swim", "distance": 3, "duration": 55},
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {"team": "Marvel", "points": 150},
            {"team": "DC", "points": 140},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {"user": "ironman@marvel.com", "workout": "HIIT", "duration": 45},
            {"user": "cap@marvel.com", "workout": "Strength", "duration": 60},
            {"user": "spiderman@marvel.com", "workout": "Cardio", "duration": 30},
            {"user": "superman@dc.com", "workout": "HIIT", "duration": 50},
            {"user": "batman@dc.com", "workout": "Strength", "duration": 55},
            {"user": "wonderwoman@dc.com", "workout": "Cardio", "duration": 40},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

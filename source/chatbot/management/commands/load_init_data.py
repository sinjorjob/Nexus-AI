from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Load initial data for SystemInstructions'

    def handle(self, *args, **options):
        fixture_dir = os.path.join(settings.BASE_DIR, 'chatbot', 'fixtures')
        fixture_file = 'system_instructions_data.json'
        fixture_path = os.path.join(fixture_dir, fixture_file)

        if not os.path.exists(fixture_path):
            self.stdout.write(self.style.WARNING(f'Fixture file not found: {fixture_path}'))
            self.stdout.write(self.style.WARNING('Please run "python manage.py export_system_instructions" first.'))
            return

        try:
            call_command('loaddata', fixture_file)
            self.stdout.write(self.style.SUCCESS('Successfully loaded initial data for SystemInstructions'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error loading data: {str(e)}'))
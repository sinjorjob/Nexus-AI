from django.core.management.base import BaseCommand
from django.core import serializers
from chatbot.models import SystemInstructions
import json

class Command(BaseCommand):
    help = 'Export SystemInstructions data to a JSON file'

    def handle(self, *args, **options):
        data = serializers.serialize("json", SystemInstructions.objects.all())
        
        with open('system_instructions_data.json', 'w') as outfile:
            json.dump(json.loads(data), outfile, indent=2)
        
        self.stdout.write(self.style.SUCCESS('Successfully exported SystemInstructions data'))
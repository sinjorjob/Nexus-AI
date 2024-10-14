from swarm import Swarm
from openai import OpenAI
from django.conf import settings

def get_openai_client():
    openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)
    return Swarm(client=openai_client)
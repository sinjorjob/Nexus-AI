from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SystemInstructions
from .agents import get_agent, run_agent
from .utils import get_openai_client
import json

@csrf_exempt
def chat_view(request):
    if request.method == 'GET':
        request.session['messages'] = []
        return render(request, 'chatbot/chat.html')
    
    elif request.method == 'POST':
        messages = request.session.get('messages', [])
        data = json.loads(request.body)
        user_input = data.get('message')
        current_agent = data.get('current_agent', '在庫管理システム')
        
        messages.append({"role": "user", "content": user_input})
        
        current_agent_obj = get_agent(current_agent)
        client = get_openai_client()
        
        response = run_agent(client, current_agent_obj, messages)
        
        messages = response.messages
        request.session['messages'] = messages
        
        return JsonResponse({
            'message': response.messages[-1]['content'],
            'agent_name': response.agent.name,
            'current_agent': '在庫管理システム' if response.agent.name == "在庫管理システム" else '顧客関係管理システム',
            'messages': messages
        })
    
    return render(request, 'chatbot/chat.html')

def update_instructions_view(request):
    instructions = SystemInstructions.objects.all()
    return render(request, 'chatbot/update_instructions.html', {'instructions': instructions})

@csrf_exempt
def update_instructions(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        agent_name = data.get('agent_name')
        instructions = data.get('instructions')
        
        system_instructions, created = SystemInstructions.objects.get_or_create(name=agent_name)
        system_instructions.instructions = instructions
        system_instructions.save()
        
        return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'error'}, status=400)
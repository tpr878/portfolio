from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import PortfolioItem
from .ai_service import get_ai_response
import re


def index(request):
    """Render the main chat interface."""
    return render(request, 'portfolio/index.html')


def chat_response(request):
    """
    API endpoint for chat responses.
    - Direct commands (projects, skills, etc.) → Show cards
    - Questions about anything → Use AI for concise explanations
    """
    message = request.GET.get('message', '').lower().strip()
    original_message = request.GET.get('message', '').strip()
    
    # Detect if this is a QUESTION (should use AI)
    question_patterns = [
        r'\?',                          # Has question mark
        r'^(can|does|is|has|what|how|where|when|why|who|could|would|should|do|did)',  # Starts with question word
        r'(know|capable|able|experience with|familiar|work with|good at)',  # Ability questions
        r'(tell me about|explain|describe)',  # Explanation requests
    ]
    
    is_question = any(re.search(pattern, message) for pattern in question_patterns)
    
    # Direct category commands (single words or short phrases without question intent)
    category_commands = {
        'projects': 'project',
        'project': 'project',
        'education': 'education',
        'experience': 'experience',
        'skills': 'skill',
        'skill': 'skill',
        'publications': 'publication',
        'publication': 'publication',
        'about': 'profile',
        'profile': 'profile',
        'contact': 'profile',
    }
    
    # If it's a direct command (1-2 words, matches category), show cards
    word_count = len(message.split())
    if not is_question and word_count <= 2:
        for cmd, category in category_commands.items():
            if cmd in message:
                items = PortfolioItem.objects.filter(category=category)
                if items.exists():
                    response_html = render_to_string('portfolio/partials/cards.html', {
                        'items': items,
                        'response_type': category
                    })
                    return JsonResponse({
                        'success': True,
                        'type': category,
                        'count': items.count(),
                        'html': response_html
                    })
    
    # For questions or longer queries, use AI
    if len(original_message) > 3:
        ai_response = get_ai_response(original_message)
        response_html = f'''
            <div class="ai-response">
                <p class="text-purple-400 text-sm mb-2">🤖 AI Response</p>
                <p class="text-gray-200 leading-relaxed">{ai_response}</p>
            </div>
        '''
        return JsonResponse({
            'success': True,
            'type': 'ai_response',
            'html': response_html
        })
    
    # Default: return greeting
    response_html = render_to_string('portfolio/partials/greeting.html')
    return JsonResponse({
        'success': True,
        'type': 'greeting',
        'html': response_html
    })



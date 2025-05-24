import random
import logging

logger = logging.getLogger(__name__)

class ResponseGenerator:
    def __init__(self):
        self.responses = {
            'high': [
                "I'm very concerned about what you shared. Your safety is important right now.",
                "I hear you're in significant pain. Please know help is available immediately."
            ],
            'medium': [
                "That sounds really difficult. Would you like to talk more about what you're experiencing?",
                "I can hear you're struggling. You're not alone in this."
            ],
            'low': [
                "Thank you for sharing. How can I support you today?",
                "I'm here to listen. What would be helpful to talk about?"
            ]
        }
        
        self.coping_techniques = {
            'high': "Try the 5-4-3-2-1 grounding technique: Name 5 things you see, 4 things you can touch, 3 things you hear, 2 things you smell, and 1 thing you can taste.",
            'medium': "When feeling this way, try box breathing: Breathe in for 4 counts, hold for 4, breathe out for 4, hold for 4. Repeat 4 times.",
            'low': "It might help to write down three things you're grateful for today, no matter how small."
        }

    def generate_response(self, analysis, session):
        """Simplified response generation that matches your NLP output"""
        try:
            risk_level = analysis.get('risk_level', 'low')
            
            # Get base response
            response = {
                'message': random.choice(self.responses[risk_level]),
                'resources': ['crisis_hotlines'] if risk_level == 'high' else [],
                'coping_strategy': self.coping_techniques[risk_level],
                'risk_level': risk_level
            }
            
            # Add depression keywords if found
            if analysis.get('keywords_found'):
                response['keywords'] = analysis['keywords_found']
                
            return response
            
        except Exception as e:
            logger.error(f"Response generation error: {str(e)}")
            return {
                'message': "I want to help but am having trouble responding. Please know you're not alone.",
                'resources': ['crisis_hotlines'],
                'coping_strategy': "Contact a professional who can help immediately",
                'risk_level': 'high'
            }
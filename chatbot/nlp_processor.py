import json
from textblob import TextBlob
import logging

logger = logging.getLogger(__name__)

class NLPProcessor:
    """Enhanced Natural Language Processor for mental health chatbot"""
    
    def __init__(self):
        self.depression_keywords = self._load_keywords()
        
    def _load_keywords(self):
        """Load depression keywords from JSON file with fallback defaults"""
        try:
            with open('data/depression_keywords.json') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading keywords: {e}")
            return {
                "emotional": ["sad", "depressed", "hopeless", "empty"],
                "behavioral": ["cant sleep", "no energy", "isolate"],
                "cognitive": ["worthless", "guilty", "failure"],
                "crisis": ["suicid", "kill myself", "end it all", "want to die"]
            }
    def analyze_message(self, message):
        if not message or not isinstance(message, str):
            return {
                'original_message': '',
                'sentiment': 0.0,
                'keywords_found': [],
                'risk_level': 'low'
            }

        message_lower = message.lower().strip()
        normalized_msg = message_lower.replace("'", "").replace(" ", "")
        
        analysis = {
            'original_message': message,
            'sentiment': TextBlob(message).sentiment.polarity,
            'keywords_found': [],
            'risk_level': 'low'
        }

        # Enhanced keyword matching
        for category, keywords in self.depression_keywords.items():
            for keyword in keywords:
                # Check both exact matches and word boundaries
                if (f' {keyword} ' in f' {message_lower} ' or 
                    keyword in normalized_msg):
                    analysis['keywords_found'].append((category, keyword))
        
        # More precise risk assessment
        if any(k[0] == 'crisis' for k in analysis['keywords_found']):
            analysis['risk_level'] = 'high'
        elif len(analysis['keywords_found']) >= 2:  # Require multiple indicators for medium
            analysis['risk_level'] = 'medium'
            
        return analysis
    
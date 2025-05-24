"""
Mental Health Screening Module
Implements PHQ-2 based screening for depression assessment
"""

import json
import os
import re
import logging

logger = logging.getLogger(__name__)

class MentalHealthScreening:
    def __init__(self):
        self.screening_questions = []
        self.current_question_index = 0
        self.user_responses = []
        self.load_screening_questions()
    
    def load_screening_questions(self):
        """Load screening questions from JSON file"""
        try:
            questions_path = 'data/screening_questions.json'
            if os.path.exists(questions_path):
                with open(questions_path, 'r') as f:
                    data = json.load(f)
                    self.screening_questions = data.get('questions', [])
            else:
                logger.warning("Screening questions file not found, using defaults")
                self.screening_questions = self.get_default_screening_questions()
        except Exception as e:
            logger.error(f"Error loading screening questions: {str(e)}")
            self.screening_questions = self.get_default_screening_questions()
    
    def get_default_screening_questions(self):
        """Return default PHQ-2 based screening questions"""
        return [
            {
                "id": 1,
                "question": "Over the past 2 weeks, how often have you been bothered by little interest or pleasure in doing things?",
                "type": "frequency",
                "responses": {
                    "not at all": 0,
                    "several days": 1,
                    "more than half the days": 2,
                    "nearly every day": 3
                }
            },
            {
                "id": 2,
                "question": "Over the past 2 weeks, how often have you felt down, depressed, or hopeless?",
                "type": "frequency",
                "responses": {
                    "not at all": 0,
                    "several days": 1,
                    "more than half the days": 2,
                    "nearly every day": 3
                }
            },
            {
                "id": 3,
                "question": "In the past month, have you had thoughts of being better off dead or hurting yourself?",
                "type": "yes_no",
                "responses": {
                    "yes": 5,
                    "no": 0
                }
            }
        ]
    
    def start_screening(self):
        """Start the screening process"""
        self.current_question_index = 0
        self.user_responses = []
        
        introduction = (
            "I'd like to ask you a few brief questions to better understand how you're feeling. "
            "This will help me provide more personalized support. Your responses are confidential.\n\n"
        )
        
        first_question = self.get_current_question()
        return introduction + first_question
    
    def get_current_question(self):
        """Get the current screening question"""
        if self.current_question_index < len(self.screening_questions):
            question_data = self.screening_questions[self.current_question_index]
            question = question_data['question']
            
            # Add response options for frequency questions
            if question_data['type'] == 'frequency':
                options = "\n".join([
                    "• Not at all",
                    "• Several days", 
                    "• More than half the days",
                    "• Nearly every day"
                ])
                return f"{question}\n\n{options}\n\nPlease respond with one of the options above."
            
            elif question_data['type'] == 'yes_no':
                return f"{question}\n\nPlease respond with 'yes' or 'no'."
            
            return question
        
        return None
    
    def process_response(self, current_state, user_response):
        """Process user response to screening question"""
        try:
            # Clean and normalize the response
            response = user_response.strip().lower()
            
            # Get current question data
            if self.current_question_index >= len(self.screening_questions):
                return self._complete_screening()
            
            question_data = self.screening_questions[self.current_question_index]
            score = self._parse_response(response, question_data)
            
            # Store the response
            self.user_responses.append({
                'question_id': question_data['id'],
                'response': response,
                'score': score
            })
            
            # Move to next question
            self.current_question_index += 1
            
            # Check if screening is complete
            if self.current_question_index >= len(self.screening_questions):
                return self._complete_screening()
            else:
                return {
                    'completed': False,
                    'next_question': self.get_current_question(),
                    'next_state': {
                        'question_index': self.current_question_index,
                        'responses': self.user_responses
                    }
                }
                
        except Exception as e:
            logger.error(f"Error processing screening response: {str(e)}")
            return self._handle_screening_error()
    
    def _parse_response(self, response, question_data):
        """Parse user response and return score"""
        response_mapping = question_data['responses']
        
        # Direct match first
        if response in response_mapping:
            return response_mapping[response]
        
        # Fuzzy matching for common variations
        response_variations = {
            'not at all': ['not', 'never', 'none', '0', 'zero'],
            'several days': ['several', 'some', 'few', 'sometimes', '1'],
            'more than half the days': ['more than half', 'most', 'often', 'frequently', '2'],
            'nearly every day': ['nearly every', 'every', 'always', 'daily', 'all', '3'],
            'yes': ['yes', 'y', 'yeah', 'yep', 'true'],
            'no': ['no', 'n', 'nope', 'false']
        }
        
        for standard_response, variations in response_variations.items():
            if any(variation in response for variation in variations):
                if standard_response in response_mapping:
                    return response_mapping[standard_response]
        
        # Default to lowest score if can't parse
        return min(response_mapping.values())
    
    def _complete_screening(self):
        """Complete the screening and generate results"""
        total_score = sum(r['score'] for r in self.user_responses)
        
        # Determine risk level based on score
        if total_score >= 6 or any(r['score'] == 5 for r in self.user_responses):
            risk_level = 'high'
        elif total_score >= 3:
            risk_level = 'medium'
        else:
            risk_level = 'low'
        
        # Generate final message and recommendations
        final_message, resources = self._generate_screening_results(total_score, risk_level)
        
        return {
            'completed': True,
            'final_message': final_message,
            'recommended_resources': resources,
            'risk_level': risk_level,
            'score': total_score
        }
    
    def _generate_screening_results(self, score, risk_level):
        """Generate personalized results message and resources"""
        if risk_level == 'high':
            message = (
                "Thank you for sharing this information with me. Based on your responses, "
                "it sounds like you're going through a really difficult time right now. "
                "I want you to know that you're not alone, and there are people who can help.\n\n"
                "I strongly encourage you to reach out to a mental health professional or "
                "a crisis helpline. Your feelings are valid, and you deserve support."
            )
            resources = ['crisis_hotlines', 'emergency_services', 'therapy_resources']
            
        elif risk_level == 'medium':
            message = (
                "Thank you for answering these questions. It sounds like you've been "
                "experiencing some challenging feelings lately. These feelings are more "
                "common than you might think, and there are effective ways to feel better.\n\n"
                "I'd recommend considering talking to a counselor or therapist, as they "
                "can provide personalized strategies to help you feel better."
            )
            resources = ['therapy_resources', 'self_help_resources', 'support_groups']
            
        else:
            message = (
                "Thank you for taking the time to answer these questions. While everyone "
                "experiences ups and downs, it sounds like you're managing relatively well overall.\n\n"
                "Remember that it's always okay to seek support when you need it, and "
                "there are many resources available if things change."
            )
            resources = ['self_help_resources', 'wellness_resources']
        
        return message, resources
    
    def _handle_screening_error(self):
        """Handle errors during screening"""
        return {
            'completed': True,
            'final_message': (
                "I'm sorry, I had trouble processing your response. "
                "Let's focus on providing you with some helpful resources instead."
            ),
            'recommended_resources': ['crisis_hotlines', 'therapy_resources'],
            'risk_level': 'medium',
            'score': 0
        }
    
    def get_current_state(self):
        """Get current screening state"""
        return {
            'question_index': self.current_question_index,
            'responses': self.user_responses
        }
    
    def reset_screening(self):
        """Reset screening to initial state"""
        self.current_question_index = 0
        self.user_responses = []

from flask import Flask, render_template, request, jsonify
from chatbot.nlp_processor import NLPProcessor
from chatbot.response_generator import ResponseGenerator
from chatbot.resource_manager import ResourceManager
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Initialize components
try:
    nlp_processor = NLPProcessor()
    response_generator = ResponseGenerator()
    resource_manager = ResourceManager()
except Exception as e:
    logger.error(f"Failed to initialize components: {str(e)}")
    raise e

@app.route('/')
def home():
    """Serve the main chat interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages with proper error handling"""
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'response': "Please type a message so I can understand how to help.",
                'resources': [],
                'risk_level': 'low'
            })

        # Process message through all components
        analysis = nlp_processor.analyze_message(user_message)
        logger.info(f"Analysis: {analysis}")
        
        response = response_generator.generate_response(analysis, {})
        logger.info(f"Generated response: {response}")
        
        # Get appropriate resources
        resource_types = []
        if analysis.get('risk_level') == 'high':
            resource_types = ['crisis_hotlines', 'emergency_services']
        elif 'resources' in response:
            resource_types = response['resources']
        
        resources = resource_manager.get_resources_by_type(resource_types)
        
        return jsonify({
            'response': response['message'],
            'resources': resources,
            'risk_level': analysis.get('risk_level', 'low'),
            'keywords': analysis.get('keywords_found', [])
        })

    except Exception as e:
        logger.error(f"Error processing message: {str(e)}", exc_info=True)
        return jsonify({
            'response': "I'm having trouble processing your message. Please try again.",
            'resources': resource_manager.get_crisis_resources(),
            'risk_level': 'high'
        })

if __name__ == '__main__':
    # Create data directory if missing
    os.makedirs('data', exist_ok=True)
    
    # Run the app with explicit parameters
    try:
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=True,
            threaded=True,
            use_reloader=False  # Disable reloader for more stable debugging
        )
    except Exception as e:
        logger.error(f"Failed to start Flask app: {str(e)}")
        raise e
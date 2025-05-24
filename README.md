AI-Based Mental Health Chatbot 🧠💚

A compassionate AI chatbot designed to provide emotional first-aid, mental health screening, and resource guidance using natural language processing and sentiment analysis.

🎯 Project Overview

This chatbot addresses real-world mental health challenges by:

    Emotional First-Aid: Detecting depressive language patterns and providing immediate support

    Mental Health Screening: Conducting brief assessments with personalized recommendations

    Resource Directory: Connecting users with professional help and self-help resources

🚀 Features

Core Functionality

    Depression keyword detection using NLP

    Sentiment analysis for emotional state assessment

    Interactive mental health screening (PHQ-2 based)

    Personalized coping strategies and CBT techniques

    Crisis resource directory with hotlines and professional help

    Conversation history tracking

    Privacy-focused design (no personal data storage)

Technical Features

    Real-time text analysis

    Responsive web interface

    JSON-based resource database

    Modular Python architecture

    Flask web framework integration

🛠️ Technology Stack

    Backend: Python 3.8+

    Web Framework: Flask

    NLP Libraries:

        NLTK (Natural Language Toolkit)

        TextBlob (Sentiment Analysis)

    Frontend: HTML5, CSS3, JavaScript

    Data Storage: JSON files (for resources and keywords)

    Development Environment: VS Code

📁 Project Structure

mental-health-chatbot/  
│  
├── app.py                 # Main Flask application  
├── chatbot/  
│   ├── __init__.py  
│   ├── nlp_processor.py   # NLP and sentiment analysis  
│   ├── screening.py       # Mental health screening logic  
│   ├── response_generator.py # Response generation  
│   └── resource_manager.py   # Resource database management  
│  
├── data/  
│   ├── depression_keywords.json  
│   ├── coping_strategies.json  
│   ├── screening_questions.json  
│   └── resources.json  
│  
├── static/  
│   ├── css/  
│   │   └── style.css  
│   └── js/  
│       └── chat.js  
│  
├── templates/  
│   └── index.html  
│  
├── tests/  
│   ├── test_nlp.py  
│   └── test_screening.py  
│  
├── requirements.txt  
├── README.md  
└── setup.py  

🏁 Getting Started

Prerequisites

    Python 3.8 or higher

    pip (Python package manager)

    VS Code (recommended)

Installation Steps

    Clone or create project directory
    bash

mkdir mental-health-chatbot  
cd mental-health-chatbot  

Set up virtual environment (Recommended)
bash

python -m venv venv  

# On Windows:  
venv\Scripts\activate  

# On macOS/Linux:  
source venv/bin/activate  

Install dependencies
bash

pip install -r requirements.txt  

Download NLTK data
python

python -c "import nltk; nltk.download('punkt'); nltk.download('vader_lexicon')"  

Run the application
bash

    python app.py  

    Open your browser
    Navigate to http://localhost:5000

🧪 Testing

Run tests to ensure everything works correctly:
bash

python -m pytest tests/  

📊 How It Works

    Depression Keyword Detection
    The chatbot analyzes user input for depression-related keywords and phrases:

    Emotional indicators: "worthless", "hopeless", "can't sleep"

    Behavioral patterns: "can't get out of bed", "no energy"

    Cognitive symptoms: "can't concentrate", "feel guilty"

    Sentiment Analysis
    Uses TextBlob to determine emotional polarity:

    Negative sentiment triggers supportive responses

    Neutral/Positive sentiment receives encouraging feedback

    Crisis indicators immediately provide emergency resources

    Mental Health Screening
    Implements a simplified PHQ-2 screening:

    Asks 2-3 key depression screening questions

    Scores responses on a scale

    Provides personalized recommendations based on results

    Response Generation

    Validation: Acknowledges user's feelings

    Coping strategies: Provides CBT techniques, grounding exercises

    Resources: Suggests appropriate professional help

🔒 Privacy & Ethics

    No personal data storage: Conversations are not permanently stored

    Crisis detection: Immediately provides emergency resources for high-risk situations

    Professional boundaries: Clearly states it's not a replacement for professional therapy

    Resource focus: Emphasizes connecting users with qualified mental health professionals

📈 Future Enhancements

    Voice input/output capabilities

    Multi-language support

    Integration with wearable devices

    Advanced ML models for better emotion detection

    Mobile app version

    Mood tracking over time

    Personalized meditation recommendations

🤝 Contributing

    Fork the repository

    Create a feature branch (git checkout -b feature/AmazingFeature)

    Commit your changes (git commit -m 'Add some AmazingFeature')

    Push to the branch (git push origin feature/AmazingFeature)

    Open a Pull Request

📞 Crisis Resources

If you or someone you know is in crisis:

    National Suicide Prevention Lifeline: 988

    Crisis Text Line: Text HOME to 741741

    International Association for Suicide Prevention: https://www.iasp.info/resources/Crisis_Centres/

📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments

    Mental health professionals who reviewed the approach

    Open-source NLP libraries that make this possible

    Crisis intervention resources that save lives

📞 Contact

Nokwanda Phewa - nokwandaphewa18@gmail.com
Project Link: https://github.com/NokwandaPhewa/mental-health-chatbot 

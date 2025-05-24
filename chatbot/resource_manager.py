import json
import logging

logger = logging.getLogger(__name__)

class ResourceManager:
    def __init__(self):
        self.resources = self._load_resources()
    
    def _load_resources(self):
        """Load mental health resources from JSON file"""
        try:
            with open('data/resources.json') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading resources: {str(e)}")
            return {
                "crisis_hotlines": [
                    {
                        "name": "National Suicide Prevention Lifeline",
                        "phone": "988",
                        "description": "24/7 free and confidential support",
                        "website": "https://suicidepreventionlifeline.org"
                    }
                ]
            }
    
    def get_crisis_resources(self):
        """Get immediate crisis resources"""
        return self.resources.get('crisis_hotlines', [])
    
    def get_resources_by_type(self, resource_types):
        """Get resources by specific types"""
        return [item for r_type in resource_types 
                for item in self.resources.get(r_type, [])]
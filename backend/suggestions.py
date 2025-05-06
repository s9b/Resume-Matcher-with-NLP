class SuggestionGenerator:
    def __init__(self):
        self.action_verbs = [
            "developed", "implemented", "designed", "managed", "led",
            "created", "optimized", "improved", "analyzed", "engineered"
        ]

    def generate_suggestions(self, resume_text: str, job_description: str) -> list[str]:
        """Generate improvement suggestions based on resume and job description."""
        suggestions = []
        
        # Check for action verbs
        used_verbs = [verb for verb in self.action_verbs if verb in resume_text.lower()]
        if len(used_verbs) < 5:
            suggestions.append(
                "Consider using more action verbs like: " + 
                ", ".join(set(self.action_verbs) - set(used_verbs))
            )

        # Add basic suggestions
        suggestions.extend([
            "Quantify your achievements with metrics where possible",
            "Ensure your resume is properly formatted and consistent",
            "Tailor your experience section to match job requirements"
        ])
        
        return suggestions
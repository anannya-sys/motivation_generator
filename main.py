
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Pre-written motivational quotes categorized by mood
motivational_quotes = {
    "anxious": [
        "Take a deep breath. You have overcome challenges before, and you will overcome this one too.",
        "Anxiety is temporary, but your strength is permanent.",
        "You are braver than you believe, stronger than you seem, and smarter than you think.",
        "This feeling will pass. Focus on what you can control right now.",
        "You've survived 100% of your difficult days so far. You're doing great."
    ],
    "unmotivated": [
        "The hardest part is starting. Once you begin, momentum will carry you forward.",
        "You don't have to be great to get started, but you have to get started to be great.",
        "Progress, not perfection. Every small step counts.",
        "Your future self will thank you for the effort you put in today.",
        "Motivation gets you started. Habit keeps you going."
    ],
    "stressed": [
        "You can't control everything, but you can control your response to it.",
        "Stress is temporary, but the lessons you learn are permanent.",
        "Take it one task at a time. You don't have to solve everything at once.",
        "Remember: you've handled stress before, and you handled it well.",
        "This too shall pass. Focus on what truly matters."
    ],
    "need_focus": [
        "Where focus goes, energy flows and results show. - Tony Robbins",
        "The successful warrior is the average person with laser-like focus. - Bruce Lee",
        "Focus on the step in front of you, not the whole staircase.",
        "Concentration is the secret of strength. - Ralph Waldo Emerson",
        "Your focus determines your reality. Choose wisely."
    ],
    "sad": [
        "Every sunset brings the promise of a new dawn.",
        "It's okay to not be okay. Healing takes time, and that's perfectly fine.",
        "You are allowed to feel your feelings. They don't define you, they guide you.",
        "Even the darkest night will end and the sun will rise. - Victor Hugo",
        "Your current chapter is not your whole story. Keep writing."
    ],
    "confident": [
        "Believe in yourself and all that you are. You are capable of amazing things.",
        "Confidence is not 'they will like me.' Confidence is 'I'll be fine if they don't.'",
        "You are your only limit. Break through and soar higher.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "The world needs what you have to offer. Share your gifts boldly."
    ],
    "tired": [
        "Rest when you're weary. Refresh and renew yourself, your body, your mind, your spirit.",
        "Sometimes the most productive thing you can do is rest.",
        "It's okay to take breaks. You're human, not a machine.",
        "Energy flows where intention goes. Rest with intention.",
        "You can't pour from an empty cup. Take care of yourself first."
    ]
}

# Custom responses for specific keywords
custom_responses = {
    'overwhelmed': [
        "Take it one step at a time. You don't have to do everything at once.",
        "Break it down into smaller pieces. Every mountain is climbed one step at a time.",
        "You've handled difficult situations before, and you'll handle this one too.",
        "It's okay to feel overwhelmed. Take a deep breath and focus on what you can control."
    ],
    'presentation': [
        "You know your material better than anyone in that room. Trust yourself.",
        "Confidence comes from preparation, and you've put in the work.",
        "They want you to succeed. Share your knowledge with confidence.",
        "Every expert was once a beginner. You've got this!"
    ],
    'work': [
        "Your hard work will pay off. Keep pushing forward.",
        "Every challenge at work is an opportunity to grow stronger.",
        "You bring unique value to your workplace. Don't forget that.",
        "Progress, not perfection. You're doing better than you think."
    ],
    'exam': [
        "You've prepared for this moment. Trust in your knowledge.",
        "One question at a time. You've got the tools you need.",
        "Your effort will show in your results. Believe in yourself.",
        "Take a deep breath. You're more ready than you realize."
    ],
    'relationship': [
        "Healthy relationships take work from both sides. Communication is key.",
        "You deserve to be treated with kindness and respect.",
        "It's okay to set boundaries. Taking care of yourself isn't selfish.",
        "Love yourself first, and others will follow."
    ],
    'lonely': [
        "You are not alone, even when it feels that way.",
        "Reaching out is a sign of strength, not weakness.",
        "This feeling is temporary. Better days are ahead.",
        "Your presence matters more than you know."
    ],
    'failure': [
        "Failure is not the opposite of success, it's part of it.",
        "Every setback is a setup for a comeback.",
        "You haven't failed until you stop trying.",
        "Learn from this moment and use it to fuel your next attempt."
    ],
    'change': [
        "Change is hard, but staying the same when you're unhappy is harder.",
        "You have the power to write a new chapter in your story.",
        "Every ending is a new beginning in disguise.",
        "Growth happens outside your comfort zone."
    ]
}

def get_motivation_by_mood(mood):
    """Get a random motivational quote based on mood"""
    if mood in motivational_quotes:
        return random.choice(motivational_quotes[mood])
    return "You are stronger than you know and more capable than you realize."

def get_custom_motivation(feeling):
    """Get motivation based on custom feeling description"""
    feeling_lower = feeling.lower()
    
    # Check for keywords in the feeling
    for keyword, responses in custom_responses.items():
        if keyword in feeling_lower:
            return random.choice(responses)
    
    # Default responses for general feelings
    general_responses = [
        "You are stronger than you know and more capable than you realize.",
        "Every challenge is an opportunity to grow and become better.",
        "Take one step at a time. Progress, not perfection.",
        "Your current situation is not your final destination.",
        "You have the power to change your story. Start writing a new chapter."
    ]
    
    return random.choice(general_responses)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-motivation', methods=['POST'])
def get_motivation():
    data = request.json
    mood = data.get('mood', '').lower()
    custom_feeling = data.get('custom_feeling', '').strip()

    if custom_feeling:
        quote = get_custom_motivation(custom_feeling)
        mood_description = "Personalized for your feelings"
    elif mood:
        quote = get_motivation_by_mood(mood)
        mood_description = f"For {mood.replace('_', ' ').title()}"
    else:
        quote = "You are stronger than you know and more capable than you realize."
        mood_description = "Daily Motivation"

    return jsonify({
        'success': True,
        'quote': quote,
        'mood_description': mood_description
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=True)

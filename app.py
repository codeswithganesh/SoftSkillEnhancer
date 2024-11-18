pip install nltk scikit-learn numpy pandas
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Predefined scenarios for communication skills
scenarios = [
    {
        "scenario": "You are in a meeting and someone interrupts you while you are speaking. How would you handle this?",
        "expected_keywords": ["calm", "assertive", "understand", "continue", "respect"]
    },
    {
        "scenario": "Your team missed a deadline and you need to inform your client. How do you approach this situation?",
        "expected_keywords": ["apologize", "plan", "resolve", "responsibility", "next steps"]
    },
    {
        "scenario": "You have a conflict with a colleague over project responsibilities. How do you resolve it?",
        "expected_keywords": ["communicate", "listen", "compromise", "understand", "solution"]
    }
]

# Initialize NLP tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in stop_words]
    return tokens

def evaluate_response(user_response, expected_keywords):
    user_tokens = preprocess_text(user_response)
    score = sum(1 for word in expected_keywords if word in user_tokens)
    return score, len(expected_keywords)

def provide_feedback(score, max_score):
    feedback = "Feedback: "
    if score == max_score:
        feedback += "Excellent response! You covered all the key points."
    elif score >= max_score / 2:
        feedback += "Good job! You covered some key points, but there is room for improvement."
    else:
        feedback += "You may need to work on this area. Try to include more relevant points in your response."
    return feedback

def main():
    print("Welcome to the Soft Skills Enhancement Application!\n")
    
    scenario = random.choice(scenarios)
    print("Scenario:", scenario["scenario"])
    
    user_response = input("\nYour Response: ")
    
    score, max_score = evaluate_response(user_response, scenario["expected_keywords"])
    feedback = provide_feedback(score, max_score)
    
    print("\n" + feedback)

if _name_ == "_main_":
    main()
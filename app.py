import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open("career_guidance_model.pkl", "rb"))

# Set up the UI
st.title("Career Guidance System")
st.write("Input your skills and traits to find the best career role for you!")

# Feature descriptions for display
feature_descriptions = {
    "Database Fundamentals": "Knowledge of how databases work, including understanding of relational databases, SQL, and data management.",
    "Computer Architecture": "Understanding the internal structure and functioning of computers, including CPU design, memory management, and hardware components.",
    "Distributed Computing Systems": "Knowledge of systems that allow for processing data across multiple computers (e.g., cloud computing, parallel computing).",
    "Cyber Security": "Understanding the protection of computer systems and networks from cyber threats, including encryption, firewalls, and security practices.",
    "Networking": "Knowledge of computer networks, protocols (e.g., TCP/IP), and how computers and devices communicate over networks.",
    "Development": "Expertise in building software applications, including knowledge of programming languages, frameworks, and development lifecycle.",
    "Programming Skills": "Ability to write code and solve problems using programming languages such as Python, Java, C++, etc.",
    "Project Management": "Ability to manage projects, including planning, execution, monitoring, and closing projects.",
    "Computer Forensics Fundamental": "Knowledge of digital forensics, including collecting and analyzing evidence from computers for legal purposes.",
    "Technical Communication": "Ability to communicate technical information clearly through written reports, presentations, and documentation.",
    "AI ML": "Understanding of AI and ML algorithms, including supervised and unsupervised learning, neural networks, and other technologies.",
    "Software Engineering": "Knowledge of software development methodologies, including requirements gathering, coding, testing, and maintenance.",
    "Business Analysis": "Ability to assess business needs and align them with IT solutions, using data to guide business decisions.",
    "Communication skills": "Effective communication, both verbal and written, in a professional setting.",
    "Data Science": "Knowledge of statistical methods, data analysis, and the ability to work with large datasets to extract insights.",
    "Troubleshooting skills": "Ability to diagnose and resolve issues in computer systems, software, and hardware.",
    "Graphics Designing": "Expertise in creating visual content using design software and principles of design.",
    "Openness": "A personality trait related to being open to new experiences, ideas, and creative thinking.",
    "Conscientiousness": "A personality trait that reflects how organized, responsible, and detail-oriented an individual is.",
    "Extraversion": "A personality trait that reflects sociability, energy, and the tendency to seek stimulation in the company of others.",
    "Agreeableness": "A personality trait that describes how cooperative, empathetic, and compassionate a person is.",
    "Emotional Range": "Reflects a person’s emotional stability and the degree to which they experience emotions.",
    "Conversation": "Ability to engage in meaningful discussions and communicate effectively.",
    "Openness to Change": "Willingness to adapt to new situations and embrace new ideas.",
    "Hedonism": "A personality trait indicating a preference for pleasure and self-gratification.",
    "Self-enhancement": "A trait reflecting the desire for self-improvement, achievement, and recognition.",
    "Self-transcendence": "A personality trait indicating the ability to look beyond personal needs and focus on helping others.",
}

# Career role names corresponding to the predicted values
career_roles = {
    0: "Software Developer",
    1: "Data Scientist",
    2: "Cyber Security Specialist",
    3: "AI Researcher",
    4: "Network Engineer",
    5: "Project Manager",
    6: "Business Analyst",
    7: "System Architect",
    8: "IT Consultant",
    9: "Graphics Designer",
}

# Input fields for technical and psychological traits
features = {}
for feature_name, description in feature_descriptions.items():
    features[feature_name] = st.slider(feature_name, 0.0, 1.0, 0.5)
    st.write(description)  # Display the description below each slider

# Predict career role
if st.button("Predict Role"):
    feature_values = np.array([val for val in features.values()]).reshape(1, -1)
    prediction = model.predict(feature_values)
    
    # Get the career role name based on the predicted number
    role_name = career_roles.get(prediction[0], "Unknown Role")
    
    # Show the predicted career role name
    st.success(f"Recommended Career Role: {role_name}")

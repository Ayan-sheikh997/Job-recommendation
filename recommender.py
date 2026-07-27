import os
import re
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class JobRecommender:
    def __init__(self, csv_path="dataset/jobs.csv"):
        self.csv_path = csv_path
        self.df = None
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = None
        self.load_and_prepare_data()

    def clean_text(self, text):
        """
        Cleans the input text by converting it to lowercase and replacing 
        programming language symbols with safe alphanumeric tokens.
        """
        if not isinstance(text, str):
            return ""
        
        # Convert to lowercase
        text = text.lower()
        
        # Replace common tech symbols that standard tokenizers strip
        text = re.sub(r'\bc\+\+\b', 'cpp', text)
        text = re.sub(r'\bc#\b', 'csharp', text)
        text = re.sub(r'\b\.net\b', 'dotnet', text)
        text = re.sub(r'\breact\.js\b', 'reactjs', text)
        text = re.sub(r'\bnode\.js\b', 'nodejs', text)
        text = re.sub(r'\bvue\.js\b', 'vuejs', text)
        text = re.sub(r'\bangular\.js\b', 'angularjs', text)
        
        # Replace punctuation except spaces and commas
        text = re.sub(r'[^a-zA-Z0-9\s,]', ' ', text)
        
        # Replace multiple spaces with a single space
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()

    def extract_min_experience(self, exp_str):
        """
        Parses an experience string (e.g. '0-2 years', '5+ years') and returns the minimum years.
        """
        if not isinstance(exp_str, str):
            return 0
        match = re.search(r'\d+', exp_str)
        if match:
            return int(match.group(0))
        return 0

    def load_and_prepare_data(self):
        """
        Loads the CSV dataset, cleans the text columns, and fits the TF-IDF Vectorizer
        on the combined Required Skills and Job Description fields.
        """
        if not os.path.exists(self.csv_path):
            raise FileNotFoundError(f"Dataset file not found at {self.csv_path}")
        
        # Read dataset
        self.df = pd.read_csv(self.csv_path)
        
        # Ensure experience column has parsed minimum values
        self.df['MinExperience'] = self.df['Experience'].apply(self.extract_min_experience)
        
        # Create cleaned representations
        cleaned_skills = self.df['Required Skills'].fillna('').apply(self.clean_text)
        cleaned_desc = self.df['Job Description'].fillna('').apply(self.clean_text)
        
        # Combine Skills and Description
        self.df['CombinedText'] = cleaned_skills + " " + cleaned_desc
        
        # Fit TF-IDF Vectorizer and transform combined text
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['CombinedText'])

    def recommend(self, user_skills, preferred_location="", user_experience=None, top_n=5):
        """
        Generates job recommendations based on user skills, with optional location and experience filtering.
        """
        if self.df is None or len(self.df) == 0:
            return []

        # 1. Clean the user's skill input
        cleaned_user_skills = self.clean_text(user_skills)
        if not cleaned_user_skills:
            return []
        
        # 2. Vectorize user input
        user_vector = self.vectorizer.transform([cleaned_user_skills])
        
        # 3. Calculate cosine similarity
        similarities = cosine_similarity(user_vector, self.tfidf_matrix).flatten()
        
        # 4. Add match scores to a copy of the dataframe
        results_df = self.df.copy()
        results_df['MatchScore'] = similarities
        
        # 5. Apply filters *before* sorting if they are provided
        
        # Location filter (case-insensitive substring search)
        if preferred_location:
            loc_clean = preferred_location.strip().lower()
            # If user types "remote", we match remote. Otherwise, check if the location matches
            results_df = results_df[results_df['Location'].str.lower().str.contains(loc_clean, na=False)]
            
        # Experience filter (User Experience >= Job Minimum Experience)
        if user_experience is not None:
            try:
                user_exp_val = int(user_experience)
                results_df = results_df[results_df['MinExperience'] <= user_exp_val]
            except (ValueError, TypeError):
                # If invalid experience, ignore the filter
                pass

        # 6. Sort by similarity score descending
        results_df = results_df.sort_values(by='MatchScore', ascending=False)
        
        # 7. Format and return recommendations
        recommendations = []
        for idx, row in results_df.head(top_n).iterrows():
            score = row['MatchScore']
            match_percentage = round(score * 100, 1)
            
            # Determine match category
            if match_percentage >= 90:
                match_category = "Excellent Match"
                badge_class = "match-excellent"
            elif match_percentage >= 70:
                match_category = "Good Match"
                badge_class = "match-good"
            else:
                match_category = "Average Match"
                badge_class = "match-average"
                
            recommendations.append({
                "job_title": row['Job Title'],
                "company": row['Company'],
                "location": row['Location'],
                "required_skills": row['Required Skills'],
                "job_description": row['Job Description'],
                "experience": row['Experience'],
                "salary": row['Salary'] if 'Salary' in row and pd.notna(row['Salary']) else "N/A",
                "match_percentage": match_percentage,
                "match_category": match_category,
                "badge_class": badge_class
            })
            
        return recommendations

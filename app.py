from flask import Flask, render_template, request, redirect, url_for, flash
from models.recommender import JobRecommender

app = Flask(__name__)
# Secret key for flash messaging session
app.secret_key = 'job_recommender_secret_key_college_project'

# Initialize the recommender engine
try:
    recommender = JobRecommender()
except Exception as e:
    print(f"Error loading recommender model: {e}")
    recommender = None

@app.route('/')
def index():
    """
    Home page route.
    """
    return render_template('index.html')

@app.route('/recommend', methods=['GET'])
def recommend_form():
    """
    Recommendation input form route.
    """
    return render_template('recommend.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    """
    Results route. Processes user input, performs TF-IDF matching, 
    applies filters, and displays matching job recommendations.
    """
    if request.method == 'GET':
        # If accessed via GET directly, redirect to the recommendation form
        return redirect(url_for('recommend_form'))

    # Retrieve form data
    skills = request.form.get('skills', '').strip()
    location = request.form.get('location', '').strip()
    experience = request.form.get('experience', '').strip()

    # Input Validation
    if not skills:
        flash("Please enter at least one skill to get recommendations.", "error")
        return redirect(url_for('recommend_form'))

    if recommender is None:
        flash("The recommendation model failed to load. Please check the dataset.", "error")
        return redirect(url_for('recommend_form'))

    try:
        # Get top 10 recommendations so the user has choices to search/filter in the UI
        # (Though we default to showing top 5, having 10 allows interactive filter features to shine!)
        recommendations = recommender.recommend(
            user_skills=skills,
            preferred_location=location,
            user_experience=experience if experience else None,
            top_n=10
        )
        
        # Parse experience for displaying back in the form
        parsed_exp = None
        if experience:
            try:
                parsed_exp = int(experience)
            except ValueError:
                pass

        return render_template(
            'results.html',
            recommendations=recommendations,
            user_skills=skills,
            user_location=location,
            user_experience=experience,
            total_matches=len(recommendations)
        )
    except Exception as e:
        flash(f"An error occurred during processing: {str(e)}", "error")
        return redirect(url_for('recommend_form'))

if __name__ == '__main__':
    # Run the Flask app on localhost, port 5000
    app.run(debug=True, host='127.0.0.1', port=5000)

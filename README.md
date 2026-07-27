# AI-Based Job Recommendation System

A complete, beginner-friendly, and modern **AI-Based Job Recommendation System** built using Python, Flask, Pandas, Scikit-learn, HTML, CSS, and JavaScript. 

This project uses Natural Language Processing (NLP) to match user technical skills with job opportunities. It computes a semantic similarity score using Term Frequency-Inverse Document Frequency (TF-IDF) and Cosine Similarity, filtering matches by location and experience.

---

## 🌟 Features

* **Modern Glassmorphic Dashboard**: A clean and premium dark/light mode toggle with smooth animations, optimized for desktop and mobile devices.
* **Semantic Match Scoring**: Translates job requirements and user profiles into TF-IDF vector spaces, using Cosine Similarity to calculate exact matching percentages.
* **Skill Badging & Interactive Tagging**: Clean skills-tags user interface with autocomplete suggestions for common tech stacks.
* **AI Progress Simulation**: Beautiful radar loading animation that visualizes the pipeline phases (e.g. data cleaning, vectorizing, matching).
* **Advanced Filters**: Narrow recommendations by specifying location and years of experience.
* **Interactive Results Page**: 
  - Dynamic client-side search across results.
  - Interactive match-grade filter (Excellent, Good, Average).
  - Circular SVG progress indicators to highlight match strength.
  - Details Modal displaying full job descriptions and complete skill listings.

---

## 🛠️ Technologies Used

### Backend
* **Python**: Base programming language.
* **Flask**: Micro web framework for routing and template serving.
* **Pandas**: Data loading, wrangling, and structured querying.
* **Scikit-learn**: Feature extraction (`TfidfVectorizer`) and mathematical calculation (`cosine_similarity`).

### Frontend
* **HTML5**: Semantic document layout.
* **Vanilla CSS3**: Design system, custom theme variables, animations, and transitions.
* **Vanilla ES6+ JavaScript**: Tag inputs, accordion filters, loading overlays, real-time results searching, and modal popups.

---

## 📂 Folder Structure

```
job_recommendation_system/
│
├── app.py                  # Main Flask application and server routes
├── requirements.txt        # Python package dependencies
├── generate_dataset.py     # Script to generate mock database
├── dataset/
│   └── jobs.csv            # 110+ high-quality tech job records
├── models/
│   └── recommender.py      # Core recommender logic (TF-IDF + Cosine Similarity)
├── templates/
│   ├── index.html          # Landing home page template
│   ├── recommend.html      # Skills input form page template
│   └── results.html        # Matching job listings template
├── static/
│   ├── css/
│   │   └── style.css       # Core stylesheet (variable colors & glassmorphism)
│   ├── js/
│   │   └── script.js       # Dynamic UI triggers & real-time sorting script
│   └── images/             # Visual elements and assets
└── README.md               # Project documentation
```

---

## 🚀 Installation & Setup

Follow these steps to run the project locally on Windows:

### Prerequisites
Make sure you have Python 3.8+ installed. You can check your version in PowerShell:
```powershell
python --version
```

### Steps

1. **Clone or Open the Project Directory**
   Navigate to the project root folder in your terminal:
   ```powershell
   cd c:\Users\ayanh\OneDrive\Desktop\miniproject
   ```

2. **Install Dependencies**
   Install the required Python packages:
   ```powershell
   pip install -r requirements.txt
   ```

3. **Verify the Dataset**
   Check if `dataset/jobs.csv` exists. If not, generate a fresh dataset containing over 100 job records:
   ```powershell
   python generate_dataset.py
   ```

4. **Launch the Server**
   Run the Flask application:
   ```powershell
   python app.py
   ```

5. **Open in Browser**
   Open your browser and navigate to:
   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📸 Screenshots

### Light Mode Landing Page
*Landing screen with floating blur shapes, introducing project architecture and direct access to recommendations.*

### Skills Tag Input
*Interactive skill search. Typing common skills (e.g. Python) offers autocomplete suggestions, compiling skills into clean, deletable badges.*

### Dynamic Loading Sequence
*Modern full-screen radar scanner, simulating vectorization and similarity computation.*

### AI Recommendations Dashboard
*Interactive results with SVG circular match score rings, salary/location metadata, search filter bar, and view detail modals.*

---

## 🔮 Future Enhancements

* **Resumé PDF Parser**: Allow users to upload their PDF/Word CVs, automatically extracting skills using OCR/Regular Expressions.
* **SQL Database Integration**: Migrate the static CSV dataset to PostgreSQL or SQLite for dynamic, persistent CRUD operations.
* **Hybrid Filtering**: Merge content-based filtering with collaborative filtering, incorporating user clicks and ratings to refine results.

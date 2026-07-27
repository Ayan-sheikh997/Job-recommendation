import os
import csv
import random

# Define fields and lists of values for diverse, realistic job postings
companies = [
    "Google", "Microsoft", "Amazon", "Meta", "Apple", "Netflix", "Salesforce", "Adobe", "Spotify", "Stripe",
    "Zoom", "Slack", "Uber", "Lyft", "Airbnb", "Pinterest", "Twitter", "LinkedIn", "HubSpot", "Shopify",
    "Oracle", "Intel", "Cisco", "IBM", "Dell", "HP", "NVIDIA", "AMD", "Tesla", "SpaceX",
    "Coinbase", "Robinhood", "Plaid", "Square", "PayPal", "Intuit", "DocuSign", "Atlassian", "Datadog", "Snowflake",
    "Elastic", "MongoDB", "Confluent", "GitLab", "GitHub", "Canva", "Figma", "Notion", "Slack", "Zoom",
    "Capgemini", "Accenture", "TCS", "Infosys", "Wipro", "Cognizant", "Deloitte", "PwC", "EY", "KPMG"
]

locations = [
    "San Francisco, CA", "New York, NY", "Seattle, WA", "Austin, TX", "Boston, MA",
    "Bangalore, India", "Hyderabad, India", "Pune, India", "Mumbai, India", "Noida, India",
    "London, UK", "Manchester, UK", "Berlin, Germany", "Munich, Germany", "Paris, France",
    "Toronto, Canada", "Vancouver, Canada", "Sydney, Australia", "Singapore", "Tokyo, Japan",
    "Remote (US)", "Remote (Europe)", "Remote (India)", "Remote (Worldwide)"
]

roles_data = [
    {
        "title": "Frontend Engineer",
        "skills": ["HTML", "CSS", "JavaScript", "React", "Redux", "TypeScript", "Tailwind CSS", "Git"],
        "descriptions": [
            "Responsible for building responsive and beautiful user interfaces using React and TypeScript. Collaborate with UI/UX designers to translate Figma mockups into interactive, high-performance web pages.",
            "Develop modern, component-based frontend architectures. Optimize application performance, ensure cross-browser compatibility, and maintain clean, reusable code."
        ],
        "experiences": ["0-2 years", "2-5 years", "5+ years"],
        "salary_range": ("$70,000 - $95,000", "$100,000 - $140,000", "$150,000 - $190,000")
    },
    {
        "title": "Backend Developer",
        "skills": ["Python", "Flask", "Django", "SQL", "PostgreSQL", "REST APIs", "Git", "Docker"],
        "descriptions": [
            "Design and build scalable server-side systems and databases. Create secure, high-performance RESTful APIs to integrate with modern web frontends.",
            "Responsible for server-side application logic, database design, optimization, and API integration. Work with Docker and cloud databases to deploy robust microservices."
        ],
        "experiences": ["0-2 years", "2-5 years", "5+ years"],
        "salary_range": ("$75,000 - $95,000", "$105,000 - $145,000", "$155,000 - $200,000")
    },
    {
        "title": "Data Scientist",
        "skills": ["Python", "Pandas", "NumPy", "Scikit-learn", "SQL", "Tableau", "Machine Learning", "Jupyter Notebook"],
        "descriptions": [
            "Apply machine learning algorithms, statistical analysis, and data modeling to solve complex business problems. Extract insights from large structured and unstructured datasets.",
            "Analyze data using Pandas and NumPy, build predictive models with Scikit-learn, and create interactive business intelligence dashboards using Tableau and SQL."
        ],
        "experiences": ["1-3 years", "3-6 years", "6+ years"],
        "salary_range": ("$85,000 - $110,000", "$120,000 - $160,000", "$170,000 - $220,000")
    },
    {
        "title": "DevOps Engineer",
        "skills": ["AWS", "Docker", "Kubernetes", "CI/CD", "Jenkins", "Terraform", "Linux", "Git"],
        "descriptions": [
            "Design and implement automated build, test, and deployment pipelines (CI/CD). Manage cloud infrastructure on AWS using Infrastructure as Code (IaC) with Terraform.",
            "Maintain high availability of applications using Kubernetes and Docker. Streamline development processes, monitor system performance, and handle container orchestration."
        ],
        "experiences": ["1-3 years", "3-5 years", "5+ years"],
        "salary_range": ("$80,000 - $110,000", "$115,000 - $155,000", "$160,000 - $210,000")
    },
    {
        "title": "Full Stack Developer",
        "skills": ["JavaScript", "React", "Node.js", "Express", "MongoDB", "SQL", "Git", "REST APIs"],
        "descriptions": [
            "Build full-lifecycle web applications. Manage database queries using MongoDB/SQL, create backend services in Node.js, and deliver rich frontend user experiences in React.",
            "Responsible for both frontend and backend development. Design user interactions, develop APIs, manage databases, and ensure performance and scalability."
        ],
        "experiences": ["0-2 years", "2-5 years", "5+ years"],
        "salary_range": ("$75,000 - $100,000", "$110,000 - $150,000", "$160,000 - $210,000")
    },
    {
        "title": "Data Analyst",
        "skills": ["SQL", "Excel", "Python", "Power BI", "Tableau", "Data Visualization", "Statistics"],
        "descriptions": [
            "Analyze key performance indicators and business metrics. Write SQL queries to extract data, create automated reports in Excel, and design dashboards in Power BI.",
            "Translate data into actionable business insights. Perform descriptive statistics, build interactive dashboards in Tableau, and clean datasets using Python and Pandas."
        ],
        "experiences": ["0-2 years", "2-4 years", "4+ years"],
        "salary_range": ("$55,000 - $75,000", "$80,000 - $105,000", "$110,000 - $145,000")
    },
    {
        "title": "UI/UX Designer",
        "skills": ["Figma", "Adobe XD", "Wireframing", "Prototyping", "User Research", "Visual Design", "UI Design"],
        "descriptions": [
            "Create user-centered designs by understanding business requirements and user feedback. Conduct user research and deliver high-fidelity wireframes and interactive prototypes in Figma.",
            "Design visual aesthetics, layout structures, and intuitive workflows for web and mobile platforms. Test interface usability and iterate based on feedback."
        ],
        "experiences": ["0-2 years", "2-5 years", "5+ years"],
        "salary_range": ("$60,000 - $80,000", "$90,000 - $125,000", "$130,000 - $170,000")
    },
    {
        "title": "Mobile App Developer",
        "skills": ["Kotlin", "Swift", "Flutter", "React Native", "Java", "Mobile App Development", "Git", "REST APIs"],
        "descriptions": [
            "Develop and launch native or cross-platform mobile apps for iOS and Android. Write clean code in Swift or Kotlin, and consume REST APIs.",
            "Design, build, and publish mobile applications. Integrate third-party libraries, handle offline storage, and optimize rendering speed across various mobile screen sizes."
        ],
        "experiences": ["0-2 years", "2-5 years", "5+ years"],
        "salary_range": ("$70,000 - $95,000", "$100,000 - $145,000", "$150,000 - $195,000")
    },
    {
        "title": "Cyber Security Analyst",
        "skills": ["Network Security", "Ethical Hacking", "Linux", "Firewall", "Wireshark", "SIEM", "Information Security"],
        "descriptions": [
            "Monitor network traffic, identify potential security breaches, and respond to cyber incidents. Conduct vulnerability assessments and secure systems with firewalls.",
            "Implement security strategies, audit systems for compliance, analyze logs using SIEM tools, and protect company infrastructure from unauthorized access."
        ],
        "experiences": ["1-3 years", "3-5 years", "5+ years"],
        "salary_range": ("$75,000 - $100,000", "$110,000 - $150,000", "$155,000 - $200,000")
    },
    {
        "title": "Cloud Architect",
        "skills": ["AWS", "Azure", "Cloud Computing", "Terraform", "Enterprise Architecture", "Docker", "Linux", "Kubernetes"],
        "descriptions": [
            "Design and oversee cloud computing strategies and deployment plans. Architect secure, scalable, and resilient multi-tenant cloud solutions using AWS and Azure.",
            "Lead the transition of legacy systems to modern cloud infrastructures. Optimize resource utilization, establish security baselines, and standardize deployment frameworks."
        ],
        "experiences": ["2-4 years", "4-7 years", "7+ years"],
        "salary_range": ("$95,000 - $130,000", "$140,000 - $185,000", "$190,000 - $250,000")
    },
    {
        "title": "Java Software Engineer",
        "skills": ["Java", "Spring Boot", "Microservices", "SQL", "Hibernate", "JUnit", "Docker", "Git"],
        "descriptions": [
            "Develop robust enterprise-grade backend services using Java and Spring Boot. Design microservices and implement unit tests with JUnit.",
            "Build scalable Java applications. Coordinate database operations with Hibernate, secure microservices, and containerize systems using Docker."
        ],
        "experiences": ["0-2 years", "2-5 years", "5+ years"],
        "salary_range": ("$70,000 - $95,000", "$100,000 - $140,000", "$150,000 - $195,000")
    },
    {
        "title": "QA Automation Engineer",
        "skills": ["Python", "Selenium", "Java", "Test Automation", "API Testing", "Postman", "CI/CD", "Git"],
        "descriptions": [
            "Build automated testing suites for web applications using Selenium and Python. Integrate tests into the CI/CD pipeline to ensure quality releases.",
            "Write automation scripts to test frontend UI and REST APIs. Write test plans, report bugs, and collaborate with developers on quick resolutions."
        ],
        "experiences": ["1-3 years", "3-5 years", "5+ years"],
        "salary_range": ("$65,000 - $85,000", "$90,000 - $120,000", "$125,000 - $160,000")
    },
    {
        "title": "Product Manager",
        "skills": ["Product Strategy", "Agile", "Scrum", "Jira", "Market Research", "Roadmapping", "Communication"],
        "descriptions": [
            "Define the product vision, roadmap, and requirements. Lead cross-functional teams of engineers and designers to launch new tech features under Agile methodologies.",
            "Drive product development from conception to launch. Conduct user research, analyze metrics, and prioritize backlog items using Jira and Agile frameworks."
        ],
        "experiences": ["1-3 years", "3-5 years", "5+ years"],
        "salary_range": ("$80,000 - $110,000", "$115,000 - $155,000", "$160,000 - $210,000")
    },
    {
        "title": "C++ Software Developer",
        "skills": ["C++", "Algorithms", "Data Structures", "Linux", "Multithreading", "Git", "Object-Oriented Programming"],
        "descriptions": [
            "Write high-performance low-level applications in C++. Optimize algorithms, design efficient data structures, and implement multithreading solutions.",
            "Responsible for memory management, real-time performance optimization, and low-level system design. Excel in Object-Oriented Design in C++ on Linux platforms."
        ],
        "experiences": ["0-2 years", "2-5 years", "5+ years"],
        "salary_range": ("$75,000 - $100,000", "$110,000 - $150,000", "$155,000 - $205,000")
    },
    {
        "title": "Machine Learning Engineer",
        "skills": ["Python", "PyTorch", "TensorFlow", "Machine Learning", "Deep Learning", "SQL", "Docker", "Git"],
        "descriptions": [
            "Design, build, and deploy machine learning models in PyTorch or TensorFlow. Scale training pipelines and run predictions on massive datasets.",
            "Research and implement deep learning algorithms, natural language processing, or computer vision models. Build inference endpoints and maintain ML models in production."
        ],
        "experiences": ["1-3 years", "3-6 years", "6+ years"],
        "salary_range": ("$90,000 - $120,000", "$130,000 - $175,000", "$180,000 - $230,000")
    }
]

# Generate 110 jobs to be safe (minimum is 100)
num_jobs_to_generate = 115
jobs = []

for i in range(num_jobs_to_generate):
    role = random.choice(roles_data)
    company = random.choice(companies)
    location = random.choice(locations)
    
    # Select experience level
    exp_idx = random.randint(0, len(role["experiences"]) - 1)
    experience = role["experiences"][exp_idx]
    salary = role["salary_range"][exp_idx]
    
    # Description
    desc_template = random.choice(role["descriptions"])
    
    # Modify description to include some custom text or company name
    job_desc = f"Join our growing team at {company} in {location}! {desc_template} We offer great benefits, flexible hours, and professional development."
    
    # Required Skills (take standard, shuffle, and add 1-2 random secondary skills)
    base_skills = list(role["skills"])
    # optionally remove a skill to create variance
    if len(base_skills) > 4 and random.random() > 0.5:
        base_skills.remove(random.choice(base_skills))
        
    secondary_skills_pool = ["Communication", "Problem Solving", "Agile", "Scrum", "Git", "SQL", "Teamwork", "Analytics", "Project Management", "Docker"]
    extra_skills = random.sample(secondary_skills_pool, random.randint(1, 3))
    
    # Merge and deduplicate
    all_skills = list(dict.fromkeys(base_skills + extra_skills))
    required_skills_str = ", ".join(all_skills)
    
    jobs.append({
        "Job Title": role["title"],
        "Company": company,
        "Location": location,
        "Required Skills": required_skills_str,
        "Job Description": job_desc,
        "Experience": experience,
        "Salary": salary
    })

# Write to CSV
os.makedirs("dataset", exist_ok=True)
csv_file_path = os.path.join("dataset", "jobs.csv")

with open(csv_file_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Job Title", "Company", "Location", "Required Skills", "Job Description", "Experience", "Salary"])
    writer.writeheader()
    writer.writerows(jobs)

print(f"Successfully generated {len(jobs)} job records and saved to '{csv_file_path}'!")

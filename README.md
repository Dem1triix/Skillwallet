# Analysing Mental Health in Student Ecosystem

Data Analytics with Tableau capstone (Skillwallet), built solo by **Atharv Bhosale**.

An interactive Tableau analysis of 1,000 student records, published as a dashboard and a story and hosted on a live website.

## Live links

| What | Link |
|---|---|
| Live website (ePortfolio) | https://student-mental-health-g6de.onrender.com/ |
| Tableau Public dashboard | https://public.tableau.com/views/StudentMentalHealthAnalysis_17912039586820/StudentMentalHealthAnalysis |
| Tableau Public story | [[Click here](https://public.tableau.com/views/Story_17912605038440/Story1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)] |
| Demo video | [[Click here](https://drive.google.com/drive/folders/1ECenNEV8yRh5H4K1Wwhq1lQi96h68Gj6?usp=drive_link)] |

## Problem statement

Counsellors and mentors want to spot at-risk students early. This project asks whether wellbeing measures, gender and study habits differ by mental health risk level, and whether study hours affect academic performance.

## Dataset

`Personalized_Psychological_Intervention_Dataset` has 1,000 student records and 16 fields: Student ID, Age, Gender, Stress, Anxiety and Depression levels, Heart Rate Variability, Sleep Duration, Attendance Rate, Study Hours Per Day, LMS Activity Score, Social Interaction Score, Academic Performance Index, Emotional Journal, Mental Health Risk and Personalized Intervention Strategy.

**Data quality checks:** no missing values, no duplicate rows, all 1,000 student IDs unique. By the 1.5 x IQR rule there are 14 outliers (12 in sleep duration, 2 in heart rate variability), which were kept because the values are realistic.

**Prepared fields:** an average **Mental Score** (mean of stress, anxiety and depression, overall 5.45) and five **grade bands** from the Academic Performance Index (A+ 90 and above, A 80-89, B 70-79, C 60-69, F below 60).

## Key findings

- **KPIs:** Mental Score 5.45, average sleep 6.49 hours, depression 5.50, attendance 79.96%.
- **Gender:** average stress ranges 5.30 to 5.61, depression 5.35 to 5.67, and heart rate variability 69 to 70 across Female, Male and Other. High-risk share is 23% to 25% in every group.
- **Grades:** spread almost evenly across the five bands (18% to 21% each).
- **Study hours vs academic score:** R-squared is about 0 with p = 0.84, so there is no relationship.
- **Sleep vs stress:** R-squared is about 0 with p = 0.87.
- **Conclusion:** no single factor predicts mental health risk. The data looks simulated, so these results should be confirmed on real student data.

## Tableau work

- 20 worksheets, 2 dashboards and 1 story.
- Final dashboard "Student Mental Health Analysis": KPI strip, stress, depression and heart rate variability by gender, risk mix by gender, grade distribution, and the study hours analyses, with a Gender filter.
- Risk colours throughout: red = High, amber = Medium, teal = Low.

## Website

The `eportfolio` folder holds a small Flask website with four pages (Home, Dashboard, Story, Portfolio). The Tableau dashboard and story are embedded from Tableau Public.

```
eportfolio/
├── app.py             Flask app with the four routes
├── build.py           exports the site to static files in build/
├── requirements.txt
├── static/            CSS and images
└── templates/         HTML templates
```

### Run locally

```
cd eportfolio
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000.

### Build the static version

```
python build.py
```

This writes the pages to `eportfolio/build/`.

### Deployment

The site is deployed as a **Render Static Site** with these settings:

- Root Directory: `eportfolio`
- Build Command: `pip install -r requirements.txt && python build.py`
- Publish Directory: `build`

Pushing to `main` redeploys the site automatically. Because it is a static site, it does not sleep.

## Tools

Tableau Desktop, Tableau Public, Python, Flask, HTML, CSS, Visual Studio Code, GitHub, Render.

## Author

Atharv Bhosale,
Skillwallet Data Analytics with Tableau capstone.

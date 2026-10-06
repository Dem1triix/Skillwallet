# Analysing Mental Health in Student Ecosystem

Skillwallet **Data Analytics with Tableau** capstone project by **Atharv Bhosale**.

An interactive Tableau analysis of 1,000 student records (16 fields) from the Personalized Psychological Intervention dataset. It looks at how sleep, study hours, attendance, stress and depression relate to mental health scores and risk levels.

## Key findings

- No single factor predicts risk: stress, depression and high-risk share (23% to 25%) are close across every gender.
- Study hours and sleep show almost no relationship with academic score or stress (study hours vs academic score: R² ≈ 0, p = 0.84).
- Risk is spread evenly, so broad, inclusive support fits better than targeting one group.
- The data looks synthetic: grade bands are almost equal and the journal text has only 10 distinct sentences.

## Live links

- Dashboard: https://public.tableau.com/views/StudentMentalHealthAnalysis_17912039586820/StudentMentalHealthAnalysis
- Story: https://public.tableau.com/views/Story_17912605038440/Story1
- Demo video: <!-- TODO: paste demo link -->

## Repository contents

| Path | What it holds |
|---|---|
| `eportfolio/` | Flask website that embeds the Tableau dashboard and story |
| PDF documents | Project documentation (planning, data quality, business questions, dashboard design, final report) |

## Run the ePortfolio website

```
cd eportfolio
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in a browser. Pages: Home, Dashboard, Story, Portfolio.

## Tools used

Tableau Public, Flask (Python), HTML, CSS, Visual Studio Code, Git and GitHub.

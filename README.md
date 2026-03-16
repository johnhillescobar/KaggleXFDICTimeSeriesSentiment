# KaggleXFDICTimeSeriesSentiment

A learning project that combines **FDIC/FRED banking time series** with **financial news sentiment** for exploratory analysis and modeling. It pulls Reuters business news via RapidAPI, cleans text for analysis, and supports notebooks for time-series modeling (XGBoost, LSTM) and portfolio work.

**Non-commercial.** This project is for learning and improving data science skills only.

---

## What’s in this repo

- **`reuters_pull.py`** – Fetches Reuters business/financial news by category and date via [RapidAPI](https://rapidapi.com/), then provides helpers to extract and clean article text (NLTK stopwords, regex) for sentiment or other NLP use.
- **Notebooks**
  - **FDIC Insured Banks EDA.ipynb** – Exploratory analysis of FDIC-insured bank data.
  - **fdic-and-fred-time-series-analysis-xgboost.ipynb** – FDIC/FRED time series with XGBoost modeling.
  - **LSTM-PortfolioFinal.ipynb** – LSTM-based time series / portfolio experiments.
  - **portfolio_optimized-time-series-analysis-final.ipynb** – Portfolio and time-series analysis.

---

## Setup

1. **Python**  
   Use a recent Python 3 environment (e.g. 3.8+).

2. **Dependencies**  
   Install at least:
   - `pandas`, `numpy`
   - `requests`
   - `nltk` (and run `nltk.download('stopwords')`, `nltk.download('punkt')` if needed)
   - `beautifulsoup4` (for HTML in article content)

   Example:
   ```bash
   pip install pandas numpy requests nltk beautifulsoup4
   ```

3. **Credentials**  
   `reuters_pull.py` expects a local module `credenciales` with:
   - `reuters_credentials` – dict with `"X-RapidAPI-Key"` and `"X-RapidAPI-Host"` (eatching the [Reuters Business and Financial News API](https://rapidapi.com/) on RapidAPI).
   - Optionally `cnbc_credentials` if you add CNBC-related scripts later.

   Create `credenciales.py` in the project root (and add it to `.gitignore`) with your keys; do not commit real keys.

---

## Usage

- **Reuters news pull**  
  Run `reuters_pull.py` to fetch articles for the configured date range and category IDs. It uses a 10-second delay between requests to respect API limits. Ensure `df_reuters` is initialized before the loop if you run the script as-is (e.g. `df_reuters = pd.DataFrame()` before the `for term in ...` loop).

- **Notebooks**  
  Open the Jupyter notebooks to run FDIC/FRED EDA, XGBoost time-series modeling, LSTM experiments, or portfolio analysis. Data paths and dependencies may need to be adjusted for your environment.

---

## Data and APIs

- **Reuters** – Sourced via RapidAPI (Reuters Business and Financial News). Categories used in the script include IDs such as 7, 10, 16, 44, 90, 92, 239; see the API docs for category meanings.
- **FDIC / FRED** – Used in the notebooks; obtain datasets from official FDIC and FRED sources as required by each notebook.

---

## License and purpose

This project has no commercial focus. It is intended only to practice and improve data science skills (APIs, time series, NLP/sentiment, and modeling).

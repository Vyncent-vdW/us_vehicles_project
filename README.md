# 🚗 Vehicles Listings App

Interactive exploration of the US used vehicles listings dataset. The project contains:

* A Jupyter notebook (`Vehicles US Project.ipynb`) for exploratory data analysis (EDA), cleaning, and feature engineering.
* A Streamlit application (`app.py`) that lets users filter listings and visualize price relationships across multiple dimensions.
* The raw dataset `vehicles_us.csv` plus lightweight preprocessing (imputation, derived columns, renaming) to create consistent, analysis‑ready fields.

## 🔍 Goals

Provide an accessible interface to:
* Inspect manufacturer inventory across model years.
* Understand price distribution drivers (condition, fuel, transmission, body type, age).
* Examine correlations via scatter, parallel coordinates, and categorical spread plots.
* Prototype derived features (Age, Age Category, Manufacturer extraction) for later modeling or pricing heuristics.

## 🗂️ Data Preparation (in `app.py`)

Key cleaning / feature steps:
* Split raw `model` into `Manufacturer` (first token) and cleaned `Model` remainder.
* Median imputation: `Model Year` (global median), `Cylinders`, `Odometer` (group median by `Model`).
* Fill missing `Paint Color` with `Unknown`.
* Rename columns to human‑readable forms (see table below).
* Standardize capitalization; force specific brands (e.g. BMW, GMC) to uppercase.
* Derive `Age = 2025 - Model Year` and bucket into `Age Category` (<5, 5–10, 10–20, >20).

### Column Mapping

| Raw | Cleaned / Derived |
|-----|-------------------|
| price | Price (USD) |
| model_year | Model Year |
| manufacturer | Manufacturer (derived from `model`) |
| model | Model (trimmed, minus manufacturer token) |
| condition | Condition |
| cylinders | Cylinders |
| fuel | Fuel |
| odometer | Odometer |
| transmission | Transmission |
| type | Type |
| paint_color | Paint Color (Unknown if missing) |
| is_4wd | 4WD |
| date_posted | Date Posted |
| days_listed | Days Listed |
| (derived) | Age, Age Category |

## 📊 App Visualizations

| Plot | Purpose |
|------|---------|
| Histogram of Price split by selectable attribute | Understand price distribution differences (e.g., by Condition, Fuel, Type) |
| Scatter (Price vs Odometer / Age / Days Listed) colored by Age Category | Inspect dependency trends and age interaction |
| Parallel Coordinates (numeric & encoded dims) | Multivariate comparison across records (color = Price) |
| Strip Plot (Price vs Manufacturer) | Compare manufacturer price dispersion |

## 🧪 Notebook

The notebook expands on: detailed EDA, missing value inspection, distribution checks, and potential future modeling targets (e.g., price prediction or time‑on‑market modeling).

## 📦 Installation

```powershell
git clone https://github.com/Vyncent-vdW/us_vehicles_project.git
cd us_vehicles_project/us_vehicles_project
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## ▶️ Running the Streamlit App

```powershell
streamlit run app.py
```
Open the provided local URL in your browser. Use the sidebar widgets / select boxes to:
* Choose a manufacturer.
* Narrow the model year range.
* Pick a categorical split for the price histogram.
* Change the y‑axis of the price dependency scatter.

## 🧮 Key Derived Logic (Summary)

* Manufacturer extraction: `df['manufacturer'] = df['model'].str.split().str[0]`
* Age: `2025 - Model Year` (static year constant for reproducibility; update as needed)
* Age buckets: custom function mapping integer age to discrete labels.
* Imputation strategy favors simplicity (median / constant) to preserve volume for interactive plots.

## 🔄 Reproducibility

Deterministic transformations with no randomness (aside from median computations). Re‑running `app.py` regenerates the same processed view given identical source CSV.

## 🚧 Limitations / Next Steps

| Area | Potential Improvement |
|------|-----------------------|
| Imputation | Use per manufacturer + model year medians; flag imputed rows |
| Age Logic | Derive from `date_posted` year dynamically |
| Outliers | Add optional IQR or percentile trimming toggle |
| Scaling | Consider caching processed DataFrame for larger datasets |
| Modeling | Add basic price prediction model & feature importance panel |
| UX | Add sidebar controls for price range & age category filtering |

## 🤝 Contributing

1. Fork the repo
2. Create a branch (`feature/your-change`)
3. Commit & push
4. Open a Pull Request describing the change and any visual impact

## 📄 License

Add a LICENSE file if you plan to distribute (MIT recommended).

## ✨ Summary

The Vehicles US Project delivers an interactive, lightweight exploratory interface over US used vehicle listings, surfacing how manufacturer, condition, fuel type, drivetrain, and age shape market pricing and listing behavior. It forms a foundation for future predictive analytics and operational dashboards.


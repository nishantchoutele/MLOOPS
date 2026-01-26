import time
import re
import requests
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
from urllib.parse import quote

# ==============================
# CONFIG
# ==============================
BASE_URL = "https://www.scrapehero.com/location-reports"
REQUEST_DELAY = 4  # strictly one request at a time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; ScrapeHero-Enterprise-Extractor/1.1)"
}

COUNTRY_MAP = {
    "USA": "USA",
    "GBR": "UK",
    "IND": "India",
    "CAN": "Canada",
    "AUS": "Australia"
}

KEYWORDS = ["stores", "locations", "hotels", "restaurants"]

# ==============================
# DATA CLEANING
# ==============================
def clean_columns(df):
    df.columns = df.columns.str.strip()
    return df


def clean_values(df):
    df["Name"] = df["Name"].astype(str).str.strip()
    df["Country"] = df["Country"].astype(str).str.strip().str.upper()
    return df


# ==============================
# URL BUILDER
# ==============================
def build_url(chain_name, iso3):
    country = COUNTRY_MAP.get(iso3)
    if not country:
        return None
    return f"{BASE_URL}/{quote(chain_name)}-{country}/"


# ==============================
# ENTERPRISE EXTRACTION LOGIC
# ==============================
def extract_data(html):
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(" ", strip=True).lower()

    # ---------- PRIMARY PATTERN ----------
    for kw in KEYWORDS:
        pattern = rf"(\d{{1,6}})\s+{kw}"
        for match in re.finditer(pattern, text):
            num = int(match.group(1))
            snippet = match.group(0)

            if 1900 <= num <= 2100:
                continue
            if num < 2 or num > 100000:
                continue

            last_updated = None
            if "updated" in text:
                idx = text.find("updated")
                last_updated = text[idx:idx + 60]

            return (
                num,
                last_updated,
                "Valid",
                "Count validated via semantic keyword match",
                snippet
            )

    # ---------- INVERSE PATTERN (FIX) ----------
    for kw in KEYWORDS:
        pattern = rf"{kw}\s*[:\-]?\s*(\d{{1,6}})"
        for match in re.finditer(pattern, text):
            num = int(match.group(1))
            snippet = match.group(0)

            if 1900 <= num <= 2100:
                continue
            if num < 2 or num > 100000:
                continue

            last_updated = None
            if "updated" in text:
                idx = text.find("updated")
                last_updated = text[idx:idx + 60]

            return (
                num,
                last_updated,
                "Valid",
                "Count validated via inverse semantic keyword match",
                snippet
            )

    return None, None, "Invalid", "No semantic count pattern found", None


# ==============================
# MAIN PROCESSING ENGINE
# ==============================
def process_dataframe(df, progress_bar, log_box):
    results = []

    for i, row in df.iterrows():
        chain = row["Name"]
        iso3 = row["Country"]

        log_box.write(f"🔍 Processing **{chain} ({iso3})**")

        url = build_url(chain, iso3)

        if not url:
            results.append({
                "Name": chain,
                "Country": iso3,
                "Reality_Count": None,
                "Last_Updated": None,
                "Validation_Status": "Invalid",
                "Validation_Notes": "Unsupported country code",
                "Count_Source_Text": None,
                "Status": "Failed",
                "Source": "scrapehero.com",
                "Source_URL": None
            })
            progress_bar.progress((i + 1) / len(df))
            continue

        try:
            r = requests.get(url, headers=HEADERS, timeout=20)

            if r.status_code != 200 or len(r.text) < 1500:
                raise Exception("Page not available on Scrape Hero")

            (
                count,
                updated,
                validation_status,
                validation_notes,
                snippet
            ) = extract_data(r.text)

            if validation_status != "Valid":
                raise Exception(validation_notes)

            results.append({
                "Name": chain,
                "Country": iso3,
                "Reality_Count": count,
                "Last_Updated": updated,
                "Validation_Status": validation_status,
                "Validation_Notes": validation_notes,
                "Count_Source_Text": snippet,
                "Status": "Success",
                "Source": "scrapehero.com",
                "Source_URL": url
            })

        except Exception as e:
            results.append({
                "Name": chain,
                "Country": iso3,
                "Reality_Count": None,
                "Last_Updated": None,
                "Validation_Status": "Invalid",
                "Validation_Notes": str(e),
                "Count_Source_Text": None,
                "Status": "Failed",
                "Source": "scrapehero.com",
                "Source_URL": url
            })

        progress_bar.progress((i + 1) / len(df))
        time.sleep(REQUEST_DELAY)

    return pd.DataFrame(results)


# ==============================
# STREAMLIT UI
# ==============================
st.set_page_config(
    page_title="Scrape Hero Enterprise POI Extractor",
    layout="wide"
)

st.title("📍 Scrape Hero Enterprise POI Extractor")
st.caption(
    "Enterprise-grade extraction with semantic validation, "
    "explicit failure reasoning, and audit-ready outputs"
)

uploaded_file = st.file_uploader(
    "Upload input file (CSV or Excel)",
    type=["csv", "xlsx"]
)

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df_input = pd.read_csv(uploaded_file)
    else:
        df_input = pd.read_excel(uploaded_file)

    df_input = clean_columns(df_input)

    if not {"Name", "Country"}.issubset(df_input.columns):
        st.error("❌ Input file must contain columns: Name, Country")
        st.stop()

    df_input = clean_values(df_input)

    st.success("✅ File loaded and validated")
    st.dataframe(df_input)

    if st.button("🚀 Start Scraping"):
        progress = st.progress(0)
        log_box = st.empty()

        with st.spinner("Scraping Scrape Hero (one request at a time)..."):
            result_df = process_dataframe(df_input, progress, log_box)

        st.success("✅ Scraping completed")
        st.dataframe(result_df)

        st.download_button(
            label="⬇️ Download Results (CSV)",
            data=result_df.to_csv(index=False).encode("utf-8"),
            file_name="scrapehero_enterprise_results.csv",
            mime="text/csv"
        )

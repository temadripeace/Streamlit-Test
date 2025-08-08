import os
import pandas as pd
import geopandas as gpd
from shapely import wkt
import streamlit as st

def load_file(path, wkt_column=None, crs=None):
    ext = os.path.splitext(path)[1].lower()

    if ext == ".csv":
        df = pd.read_csv(path)
        if wkt_column and wkt_column in df.columns:
            gdf = gpd.GeoDataFrame(df.copy())
            gdf['geometry'] = df[wkt_column].apply(wkt.loads)
            gdf.set_crs(crs or "EPSG:4326", inplace=True)
            return gdf
        return df

    elif ext in [".xls", ".xlsx"]:
        df = pd.read_excel(path, engine="openpyxl")
        if wkt_column and wkt_column in df.columns:
            gdf = gpd.GeoDataFrame(df.copy())
            gdf['geometry'] = df[wkt_column].apply(wkt.loads)
            gdf.set_crs(crs or "EPSG:4326", inplace=True)
            return gdf
        return df

    elif ext in [".geojson", ".json"]:
        gdf = gpd.read_file(path)
        if crs:
            gdf = gdf.to_crs(crs)
        return gdf

    elif ext == ".kml":
        try:
            gdf = gpd.read_file(path, driver='KML')
        except Exception:
            gdf = gpd.read_file(path)
        if crs:
            gdf = gdf.to_crs(crs)
        return gdf

    else:
        raise ValueError("Unsupported file type: " + ext)

# Streamlit UI
st.title("Upload and View Geospatial Data")

uploaded = st.file_uploader("Upload CSV, Excel, KML, or GeoJSON", 
                             type=["csv", "xls", "xlsx", "kml", "geojson", "json"])

if uploaded is not None:
    # Save uploaded file to temp
    import tempfile
    suffix = os.path.splitext(uploaded.name)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded.getvalue())
        tmp_path = tmp.name

    # Ask user for WKT column if needed
    wkt_col = st.text_input("If CSV/Excel has WKT geometry, enter column name (leave blank if none)")

    try:
        data = load_file(tmp_path, wkt_column=(wkt_col or None))
        st.success(f"Loaded file: {uploaded.name}")

        st.write("Preview of data:")
        st.write(data.head())

        if isinstance(data, gpd.GeoDataFrame):
            st.map(data)

    except Exception as e:
        st.error(f"Error loading file: {e}")







import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

latitude = -3.539241
longitude = 118.941828


def display_map():
    map = folium.Map(
        location=[latitude, longitude],
        zoom_start=12,
        scrollWheelZoom=False,
    )

    geo_data = "map.geojson"

    data = pd.read_csv("kec_banggaetimur.csv")

    st.write(data.head())

    choropleth = folium.Choropleth(
        geo_data=geo_data,
        data=data,
        columns=["DESA", "JUMLAH PENDUDUK"],
        key_on="feature.properties.DESA",
        fill_color="Reds",
        fill_opacity=0.95,
        # threshold_scale=[0, 3000, 6000, 9000, 12000],
        threshold_scale=[0, 1000, 1500, 1600, 1900, 2000, 5000, 6000, 6300, 6585],
        legend_name="JUMLAH PENDUDUK",
    )

    choropleth.geojson.add_to(map)
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(["DESA", "JUMLAH PENDUDUK"], labels=False),
    )

    map.save("index.html")

    st_folium(map, width=600, height=400)


st.markdown(
    """
    <style>
    h1 {
        text-align: left;
        font-size: 32px;
        color: #1E90FF;
        margin: 0;
        padding: 0;
    }
    h2 {
        text-align: left;
        font-size: 25px;
        margin: 0;
        padding: 0;
    }
    h4 {
        text-align: left;
        font-size: 15px;
        margin: 10;
        padding: 30;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "<h1>Peta Geografis Jumlah Penduduk</h1>",
    unsafe_allow_html=True,
)

st.markdown(
    "<h2>Kec. Banggae Timur, Kab. Majene, Prov. Sulawesi Barat</h2>",
    unsafe_allow_html=True,
)

st.markdown(
    "<h4><u>Source: BPS Majene | Hendra Usman - D0221079</u></h4>",
    unsafe_allow_html=True,
)

display_map()

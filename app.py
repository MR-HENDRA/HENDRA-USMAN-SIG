# import streamlit as st
# import pandas as pd
# import folium
# from streamlit_folium import st_folium

# latitude = -3.539241
# longitude = 118.941828

# def display_map(selected_area):
#     map = folium.Map(
#         location=[latitude, longitude],
#         zoom_start=12,
#         scrollWheelZoom=False,
#     )

#     geo_data = "map.geojson"

#     if selected_area == "None":
#         # Display the choropleth map based on the population
#         choropleth = folium.Choropleth(
#             geo_data=geo_data,
#             data=data,
#             columns=["DESA", "JUMLAH PENDUDUK"],
#             key_on="feature.properties.DESA",
#             fill_color="Reds",
#             fill_opacity=0.95,
#             threshold_scale=[0, 1000, 1500, 1600, 1900, 2000, 5000, 6000, 6300, 6585],
#             legend_name="JUMLAH PENDUDUK",
#         )
#         choropleth.geojson.add_to(map)
#         choropleth.geojson.add_child(
#             folium.features.GeoJsonTooltip(["DESA", "JUMLAH PENDUDUK"], labels=False),
#         )
#     else:
#         # Highlight only the selected area
#         def style_function(feature):
#             if feature['properties']['DESA'] == selected_area:
#                 return {
#                     'fillColor': 'red',
#                     'color': 'black',
#                     'weight': 2,
#                     'fillOpacity': 0.6,
#                 }
#             else:
#                 return {
#                     'fillColor': 'white',
#                     'color': 'black',
#                     'weight': 1,
#                     'fillOpacity': 0.1,
#                 }

#         folium.GeoJson(
#             geo_data,
#             name='geojson',
#             style_function=style_function,
#             tooltip=folium.GeoJsonTooltip(
#                 fields=["DESA", "JUMLAH PENDUDUK"],
#                 aliases=["Desa:", "Jumlah Penduduk:"],
#                 localize=True
#             )
#         ).add_to(map)

#     st_folium(map, width=600, height=400)

# # Read the data to get the list of areas
# data = pd.read_csv("kec_banggaetimur.csv")
# areas = ["None"] + data["DESA"].unique().tolist()

# st.markdown(
#     """
#     <style>
#     h1 {
#         text-align: left;
#         font-size: 32px;
#         color: #1E90FF;
#         margin: 0;
#         padding: 0;
#     }
#     h2 {
#         text-align: left;
#         font-size: 25px;
#         margin: 0;
#         padding: 0;
#     }
#     h4 {
#         text-align: left;
#         font-size: 15px;
#         margin: 10;
#         padding: 30;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# st.markdown(
#     "<h1>Peta Geografis Jumlah Penduduk</h1>",
#     unsafe_allow_html=True,
# )

# st.markdown(
#     "<h2>Kec. Banggae Timur, Kab. Majene, Prov. Sulawesi Barat</h2>",
#     unsafe_allow_html=True,
# )

# st.markdown(
#     "<h4><u>Source: BPS Majene | Hendra Usman - D0221079</u></h4>",
#     unsafe_allow_html=True,
# )

# # Display the table
# st.write(data.head())

# # Add a dropdown menu for selecting the area
# selected_area = st.selectbox("Pilih daerah yang ingin ditampilkan:", areas)

# # Display the map
# display_map(selected_area)

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

latitude = -3.539241
longitude = 118.941828


def display_map(selected_area):
    map = folium.Map(
        location=[latitude, longitude],
        zoom_start=12,
        scrollWheelZoom=False,
    )

    geo_data = "map.geojson"

    if selected_area == "None":
        # Display the choropleth map based on the population
        choropleth = folium.Choropleth(
            geo_data=geo_data,
            data=data,
            columns=["DESA", "JUMLAH PENDUDUK"],
            key_on="feature.properties.DESA",
            fill_color="Reds",
            fill_opacity=0.95,
            threshold_scale=[0, 1000, 1500, 1600, 1900, 2000, 5000, 6000, 6300, 6585],
            legend_name="JUMLAH PENDUDUK",
        )
        choropleth.geojson.add_to(map)
        choropleth.geojson.add_child(
            folium.features.GeoJsonTooltip(["DESA", "JUMLAH PENDUDUK"], labels=False),
        )
    else:
        # Highlight only the selected area
        def style_function(feature):
            if feature["properties"]["DESA"] == selected_area:
                return {
                    "fillColor": "red",
                    "color": "black",
                    "weight": 2,
                    "fillOpacity": 1,
                }
            else:
                return {
                    "fillColor": "blue",  # Ganti warna yang tidak dipilih menjadi biru
                    "color": "black",
                    "weight": 1,
                    "fillOpacity": 0.5,
                }

        folium.GeoJson(
            geo_data,
            name="geojson",
            style_function=style_function,
            tooltip=folium.GeoJsonTooltip(
                fields=["DESA", "JUMLAH PENDUDUK"],
                aliases=["Desa:", "Jumlah Penduduk:"],
                localize=True,
            ),
        ).add_to(map)

    st_folium(map, width=600, height=400)


# Read the data to get the list of areas
data = pd.read_csv("kec_banggaetimur.csv")
areas = ["None"] + data["DESA"].unique().tolist()

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

# Display the table
st.write(data.head())

# Add a dropdown menu for selecting the area
selected_area = st.selectbox("Pilih daerah yang ingin ditampilkan:", areas)

# Display the map
display_map(selected_area)

import streamlit as st
import pydeck as pdk

def display_map(df):
    ICON_DATA = {
        "url": "https://img.icons8.com/?size=100&id=uzeKRJIGwbBY&format=png&color=000000",
        "width": 50,
        "height": 50,
        "anchorY": 50
    }

    df["icon_data"] = [ICON_DATA for _ in range(len(df))]

    layer = pdk.Layer(
        "IconLayer",
        df,
        get_position=['longitude', 'latitude'],
        get_icon="icon_data",
        get_size=4,
        size_scale=15,
        pickable=True,
    )

    view_state = pdk.ViewState(
        latitude=df['latitude'].mean(),
        longitude=df['longitude'].mean(),
        zoom=11,
        pitch=0,
    )

    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "{name}"},
        map_style="mapbox://styles/mapbox/light-v9",
    )

    st.pydeck_chart(r)


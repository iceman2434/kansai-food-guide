import streamlit as st
from data_processing import load_data
from restaurant_recommender import get_recommendations
from map_utils import display_map
from geolocate import get_coordinates
from simulate_typing import slow_print
from config import API_KEY

st.markdown("""
<style>
div.stButton > button:first-child {
    background: linear-gradient(to bottom right, #4c9444, #2e5a29);
    color: white;
    border: 2px solid #2e5a29;
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    background: linear-gradient(to bottom right, #5ab04f, #3a7234);
    border-color: #3a7234;
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
}

div.stButton > button:active {
    background: linear-gradient(to bottom right, #3a7234, #2e5a29);
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    transform: translateY(2px);
}
</style>
""", unsafe_allow_html=True)    

df = load_data()

st.title("🐙 Kansai Food Guide")

if 'restart' not in st.session_state:
    st.session_state.restart = False

if st.session_state.restart:
    st.session_state.restart = False
    st.experimental_rerun()

cuisine = st.text_input('Enter a cuisine (e.g., Japanese, Vegan, Italian, Cafe, etc.):')       
price_level = st.selectbox('Select a price level:', ['Any', '$', '$$ - $$$', '$$$$'])

if cuisine and price_level:
    col1, col2 = st.columns([3, 1])
    
    with col1:
        slow_print(f"You selected: {cuisine} cuisine(s) with a price level of {price_level}")
    
    with col2:
        confirm = st.button("✓  Confirm selections", use_container_width=True)

    if confirm:
        with st.spinner("Generating recommendations..."):
            recommendations, result_df = get_recommendations(df, cuisine, price_level)

        if recommendations is None:
            slow_print("No valid recommendations found for the selected cuisine(s) and price level.")
            if st.button("Restart", key="restart_no_rec"):
                st.session_state.restart = True
                st.experimental_rerun()
        else:
            st.subheader("Recommendations")
            slow_print(recommendations)

            # if API_KEY and not result_df.empty:
            if API_KEY and result_df is not None:
                print("Restaurant Locations")
                print(result_df[['name', 'address', 'latitude', 'longitude']])

                st.subheader("Map of Recommended Restaurants")
                display_map(result_df)
                slow_print("The map locations are approximations and may not be exact.")
            else:
                st.warning("Map feature is not available without a valid API key.")

            slow_print("Would you like to restart?")
            if st.button("Restart", key="restart"):
                st.session_state.restart = True
                st.experimental_rerun()
else:
    slow_print("Please enter a cuisine and select a price level to proceed.")

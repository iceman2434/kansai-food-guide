import pandas as pd
import streamlit as st
from langchain_community.llms import Ollama
import re
from geolocate import get_coordinates
from config import MODEL_NAME, API_KEY

llm = Ollama(model=MODEL_NAME)

def get_recommendations(df, cuisine, price_level):
    filtered_df = df[df['cuisines'].str.contains(cuisine, case=False, na=False)]

    if price_level != 'Any':
        filtered_df = filtered_df[filtered_df['pricelevel'] == price_level]

    if filtered_df.empty:
        return None, None

    desired_columns = ['name', 'address', 'rankingPosition', 'rawRanking', 'priceLevel', 'numberOfReviews', 'priceRange', 'description', 'cuisines']
    available_columns = [col for col in desired_columns if col in filtered_df.columns]
    data_str = filtered_df[available_columns].to_string(index=False)

    prompt = (
        f"Given the following restaurants in Osaka, Japan:\n{data_str}\n"
        f"Create a response that recommends **at most 3** restaurants in Osaka, Japan that fall within the **{price_level}** price level and serve **{cuisine}** cuisine.\n"
        f"For each restaurant, format your recommendation like this:\n"
        f"\n1. **Restaurant Name** ({price_level}):\n"
        f"   A brief description (2-3 sentences) that includes: Type of establishment, Signature dishes or specialties, Unique features or atmosphere.\n"
        f"   Address: [Complete address including street, neighborhood, city, and prefecture]\n"
        f"Make sure to include all requested details for each restaurant in the specified format.\n"
        f"Note that menu items and availability may change, so it's always best to call ahead or check the restaurant's website for the latest information."
)

    response = llm(prompt)

    pairs = re.findall(r'\*\*(.*?)\*\*.*?Address: (.*?)(?:\n|$)', response, re.DOTALL)
    result_df = pd.DataFrame(pairs, columns=['name', 'address'])

    if API_KEY:
        result_df['latitude'], result_df['longitude'] = zip(*result_df['address'].apply(get_coordinates))

    return response, result_df

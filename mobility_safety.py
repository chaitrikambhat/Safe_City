import requests
import folium
import osmnx as ox
import streamlit as st

RAPIDAPI_KEY = st.secrets["RAPIDAPI_KEY"]

def fetch_crime_data(lat, lon):
    url = "https://jgentes-crime-data-v1.p.rapidapi.com/crime"
    querystring = {
        "lat": lat,
        "long": lon,
        "startdate": "2024-01-01",
        "enddate": "2024-12-31"
    }
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "jgentes-crime-data-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

def build_route_map(origin, destination):
    G = ox.graph_from_point(origin, dist=2000, network_type='walk')
    orig_node = ox.nearest_nodes(G, origin[1], origin[0])
    dest_node = ox.nearest_nodes(G, destination[1], destination[0])
    route = ox.shortest_path(G, orig_node, dest_node, weight='length')

    m = folium.Map(location=origin, zoom_start=15)
    route_coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in route]
    folium.PolyLine(route_coords, color="blue", weight=5).add_to(m)
    return m
import streamlit as st
from youtube_comments import fetch_comments, score_toxicity
from mobility_safety import build_route_map

st.set_page_config(page_title="Safe Cities for Women", layout="wide")
st.title("👩‍💻 Safe Cities for Women Dashboard")

tab1, tab2 = st.tabs(["Online Harassment Analysis", "Safe Route Mapper"])

with tab1:
    st.header("Analyze YouTube Comment Toxicity")
    video_id = st.text_input("Enter YouTube Video ID")
    if st.button("Analyze Comments"):
        comments = fetch_comments(video_id)
        st.write(f"Fetched {len(comments)} comments.")
        scores = [score_toxicity(c) for c in comments]
        st.write(f"Average Toxicity: {sum(scores)/len(scores):.2f}")
        st.bar_chart(scores)

with tab2:
    st.header("Find a Safer Walking Route")
    start = st.text_input("Start (latitude,longitude)", "40.748817,-73.985428")
    end = st.text_input("Destination (latitude,longitude)", "40.730610,-73.935242")
    if st.button("Show Safe Route"):
        origin = tuple(map(float, start.split(',')))
        destination = tuple(map(float, end.split(',')))
        route_map = build_route_map(origin, destination)
        st.components.v1.html(route_map._repr_html_(), height=600, scrolling=True)
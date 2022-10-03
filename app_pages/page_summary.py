import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a fungal disease that affects a  wide range of plants. " 
        f"This disease can grows well in environments with high humidity and moisture.\n"
        f"* Cherry leaves are used and examined for this study. Visual criteria are used to detect the existence "
        f"of powdery mildew on the leaves. \n"
        f"* According to [Wikipedia](https://en.wikipedia.org/wiki/Powdery_mildew), "
        f"Powdery mildew is one of the easier plant diseases to identify, as its symptoms are quite distinctive. "
        f"Infected plants display white powdery spots on the leaves and stems."
        f" The lower leaves are the most affected, but the mildew can appear on any above-ground part of the plant. \n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains 4208 cherry leaf images, of which 2104 are healthy, and the rest, 2104, "
        f" have powdery mildew."
        f" ")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/HaimanotA/Instant-Mildew-Detector#README.md).")
   

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a study to differentiate "
        f"a cherry leaf that contains powdery mildew or a healthy one visually.\n"
        f"* 2 - The client is interested to tell whether a given leaf contains powdery mildew or not. "
        )

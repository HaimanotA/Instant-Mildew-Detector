import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a fungal disease that affects a  wide range of plants. 
        It can grow on any organic matter and is caused by humidity and moisture "
        f"\n Powdery mildew diseases are caused by many different species of fungi in the order "
        f"* Erysiphales."
        f"\n Powdery mildew is one of thte easier plant disease to identify, as its symptoms are quite distinctive."
        f"* According to [Wikipedia](https://www.en.m.wikipedia.org), "
        f"Infected plants display white powdery spots on the leaves and stems"
        f"e. "
        f"The lower leaves are tthe most affected, but the mildew can appear on any above-ground part of the plant."
        f"of all malaria deaths worldwide in 2019.\n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains +4000 out of +27 thousand images taken from "
        f""
        f".")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/GyanShashwat1611/WalkthroughProject01/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a study to differentiate "
        f"a cherry leaf which contains a powdery mildew or a healthy one visually.\n"
        f"* 2 - The client is interested to tell whether a given leaf contains powdery mildew or not. "
        )

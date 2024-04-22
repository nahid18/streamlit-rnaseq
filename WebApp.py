import streamlit as st
from utils import icon, data, category

# UI configurations
st.set_page_config(page_title="RNASeq Tools", page_icon=":dna:", layout="wide")
icon.show_icon(":computer:")
st.markdown("# RNASeq Tools")

# Input CSV
INPUT_CSV = "rna_seq.csv"
df = data.get_data(INPUT_CSV)
categories = category.get_category_map()


graph_images = [
    "https://raw.githubusercontent.com/Mangul-Lab-USC/RNA-seq/master/figures/5e.png",
    "https://raw.githubusercontent.com/Mangul-Lab-USC/RNA-seq/master/figures/citations_per_year.png",
    "https://raw.githubusercontent.com/Mangul-Lab-USC/RNA-seq/master/figures/figure4a.png",
    "https://raw.githubusercontent.com/Mangul-Lab-USC/RNA-seq/master/figures/figure4b.png",
    "https://raw.githubusercontent.com/Mangul-Lab-USC/RNA-seq/master/figures/figure4c.png",
    "https://raw.githubusercontent.com/Mangul-Lab-USC/RNA-seq/master/figures/figure5a.png",
    "https://raw.githubusercontent.com/Mangul-Lab-USC/RNA-seq/master/figures/figure5b.png",
    "https://raw.githubusercontent.com/Mangul-Lab-USC/RNA-seq/master/figures/figure5c.png",
    "https://raw.githubusercontent.com/Mangul-Lab-USC/RNA-seq/master/figures/figure5d.png",
    "https://raw.githubusercontent.com/Mangul-Lab-USC/RNA-seq/master/figures/most&all.png",
    "https://raw.githubusercontent.com/Mangul-Lab-USC/RNA-seq/master/figures/most&all_scatter.png",
    "https://raw.githubusercontent.com/Mangul-Lab-USC/RNA-seq/master/figures/sum_citations.png",
]

def display_graphs(image_urls):
    cols = st.columns(2)

    for i, url in enumerate(image_urls):
        col_index = i % 2
        cols[col_index].markdown("<img src='{}' width='400' style='display: block; margin: 0 auto;'>".format(url), unsafe_allow_html=True)


def configure_sidebar() -> None:
    """
    Setup and display the sidebar elements.
    """
    with st.sidebar:
        with st.form(key="rna_form"):
            st.info("**Start here ↓**", icon="👋🏾")
            filter_tools = st.multiselect(
                "Filter",
                categories.values(),
                [],
            )
            submitted = st.form_submit_button(
                "Submit",
                type="primary",
                use_container_width=True,
            )

        # Add a button for graphs
        if st.button("View All Graphs"):
            st.session_state['show_graphs'] = True

        # Add a "Home" button
        if st.button("Home"):
            st.session_state['show_graphs'] = False

        st.markdown(
            """
            ---
            Follow us on:

            𝕏 → [@serghei_mangul](https://x.com/serghei_mangul)

            Website → [https://mangul-lab-usc.github.io](https://mangul-lab-usc.github.io)

            """
        )

        return (
            submitted,
            filter_tools,
        )

def main_page(submitted: bool = False, filter_tools: list = []):
    COLUMNS = 3

    # make a copy of data
    df_copy = df.copy()

    # filter
    if submitted and len(filter_tools) > 0:
        filter_tools_keys = [k for k, v in categories.items() if v in filter_tools]
        df_copy = df_copy[df_copy["type"].isin(filter_tools_keys)]

    # sort by tool name
    df_copy = df_copy.sort_values(by="tool")

    # format data into list of dictionaries
    tools_data = list(df_copy.T.to_dict().values())

    for i in range(0, len(tools_data), COLUMNS):
        row = st.columns(COLUMNS)
        for j in range(COLUMNS):
            if i + j < len(tools_data):
                # each tool card
                current = tools_data[i + j]
                title = current["tool"]
                category = categories[current["type"]]
                features = current["features"]
                language = current["language"]
                software = current["software"]

                with row[j].expander(title):
                    st.markdown(f"**{features}**")
                    st.markdown(f"Language: **{language}**")
                    st.markdown(f"Category: **{category}**")
                    st.write(software)

def main():
    """
    Main function to run the Streamlit application.
    """
    (
        submitted,
        filter_tools,
    ) = configure_sidebar()


    if 'show_graphs' not in st.session_state:
        st.session_state['show_graphs'] = False

    if st.session_state['show_graphs']:
        display_graphs(graph_images)
    else:
        main_page(submitted=submitted, filter_tools=filter_tools)

if __name__ == "__main__":
    main()

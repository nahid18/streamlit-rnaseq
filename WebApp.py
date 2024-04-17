import streamlit as st
from utils import icon, data, category
# import streamlit.components.v1 as components
# from pandas.api.types import (
#     is_categorical_dtype,
#     is_datetime64_any_dtype,
#     is_numeric_dtype,
#     is_object_dtype,
# )


# UI configurations
st.set_page_config(page_title="RNASeq Tools", page_icon=":dna:", layout="wide")
icon.show_icon(":computer:")
st.markdown("# RNASeq Tools")


# Input CSV
INPUT_CSV = "rna_seq.csv"
df = data.get_data(INPUT_CSV)
categories = category.get_category_map()


# Configure Layout
def configure_sidebar() -> None:
    """
    Setup and display the sidebar elements.

    This function configures the sidebar of the Streamlit application,
    including the form for user inputs and the resources section.
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

    This function initializes the sidebar configuration and the main page layout.
    It retrieves the user inputs from the sidebar, and passes them to the main page function.
    """
    (
        submitted,
        filter_tools,
    ) = configure_sidebar()

    main_page(submitted=submitted, filter_tools=filter_tools)


if __name__ == "__main__":
    main()

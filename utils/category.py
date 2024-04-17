import streamlit as st


@st.cache_data
def get_category_map():
    return {
        "qc": "Quality Control",
        "read_alignment": "Read Alignment",
        "gene_annot": "Gene Annotation",
        "trans_assemb": "Transcriptome Assembly",
        "trans_quant": "Transcriptome Quantification",
        "diff_exp": "Differential Expression",
        "rna_splice": "RNA Splicing",
        "cell_conv": "Cell Deconvolution",
        "imm_prof": "Immune Repertoire Profiling",
        "allele_exp": "Allele-Specific Expression",
        "viral_detect": "Viral Detection",
        "fusion_detect": "Fusion Detection",
        "circrna_detect": "circRNA Detection",
        "srna_detect": "Small RNA Detection",
        "mirna_detect": "miRNA Detection",
        "visualize": "Visualization",
    }


@st.cache_data
def get_category_title(category: str):
    """Shows the title of a category.

    Args:
        category (str): name of the category, i.e. "visualize"
    """
    category_title_map = get_category_map()
    st.markdown(f"##### {category_title_map[category]}")

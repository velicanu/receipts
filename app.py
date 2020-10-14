import streamlit as st
import boto3
from textract import df_from_textract

st.title("TJs Receipt Scanner")
file_ = st.file_uploader("upload")

if file_:
    client = boto3.client("textract")
    st.text("Analyzing...")
    response = client.analyze_document(
        Document={"Bytes": file_.read()}, FeatureTypes=["TABLES", "FORMS"]
    )

    df = df_from_textract(response)
    st.dataframe(df)

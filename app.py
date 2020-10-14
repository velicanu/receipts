import os

import boto3
import streamlit as st

from textract import df_from_textract


def main():
    st.title("TJs Receipt Scanner")
    password = st.text_input("Enter a password", type="password")
    if not os.getenv("TJ_PASSWORD") or password != os.getenv("TJ_PASSWORD"):
        return

    file_ = st.file_uploader("upload")

    if not file_:
        return

    client = boto3.client("textract")
    st.text("Analyzing...")
    response = client.analyze_document(
        Document={"Bytes": file_.read()}, FeatureTypes=["TABLES", "FORMS"]
    )

    df = df_from_textract(response)
    st.dataframe(df)


if __name__ == "__main__":
    main()

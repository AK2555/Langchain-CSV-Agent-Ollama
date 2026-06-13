import streamlit as st
import pandas as pd

from langchain_ollama import OllamaLLM
from langchain_experimental.agents.agent_toolkits import (
    create_pandas_dataframe_agent,
)


def main():
    st.set_page_config(page_title="Ask Your CSV 📈")
    st.header("Ask Your CSV 📈")

    uploaded_file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    if uploaded_file is not None:

        # Read CSV using pandas
        df = pd.read_csv(uploaded_file)

        st.subheader("Preview")
        st.dataframe(df.head())

        user_question = st.text_input(
            "Ask a question about your CSV"
        )

        if user_question:

            llm = OllamaLLM(
                model="llama3.2"
            )

            agent = create_pandas_dataframe_agent(
                llm=llm,
                df=df,
                verbose=True,
                allow_dangerous_code=True
            )

            with st.spinner("Thinking..."):

                result = agent.invoke(
                    {"input": user_question}
                )

                st.success("Answer")

                if isinstance(result, dict):
                    st.write(result["output"])
                else:
                    st.write(result)


if __name__ == "__main__":
    main()
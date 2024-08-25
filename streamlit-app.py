import os
import streamlit as st
from openai import OpenAI
from langchain.document_loaders import youtube
from langchain.text_splitter import RecursiveCharacterTextSplitter


st.set_page_config(page_title="YOUTUBE SUMMARISER")
st.header="YOUTUBE SUMMARISER"

url=st.text_input("enter the url from youtube")

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

if st.button("Submit",type="primary"):
    if url is not None:
        print(url)
        loader=youtube.YoutubeLoader.from_youtube_url(url)
        docs=loader.load()
        ts=RecursiveCharacterTextSplitter(chunk_size=7000,chunk_overlap=0)
        sentences=ts.split_documents(docs)
        l=[]
        for sentence in sentences:
            response=client.chat.completions.create(model="gpt-4o",
            messages=[
                {"role":"system","content":"you are a helpful intelligent AI assistant"},
                {"role":"user","content":f"summarize the following paragraph into bullet points in Korean:\n\n{xx}"}
            
            ])
            msg=response.choices[0].message.content
            l.append(msg)
        st.write("".join(l))



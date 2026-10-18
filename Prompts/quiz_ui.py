from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import streamlit as st
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate, load_prompt


load_dotenv()
llm1= HuggingFacePipeline.from_model_id(model_id="microsoft/Phi-3-mini-4k-instruct",
     task="text-generation",pipeline_kwargs=dict(temperature=0.4,max_new_tokens=512)
         )
model1 = ChatHuggingFace(llm=llm1)
st.header('Quiz Preparation Tool')
topic_input = st.selectbox('Select Topic',['Select','Supervised Learning','Decision Trees', 'SVM',"Knn","Logistic and Linear regression", "K means"])

template1 = load_prompt("C:\\Users\\Madhura\\Desktop\\Langchain_Models\\Prompts\\template1.json")

if st.button("Questions"):
    chain1 = template1 | model1
    result1 = chain1.invoke({
    'topic_input':topic_input})
    
    st.write(result1.content)
    #static prompt is when you always have to write a new query for a new question
    #Based on prompt, llm output changes a lot, so if the user writes a weak prompt they might get a wrong answer.
    #Hence we need dynamic prompting- a template so that users get the same style of response everytime.
    #using chains, only one invoke will suffice
    #'style_input':style_input,
    #'length_input':length_input

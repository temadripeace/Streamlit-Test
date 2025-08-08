#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamkit as st


# In[ ]:


st.title (" Simple Streamlit App")
st.header("Welcome")
st.write ("This is a basic streamlit app")
   
number = st.slider("Pick your age", 0,100)
st.write(f "your age is" {number})


# In[ ]:





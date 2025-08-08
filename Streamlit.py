#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamkit as st


# In[ ]:


st.title (" Simple Streamlit App")
st.header("Welcome")
st.write ("This is a basic streamlit app")


# In[ ]:


name = st.text_input("Enter Your Name")
if name:
    st.success (f "Hello", (name)! \n "How are you")
    
number = st.slider("Pick your age", 0,100)
st.write(f "your age is" {number})


# In[ ]:





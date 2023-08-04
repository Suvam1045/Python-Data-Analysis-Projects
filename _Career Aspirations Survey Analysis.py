#!/usr/bin/env python
# coding: utf-8

# # Career Aspirations Survey Analysis
# 
# 

# ## About The Project
# 
# 
# #### Career Aspirations Survey Analysis refers to the process of examining and interpreting data collected from a survey focused on individuals' career goals and ambitions. This analysis aims to gain insights into the respondents' desired career paths, their motivations, the skills they prioritize, and their overall aspirations in the professional realm.
# 
# #### During a Career Aspirations Survey Analysis, various statistical techniques and methodologies may be employed to derive meaningful conclusions from the survey data.These techniques could include data visualization, descriptive statistics, correlation analysis, and potentially more advanced methods like factor analysis or clustering.
# 
# #### The information gathered from a career aspirations survey helps in understanding an individual’s:-
# 
# #### 1-Long term goals
# #### 2-Preferred work environment
# #### 3-Preferred role and responsibilities
# #### 4-Interests and values

# ### Questions which were answered during analysis of the survey data :-
# 
# #### 1-Current country of the people who submitted answers to this career aspirations survey.
# #### 2-Factors influencing the career aspirations of Genz.
# #### 3-How many want to pursue higher education outside India with their investment?
# #### 4-How likely Genz is to work for one employer for three years or more?
# #### 5-Will GenZ work for a company whose mission is not clearly?
# #### 6-How likely the Genz will work for a company whose mission is not bringing any social impact (on a scale of 1 – 10)?
# #### 7-Preferred working environment of Genz.
# #### 8-What kind of employers Genz wants to work with?
# #### 9-Which type of learning environment the Genz are most likely to work in?
# #### 10-What type of managers Genz wants to work under?

# ## Importing The Datset Using Panda Library

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\Datasets\Career Aspiration Analysis\Your Career Aspirations of GenZ.csv")
print(data.head())


# ### The column names in the dataset contain questions asked in the survey, and the rows contain the answers submitted by the people of generation z. Let’s look at all the questions asked in the survey:-

# In[2]:


print(data.columns)


# ##  Current country of the people who submitted answers to this career aspirations survey:-

# In[3]:


country = data["Your Current Country."].value_counts()
label = country.index
counts = country.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Location of Participants ')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# ### Observations:-
# 
# #### So 98.3% of the people who submitted answers to the survey live in India.

# ## Factors influencing the career aspirations of Genz:-

# In[4]:


question1 = data["Which of the below factors influence the most about your career aspirations ?"].value_counts()
label = question1.index
counts = question1.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Factors influencing career aspirations')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# ### Observations:-
# 
# #### 1-33.6% of the Genz are influenced by parents<br>
# #### 2-24.3% are influenced by the people who have changed the world for the better<br>
# #### 3-16.6% are influenced by people from their circle but not family.<br>
# #### 4-15.7% are influenced by influencers having successful careers.<br>

# ## How many want to pursue higher education outside India with their investment?

# In[5]:


question2 = "Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it."
question2 = data[question2].value_counts()
label = question2.index
counts = question2.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Will you pursue a Higher Education outside India with your investment?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# ### Observations:-
# 
# #### 1) 46.8% believe in pursuing higher education outside India with their self-earned income.<br>
# #### 2) 27.7% don’t want to pursue higher education outside of India.<br>
# #### 3) 25.5% can only pursue higher education outside India if someone can bare that cost.<br>

# ## How likely Genz is to work for one employer for three years or more?

# In[6]:


question3 = "How likely is that you will work for one employer for 3 years or more ?"
question3 = data[question3].value_counts()
label = question3.index
counts = question3.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='How likely is that you will work for one employer for 3 years or more?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# ### Observations:-
# 
# #### 1) 59.1% find it hard, but they can only if the company is good.<br>
# #### 2) 33.6% don’t have any problem working for three years or more.<br>
# #### 3) Only 7.23% say that they will don’t work for so long by any chance.<br>

#  ## Will GenZ work for a company whose mission is not clearly?

# In[7]:


question5 = "How likely would you work for a company whose mission is misaligned with their public actions or even their product ?"
question5 = data[question5].value_counts()
label = question5.index
counts = question5.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='How likely would you work for a company whose mission is misaligned with their actions?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# ### Observations:-
# 
# ####  67.2%  partcipants didn't agree to work with such company, while only 32.8% participants don't have any issues in working with such companies  .
# 

# ## How likely the Genz will work for a company whose mission is not bringing any social impact (on a scale of 1 – 10)?

# In[8]:


question6 = "How likely would you work for a company whose mission is not bringing social impact ?"
question6 = data[question6].value_counts()
label = question6.index
counts = question6.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='How likely would you work for a company whose mission is not bringing social impact?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# ### Observation:-
# 
# #### Most people are unhappy working with a company whose mission is not to bring any social impact.

# ## Preferred working environment of Genz:-

# In[9]:


question7 = "What is the most preferred working environment for you."
question7 = data[question7].value_counts()
label = question7.index
counts = question7.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='What is the most preferred working environment for you?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# ### Observations:-
# 
# #### 1)25.5% of Genz want a fully remote working environment with options to travel.
# #### 2)24.3% of Genz want a hybrid working environment with less than 15 days a month at the office.
# #### 3)21.3% of Genz are happy with every day at the office.

# ## What kind of employers Genz wants to work with?

# In[10]:


question8 = "Which of the below Employers would you work with."
question8 = data[question8].value_counts()
label = question8.index
counts = question8.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Which of the below Employers would you work with?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# ### Observations:-
# 
# #### 1)48.1% of Genz wants employers who push their limits by enabling a learning environment and reward them at the end.
# #### 2)31.9% want employers who appreciate a learning environment.
# #### 3)15.3% want an employer who enables a rewarding environment.

# ## Which type of learning environment the Genz are most likely to work in?

# In[11]:


question9 = "Which type of learning environment that you are most likely to work in ?"
question9 = data[question9].value_counts()
label = question9.index
counts = question9.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Which type of learning environment that you are most likely to work in?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# ### Observations:-
# 
# #### 1)25.1% want a self-paced learning portal and an instructor learning program
# #### 2)19.1% want an instructor or expert learning program and trial-and-error side projects within the company
# #### 3)17.4% want an instructor or expert learning program and want to learn by observing others
# #### 4)16.2% want a self-paced learning portal and want to learn by observing others

# ## What type of managers Genz wants to work under?

# In[12]:


question10 = "What type of Manager would you work without looking into your watch ?"
question10 = data[question10].value_counts()
label = question10.index
counts = question10.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='What type of Manager would you work without looking into your watch?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# ### Observations:-
# 
# #### Most Genz wants managers who can explain expectations clearly, and who set goals and help achieve them.

# In[ ]:





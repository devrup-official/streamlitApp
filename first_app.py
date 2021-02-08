import streamlit as st
import numpy as np 
import pandas as pd 

#streamlit run [filename]

st.title('StackOverflow 2019 Developer Survey')
st.write('(This data only reflects 50 rows for performance purposes)')
st.subheader('Use the sidebar to filter the data set by student status. The below charts will auto-generate based on your selections.')
st.subheader(' ')
st.subheader(' ')

#Caching allows you to reuse the already load variable
#instead of reloading/recomputing
@st.cache
def get_data(nrows):
    return pd.read_csv('survey_results_public.csv', nrows=nrows)

#data_load_state = st.text('Loading data...')
df = get_data(50)
df.rename(columns={'Student': 'Selection'}, inplace=True)
#data_load_state.text("Done! (using st.cache)")

# inspect raw data
if st.checkbox('Select to see raw dataset'):
    st.write(df)


 # Create a Check box to show few summary details.
if st.checkbox('Select to see top 10 databases and frameworks used'):
    grp_data = df.copy()
    grp_data['Count'] = 1
    st.subheader('Top 10 Databases used')
    st.write(pd.DataFrame(grp_data.groupby(['DatabaseWorkedWith'], sort=False)['Count'].count().rename_axis(["DatabaseWorkedWith"]).nlargest(10)))
    st.subheader('Top 10 Frameworks used')
    st.write(pd.DataFrame(grp_data.groupby(['WebFrameWorkedWith'], sort=False)['Count'].count().rename_axis(["WebFrameWorkedWith"]).nlargest(10)))

st.subheader(' ')
st.subheader('Filtered data table - selected columns will be added to the end')
student_status_selection = st.sidebar.multiselect("Filter by student status here:", df['Selection'].unique())
#st.write("Selected:", student_selection)

variables = st.sidebar.multiselect("Select the columns you'd like to see:", df.columns)
#st.write("You selected these variables", variables)

selected_segmented_data = df[(df['Selection'].isin(student_status_selection))]

all_status_data = selected_segmented_data[variables]
#student_data_is_check = st.checkbox("Display the data of selected student status")
#if student_data_is_check:
#    st.write(all_status_data)
st.write(all_status_data)

st.subheader('Country breakdown')
country = selected_segmented_data.groupby('Country')['Selection'].count()
st.bar_chart(country)

st.subheader('Hobbyist?')
hobbyist = selected_segmented_data.groupby('Hobbyist')['Selection'].count()
st.bar_chart(hobbyist)

st.subheader('Gender breakdown')
gender = selected_segmented_data.groupby('Gender')['Selection'].count()
st.bar_chart(gender)

st.subheader('Education level')
edlevel = selected_segmented_data.groupby('EdLevel')['Selection'].count()
st.bar_chart(edlevel)

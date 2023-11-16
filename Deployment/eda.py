import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




st.set_page_config(
    page_title ='H8 Online customer shopping intention Exploratory Data Analysis',
    layout = 'wide',
    initial_sidebar_state = 'expanded'
)

def run():
    # title
    st.title('H8 Online customer shopping intention')

    # sub header
    st.subheader('EDA for analysis of H8 online shopping intention')

    # show dataframe
    df = pd.read_csv('online_shoppers_intention.csv')
    st.dataframe(df)
    
    st.write('#### Comparison between visitor who make purchase and visitor who does not make purchase ')
    buy_count = df['Revenue'].value_counts()
    fig = plt.figure(figsize=(15,5))
    plt.pie(buy_count,
        labels=['Not Buy', 'Buy'], startangle=90,
        autopct='%1.1f%%', explode=[0,0.1])
    st.pyplot(fig)
    st.write('Based on the results above, it can be seen that only 15.5% of the total visitors ended up buying something from the company or around 1908 people in a period of 10 months, while 84.5% of visitors or 10422 visitors did not buy anything from the website. This pie chart also informs us that the revenue column is very unbalanced in its class distribution.')


    fig = plt.figure(figsize=(15,5))
    sns.histplot(data=df, x='Month', hue='Revenue', palette='pastel')
    st.pyplot(fig)
    st.write('Above is the result of a sales histogram by month, the highest number of visitors is in May followed by November and March. But the highest number of buyers is in November, followed by May, then December. This can be attributed to the month of November where it is already a month at the end of the year and can be one of the reasons for many purchases.')


    fig = plt.figure(figsize=(15,5))
    sns.histplot(data=df, x='Region', hue='Revenue', palette='pastel')
    st.pyplot(fig)
    st.write('Based on the histogram above, it can be seen that the most users are in region 1 (Jabodetabek) followed by region 3 (Central Java) and region 4 (East Java).')


    st.write('#### Comparison between returning visitor and new visitor')
    visitor_count = df['VisitorType'].value_counts()
    fig = plt.figure(figsize=(15,5))
    plt.pie(visitor_count,
        labels=['Returning Visitor', 'New Visitor','Other'], startangle=90,
        autopct='%1.1f%%')
    st.pyplot(fig)
    st.write('It can be seen that 85.6% of website visitors are returning visitors while 13.7% are new visitors.')
    st.write('After exploring in more detail, 1470 returning visitors made purchases on the website and 9081 visitors did not make purchases. Then as many as 422 new visitors made purchases on the website and 1272 new visitors did not make purchases. This indicates that the website that H8 has has a good ability to get new visitors to make purchases where as many as 422 of the total visitors, namely 1694 or 25% of new visitors make purchases. Meanwhile, there are only 1470 old visitors out of a total of 10551 old visitors. This indicates that only 14% of old visitors made a purchase. The total number of old visitors is a good number but the H8 website has a weakness in convincing old visitors to make a purchase.')

    fig = plt.figure(figsize=(15,5))
    sns.countplot(data=df, x='Weekend', hue='Revenue', palette='pastel')
    st.pyplot(fig)
    st.write('Based on the count plot above, it can be seen that there are more website visitors on weekdays compared to weekends and more purchases are also made on weekdays compared to weekends.')

    fig = plt.figure(figsize=(15,5))
    sns.boxenplot(x=df['ProductRelated_Duration'],y=df['Revenue'], palette = 'pastel', orient = 'h')
    st.pyplot(fig)
    st.write('Based on the results above, the distribution for visitors who buy is greater than for visitors who do not buy where the distribution in the visitors who do not buy has more outlier results than users who eventually buy. From the distribution of this data, it shows that there are visitors who look at similar products for a very long time but in the end do not make a purchase, so the party must improve the algorithm so that it can attract users who browse the website but do not buy so that they can find products that match their wishes.')

    fig = plt.figure(figsize=(15,5))
    sns.boxenplot(x=df['BounceRates'],y=df['Revenue'], palette = 'pastel', orient = 'h')
    st.pyplot(fig)
    st.write('From the box plot above, it can be seen that most visitors who do not buy are visitors who have a high bounce rate, namely visitors who do not open other pages or leave immediately after entering the website. This provides information that, parties must make their landing pages as attractive and good as possible in order to make visitors who come to the website so that they are interested in browsing the website further to see the products and promos offered.')


    fig = plt.figure(figsize=(15,5))
    sns.stripplot(x=df['PageValues'], y=df['Revenue'], palette = 'pastel',orient = 'h')
    st.pyplot(fig)
    st.write('Based on the data above, most visitors who eventually make a purchase are visitors who have high page values.Based on information from https://support.google.com/analytics/answer/2695658?hl=en Page Value is the average value for the pages a user visits before landing on the destination page or completing an Ecommerce transaction (or both). This value is meant to give users an idea of which pages on the site contribute more to the site own revenue. Therefore, H8 should check which pages of their site provide the greatest page values in order to improve their site to attract more customers.')

if __name__== '__main__':
    run()





import streamlit as st
import pandas as pd
import numpy as np
import pickle


#Load all files
with open('preprocess_pipeline.pkl','rb') as file_1:
  preprocess_pipeline = pickle.load(file_1)

with open('best_rf_2.pkl','rb') as file_2:
  best_rf_2 = pickle.load(file_2)


def run():
    # Membuat form
    with st.form(key='form parameters'):
        Administrative = st.number_input('Administrative', min_value=0, max_value=9999999999999,value=0, help='This is the number of pages of this type (administrative) that the user visited.')
        Administrative_Duration = st.number_input('Administrative_Duration', min_value=0, max_value=9999999999999,value=0, help='This is the amount of time spent in this category of pages.')
        Informational = st.number_input('Informational', min_value=0, max_value=9999999999999,value=0, help='This is the number of pages of this type (informational) that the user visited.')
        Informational_Duration = st.number_input('Informational_Duration', min_value=0, max_value=9999999999999,value=0, help='This is the number of pages of this type (informational) that the user visited.')
        ProductRelated = st.number_input('ProductRelated', min_value=0, max_value=9999999999999,value=0, help='This is the number of pages of this type (product related) that the user visited.')
        ProductRelated_Duration = st.number_input('Informational_Duration', min_value=0, max_value=9999999999999,value=0, help='This is the amount of time spent in this category of pages.')
        st.markdown('---')

        BounceRates = st.number_input('User Bounce Rate',min_value=0.0, max_value=0.2,value=0.0, help='The percentage of visitors who enter the website through that page and exit without triggering any additional tasks.' )
        ExitRates = st.number_input('User Exit Rate',min_value=0.0, max_value=0.2,value=0.0, help=' The percentage of pageviews on the website that end at that specific page' )
        PageValues = st.number_input('User Page Rates',min_value=0, max_value=362,value=0, help='he average value of the page averaged over the value of the target page and/or the completion of an eCommerce transaction.' )
        SpecialDay = st.number_input('User closeness to special day',min_value=0, max_value=1,value=0, help='This value represents the closeness of the browsing date to special days or holidays (eg Mothers Day or Valentines day) in which the transaction is more likely to be finalized. More information about how this value is calculated below.' )
        Month = st.text_input('Month:', value='Nov')
        st.markdown('---')

        OperatingSystems = st.number_input('User Operating systems',min_value=1, max_value=8,value=1)
        Browser = st.number_input('User browser?',min_value=1, max_value=13,value=1)
        Region = st.number_input('User Region',min_value=-1, max_value=9,value=0, help='(1: Jabodetabek, 2: Jawa Barat, 3: Jawa Tengah, 4:Jawa Timur, 5:Bali,NTB,NTT, 6: Sumatera Selatan, Lampung, Bengkulu, Bangka Belitung, 7: Sumatera Utara, Aceh, Sumatera Barat, Kepulauan Riau, 8: Kalimantan, 9: Sulawesi)' )
        TrafficType = st.number_input('User traffic status?',min_value=1, max_value=20,value=1, help='An integer value representing what type of traffic the user is categorized into.' )
        VisitorType = st.selectbox('Visitor Type?', ('New_Visitor','Returning_Visitor','Other'))
        st.write('Is it on wekend?')
        Weekend = st.checkbox('Yes', value=True)
        st.markdown('---')

        submitted = st.form_submit_button('Predict')


        data_inf = {
        'Administrative': Administrative,
        'Administrative_Duration':Administrative_Duration,
        'Informational':Informational,
        'Informational_Duration':Informational_Duration,
        'ProductRelated':ProductRelated,
        'ProductRelated_Duration':ProductRelated_Duration,
        'BounceRates':BounceRates,
        'ExitRates':ExitRates,
        'PageValues':PageValues,
        'SpecialDay':SpecialDay,
        'Month':Month,
        'OperatingSystems':OperatingSystems,
        'Browser':Browser,
        'Region':Region,
        'TrafficType':TrafficType,
        'VisitorType':VisitorType,
        'Weekend':Weekend
    }
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        pd_inf_scaled = preprocess_pipeline.transform(data_inf)
        y_pred_inf = best_rf_2.predict(pd_inf_scaled)

        st.write('### Customer make a purchase?:', str(int(y_pred_inf)))
        if y_pred_inf == 1:
           st.write('Purchased')
        else:
           st.write('Not Purchased')

if __name__ == '__main__':
    run()
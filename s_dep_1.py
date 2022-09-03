# -*- coding: utf-8 -*-
"""S_Dep_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LVxvWortsmuRuMJnNQrejY85zKEk4_qU
"""
import warnings
warnings.filterwarnings("ignore")
import time
import streamlit as st
import numpy as np
import pandas as pd
import pickle
import random
from scipy.sparse import hstack


start = time.time()

st.header('AIRBNB TRAVEL DESTINATION PREDICTOR')
st.subheader('''
(A model deployment by SHRADHANJALI )''')
st.write('''
Consider yourself an American traveller who made a reservation for a vacation spot on the Airbnb website.
This programme essentially uses machine learning to determine your top 5 potential trip locations.
Please provide the facts you feel best describes you, then have pleasure in your forecasts.
''')


left_column, right_column = st.columns(2)
# Or even better, call Streamlit functions inside a "with" block:
with left_column:
    gender = st.radio('GENDER',('Male','Female', 'Other',  'Unkown'))


    
age = st.slider('AGE')  # 👈 this is a widget



pro_df = pd.DataFrame({'aff_pro': ['direct', 'google', 'facebook', 'bing', 'yahoo', 'baidu', 'email_marketing', 'padmapper', 'facebook_open_graph', 'gsp', 'vast' ,'yandex', 'meetup', 'craigslist', 'daum', 'naver', 'other']
    })
affiliate_provider = st.selectbox('AFFILIATE PROVIDER', pro_df['aff_pro'])
# st widget to choose user's affiliate provider. Default = first value



chn_df = pd.DataFrame({'aff_chn': ['seo', 'api', 'sem_brand', 'sem_non_brand', 'content', 'remarketing', 'direct', 'other']
    })
affiliate_channel = st.selectbox('AFFILIATE CHANNEL', chn_df['aff_chn'])






left_column, right_column = st.columns(2)
with right_column:
    signup_app = st.radio('OS',('iOS','Web',  'Android', 'Moweb'))
with left_column:
    signup_method = st.radio('SIGNUP METHOD',('basic', 'google', 'facebook'))
# st widget to choose user's signup-methods and signup-apps. Default = first value    

    
    


browser = pd.DataFrame({'browser': ['Chrome', 'Chrome_Mobile', 'Android_Browser', 'Safari', 'Mobile_Safari','Mobile_Firefox', 'Apple_Mail', 'Firefox','SiteKiosk', 'IE', 'Chromium', 'Opera', 'Silk','AOL_Explorer','IE_Mobile','Opera_Mini', 'Maxthon','Sogou_Explorer', 'BlackBerry_Browser', 'Yandex_Browser', 'IceWeasel', 'Iron', 'wOSBrowser', 'SeaMonkey','TenFourFox', 'Mozilla', 'Googlebot', 'Outlook_2007', 'Pale_Moon','CoolNovo',  'IceDragon', 'TheWorld_Browser', 'RockMelt', 'Avant_Browser', 'unknown']})

first_browser = st.selectbox('SELECT BROWSER', browser['browser'])
# st widget to choose user's browser. Default = first value
 

    

device_df = pd.DataFrame({'device': ['Mac_Desktop', 'iPhone', 'iPad', 'Windows_Desktop', 'Android_Tablet', 'Desktop_Other', 'Android_Phone', 'Smartphone_Other','Other_Uknown']})

first_device_type = st.selectbox('CHOOSE YOUR DEVICE', device_df['device'])
# st widget to choose user's device type. Default = first value




# st widget to choose user's language. Default = first value

language_data = pd.DataFrame({'language': ['English', 'French', 'Italian', 'Chinese Mandarin', 'Chinese Simplified', 'Korean', 'Espanol', 'Hungarian', 'German', 'Russian', 'Japanese', 'Portugese','Swedish','Dutch','Polish', 'Turkish', 'Danish','Thai','Bahasa Indonesia', 'Greek', 'Norwegian', 'Finnish','IS', 'Catalan']})
L_DF = st.selectbox('SELECT YOUR LANGUAGE', language_data['language'])

if L_DF == 'English':
    language = 'en'
if L_DF == 'French':
    language = 'fr' 
if L_DF == 'Italian':
    language = 'it'   
if L_DF == 'Chinese Mandarin':
    language = 'zh'
if L_DF == 'Chinese Simplified':
    language = 'cs'    
if L_DF == 'Korean':
    language = 'ko'
if L_DF == 'Russian':
    language = 'ru'
if L_DF == 'German':
    language = 'de'
if L_DF == 'Japanese':
    language = 'ja'
if L_DF == 'Espanol':
    language = 'es'
if L_DF == 'Thai':
    language = 'th'
if L_DF == 'Portugese':
    language = 'pt'
if L_DF == 'Swedish':
    language = 'sv'
if L_DF == 'Dutch':
    language = 'nl'
if L_DF == 'Polish':
    language = 'pl'
if L_DF == 'Turkish':
    language = 'tr'   
if L_DF == 'Danish':
    language = 'da'
if L_DF == 'Finnish':
    language = 'fi'
if L_DF == 'Bahasa Indonesia':
    language = 'id'
if L_DF == 'Norwegian':
    language = 'no'
if L_DF == 'Greek':
    language = 'el'
if L_DF == 'IS':
    language = 'is'
if L_DF == 'Catalan':
    language = 'ca'
if L_DF == 'Hungarian':
    language = 'hu'

# Time is "simulated" in this cell. The time in the training set represents the entire amount of time (in seconds) that a user spends choosing a location.
# It is impossible to obtain an actual time range equivalent to those in training data because we are inputting numbers during deployment very quickly.
# As a result, I made some adjustments to keep the time range consistent with the training data.
# this cell fetches suer's account created day and month
account_month_df = pd.DataFrame({'month': [x for x in range(1,13)]})
account_day_df = pd.DataFrame({'day': [x for x in range(1,32)]})
account_created_month = st.selectbox('MONTH WHEN YOU HAVE CREATED THE ACCOUNT', account_month_df['month'])
account_created_day = st.selectbox('DAY WHEN YOU HAVE CREATED THE ACCOUNT', account_day_df['day'])



# forming a dataframe of query point
rand_n = random.randint(2, 50)
end = time.time()
secs_elapsed = rand_n * (end - start)*100000



qp_df = pd.DataFrame({'gender': gender,
                     'age': age,
                     'signup_flow' : 0,
                     'language' : language,
                     'signup_method' : signup_method,
                     'signup_app' : signup_app,
                     'affiliate_provider' : affiliate_provider,
                     'affiliate_channel': affiliate_channel,
                     'first_browser' : first_browser,
                     
                     'first_device_type' : first_device_type ,
                     'account_created_month': account_created_month,
                     'account_created_day' : account_created_day,
                     'first_booking_month' : 0,
                     'first_booking_day': 0,
                     'action': 'create',
                     'action_type' : '-unknown-  -unknown-',
                     'action_detail' : '-unknown-  -unknown-',
                     'secs_elapsed' : secs_elapsed
                     }, index=[0])

query_point = qp_df
st.write('Query Point:')
query_point

print(query_point.columns)

print(query_point.shape)

#separating out the features in query point

gender = query_point['gender'].values
age = query_point['age'].values
signup_method = query_point['signup_method'].values
signup_flow = query_point['signup_flow'].values
language = query_point['language'].values
affiliate_channel = query_point['affiliate_channel'].values
affiliate_provider = query_point['affiliate_provider'].values
signup_app = query_point['signup_app'].values
first_device_type = query_point['first_device_type'].values
first_browser = query_point['first_browser'].values
account_created_day = query_point['account_created_day'].values
account_created_month = query_point['account_created_month'].values
first_booking_day = query_point['first_booking_day'].values
first_booking_month = query_point['first_booking_month'].values
action = query_point['action'].values
action_type = query_point['action_type'].values
action_detail = query_point['action_detail'].values
secs_elapsed = query_point['secs_elapsed'].values

# bringing in the pre-trained vectorizers and the Model
path = 'C:\BNB_Deployment\Model_Vectors'

gender_vectorizer = pickle.load(open('gender_vectorizer.pkl', 'rb'))
#action_vectorizer = pickle.load(open('action_vectorizer.pkl', 'rb'))
action_detail_vectorizer = pickle.load(open('action_detail_vectorizer.pkl', 'rb'))
action_type_vectorizer = pickle.load(open('action_type_vectorizer.pkl', 'rb'))
affiliate_channel_vectorizer = pickle.load(open('affiliate_channel_vectorizer.pkl', 'rb'))
affiliate_provider_vectorizer = pickle.load(open('affiliate_provider_vectorizer.pkl', 'rb'))
first_browser_vectorizer = pickle.load(open('first_browser_vectorizer.pkl', 'rb'))
first_device_type_vectorizer = pickle.load(open('first_device_type_vectorizer.pkl', 'rb'))
language_vectorizer = pickle.load(open('language_vectorizer.pkl', 'rb'))
signup_app_vectorizer = pickle.load(open('signup_app_vectorizer.pkl', 'rb'))
signup_method_vectorizer = pickle.load(open('signup_method_vectorizer.pkl', 'rb'))


# # Vectorizing non-numeric features

# vectorizing gender

vector_gender = gender_vectorizer.transform(gender)
print('Shape:',vector_gender.shape)
#vector_gender.toarray()

# vectorizing action

#vector_action = action_vectorizer.transform(action)
vector_action = pickle.load(open('action_vector.pkl', 'rb'))
print('Shape:',vector_action.shape)
#print(vector_action.toarray())
#vector_action

# vectorizing action_detail

vector_action_detail = action_detail_vectorizer.transform(action_detail)

print('Shape:',vector_action_detail.shape)
#print(vector_action_detail.toarray())
#vector_action_detail

# vectorizing action_type

vector_action_type = action_type_vectorizer.transform(action_type)

print('Shape:',vector_action_type.shape)
#print(vector_action_type.toarray())
#vector_action_type

# vectorizing affiliate_channel

vector_affiliate_channel = affiliate_channel_vectorizer.transform(affiliate_channel)

print('Shape:',vector_affiliate_channel.shape)
print(vector_affiliate_channel.toarray())
#vector_affiliate_channel

# vectorizing affiliate_provider

vector_affiliate_provider = affiliate_provider_vectorizer.transform(affiliate_provider)

print('Shape:',vector_affiliate_provider.shape)
print(vector_affiliate_provider.toarray())
#vector_affiliate_provider

# vectorizing first_browser

vector_first_browser = first_browser_vectorizer.transform(first_browser)

print('Shape:',vector_first_browser.shape)
print(vector_first_browser.toarray())
#vector_first_browser

# vectorizing first_device_type

vector_first_device_type = first_device_type_vectorizer.transform(first_device_type)

print('Shape:',vector_first_device_type.shape)
print(vector_first_device_type.toarray())
#vector_first_device_type

# vectorizing language

vector_language = language_vectorizer.transform(language)
print('Shape:',vector_language.shape) 
print(vector_language.toarray())
#vector_language

# vectorizing signup_app

vector_signup_app = signup_app_vectorizer.transform(signup_app)

print('Shape:',vector_signup_app.shape)
print(vector_signup_app.toarray())
#vector_signup_app

# vectorizing signup_method

vector_signup_method = signup_method_vectorizer.transform(signup_method)

print('Shape:',vector_signup_method.shape)
print(vector_signup_method.toarray())
#vector_signup_method

# input to the model for prediction

input = hstack((vector_gender,
                 age,
                vector_signup_method,
                signup_flow,
                vector_language,
                vector_affiliate_channel,
                vector_affiliate_provider,
                vector_signup_app,
                vector_first_device_type,
                vector_first_browser,
                account_created_day,
                account_created_month,
                first_booking_day,
                first_booking_month,
                vector_action,
                vector_action_type,
                vector_action_detail,
                secs_elapsed)).tocsr()

print(input.shape)


# # Performing the prediction

import numpy as np
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from tqdm import tqdm

# instentiating the models

knn = KNeighborsClassifier(n_neighbors=51)
lr = LogisticRegression()
rf1 = RandomForestClassifier(n_estimators=100, max_depth=3)
dt = DecisionTreeClassifier(max_depth = 2, min_samples_split = 50 )
rf2 = RandomForestClassifier(n_estimators=50, max_depth=2)
nb = GaussianNB(var_smoothing = 1e-8)
xgb = XGBClassifier(max_depth=3, n_estimators=50, n_jobs = -1)
xgb2 = XGBClassifier(max_depth=3, n_estimators=50, n_jobs = -1)

baseline_models=[knn, rf1, dt, rf2, nb, xgb, xgb2] 
 
metamodel=lr

# Building custom stacking classifier

class Stacking_classifier():
    def __init__(self,val,estimators,metamodel):
        self.estimators=estimators
        self.metamodel=metamodel
        self.val=val   
        
    def fit(self,x,y):
        #spliting the training data into train(50) and test(50)
        self.x=x
        self.y=y
        D1, D2 , D1_val, D2_val = train_test_split(self.x , self.y , test_size=0.5, random_state=42)

        # Stacking the  D_train and D_test with target values
        D1_val=D1_val.reshape(-1,1)
        D2_val=D2_val.reshape(-1,1)
        Data1=hstack((D1, D1_val))
        Data2=hstack((D2, D2_val))

        #Creating sample data sets from Data1
        rng = np.random.default_rng()
        D_sample=[]
        for i in range(self.val):
            chs=rng.choice(Data1.toarray(),size=20000)
            D_sample.append(chs)

        #building custom stacking classifier
        Data2=Data2.toarray()
        d2_y = Data2[:,-1]
        d2_X = np.delete( Data2, -1 , axis=1)
        predictions=[]
        for i in tqdm(range(len(self.estimators))):
            y_sample = D_sample[i][:,-1]
            X_sample =np.delete(D_sample[i], -1 , axis=1)
            self.estimators[i].fit(X_sample,y_sample)
            pred = self.estimators[i].predict_proba(d2_X)
            predictions.append(pred)
        prediction = np.concatenate((predictions),axis=1)
        self.meta= metamodel.fit(prediction,d2_y)
    
    def proba_predict(self,X_test):
      #Getting predictions from the stacked models
        pred=[]
        for i in range(len(self.estimators)):
            p = self.estimators[i].predict_proba(X_test.toarray())
            pred.append(p)
        data = np.concatenate((pred),axis=1)
        proba = self.meta.predict_proba(data)
        return proba

modelsc = pickle.load(open('modelrf.pkl', 'rb'))

from sklearn.model_selection import train_test_split
from scipy.sparse import hstack

preds = modelsc.predict_proba(input)

print(preds)

dests  = ['Australia', 'Canada', 'Denmark', 'Espain', 'France', 'Great Britain', 'Italy', 'NDF', 'Netherlands', 'Portugal', 'US', 'other']

# Getting the final results

'Starting the prediction...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(11):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Prediction progress : {10*i}%')
  bar.progress(10*i)
  time.sleep(0.1)

'Done!'

pred_df = pd.DataFrame({'Destination': dests,
                       'Probability (%)' : preds[0]*100})

top_5_dests = pred_df.sort_values(by=['Probability (%)'], ascending=False)[:5]
st.write("According to my Machine Learning model's prediction, here are your top 5 destinations you might be interested in:")
st.write(top_5_dests['Destination'])

# this cell is to shoe model interptratation

if st.checkbox('Show Model interpretation'):
    top_5_dests
    
st.write('*********** PREDICTION ENDS HERE. THANK YOU FOR GIVING IT A TRY! ****************')


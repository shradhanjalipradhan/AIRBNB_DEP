# -*- coding: utf-8 -*-
"""S_Dep_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LVxvWortsmuRuMJnNQrejY85zKEk4_qU
"""

import numpy as np
import pandas as pd
import streamlit as st
import pickle
import random
from scipy.sparse import hstack
import warnings
warnings.filterwarnings("ignore")
import time

start = time.time()

st.header('AIRBNB TRAVEL DESTINATION PREDICTOR')
st.subheader('''
(A model deployment by SHRADHANJALI  PRADHAN )''')
st.write('''
Consider yourself an American traveller who made a reservation for a vacation spot on the Airbnb website.
This programme essentially uses machine learning to determine your top 5 potential trip locations.
Please provide the facts you feel best describes you, then have pleasure in your forecasts.
''')

age = st.slider('AGE')  # 👈 this is a widget

left_column, right_column = st.columns(2)

# Or even better, call Streamlit functions inside a "with" block:
with left_column:
    gender = st.radio('SELECT YOUR GENDER',('Female', 'Male', 'Unkown', 'Other'))

aff_chn_df = pd.DataFrame({'aff_chn': ['direct', 'sem_brand', 'sem_non_brand', 'seo', 'api', 'content', 'other', 'remarketing']
    })

affiliate_channel = st.selectbox('SELECT YOUR MEDIUM', aff_chn_df['aff_chn'])

# st widget to choose user's affiliate provider. Default = first value

aff_pro_df = pd.DataFrame({'aff_pro': ['direct', 'google', 'other', 'bing', 'facebook', 'padmapper', 'email_marketing', 'yahoo', 'facebook_open_graph', 'gsp', 'vast', 'naver', 'baidu', 'yandex', 'meetup', 'craigslist', 'daum']
    })

affiliate_provider = st.selectbox('CHOOSE YOUR PROVIDER', aff_pro_df['aff_pro'])

#affiliate_provider = list(affiliate_provider)

# st widget to choose user's signup-methods and signup-apps. Default = first value

left_column, right_column = st.columns(2)

with left_column:
    signup_method = st.radio('METHOD TO SIGNUP',('basic', 'facebook', 'google'))
    
with right_column:
    signup_app = st.radio('SIGNUP METHOD',('Web', 'iOS', 'Android', 'Moweb'))

# st widget to choose user's device type. Default = first value

device_df = pd.DataFrame({'device': ['Mac_Desktop', 'Windows_Desktop', 'Desktop_Other', 'iPhone', 'iPad', 'Android_Phone', 'Android_Tablet', 'Smartphone_Other','Other_Uknown']})

first_device_type = st.selectbox('CHOOSE YOUR DEVICE', device_df['device'])

#first_device_type = list(first_device_type)

# st widget to choose user's browser. Default = first value

browser_df = pd.DataFrame({'browser': ['Chrome', 'Safari', 'Firefox', 'IE', 'Chromium', 'Mobile_Safari', 'Chrome_Mobile', 'Android_Browser', 'Opera', 'Silk','AOL_Explorer','IE_Mobile','Mobile_Firefox', 'Maxthon', 'Apple_Mail','Sogou_Explorer', 'BlackBerry_Browser','SiteKiosk', 'Yandex_Browser', 'IceWeasel', 'Iron', 'Pale_Moon','CoolNovo', 'Opera_Mini', 'wOSBrowser', 'SeaMonkey','TenFourFox', 'Mozilla', 'Googlebot', 'Outlook_2007', 'IceDragon', 'TheWorld_Browser', 'RockMelt', 'Avant_Browser', 'unknown']})

first_browser = st.selectbox('SELECT BROWSER', browser_df['browser'])
#first_browser = list(first_browser)

# st widget to choose user's language. Default = first value

lang_df = pd.DataFrame({'language': ['English', 'Chinese Mandarin', 'Korean', 'French', 'Espanol', 'German', 'Russian', 'Italian', 'Japanese', 'Portugese','Swedish','Dutch','Polish', 'Turkish', 'Danish','Thai', 'Chinese Simplified','Bahasa Indonesia', 'Greek', 'Norwegian', 'Finnish', 'Hungarian','IS', 'Catalan']})

lang = st.selectbox('SELECT YOUR LANGUAGE', lang_df['language'])

if lang == 'English':
    language = 'en'
if lang == 'Chinese Mandarin':
    language = 'zh'
if lang == 'Korean':
    language = 'ko'
if lang == 'French':
    language = 'fr'
if lang == 'Espanol':
    language = 'es'
if lang == 'German':
    language = 'de'
if lang == 'Russian':
    language = 'ru'
if lang == 'Italian':
    language = 'it'
if lang == 'Japanese':
    language = 'ja'
if lang == 'Portugese':
    language = 'pt'
if lang == 'Swedish':
    language = 'sv'
if lang == 'Dutch':
    language = 'nl'
if lang == 'Polish':
    language = 'pl'
if lang == 'Turkish':
    language = 'tr'
if lang == 'Danish':
    language = 'da'
if lang == 'Thai':
    language = 'th'
if lang == 'Chinese Simplified':
    language = 'cs'
if lang == 'Bahasa Indonesia':
    language = 'id'
if lang == 'Greek':
    language = 'el'
if lang == 'Norwegian':
    language = 'no'
if lang == 'Finnish':
    language = 'fi'
if lang == 'Hungarian':
    language = 'hu'
if lang == 'IS':
    language = 'is'
if lang == 'Catalan':
    language = 'ca'

#language = list(language)

# this cell fetches suer's account created day and month

account_day_df = pd.DataFrame({'day': [x for x in range(1,32)]})
account_month_df = pd.DataFrame({'month': [x for x in range(1,13)]})
account_created_day = st.selectbox('MONTH WHEN YOU HAVE CREATED THE ACCOUNT', account_day_df['day'])
account_created_month = st.selectbox('DAY WHEN YOU HAVE CREATED THE ACCOUNT', account_month_df['month'])

# this cell 'simulates' time. The time in training data denotes total time (in seconds) a user spends to book a destination.
# Since we're entering values during deployment very quickly, its impossible to get actual time range similar to those in trng dat.
# Hence I have done some maniplations so that the time-range remains same as those in training data

num = random.randint(2, 50)
end = time.time()
secs_elapsed = num*(end - start)*100000

# forming a dataframe of query point

qp_df = pd.DataFrame({'gender': gender,
                     'age': age,
                     'signup_method' : signup_method,
                     'signup_flow' : 0,
                     'language' : language,
                     'affiliate_channel': affiliate_channel,
                     'affiliate_provider' : affiliate_provider,
                     'signup_app' : signup_app,
                     'first_device_type' : first_device_type ,
                     'first_browser' : first_browser,
                     'account_created_day' : account_created_day,
                     'account_created_month': account_created_month,
                     'first_booking_day': 0,
                     'first_booking_month' : 0,
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

'*** PREDICTING THE DESTINATIONS ***'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(11):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Prediction progress : {10*i}%')
  bar.progress(10*i)
  time.sleep(0.1)

'YOU ARE ALMOST DONE!'

pred_df = pd.DataFrame({'Destination': dests,
                       'Probability (%)' : preds[0]*100})

top_5_dests = pred_df.sort_values(by=['Probability (%)'], ascending=False)[:5]
st.write("According to my Machine Learning model's prediction, here are your top 5 destinations you might be interested in:")
st.write(top_5_dests['Destination'])

# this cell is to shoe model interptratation

if st.checkbox('MODEL INTERPRETATION'):
    top_5_dests
    
st.write('THANK YOU FOR VISITING THIS SITE.... HAPPY JOURNEY...')


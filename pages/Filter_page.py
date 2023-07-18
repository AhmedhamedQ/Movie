import requests 
from bs4 import BeautifulSoup as bs
import plotly.express as px 
import streamlit as st 
import pandas as pd 
st.set_page_config(page_title = 'Movies Data' , page_icon='🎞️')

df = pd.read_csv("25k IMDb movie Dataset cleand.csv").sample(50)
df.reset_index(inplace=True)
filter_list = ['Rating','Genres','Rating and Genres' , 'Director Name, Rating and Generes and year' ,  'Director Name, Rating , Generes and Time period']
choies = st.selectbox('Select type of filter from here : ' , filter_list)
if choies == 'Rating and Generes' :
    col1 , col2 , col3 = st.columns([1,0.3 ,1])
    with col1 :
        Genres = df['Generes'].unique()
        g = st.selectbox('select Genres :' , Genres) 
    with col3 :
        Rating = st.slider('Rating',min_value=1.0 ,step= 0.1 ,max_value = 9.9)
    df2 = df[(df['Generes']==g) & (df['Rating']>=Rating)]
    st.header('____________________________________________')
    for i in range(df2.shape[0]) :
        try :
            url = df2['path'][i]+'mediaindex?ref_=tt_ov_mi_sm'
            response = requests.get(url)
            soup = bs(response.text , 'html.parser')
            img = soup.find('div', attrs={'class' : 'subpage_title_block'}).find('img' , {'class':'poster'}).get('src')
            video= 'https://www.imdb.com'+soup.find('span' , attrs={'class':"video_slate"}).find('a' , attrs={'class':"video-modal"}).get('href')
            st.subheader('Movie title : ')
            st.write(df2['movie title'][i])
            st.subheader('Movie link: ')
            st.write(df2['path'][i])
            st.subheader('overview about movie : ')
            st.write( df2['Overview'][i])
            st.subheader('Director name : ' )
            st.write(df2['Director'][i])
            st.subheader('Rating : ')
            st.write(df2['Rating'][i])
            st.subheader('Users rating count : ')
            st.write(df2['User Rating'][i])
            st.subheader('Movie Poster :')
            st.image(img , width=125)
            st.subheader('Movie trailer :')
            st.video(video+'.mp4','rb')
            st.write('You can watch trailer from this link if it dosent playing: ', video )
            st.subheader('____________________________________________')
        except :
            print('')
            
elif choies == 'Director Name, Rating and Genres and year' :
    col11 , col21 , col31 = st.columns([1,0.3 ,1])
    with col11 :
        Director = st.selectbox('Select Director name from here : ' , df['Director'].unique())
    with col31 :
        genres = st.selectbox('Select genres : ' , df[df['Director']==Director]['Generes'].unique())
    coll1 , coll2 , coll3 = st.columns([1,0.3 ,1])
    with coll1 :
        Rating = st.slider('Rating',min_value=1.0 ,step= 0.1 ,max_value = 9.9)
    with coll3 :
        Date = st.selectbox('Select year : ',df[(df['Director']==Director)&(df['Generes']==genres)]['year'].unique())
        
    df3 = df[(df['Director']==Director) & (df['Generes']==genres)][(df['Rating']>=Rating) & (df['year']==Date)]
    st.header('____________________________________________')
    for i in range(df3.shape[0]) :
        try :
            url = df3['path'][i]+'mediaindex?ref_=tt_ov_mi_sm'
            response = requests.get(url)
            soup = bs(response.text , 'html.parser')
            img = soup.find('div', attrs={'class' : 'subpage_title_block'}).find('img' , {'class':'poster'}).get('src')
            video= 'https://www.imdb.com'+soup.find('span' , attrs={'class':"video_slate"}).find('a' , attrs={'class':"video-modal"}).get('href')
            st.subheader('Movie title : ')
            st.write(df3['movie title'][i])
            st.subheader('Movie link: ')
            st.write(df3['path'][i])
            st.subheader('overview about movie : ')
            st.write( df3['Overview'][i])
            st.subheader('Director name : ' )
            st.write(df3['Director'][i])
            st.subheader('Rating : ')
            st.write(df3['Rating'][i])
            st.subheader('Users rating count : ')
            st.write(df3['User Rating'][i])
            st.subheader('Movie Poster :')
            st.image(img , width=125)
            st.subheader('Movie trailer :')
            st.video(video+'.mp4','rb')
            st.write('You can watch trailer from this link if it dosent playing: ', video )
            st.subheader('____________________________________________')
        except :
            print('')
    
elif choies ==  'Director Name, Rating , Generes and Time period' :
    col11 , col21 , col31 = st.columns([1,0.3 ,1])
    with col11 :
        Director = st.selectbox('Select Director name from here : ' , df['Director'].unique())
    with col31 :
        genres = st.selectbox('Select genres : ' , df[df['Director']==Director]['Generes'].unique())
    coll1 , coll2 , coll3 = st.columns([1,0.3 ,1])
    with coll1 :
        Rating = st.slider('Rating',min_value=1.0 ,step= 0.1 ,max_value = 9.9)
    with coll3 :
            Time_period = st.selectbox('select Time period : ', df[(df['Director']==Director)&(df['Generes']==genres)]['Time period'].unique())
        
    df4 = df[(df['Director']==Director) & (df['Generes']==genres)][(df['Rating']>=Rating) & (df['Time period']==Time_period)]
    st.header('____________________________________________')
    for i in range(df4.shape[0]) :
        try :
            url = df4['path'][i]+'mediaindex?ref_=tt_ov_mi_sm'
            response = requests.get(url)
            soup = bs(response.text , 'html.parser')
            img = soup.find('div', attrs={'class' : 'subpage_title_block'}).find('img' , {'class':'poster'}).get('src')
            video= 'https://www.imdb.com'+soup.find('span' , attrs={'class':"video_slate"}).find('a' , attrs={'class':"video-modal"}).get('href')
            st.subheader('Movie title : ')
            st.write(df4['movie title'][i])
            st.subheader('Movie link: ')
            st.write(df4['path'][i])
            st.subheader('overview about movie : ')
            st.write(df4['Overview'][i])
            st.subheader('Director name : ' )
            st.write(df4['Director'][i])
            st.subheader('Rating : ')
            st.write(df4['Rating'][i])
            st.subheader('Users rating count : ')
            st.write(df4['User Rating'][i])
            st.subheader('Movie Poster :')
            st.image(img , width=125)
            st.subheader('Movie trailer :')
            st.video(video+'.mp4','rb')
            st.write('You can watch trailer from this link if it dosent playing: ', video )
            st.subheader('____________________________________________')
        except :
            print('')
elif choies == 'Rating' :
    Rating = st.slider('Rating',min_value=1.0 ,step= 0.1 ,max_value = 9.9)
    df5 = df[df['Rating']>=Rating]
    st.header('____________________________________________')
    for i in range(df5.shape[0]) :
        try :
            url = df5['path'][i]+'mediaindex?ref_=tt_ov_mi_sm'
            response = requests.get(url)
            soup = bs(response.text , 'html.parser')
            img = soup.find('div', attrs={'class' : 'subpage_title_block'}).find('img' , {'class':'poster'}).get('src')
            video= 'https://www.imdb.com'+soup.find('span' , attrs={'class':"video_slate"}).find('a' , attrs={'class':"video-modal"}).get('href')
            st.subheader('Movie title : ')
            st.write(df5['movie title'][i])
            st.subheader('Movie link: ')
            st.write(df5['path'][i])
            st.subheader('overview about movie : ')
            st.write( df5['Overview'][i])
            st.subheader('Director name : ' )
            st.write(df5['Director'][i])
            st.subheader('Rating : ')
            st.write(df5['Rating'][i])
            st.subheader('Users rating count : ')
            st.write(df5['User Rating'][i])
            st.subheader('Movie Poster :')
            st.image(img , width=125)
            st.subheader('Movie trailer :')
            st.video(video+'.mp4','rb')
            st.write('You can watch trailer from this link if it dosent playing: ', video )
            st.subheader('____________________________________________')
        except :
            print('')
else :
    Genres = df['Generes'].unique()
    g = st.selectbox('select Genres :' , Genres) 
    df5 = df[df['Generes']>=g]
    st.header('____________________________________________')
    for i in range(df5.shape[0]) :
        try :
            url = df5['path'][i]+'mediaindex?ref_=tt_ov_mi_sm'
            response = requests.get(url)
            soup = bs(response.text , 'html.parser')
            img = soup.find('div', attrs={'class' : 'subpage_title_block'}).find('img' , {'class':'poster'}).get('src')
            video= 'https://www.imdb.com'+soup.find('span' , attrs={'class':"video_slate"}).find('a' , attrs={'class':"video-modal"}).get('href')
            st.subheader('Movie title : ')
            st.write(df5['movie title'][i])
            st.subheader('Movie link: ')
            st.write(df5['path'][i])
            st.subheader('overview about movie : ')
            st.write( df5['Overview'][i])
            st.subheader('Director name : ' )
            st.write(df5['Director'][i])
            st.subheader('Rating : ')
            st.write(df5['Rating'][i])
            st.subheader('Users rating count : ')
            st.write(df5['User Rating'][i])
            st.subheader('Movie Poster :')
            st.image(img , width=125)
            st.subheader('Movie trailer :')
            st.video(video+'.mp4','rb')
            st.write('You can watch trailer from this link if it dosent playing: ', video )
            st.subheader('____________________________________________')
        except :
            print('')

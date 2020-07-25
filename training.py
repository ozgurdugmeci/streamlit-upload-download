import pandas as pd
import streamlit as st
from random import randint
import base64
from io import BytesIO
from datetime import datetime
from PIL import Image

def downloadStoklar():
 namo= str(datetime.now())
 namo=namo.replace(' ','')
 namo=namo.replace('-','')
 namo=namo.replace(':','')
 namo=namo.replace('.','')
 b=randint(10,99)
 namo= 'Stoklar_'+namo+'-'+str(b) +'.csv'
 #liste= {}
 #df_download_stoklar= pd.DataFrame.from_dict(liste)
 #df_download_stoklar= pd.DataFrame(liste)

 return df_download_stoklar, namo

def downloadSatslarY():
 namo= str(datetime.now())
 namo=namo.replace(' ','')
 namo=namo.replace('-','')
 namo=namo.replace(':','')
 namo=namo.replace('.','')
 b=randint(10,99)
 namo= 'Satslar20_'+namo+'-'+str(b) +'.csv'
 #liste= {}
 #df_download_stoklar= pd.DataFrame.from_dict(liste)
 #df_download_stoklar= pd.DataFrame(liste)

 return df_download_stoklar, namo

def downloadSatslarK():
 namo= str(datetime.now())
 namo=namo.replace(' ','')
 namo=namo.replace('-','')
 namo=namo.replace(':','')
 namo=namo.replace('.','')
 b=randint(10,99)
 namo= 'Satslar40_'+namo+'-'+str(b) +'.csv'
 #liste= {}
 #df_download_stoklar= pd.DataFrame.from_dict(liste)
 #df_download_stoklar= pd.DataFrame(liste)
 return df_download_stoklar, namo


def downloadSatslarA():
 namo= str(datetime.now())
 namo=namo.replace(' ','')
 namo=namo.replace('-','')
 namo=namo.replace(':','')
 namo=namo.replace('.','')
 b=randint(10,99)
 namo= 'Satslar60_'+namo+'-'+str(b) +'.csv'
 #liste= {}
 #df_download_stoklar= pd.DataFrame.from_dict(liste)
 #df_download_stoklar= pd.DataFrame(liste)
 return df_download_stoklar, namo

def downloadSatslarS():
 namo= str(datetime.now())
 namo=namo.replace(' ','')
 namo=namo.replace('-','')
 namo=namo.replace(':','')
 namo=namo.replace('.','')
 b=randint(10,99)
 namo= 'Satslar80_'+namo+'-'+str(b) +'.csv'
 #liste= {}
 #df_download_stoklar= pd.DataFrame.from_dict(liste)
 #df_download_stoklar= pd.DataFrame(liste)
 return df_download_stoklar, namo



st.sidebar.title('İçerik')
yan_sayfa_secenek = st.sidebar.radio(
    '',
    ('Sayfa1', 'Verileri Hazırlama', 'Sayfa3')
)

# SAYFA1--------------------- 
# SAYFA1--------------------- 
if yan_sayfa_secenek == 'Sayfa1' :
 st.title("ANALİZE BAŞLA")
 st.set_option('deprecation.showfileUploaderEncoding', False)
 uploaded_file = st.file_uploader("Dosya Seç", type=['csv'],encoding='ISO-8859-1')
 
 
 if uploaded_file:
  df = pd.read_csv(uploaded_file, delimiter= ';')
  st.dataframe(df)
  
  df['Stok Yeterlilik']= df[df.columns[1]]*2
  st.title('Analiz Sonucu')
  df['Stok Yeterlilik']
  
elif yan_sayfa_secenek == 'Verileri Hazırlama' :
 #STOKLAR
 st.title('1- Stok Yükleme')
 #df_download_stoklar = downloadStoklar()[0]
 df_download_stoklar= pd.read_csv('C:\\Users\\ozgur.dugmeci\\AppData\\Local\\Programs\\Python\\csv\\sablon_stok.csv',encoding='ISO-8859-1')
 namo= downloadStoklar()[1]

 csv = df_download_stoklar.to_csv(index=False,encoding='ISO-8859-1')
 
 b64 = base64.b64encode(csv.encode(encoding='ISO-8859-1')).decode(encoding='ISO-8859-1')  # some strings
 linko= f'<a href="data:file/csv;base64,{b64}" download={namo}>Stoklar CSV dosyasını indir</a>'
  
 'Stokları yüklemek için boş "Stoklar_.CSV" dosyasını aşağıdaki linkten indirin.'
 st.markdown(linko, unsafe_allow_html=True)  
 #image = Image.open('C:\\Users\\ozgur.dugmeci\\AppData\\Local\\Programs\\Python\\media\\stok_resim.jpg')
 #st.image(image, caption= 'Stok Verisi', width=300)
 'Resimde görüldüğü gibi sıfırdan büyük Urun_No ve Stok Adet bilgilerini indirilen dosyaya kopyalayıp yapıştırın.'
 warning= f'<p style="color:red;">Kopyalayıp yapıştırdığınız veride Türkçe karakter kullanmayın ve dosyayı kaydedin.</p>'
 st.markdown(warning, unsafe_allow_html=True)  
 
 #20 GUNLUK SATISLAR 
 st.title('2- 20 günlük Satışları Yükleme')
 df_download_satslar20 = downloadSatslarY()[0]
 df_download_satslar20= pd.read_csv('C:\\Users\\ozgur.dugmeci\\AppData\\Local\\Programs\\Python\\csv\\sablon_sats_20.csv',encoding='ISO-8859-1')
 namo2= downloadSatslarY()[1]
 csv2 = df_download_satslar20.to_csv(index=False)
 b64 = base64.b64encode(csv2.encode(encoding='ISO-8859-1')).decode(encoding='ISO-8859-1')  # some strings
 linko2= f'<a href="data:file/csv;base64,{b64}" download={namo2}>Satslar20 CSV dosyasını indir</a>'
  
 '20 günlük satışları yüklemek için boş "Satslar20_.CSV" dosyasını aşağıdaki linkten indirin.'
 st.markdown(linko2, unsafe_allow_html=True)  
 image2 = Image.open('C:\\Users\\ozgur.dugmeci\\AppData\\Local\\Programs\\Python\\media\\sats20_resim.jpg')
 st.image(image2, caption= '20 Günlük Satış Verisi', width=300)
 'Resimde görüldüğü gibi sıfırdan buyuk Urun_No ve Sats_20 (20 günlük satış) bilgilerini indirilen dosyaya kopyalayıp yapıştırın.'
 
 warning= f'<p style="color:red;">Kopyalayıp yapıştırdığınız veride Türkçe karakter kullanmayın ve dosyayı kaydedin</p>'
 st.markdown(warning, unsafe_allow_html=True)  
  
 #40 GUNLUK SATISLAR 
 st.title('3- 40 günlük Satışları Yükleme')
 #df_download_satslar40 = downloadSatslarK()[0]
 df_download_satslar40= pd.read_csv('C:\\Users\\ozgur.dugmeci\\AppData\\Local\\Programs\\Python\\csv\\sablon_sats_40.csv',encoding='ISO-8859-1')
 namo3= downloadSatslarK()[1]
 csv3 = df_download_satslar40.to_csv(index=False)
 b64 = base64.b64encode(csv3.encode(encoding='ISO-8859-1')).decode(encoding='ISO-8859-1')  # some strings
 linko3= f'<a href="data:file/csv;base64,{b64}" download={namo3}>Satslar40 CSV dosyasını indir</a>'
  
 '40 günlük satışları yüklemek için boş "Satslar40_.CSV" dosyasını aşağıdaki linkten indirin.'
 st.markdown(linko3, unsafe_allow_html=True)  
 image3 = Image.open('C:\\Users\\ozgur.dugmeci\\AppData\\Local\\Programs\\Python\\media\\sats40_resim.jpg')
 st.image(image3, caption= '40 Günlük Satış Verisi', width=300)
 'Resimde görüldüğü gibi sıfırdan buyuk Urun_No ve Sats_40 (40 günlük satış) bilgilerini indirilen dosyaya kopyalayıp yapıştırın.'
 warning= f'<p style="color:red;">Kopyalayıp yapıştırdığınız veride Türkçe karakter kullanmayın ve dosyayı kaydedin</p>'
 st.markdown(warning, unsafe_allow_html=True)

 #60 GUNLUK SATISLAR 
 st.title('4- 60 günlük Satışları Yükleme')
 #df_download_satslar40 = downloadSatslarK()[0]
 df_download_satslar60= pd.read_csv('C:\\Users\\ozgur.dugmeci\\AppData\\Local\\Programs\\Python\\csv\\sablon_sats_60.csv',encoding='ISO-8859-1')
 namo4= downloadSatslarA()[1]
 csv4 = df_download_satslar60.to_csv(index=False)
 b64 = base64.b64encode(csv4.encode(encoding='ISO-8859-1')).decode(encoding='ISO-8859-1')  # some strings
 linko4= f'<a href="data:file/csv;base64,{b64}" download={namo4}>Satslar60 CSV dosyasını indir</a>'
  
 '60 günlük satışları yüklemek için boş "Satslar60_.CSV" dosyasını aşağıdaki linkten indirin.'
 st.markdown(linko4, unsafe_allow_html=True)  
 image4 = Image.open('C:\\Users\\ozgur.dugmeci\\AppData\\Local\\Programs\\Python\\media\\sats60_resim.jpg')
 st.image(image4, caption= '60 Günlük Satış Verisi', width=300)
 'Resimde görüldüğü gibi sıfırdan buyuk Urun_No ve Sats_60 (60 günlük satış) bilgilerini indirilen dosyaya kopyalayıp yapıştırın.'
 warning= f'<p style="color:red;">Kopyalayıp yapıştırdığınız veride Türkçe karakter kullanmayın ve dosyayı kaydedin</p>'
 st.markdown(warning, unsafe_allow_html=True)
 
 #80 GUNLUK SATISLAR 
 st.title('5- 80 günlük Satışları Yükleme')
 #df_download_satslar40 = downloadSatslarK()[0]
 df_download_satslar80= pd.read_csv('C:\\Users\\ozgur.dugmeci\\AppData\\Local\\Programs\\Python\\csv\\sablon_sats_80.csv',encoding='ISO-8859-1')
 namo5= downloadSatslarS()[1]
 csv5 = df_download_satslar80.to_csv(index=False)
 b64 = base64.b64encode(csv5.encode(encoding='ISO-8859-1')).decode(encoding='ISO-8859-1')  # some strings
 linko5= f'<a href="data:file/csv;base64,{b64}" download={namo5}>Satslar80 CSV dosyasını indir</a>'
  
 '80 günlük satışları yüklemek için boş "Satslar80_.CSV" dosyasını aşağıdaki linkten indirin.'
 st.markdown(linko5, unsafe_allow_html=True)  
 image5 = Image.open('C:\\Users\\ozgur.dugmeci\\AppData\\Local\\Programs\\Python\\media\\sats80_resim.jpg')
 st.image(image5, caption= '80 Günlük Satış Verisi', width=300)
 'Resimde görüldüğü gibi sıfırdan buyuk Urun_No ve Sats_80 (80 günlük satış) bilgilerini indirilen dosyaya kopyalayıp yapıştırın.'
 warning= f'<p style="color:red;">Kopyalayıp yapıştırdığınız veride Türkçe karakter kullanmayın ve dosyayı kaydedin</p>'
 st.markdown(warning, unsafe_allow_html=True)

  
 
 
 
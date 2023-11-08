import streamlit as st
import pandas as pd
from PIL import Image

def run():
    st.title('Healthcare Stroke Data Exploratory')
    # Memanggil data csv
    data = pd.read_csv('healthcare-dataset-stroke-data.csv')
    st.dataframe(data)

    # Menampilkan 5 data teratas
    st.caption('Data Head')
    st.table(data.head(5))
    # Menampilkan 5 data terbawah
    st.caption('Data Tail')
    st.table(data.tail(5))

    # Menampilkan visualisasi 1
    st.title('Bagaimana distribusi status stroke?')
    image = Image.open('image1.jpg')
    st.image(image, caption='Figure 1')

    # Menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Berdasarkan pie chart di atas, dapat dilihat distribusi kasus stroke dalam dataset yang secara efektif mengkategorikan menjadi kategori "Stroke" dan "Tidak Stroke". Terdapat ketidakseimbangan kelas dalam dataset, dengan jumlah orang yang tidak stroke lebih besar dibandingkan orang yang stroke. Total orang yang tidak stroke adalah sebesar 4861 sedangkan orang yang mengalami stroke sebanyak 249. Namun, diagram ini secara utama hanya menggambarkan distribusi kasus stroke dan mungkin tidak memberikan wawasan yang lebih dalam tentang faktor-faktor lainnya.')

    # Menampilkan visualisasi 2
    st.title('Apakah usia pasien berhubungan dengan risiko stroke?')
    image = Image.open('image2.jpg')
    st.image(image, caption='Figure 2')

    # Menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Berdasarkan visualisasi di atas, dapat dilihat bahwa risiko stroke cenderung meningkat seiring bertambahnya usia, dimana kasus stroke yang lebih banyak terjadi pada populasi lansia.')

    # Menampilkan visualisasi 3
    st.title('Apakah ada hubungan antara BMI dengan kemungkinan terkena stroke?')
    image = Image.open('image3.jpg')
    st.image(image, caption='Figure 3')

    # Menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Berdasarkan visualisasi di atas, dapat dilihat bahwa tidak ada korelasi yang signifikan antara BMI dan terjadinya stroke. Jika BMI memiliki hubungan dengan terjadinya stroke maka seharusnya orang-orang yang Extreme Obesity akan lebih mudah terkena stroke, nyatanya dalam visualiasi di atas tidak begitu. Jadi stroke dapat terjadi di berbagai nilai BMI.')

    # Menampilkan visualisasi 4
    st.title('Bagaimana distribusi status merokok?')
    image = Image.open('image4.jpg')
    st.image(image, caption='Figure 4')

    # Menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Berdasarkan visualisasi di atas, kita dapat melihat bahwa sebagian besar individu termasuk dalam kategori "tidak pernah merokok," diikuti oleh "pernah merokok" dan "merokok."')

    # Menampilkan visualisasi 5
    st.title('Bagaimana perbedaan rata-rata kadar gula darah (glucose) antara individu yang stroke dan yang tidak?')
    image = Image.open('image5.png')
    st.image(image, caption='Figure 5')

    # Menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Berdasarkan visualiasi di atas, kita dapat melihat bahwa individu yang memiliki diabetes cenderung memiliki risiko stroke tertinggi, sementara individu dengan rata-rata kadar gula darah rendah memiliki risiko paling rendah.')

if __name__ == '__main__':
    run()
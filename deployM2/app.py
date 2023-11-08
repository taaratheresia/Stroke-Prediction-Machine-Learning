import streamlit as st
import eda
import prediction
import imblearn

page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Predict Stroke'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    st.write('Milestone 2')
    st.write('Nama      : Taara Mona Theresia')
    st.write('Batch     : 008')
    st.write('Tujuan Milestone    : Program ini dibuat untuk memprediksi kemungkinan seorang pasien terkena stroke berdasarkan parameter input seperti jenis kelamin, usia, berbagai penyakit, dan status merokok.')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('Stroke adalah kondisi medis serius yang dapat menimbulkan konsekuensi yang mengubah hidup dan diakui sebagai salah satu penyebab utama kematian secara global. Menurut data terbaru dari Organisasi Kesehatan Dunia (WHO), stroke masih menjadi penyebab kematian nomor dua di dunia, menyumbang sekitar 11% dari total kematian.')

    with st.expander("Problem Statement"):
            st.caption('Dalam analisis ini, kami mengeksplorasi faktor-faktor yang mempengaruhi kejadian stroke dan menggunakan teknik pembelajaran mesin untuk memprediksi risiko stroke. Dataset ini digunakan untuk memprediksi kemungkinan seorang pasien terkena stroke berdasarkan parameter input seperti jenis kelamin, usia, berbagai penyakit, dan status merokok. Setiap baris dalam data memberikan informasi yang relevan tentang pasien. Prediksi dini dan identifikasi potensi kasus stroke sangat penting untuk intervensi medis yang tepat waktu dan hasil kesehatan yang lebih baik. Proses ini bertujuan untuk berkontribusi pada pemahaman yang lebih baik tentang risiko dan pencegahan stroke.')

    with st.expander("Kesimpulan"):
        st.caption('Saran untuk Mengurangi Resiko Stroke')
        st.caption('1. Pertahankan Pola Makan Sehat: ')
        st.caption('Mengonsumsi makanan seimbang yang kaya akan buah-buahan, sayuran, biji-bijian, protein tanpa lemak, dan lemak sehat dapat membantu mengontrol berat badan dan mengurangi risiko stroke.')
        st.caption('2. Aktivitas Fisik Secara Teratur:')
        st.caption('Melakukan olahraga teratur, seperti jalan cepat, berenang, atau bersepeda, dapat meningkatkan kesehatan jantung dan mengurangi risiko stroke.')
        st.caption('3. Pantau Tekanan Darah:')
        st.caption('Tekanan darah tinggi merupakan faktor risiko utama terjadinya stroke. Periksa tekanan darah Anda secara teratur dan ikuti saran medis untuk mengelola hipertensi.')
        st.caption('4. Kelola Kadar Kolesterol:')
        st.caption('Kadar kolesterol tinggi dapat menyebabkan penumpukan plak di arteri, sehingga meningkatkan risiko stroke. Konsultasikan dengan penyedia layanan kesehatan untuk manajemen kolesterol.')
        st.caption('5. Berhenti Merokok:')
        st.caption('Merokok merusak pembuluh darah dan meningkatkan risiko penggumpalan darah. Berhenti merokok adalah salah satu cara paling efektif untuk mengurangi risiko stroke.')
        st.caption('6. Batasi Konsumsi Alkohol:')
        st.caption('Asupan alkohol berlebihan dapat meningkatkan tekanan darah dan berkontribusi terhadap risiko stroke. Konsumsi alkohol secukupnya atau sesuai anjuran profesional kesehatan.')
        st.caption('7. Mengontrol Diabetes:')
        st.caption('Jika Anda menderita diabetes, tangani dengan hati-hati melalui pengobatan, pola makan, dan pemantauan rutin untuk mencegah komplikasi yang meningkatkan risiko stroke.')
        st.caption('8. Pertahankan Berat Badan yang Sehat:')
        st.caption('Obesitas dikaitkan dengan risiko stroke yang lebih tinggi. Mencapai dan mempertahankan berat badan yang sehat dapat mengurangi risiko ini.')
        st.caption('9. Tetap Terhidrasi:')
        st.caption('Hidrasi yang tepat penting untuk kesehatan secara keseluruhan, termasuk kesehatan jantung. Minumlah air dalam jumlah yang cukup setiap hari.')
        st.caption('10. Kelola Stres:')
        st.caption('Stres kronis dapat berkontribusi terhadap tekanan darah tinggi dan faktor risiko stroke lainnya. Latih teknik pengurangan stres seperti meditasi atau yoga.')
        st.caption('\nIngat:')
        st.caption('Mengurangi risiko stroke melibatkan pemilihan gaya hidup sehat dan mencari bimbingan medis bila diperlukan. Konsultasikan dengan profesional kesehatan untuk mendapatkan rekomendasi yang dipersonalisasi.')


elif page == 'Exploration Data Analysis':
    eda.run()
else:
     prediction .run()
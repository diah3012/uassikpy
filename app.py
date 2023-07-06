import streamlit as st

st.snow()

def main():
    st.title("~~BIOGRAPHY~~")
if st.button("~~BIOGRAPHY~~"):
    st.write('this is my biography')
    st.image("foto.PNG")
    st.header("**DIAH RAHMA PERTIWI**")
    st.write("SEMARANG,30-12-2002")
    st.subheader("Programmer Kesehatan")
    
    st.write("_Saya adalah seorang programmer yang memiliki minat dalam pengembangan web dan data science dalam bidang kesehatan.Saat ini programmer dalam bidang kesehatan masih jarang dan sangat dibutuhkan di Indonesia.Sebagai seorang programer, Saya telah terlibat dalam pengembangan aplikasi dan sistem yang mengoptimalkan layanan kesehatan. saya juga berkontribusi dalam pengembangan aplikasi mobile yang memungkinkan pasien untuk memantau kondisi kesehatan mereka, memperoleh informasi medis yang relevan, dan menghubungkan dengan tenaga medis secara virtual_")
    
    st.subheader("Pendidikan")
    st.write("- Sarjana Manajemen Informasi Kesehatan, Universitas Nasional Karangturi")
    
    st.subheader("Pengalaman Kerja")
    st.write("- Saya pernah  magang di Pt.healthcare disitu saya Terlibat dalam pengembangan aplikasi web untuk manajemen dan analisis data klinis.Membantu dalam implementasi kecerdasan buatan untuk mendukung pengambilan keputusan klinis.Berkontribusi dalam pengujian dan pemeliharaan sistem aplikasi yang ada.")
    
else:
    st.write('click button')
    
if __name__ == "__main__":
    main()

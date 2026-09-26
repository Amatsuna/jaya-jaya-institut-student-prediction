# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan tinggi yang berdiri sejak tahun 2000 dan telah menghasilkan banyak lulusan. Namun, institusi juga menghadapi permasalahan berupa mahasiswa yang tidak menyelesaikan pendidikannya atau mengalami dropout. Kondisi tersebut menjadi perhatian karena dapat memengaruhi keberhasilan mahasiswa dalam menyelesaikan pendidikan.

Untuk membantu menangani permasalahan tersebut, data karakteristik mahasiswa serta performa akademik dapat digunakan untuk memahami pola yang berkaitan dengan status mahasiswa. Proyek ini berfokus pada analisis data mahasiswa dan pembangunan model machine learning yang dapat membantu memprediksi status mahasiswa berdasarkan data yang tersedia.

Dengan adanya prediksi tersebut, institusi dapat memperoleh informasi pendukung untuk mengidentifikasi mahasiswa yang memiliki kemungkinan mengalami dropout sehingga dapat menjadi bahan pertimbangan dalam pemberian bimbingan atau pendampingan lebih awal.

### Permasalahan Bisnis

Jaya Jaya Institut menghadapi permasalahan mahasiswa yang tidak menyelesaikan pendidikan atau mengalami dropout. Kondisi ini menjadi perhatian bagi institusi karena mahasiswa yang tidak menyelesaikan pendidikan dapat memengaruhi tingkat keberhasilan penyelesaian studi dan capaian institusi dalam menghasilkan lulusan.

Permasalahan tersebut juga menjadi lebih sulit ditangani apabila mahasiswa yang berisiko mengalami dropout baru diketahui setelah mengalami penurunan performa akademik yang cukup jauh atau sudah tidak melanjutkan pendidikan. Tanpa adanya informasi yang dapat membantu mengidentifikasi mahasiswa yang berpotensi mengalami dropout sejak lebih awal, institusi akan lebih sulit menentukan mahasiswa yang membutuhkan perhatian dan pendampingan.

Jika kondisi tersebut terus berlangsung tanpa adanya upaya identifikasi dan pendampingan yang lebih awal, jumlah mahasiswa yang tidak menyelesaikan pendidikan dapat terus bertambah. Hal ini dapat berdampak pada tingkat penyelesaian studi serta efektivitas institusi dalam memberikan dukungan kepada mahasiswa.


### Cakupan Proyek

Cakupan proyek meliputi:

1. Mengambil dataset students' performance dari sumber dataset yang telah disediakan oleh Dicoding.
2. Melakukan data understanding untuk memahami struktur, tipe data, distribusi nilai, unique values, missing values, dan duplikasi data.
3. Melakukan data preparation, termasuk menentukan fitur dan target, memilih fitur yang tersedia untuk deteksi lebih awal, membagi data menjadi training dan testing, serta melakukan preprocessing data.
4. Melakukan Exploratory Data Analysis (EDA) untuk memahami distribusi data dan hubungan beberapa variabel dengan status mahasiswa.
5. Membangun dan membandingkan tiga model klasifikasi:
   - Logistic Regression
   - Decision Tree
   - Random Forest
6. Mengevaluasi performa model menggunakan Accuracy, Precision, Recall, F1-Score, Macro F1-Score, Confusion Matrix, dan Classification Report.
7. Menentukan model final berdasarkan hasil evaluasi pada data pengujian.
8. Menyimpan model final dalam format `.pkl`.
9. Membuat script `prediction.py` untuk melakukan prediksi terhadap data mahasiswa baru menggunakan model yang telah disimpan.
10. Membuat sistem machine learning menggunakan Streamlit untuk menyediakan antarmuka prediksi status mahasiswa.
11. Menyediakan `requirements.txt` agar environment proyek dapat dipersiapkan kembali.
12. Membuat dashboard visualisasi menggunakan Google Looker Studio untuk menampilkan distribusi status mahasiswa serta pola karakteristik dan performa akademik berdasarkan status mahasiswa.

### Batasan Proyek

Batasan dalam proyek ini meliputi:

1. Analisis menggunakan dataset `students' performance` yang disediakan oleh Dicoding.
2. Model menggunakan 30 fitur yang berasal dari informasi karakteristik mahasiswa dan performa akademik semester pertama.
3. Fitur yang berkaitan dengan performa semester kedua tidak digunakan sebagai input model karena proyek diarahkan untuk mendukung identifikasi mahasiswa lebih awal.
4. Exploratory Data Analysis (EDA) digunakan untuk melihat pola dan karakteristik data secara deskriptif dan tidak digunakan untuk menyimpulkan hubungan sebab-akibat.
5. Model menghasilkan tiga kategori status mahasiswa, yaitu `Dropout`, `Enrolled`, dan `Graduate`.
6. Hasil prediksi model merupakan informasi pendukung untuk proses identifikasi awal dan tidak digunakan sebagai satu-satunya dasar dalam menentukan tindakan terhadap mahasiswa.

### Output Proyek

Output yang dihasilkan dari proyek ini meliputi:

1. Notebook analisis data yang berisi proses Data Understanding, Data Preparation, Exploratory Data Analysis (EDA), Modeling, dan Evaluation.
2. Model machine learning final dalam file `model_dropout.pkl`.
3. Script `prediction.py` untuk melakukan prediksi status mahasiswa berdasarkan data mahasiswa yang dimasukkan.
4. Dashboard visualisasi menggunakan Google Looker Studio untuk menampilkan distribusi status mahasiswa serta pola karakteristik dan performa akademik.
5. Aplikasi machine learning menggunakan Streamlit untuk melakukan prediksi status mahasiswa secara interaktif.
6. File `requirements.txt` yang berisi dependency yang diperlukan untuk menjalankan proyek.

### Persiapan
1. Sumber dataset

https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance
Dataset students' performance yang digunakan dalam proyek ini berasal dari repository dataset Dicoding.

2. Struktur File

Proyek Menyelesaikan Permasalahan Jaya Jaya Institut/
├── notebook.ipynb
├── prediction.py
├── app.py
├── model_dropout.pkl
├── requirements.txt
└── README.md
└── ulum_al_hikam-dashboard.png

3. Library yang digunakan:

pandas==3.0.6
numpy==2.5.3
matplotlib==3.11.2
seaborn==0.13.2
scikit-learn==1.9.1
scipy==1.18.1
joblib==1.6.0
streamlit==1.64.0

4. Setup Environment - Anaconda

Pastikan Anaconda sudah terpasang pada komputer. Kemudian buka Anaconda Prompt dan jalankan perintah berikut untuk membuat environment baru:
conda create --name main-ds python=3.9
conda activate main-ds

Setelah environment berhasil dibuat dan diaktifkan, instal seluruh dependency proyek menggunakan:
pip install -r requirements.txt

5. Setup Environment - Shell/Termina:

Instal Pipenv dengan perintah:
pip install pipenv

Kemudian jalankan perintah berikut:
pipenv install
pipenv shell

Setelah environment aktif, instal seluruh dependency proyek menggunakan:
pip install -r requirements.txt

6. Menjalankan Prediction Script

Setelah seluruh dependency terpasang dan file model_dropout.pkl tersedia, prediction script dapat dijalankan menggunakan:
python prediction.py

Script tersebut akan menerima data mahasiswa contoh dan menampilkan hasil prediksi status mahasiswa beserta probabilitas untuk setiap kelas.


## Business Dashboard 
Business Dashboard pada proyek ini dibuat menggunakan Google Looker Studio untuk menampilkan analisis karakteristik mahasiswa dan status akademik.
Link dashboard: https://datastudio.google.com/reporting/63177695-9c15-41cb-82ee-8e6f0c11d800

## Menjalankan Sistem Aplikasi Streamlit Machine Learning

Setelah seluruh dependency terpasang dan file model_dropout.pkl tersedia, dashboard dapat dijalankan menggunakan perintah:
python -m streamlit run app.py

Setelah perintah dijalankan, Streamlit akan menjalankan aplikasi dan memberikan alamat lokal untuk mengakses aplikasi melalui browser.
aplikasi digunakan untuk memasukkan karakteristik mahasiswa dan performa akademik semester pertama, kemudian menampilkan hasil prediksi status mahasiswa berupa:
- Dropout
- Enrolled
- Graduate
aplikasi juga menampilkan probabilitas dari masing-masing status berdasarkan hasil prediksi model.

Link Streamlit : https://jaya-jaya-institut-student-prediction-bucwrhu6qceducserup3mq.streamlit.app/

## Conclusion

Berdasarkan hasil Data Understanding dan Exploratory Data Analysis (EDA), dataset students' performance yang digunakan dalam proyek ini terdiri dari 4.424 data mahasiswa dengan 37 kolom. Dataset memiliki tiga kategori pada target `Status`, yaitu `Dropout`, `Enrolled`, dan `Graduate`. Berdasarkan distribusi target, terdapat 2.209 mahasiswa berstatus Graduate, 1.421 mahasiswa berstatus Dropout, dan 794 mahasiswa berstatus Enrolled.

Pada tahap Data Preparation, digunakan 30 fitur yang terdiri dari karakteristik mahasiswa, informasi penerimaan, kondisi sosial dan finansial, serta performa akademik semester pertama. Fitur yang berkaitan dengan semester kedua tidak digunakan karena proyek ini diarahkan untuk melakukan prediksi berdasarkan informasi yang tersedia lebih awal.

Hasil Exploratory Data Analysis menunjukkan adanya perbedaan pola pada beberapa karakteristik mahasiswa berdasarkan statusnya. Perbedaan tersebut dapat diamati melalui variabel karakteristik mahasiswa, kondisi finansial, serta performa akademik semester pertama. Beberapa variabel akademik semester pertama juga menunjukkan pola yang berbeda berdasarkan status mahasiswa. Hasil EDA bersifat deskriptif sehingga pola yang ditemukan tidak dapat digunakan untuk menyimpulkan hubungan sebab-akibat.

Untuk membangun model prediksi, tiga algoritma klasifikasi dibandingkan, yaitu Logistic Regression, Decision Tree, dan Random Forest. Evaluasi dilakukan menggunakan Accuracy, Precision, Recall, F1-Score, dan Macro F1-Score pada data pengujian.

Hasil evaluasi adalah sebagai berikut:

| Model | Accuracy | Precision | Recall | F1-Score | Macro F1-Score |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.7401 | 0.7202 | 0.7401 | 0.7252 | 0.6514 |
| Decision Tree | 0.6576 | 0.6641 | 0.6576 | 0.6607 | 0.5966 |
| Random Forest | 0.7141 | 0.6790 | 0.7141 | 0.6837 | 0.5938 |

Berdasarkan hasil pengujian pada dataset ini, Logistic Regression memperoleh nilai Accuracy, Precision, Recall, F1-Score, dan Macro F1-Score yang lebih tinggi dibandingkan Decision Tree dan Random Forest. Oleh karena itu, Logistic Regression digunakan sebagai model final dalam proyek ini.

Model Logistic Regression memperoleh Accuracy sebesar 74,01% dengan F1-Score weighted sebesar 72,52%. Pada evaluasi per kelas, model memiliki performa yang berbeda untuk setiap status. Untuk kelas `Graduate`, model memperoleh recall sebesar 89%, sedangkan untuk kelas `Dropout` memperoleh recall sebesar 75%. Sementara itu, kelas `Enrolled` memiliki recall sebesar 30%, sehingga model masih memiliki keterbatasan dalam mengidentifikasi mahasiswa yang termasuk dalam kategori tersebut.

Confusion Matrix menunjukkan bahwa model mampu mengidentifikasi sebagian besar mahasiswa pada kelas `Graduate` dan `Dropout`, tetapi masih terdapat kesalahan prediksi terutama pada kelas `Enrolled`. Hal ini menunjukkan bahwa distribusi kelas yang tidak seimbang serta karakteristik antarstatus yang dapat memiliki kemiripan masih menjadi tantangan dalam proses klasifikasi.

Dengan demikian, model yang dibangun dapat digunakan sebagai prototype untuk membantu memberikan informasi pendukung mengenai status mahasiswa berdasarkan karakteristik dan performa akademik semester pertama. Hasil prediksi sebaiknya digunakan sebagai salah satu bahan pertimbangan dalam proses identifikasi mahasiswa yang membutuhkan perhatian lebih lanjut dan tidak digunakan sebagai satu-satunya dasar dalam menentukan tindakan terhadap mahasiswa.

### Rekomendasi Action Items (Optional)

Berdasarkan hasil Exploratory Data Analysis dan evaluasi model, beberapa action items yang dapat diterapkan oleh Jaya Jaya Institut adalah:

1. **Memprioritaskan mahasiswa dengan performa akademik semester pertama yang rendah.**  
   Hasil analisis menunjukkan bahwa mahasiswa berstatus `Dropout` memiliki rata-rata nilai semester pertama sekitar 7,2 dan rata-rata unit yang disetujui sekitar 2,6. Sebagai tahap awal screening, mahasiswa dengan nilai semester pertama di bawah 8 atau jumlah unit yang disetujui maksimal 3 dapat dimasukkan ke dalam daftar mahasiswa yang perlu mendapatkan perhatian lebih lanjut. Batas tersebut digunakan sebagai indikator screening awal berdasarkan pola pada dataset dan bukan sebagai batas risiko yang bersifat mutlak.
   
2. **Menggabungkan beberapa indikator akademik dalam proses identifikasi.**  
   Institusi dapat memberikan prioritas lebih tinggi pada mahasiswa yang menunjukkan kombinasi performa akademik yang rendah, misalnya nilai semester pertama di bawah 8 dan jumlah unit yang disetujui maksimal 3. Penggunaan beberapa indikator secara bersamaan dapat membantu memberikan gambaran yang lebih lengkap dibandingkan hanya menggunakan satu indikator.

3. **Menggunakan hasil prediksi Logistic Regression sebagai informasi pendukung untuk screening awal.**  
   Model final memiliki recall sebesar 75% pada kelas `Dropout`, sehingga model dapat digunakan untuk membantu menyaring mahasiswa yang perlu diperhatikan lebih lanjut. Mahasiswa yang diprediksi `Dropout` dapat dimasukkan ke dalam daftar screening untuk kemudian ditinjau oleh pihak akademik.

4. **Melakukan verifikasi oleh pihak akademik sebelum memberikan tindak lanjut.**  
   Hasil prediksi dan indikator akademik tidak digunakan sebagai satu-satunya dasar dalam menentukan tindakan terhadap mahasiswa. Pihak akademik dapat meninjau kembali kondisi mahasiswa, seperti perkembangan akademik dan kebutuhan pendampingan, sebelum menentukan bentuk tindak lanjut yang sesuai.

5. **Melakukan pemantauan secara berkala terhadap mahasiswa yang masuk daftar perhatian.**  
   Setelah proses screening dan pendampingan dilakukan, perkembangan mahasiswa dapat dipantau secara berkala berdasarkan performa akademik semester berikutnya. Hasil pemantauan tersebut dapat digunakan sebagai bahan evaluasi untuk menentukan apakah mahasiswa masih membutuhkan pendampingan lebih lanjut.

6. **Melakukan evaluasi model secara berkala menggunakan data terbaru.**  
   Model memiliki recall sebesar 30% pada kelas `Enrolled`, sehingga masih terdapat keterbatasan dalam membedakan mahasiswa pada kategori tersebut. Institusi dapat melakukan evaluasi menggunakan data mahasiswa terbaru dan mempertimbangkan pengembangan model atau preprocessing tambahan apabila performa model belum memenuhi kebutuhan institusi.



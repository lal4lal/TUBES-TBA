# TUBES-TBA
Tugas Besar Teori Bahasa dan Automata 2024
Buatlah sebuah parser sederhana untuk memeriksa kevalidan struktur kalimat berbahasa Indonesia. Struktur kalimat yang dikenali adalah kalimat berita aktif dengan struktur:

S – P – O – K 

S – P – K

S – P – O 

S – P

Adapun jenis subyek, predikat, obyek dan keterangan yang dikenali ditentukan oleh kelompok masing-masing dengan jumlah kata masing- masing sebanyak 5.

Tugas Anda:
1.	Bangunlah sebuah token recognizer menggunakan Finite Automata yang mengenali setiap kata apakah masuk ke dalam kelompok S, P, O atau K.
2.	Bangunlah sebuah parser menggunakan Pushdown Automata yang mengenali apakah kalimat yang diinputkan valid berdasarkan struktur yang disebutkan di atas. Parser yang dibangun menggunakan token recognizer yang dibuat pada no 1.

Ketentuan:
1.	Kelompok berjumlah 2-3 orang
2.	Tidak diperkenankan menggunakan fungsi string matching
3.	Bahasa pemrograman yang diperkenankan Go, C++, atau Python
4.	Tidak wajib menggunakan GUI Hasil pekerjaan:
1.	Rancangan Finite Automata untuk masing-masing kelompok S, P, O dan K.
2.	Rancangan Context Free Grammar untuk struktur kalimat yang valid.
3.	Program token recognizer dan parser.
4.	Video penjelasan mengenai cara kerja program yang sudah dibuat.
5.	
Tanggal pengumpulan: 18 Juni 2024  jam23.59 di LMS


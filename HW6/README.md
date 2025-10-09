# Geometry Calculations (Geometri Analitik 2D)

## 📘 Tujuan
Program ini dibuat untuk mengimplementasikan konsep **Geometri Analitik dan Aljabar Linier** dalam bentuk skrip Python berorientasi objek. Melalui kelas-kelas dan fungsi yang disusun, pengguna dapat melakukan perhitungan dan transformasi terhadap objek-objek geometris 2D seperti titik, garis, lingkaran, dan segitiga.

---

## 🧩 Struktur Program

### 1. Kelas dan Desain OOP
Program ini memiliki empat kelas utama:

#### 🟢 **Class Point (Titik)**
- **Atribut:** `x`, `y`
- **Metode:**
  - `distance_to(other)`: menghitung jarak ke titik lain menggunakan rumus Euclidean.
  - `translate(dx, dy)`: mentranslasikan titik sejauh `(dx, dy)`.
  - `scale(factor, center)`: menskalakan posisi titik relatif terhadap pusat tertentu.
  - `rotate(angle, center)`: memutar titik sejauh `angle` derajat terhadap pusat tertentu.

#### 🔵 **Class Line (Garis)**
- **Representasi:** `Ax + By + C = 0`
- **Metode:**
  - `from_points(p1, p2)`: classmethod untuk membentuk garis dari dua titik.
  - `translate(dx, dy)`: mentranslasikan garis sejauh `(dx, dy)`.

#### 🔴 **Class Circle (Lingkaran)**
- **Atribut:** `center (Point)`, `radius`
- **Metode:**
  - `translate(dx, dy)`: memindahkan lingkaran.
  - `scale(factor, center)`: menskalakan ukuran lingkaran.
  - `rotate(angle, center)`: memutar lingkaran (pusat ikut berputar, radius tetap).

#### 🟡 **Class Triangle (Segitiga)**
- **Atribut:** `p1`, `p2`, `p3` (objek Point)
- **Metode:**
  - `side_lengths()`: menghitung panjang ketiga sisi.
  - `perimeter()`: menghitung keliling.
  - `area()`: menghitung luas dengan **Rumus Heron** atau **Shoelace Formula**.
  - `triangle_type()`: menentukan jenis segitiga (sama sisi, siku-siku, sama kaki, sembarang).
  - Transformasi (`translate`, `scale`, `rotate`) berlaku pada seluruh titik pembentuk segitiga.

---

## 🔢 Fungsi Komputasi Global

### 1. `intersect_lines(line1, line2)`
Menentukan titik potong dua garis. Jika sejajar → tidak ada solusi; jika berimpit → infinite solutions.

### 2. `intersect_circles(c1, c2)`
Menghitung titik potong dua lingkaran berdasarkan jarak antar pusat dan radius. Dapat menghasilkan 0, 1, atau 2 titik potong.

### 3. `intersect_line_circle(line, circle)`
Menyelesaikan sistem persamaan garis dan lingkaran menggunakan **discriminant kuadrat**.

### 4. `perpendicular_line_from_point(line, point)`
Membentuk persamaan garis tegak lurus terhadap `line` yang melalui `point`.

### 5. `find_foot_of_perpendicular(line, point)`
Menentukan **titik kaki garis tegak lurus** dari `point` ke `line`.

### 6. `verify_pythagorean_theorem(p1, p2, p3)`
Memverifikasi apakah tiga titik membentuk **segitiga siku-siku** berdasarkan hubungan:
\[ a^2 + b^2 ≈ c^2 \]
Menggunakan toleransi kesalahan `EPS = 1e-9`.

---

## ⚙️ Presisi dan Penanganan Numerik
- Semua perbandingan floating-point menggunakan **epsilon kecil (`EPS = 1e-9`)**.
- Tujuannya untuk menghindari error akibat representasi pecahan biner pada tipe `float`.

---

## 🔬 Prinsip Matematis di Balik Program
1. **Geometri Analitik 2D**: setiap objek direpresentasikan dengan persamaan koordinat.
2. **Aljabar Linier**: digunakan untuk rotasi dan transformasi matriks.
3. **Trigonometri**: digunakan dalam rotasi titik dan perhitungan jarak.
4. **Teorema Pythagoras**: digunakan untuk mendeteksi segitiga siku-siku.

---

## 💻 Cara Verifikasi Teorema Pythagoras di Program
1. Tentukan tiga titik (misalnya `A(0,0)`, `B(3,0)`, `C(0,4)`).
2. Panggil fungsi:
   ```python
   verify_pythagorean_theorem(A, B, C)
   ```
3. Program akan menghitung ketiga sisi segitiga:
   - AB, BC, dan AC
   - Mengecek apakah \( a^2 + b^2 ≈ c^2 \)
4. Jika benar, fungsi akan mengembalikan **True** dan menampilkan bahwa segitiga tersebut **siku-siku**.

---

## 🧠 Contoh Eksekusi (Main Block)
```python
if __name__ == "__main__":
    # Contoh penggunaan kelas Point
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    print("Jarak p1 ke p2:", p1.distance_to(p2))

    # Garis dari dua titik
    L1 = Line.from_points(Point(0, 0), Point(1, 1))
    L2 = Line.from_points(Point(0, 1), Point(1, 0))
    print("Titik potong L1 dan L2:", intersect_lines(L1, L2))

    # Lingkaran
    C1 = Circle(Point(0, 0), 5)
    C2 = Circle(Point(4, 0), 3)
    print("Titik potong dua lingkaran:", intersect_circles(C1, C2))

    # Verifikasi segitiga siku-siku
    A, B, C = Point(0, 0), Point(3, 0), Point(0, 4)
    print("Apakah segitiga ABC siku-siku?", verify_pythagorean_theorem(A, B, C))
```

---

## 📖 Kesimpulan
Program ini memadukan **konsep matematis dan pemrograman berorientasi objek (OOP)** untuk menyelesaikan permasalahan geometris secara terstruktur. Semua perhitungan didasarkan pada **Geometri Analitik**, **Teorema Pythagoras**, dan **Trigonometri**, menjadikannya contoh ideal untuk pembelajaran dasar komputasi matematis dua dimensi.

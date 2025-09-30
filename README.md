# 🎯 เกมลากตัวอักษร (Word Drag Game)

เกมเรียงตัวอักษรที่สนุกและท้าทาย! ลากตัวอักษรที่สุ่มมาเรียงให้เป็นคำที่ถูกต้อง รองรับทั้งภาษาไทยและอังกฤษ พร้อมระบบคะแนนและระดับความยาก

![Django](https://img.shields.io/badge/Django-5.2.2-green)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![Vue.js](https://img.shields.io/badge/Vue.js-3-brightgreen)

## ✨ คุณสมบัติ

- 🌐 **รองรับ 2 ภาษา**: ไทย และ อังกฤษ
- 🎮 **3 ระดับความยาก**: ง่าย, ปานกลาง, ยาก
- 🏆 **ระบบคะแนน**: เก็บคะแนนและจำนวนรอบที่เล่น
- 💡 **ระบบใบ้**: แสดงตัวอักษรแรกของคำ
- 🎨 **UI สวยงาม**: ใช้ Tailwind CSS และ Vue.js
- ↔️ **Drag & Drop**: ลากตัวอักษรได้อย่างลื่นไหลด้วย SortableJS
- 💾 **จัดการคำศัพท์**: เพิ่ม/แก้ไข/ลบคำผ่าน Django Admin

## 🛠️ เทคโนโลジีที่ใช้

### Backend
- **Django 5.2.2** - Python Web Framework
- **SQLite** - Database
- **Django REST API** - API Endpoints

### Frontend
- **Vue.js 3** - JavaScript Framework
- **Tailwind CSS** - Styling
- **SortableJS** - Drag & Drop
- **Axios** - HTTP Client

## 📋 ข้อกำหนดของระบบ

- Python 3.8 หรือสูงกว่า
- pip (Python package manager)
- Git (สำหรับ clone โปรเจกต์)

## 🚀 วิธีติดตั้งและรันโปรเจกต์

### 1. Clone โปรเจกต์

```bash
git clone <repository-url>
cd word_game
```

### 2. สร้าง Virtual Environment (แนะนำ)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. ติดตั้ง Dependencies

```bash
pip install django==5.2.2
pip install django-cors-headers
```

หรือสร้างไฟล์ `requirements.txt` และรัน:
```bash
pip install -r requirements.txt
```

### 4. สร้าง Database และ Tables

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. เพิ่มคำศัพท์เริ่มต้น

```bash
python manage.py populate_words
```

คำสั่งนี้จะเพิ่มคำศัพท์ 72 คำ (36 คำไทย + 36 คำอังกฤษ) เข้าสู่ database

### 6. สร้าง Superuser สำหรับ Admin (Optional)

```bash
python manage.py createsuperuser
```

ป้อนข้อมูล:
- Username: (ชื่อที่คุณต้องการ)
- Email: (อีเมลของคุณ)
- Password: (รหัสผ่าน)

### 7. รัน Development Server

```bash
python manage.py runserver
```

Server จะรันที่ `http://127.0.0.1:8000/`

### 8. เปิดเว็บในเบราว์เซอร์

- **หน้าเกม**: http://127.0.0.1:8000/
- **Django Admin**: http://127.0.0.1:8000/admin/

## 📁 โครงสร้างโปรเจกต์

```
word_game/
├── game/                          # Django App หลัก
│   ├── management/
│   │   └── commands/
│   │       └── populate_words.py  # คำสั่งเพิ่มคำศัพท์
│   ├── migrations/                # Database migrations
│   ├── admin.py                   # Django Admin configuration
│   ├── models.py                  # Models (Word, GameSession)
│   ├── views.py                   # API Views
│   └── urls.py                    # URL routing
├── templates/
│   └── game/
│       └── index.html             # หน้าเกมหลัก (Vue.js)
├── word_game/                     # Django Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py                      # Django management script
└── db.sqlite3                     # SQLite database (สร้างอัตโนมัติ)
```

## 🎮 วิธีเล่น

1. **เลือกภาษา**: ไทย หรือ English
2. **เลือกระดับ**: ง่าย (3-4 ตัวอักษร), ปานกลาง (5-7 ตัวอักษร), ยาก (8+ ตัวอักษร)
3. **ลากตัวอักษร**: จากช่องบนลงมาเรียงในช่องด้านล่าง
4. **ตรวจคำตอบ**: กดปุ่ม "ตรวจคำตอบ" เมื่อเรียงเสร็จ
5. **ใช้ใบ้**: กดปุ่ม "ใบ้" ถ้าติดขัด (แสดงตัวอักษรแรก)
6. **เล่นต่อ**: กดปุ่ม "คำต่อไป" เพื่อเล่นรอบใหม่

## 🔧 การจัดการคำศัพท์

### เพิ่มคำศัพท์ผ่าน Django Admin

1. เข้า http://127.0.0.1:8000/admin/
2. Login ด้วย superuser
3. ไปที่ **Words** → **Add Word**
4. กรอกข้อมูล:
   - **Word**: คำศัพท์
   - **Language**: th (ไทย) หรือ en (อังกฤษ)
   - **Difficulty**: 1 (ง่าย), 2 (ปานกลาง), 3 (ยาก)
5. บันทึก

### เพิ่มคำศัพท์จำนวนมากผ่าน Code

แก้ไขไฟล์ `game/management/commands/populate_words.py` แล้วรัน:

```bash
python manage.py populate_words
```

## 🌐 API Endpoints

### GET `/api/get-word/`
ดึงคำสุ่มจาก database

**Parameters:**
- `language` (string): 'th' หรือ 'en'
- `difficulty` (int): 1, 2, หรือ 3

**Response:**
```json
{
  "success": true,
  "word": "แมว",
  "shuffled_letters": ["ว", "แ", "ม"]
}
```

### POST `/api/check-word/`
ตรวจคำตอบ

**Body:**
```json
{
  "user_word": "แมว",
  "correct_word": "แมว"
}
```

**Response:**
```json
{
  "success": true,
  "is_correct": true
}
```

### POST `/api/save-score/`
บันทึกคะแนน

**Body:**
```json
{
  "session_id": "session_123",
  "score": 100,
  "words_completed": 10
}
```

## 🐛 การแก้ปัญหา

### ปัญหา: ไม่มีคำศัพท์ในเกม
**แก้ไข**: รันคำสั่ง `python manage.py populate_words`

### ปัญหา: Static files ไม่โหลด
**แก้ไข**: สร้างโฟลเดอร์ `static/` ใน root directory หรือปิด DEBUG mode

### ปัญหา: CORS Error
**แก้ไข**: ตรวจสอบ `CORS_ALLOWED_ORIGINS` ใน `settings.py`

### ปัญหา: Database ล็อก
**แก้ไข**: ปิด server แล้วรันใหม่ หรือลบไฟล์ `db.sqlite3` แล้วรัน migrate ใหม่

## 📝 คำสั่ง Django ที่ใช้บ่อย

```bash
# รัน development server
python manage.py runserver

# สร้าง migrations
python manage.py makemigrations

# รัน migrations
python manage.py migrate

# สร้าง superuser
python manage.py createsuperuser

# เพิ่มคำศัพท์
python manage.py populate_words

# เปิด Django shell
python manage.py shell
```

## 📄 License

MIT License - คุณสามารถใช้, แก้ไข, และแจกจ่ายโปรเจกต์นี้ได้อย่างเสรี

## 👨‍💻 พัฒนาโดย

โปรเจกต์เกมลากตัวอักษร - สร้างด้วย Django และ Vue.js

## 🤝 การมีส่วนร่วม

หากต้องการเพิ่มฟีเจอร์หรือแก้ไขบัค:

1. Fork โปรเจกต์
2. สร้าง Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit การเปลี่ยนแปลง (`git commit -m 'Add some AmazingFeature'`)
4. Push ไปยัง Branch (`git push origin feature/AmazingFeature`)
5. เปิด Pull Request

## 📞 ติดต่อ

หากมีคำถามหรือข้อเสนอแนะ กรุณาเปิด Issue ใน repository

---

**สนุกกับการเล่นเกม! 🎉**
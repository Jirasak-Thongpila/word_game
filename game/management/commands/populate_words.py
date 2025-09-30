# management/commands/populate_words.py
# สร้างโฟลเดอร์: game/management/commands/

from django.core.management.base import BaseCommand
from game.models import Word

class Command(BaseCommand):
    help = 'เพิ่มคำศัพท์ลงในฐานข้อมูล'

    def handle(self, *args, **options):
        # คำภาษาไทย
        thai_words = [
            # ระดับง่าย (3-4 ตัวอักษร)
            ('แมว', 'th', 1), ('หมา', 'th', 1), ('นก', 'th', 1), ('ปลา', 'th', 1),
            ('บ้าน', 'th', 1), ('รถ', 'th', 1), ('เก้าอี้', 'th', 1), ('โต๊ะ', 'th', 1),
            ('หนังสือ', 'th', 1), ('ดินสอ', 'th', 1), ('กระเป๋า', 'th', 1), ('รองเท้า', 'th', 1),

            # ระดับปานกลาง (5-7 ตัวอักษร)
            ('ช้าง', 'th', 2), ('วัว', 'th', 2), ('กบ', 'th', 2), ('ผีเสื้อ', 'th', 2),
            ('โรงเรียน', 'th', 2), ('ห้องสมุด', 'th', 2), ('โรงพยาบาล', 'th', 2), ('ร้านค้า', 'th', 2),
            ('เครื่องบิน', 'th', 2), ('รถไฟ', 'th', 2), ('เรือ', 'th', 2), ('จักรยาน', 'th', 2),

            # ระดับยาก (8+ ตัวอักษร)
            ('คอมพิวเตอร์', 'th', 3), ('โทรศัพท์', 'th', 3), ('โทรทัศน์', 'th', 3), ('ตู้เย็น', 'th', 3),
            ('เครื่องซักผ้า', 'th', 3), ('เครื่องปรับอากาศ', 'th', 3), ('มหาวิทยาลัย', 'th', 3), ('ห้างสรรพสินค้า', 'th', 3),
            ('ซูเปอร์มาร์เก็ต', 'th', 3), ('พิพิธภัณฑ์', 'th', 3), ('สนามบิน', 'th', 3), ('สถานเอกอัครราชทูต', 'th', 3),
        ]

        # คำภาษาอังกฤษ
        english_words = [
            # ระดับง่าย (3-4 ตัวอักษร)
            ('CAT', 'en', 1), ('DOG', 'en', 1), ('BIRD', 'en', 1), ('FISH', 'en', 1),
            ('HOUSE', 'en', 1), ('CAR', 'en', 1), ('BOOK', 'en', 1), ('PEN', 'en', 1),
            ('BAG', 'en', 1), ('SHOE', 'en', 1), ('TREE', 'en', 1), ('SUN', 'en', 1),

            # ระดับปานกลาง (5-7 ตัวอักษร)
            ('WATER', 'en', 2), ('TABLE', 'en', 2), ('CHAIR', 'en', 2), ('PENCIL', 'en', 2),
            ('SCHOOL', 'en', 2), ('FAMILY', 'en', 2), ('FRIEND', 'en', 2), ('FLOWER', 'en', 2),
            ('ANIMAL', 'en', 2), ('GARDEN', 'en', 2), ('WINDOW', 'en', 2), ('KITCHEN', 'en', 2),

            # ระดับยาก (8+ ตัวอักษร)
            ('COMPUTER', 'en', 3), ('ELEPHANT', 'en', 3), ('BIRTHDAY', 'en', 3), ('SANDWICH', 'en', 3),
            ('HOSPITAL', 'en', 3), ('AIRPLANE', 'en', 3), ('MOUNTAIN', 'en', 3), ('UMBRELLA', 'en', 3),
            ('BUTTERFLY', 'en', 3), ('TELEPHONE', 'en', 3), ('LIBRARY', 'en', 3), ('VACATION', 'en', 3),
        ]

        all_words = thai_words + english_words

        for word_text, language, difficulty in all_words:
            word, created = Word.objects.get_or_create(
                word=word_text,
                language=language,
                defaults={'difficulty': difficulty}
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'เพิ่มคำ "{word_text}" สำเร็จ')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'คำ "{word_text}" มีอยู่แล้ว')
                )

        self.stdout.write(
            self.style.SUCCESS(f'เพิ่มคำศัพท์เสร็จสิ้น! รวม {len(all_words)} คำ')
        )

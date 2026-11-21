# برنامج الاقتباسات 📖
# شغّله من الترمينال بالأمر: python quotes.py
# الفكرة: بنقرأ الاقتباسات من ملف quotes.txt وبعدين نختار واحد عشوائي ونطبعه

import random  # مكتبة جاهزة في بايثون بتساعدنا نختار حاجة عشوائية
from pathlib import Path  # بنستخدمها عشان نوصّل لمسار الملف بشكل مضمون

# __file__ هو مسار البرنامج نفسه
# with_name بترجع نفس المسار لكن مع تغيير اسم الملف في الآخر
# كده البرنامج هيقرا quotes.txt اللي جنبه دايماً، مهما شغّلناه من أي مكان
FILE_NAME = Path(__file__).with_name("quotes.txt")


def read_quotes(file_name):
    """بتقرا الاقتباسات من الملف وترجعها في قائمة"""
    quotes = []  # قائمة فاضية هنحط فيها الاقتباسات واحد واحد

    # بنفتح الملف بترميز UTF-8 عشان اللغة العربية تظهر صح
    with open(file_name, encoding="utf-8") as file:
        for line in file:  # بنمشي على كل سطر في الملف
            line = line.strip()  # نشيل المسافات والسطر الجديد من الطرفين

            # بنتجاهل الأسطر الفاضية وأسطر التعليقات اللي بتبدأ بـ #
            if not line or line.startswith("#"):
                continue

            # شكل السطر: الاقتباس | المؤلف | المصدر
            # split بتقطّع السطر عند علامة | وترجع الأجزاء في قائمة
            parts = [part.strip() for part in line.split("|")]

            text = parts[0]  # الجزء الأول هو نص الاقتباس
            author = parts[1] if len(parts) > 1 else "غير معروف"
            source = parts[2] if len(parts) > 2 else ""

            # بنخزن الاقتباس في قاموس (قاموس = مجموعة مفاتيح وقيم)
            quotes.append({"text": text, "author": author, "source": source})

    return quotes


def print_random_quote(quotes):
    """بتختار اقتباس عشوائي وتطبعه بشكل حلو"""
    quote = random.choice(quotes)  # اختيار عنصر عشوائي من القائمة

    print()
    print('"' + quote["text"] + '"')

    attribution = "— " + quote["author"]
    if quote["source"]:  # لو فيه مصدر مسجل نضيفه
        attribution += "، " + quote["source"]
    print(attribution)


def main():
    try:
        quotes = read_quotes(FILE_NAME)
    except FileNotFoundError:
        # يعني ملف quotes.txt مش موجود جنب البرنامج
        print("مش لاقي ملف الاقتباسات! تأكد إن ملف quotes.txt موجود جنب البرنامج.")
        return

    if not quotes:
        print("الملف فاضي، ضيف شوية اقتباسات في ملف quotes.txt")
        return

    print_random_quote(quotes)


main()

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    # هذا السطر سيقرأ الإحداثيات من الرابط، مثلاً: ly01.onrender.com/?lat=24.0&lon=33.0
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    if lat and lon:
        # هنا يمكنك حفظ الإحداثيات في ملف نصي على الخادم أو إرسالها لنفسك
        print(f"تم الحصول على إحداثيات جديدة: خط العرض {lat} وخط الطول {lon}")
        return f"تم استلام الموقع: {lat}, {lon}"
    else:
        return "يرجى إرسال الإحداثيات عبر الرابط."

if __name__ == "__main__":
    app.run()

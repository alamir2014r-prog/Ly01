from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    # هذا السطر سيقرأ الإحداثيات من الرابط مباشرة بدلاً من input
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    if lat and lon:
        return f"تم استلام الموقع: خط العرض {lat} وخط الطول {lon}"
    return "مرحباً! يرجى إرسال الإحداثيات عبر الرابط."

if __name__ == "__main__":
    app.run()

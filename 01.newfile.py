from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    # سيبحث الموقع عن الإحداثيات في الرابط: /?lat=32&lon=13
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    if lat and lon:
        return f"تم استلام الموقع بنجاح: خط العرض {lat} وخط الطول {lon}"
    else:
        return "يرجى إضافة الإحداثيات إلى الرابط، مثال: /?lat=32.8&lon=13.1"

if __name__ == "__main__":
    app.run()

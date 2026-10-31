from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import include, path


# دالة لتسجيل الخروج السريع وتجاوز خطأ 405
def quick_logout(request):
    logout(request)
    return redirect('accounts:login')


urlpatterns = [
    # مسار الخروج المباشر قبل مسارات الـ Admin
    path('admin/logout/', quick_logout),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('students/', include('students.urls')),
    path('academics/', include('academics.urls')),
    path('attendance/', include('attendance.urls')),
    path('library/', include('library.urls')),
    # الصفحة الرئيسية = لوحة التحكم
    path('', include('dashboard.urls')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
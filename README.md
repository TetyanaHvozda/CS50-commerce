# CS50-commerce
CS50 Commerce

image upload with pillow

https://github.com/NavTheRaj/image_upload_django
https://www.youtube.com/watch?v=PxLasCh5E8I

run a command --> python3 -m pip install Pillow

create a folder media/images for storing images when you upload them

add bellow code in settings.py of your django project –

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
in urls.py file add the configurations –

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

request.GET.get explained here:
https://stackoverflow.com/questions/51365788/what-is-request-get-get-doing

from django.contrib import admin
from .models import Gallery         #importing model Gallery from models.py
from .models import Team  #importing model Team from models.py
from .models import AboutUs
from .models import Intro
from django.utils.html import format_html
from django.contrib.auth.models import Group
from imagekit.admin import AdminThumbnail

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ('Date', 'Input_image','Output_image','input_thumbnail','output_thumbnail') #displaying information on a table
    list_per_page = 25               #only 25 information per page

    def input_thumbnail(self, obj):  #function for thumbnail
        return format_html('<img src="{}" style="width: 130px; \
                              height: 100px"/>'.format(obj.Input_image))  #here Input_image came from Gallery

    input_thumbnail.short_description = 'input thumbnail'

    def output_thumbnail(self, obj):   #function for thumbnail
        return format_html('<img src="{}" style="width: 130px; \
                              height: 100px"/>'.format(obj.Output_image))
        #here Output_image came from Gallery

admin.site.register(Gallery, ImageAdmin)

class TAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','roll_no','image','t_thumbnail','facebook_url','github_url','linkedin_url')
    
    
    def t_thumbnail(self, obj):
        return format_html('<img src="{}" style="width: 130px; \
                              height: 170px"/>'.format(obj.image.url))

    t_thumbnail.short_description = 'thumbnail'

admin.site.register(Team, TAdmin)

class AboutusAdmin(admin.ModelAdmin):
    list_display = ('a_image','description')

admin.site.register(AboutUs, AboutusAdmin)

class IntroAdmin(admin.ModelAdmin):
    list_display = ("topic",'i_image','description')

admin.site.register(Intro, IntroAdmin)

admin.site.site_header = "Image Colorization Admin"#changing title to image colorization
#admin.site.unregister(Group)
admin.site.site_title = "Image Colorization"

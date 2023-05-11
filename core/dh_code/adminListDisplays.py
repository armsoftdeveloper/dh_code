from django.contrib import admin

# Basic List Display RU & EN

class Basic_List_Display_RU(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'time_create' , 'time_update')
    list_display_links = ('id', 'title' , 'description' , 'time_create' , 'time_update')
    search_fields = ('title', 'description')
    list_filter = ('time_create' , )

class Basic_List_Display_EN(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'time_create' , 'time_update')
    list_display_links = ('id', 'title' , 'description' , 'time_create' , 'time_update')
    search_fields = ('title', 'description')
    list_filter = ('time_create' , )

# Etaps List Display RU & EN

class Etaps_List_Display_RU(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'time_create' , 'time_update')
    list_display_links = ('id', 'title' , 'description' , 'time_create' , 'time_update')
    search_fields = ('title', 'description')
    list_filter = ('time_create' , )

class Etaps_List_Display_EN(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'time_create' , 'time_update')
    list_display_links = ('id', 'title' , 'description' , 'time_create' , 'time_update')
    search_fields = ('title', 'description')
    list_filter = ('time_create' , )

# Services List Display RU & EN

class Services_List_Display_RU(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'time_create' , 'time_update')
    list_display_links = ('id', 'title' , 'description' , 'time_create' , 'time_update')
    search_fields = ('title', 'description')
    list_filter = ('time_create' , )

class Services_List_Display_EN(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'time_create' , 'time_update')
    list_display_links = ('id', 'title' , 'description' , 'time_create' , 'time_update')
    search_fields = ('title', 'description')
    list_filter = ('time_create' , )

# Advantages List Display RU & EN

class Advantages_List_Display_RU(admin.ModelAdmin):
    list_display = ('id', 'description', 'time_create' , 'time_update')
    list_display_links = ('id', 'description' , 'time_create' , 'time_update')
    search_fields = ('description' , )
    list_filter = ('time_create' , )

class Advantages_List_Display_EN(admin.ModelAdmin):
    list_display = ('id', 'description', 'time_create' , 'time_update')
    list_display_links = ('id', 'description' , 'time_create' , 'time_update')
    search_fields = ('description' , )
    list_filter = ('time_create' , )

# Reviews List Display RU & EN

class Reviews_List_Display_RU(admin.ModelAdmin):
    list_display = ('id', 'userIcon', 'userName' , 'href' , 'body' , 'time_create' , 'time_update')
    list_display_links = ('id', 'userIcon', 'userName' , 'href' , 'body' , 'time_create' , 'time_update')
    search_fields = ('userName' , )
    list_filter = ('time_create' , )

class Reviews_List_Display_EN(admin.ModelAdmin):
    list_display = ('id', 'userIcon', 'userName' , 'href' , 'body' , 'time_create' , 'time_update')
    list_display_links = ('id', 'userIcon', 'userName' , 'href' , 'body' , 'time_create' , 'time_update')
    search_fields = ('userName' , )
    list_filter = ('time_create' , )

# Contact List Display Default For All Languages

class Contact_List_Display_Default(admin.ModelAdmin):
    list_display = ('id', 'whatsapp', 'gmail' , 'telegram' , 'phone_number' , 'fl_name' , 'time_create' , 'time_update')
    list_display_links = ('id', 'whatsapp', 'gmail' , 'telegram' , 'phone_number' , 'fl_name' , 'time_create' , 'time_update')
    search_fields = ('id', 'whatsapp', 'gmail' , 'telegram' , 'phone_number' , 'fl_name' , 'time_create' , 'time_update')
    list_filter = ('time_create' , )

# Portfolio List Display Default For All Languages

class Portfolio_List_Display_Default(admin.ModelAdmin):
    list_display = ('id', 'img', 'time_create' , 'time_update')
    list_display_links = ('id', 'img', 'time_create' , 'time_update')
    search_fields = ('id', 'img', 'time_create' , 'time_update')
    list_filter = ('time_create' , )
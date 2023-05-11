from django.contrib import admin
from .models import *
from .adminListDisplays import *

# ADMIN REGISTER RU MODELS
admin.site.register(BasicRU , Basic_List_Display_RU)
admin.site.register(EtapsRU , Etaps_List_Display_RU)
admin.site.register(ServicesRU , Services_List_Display_RU)
admin.site.register(AdvantagesRU , Advantages_List_Display_RU)
admin.site.register(ReviewsRU , Reviews_List_Display_RU)
# ADMIN REGISTER EN MODELS
admin.site.register(BasicEN , Basic_List_Display_EN)
admin.site.register(EtapsEN , Etaps_List_Display_EN)
admin.site.register(ServicesEN , Services_List_Display_EN)
admin.site.register(AdvantagesEN , Advantages_List_Display_EN)
admin.site.register(ReviewsEN , Reviews_List_Display_EN)
# ADMIN REGISTER DEFAULT MODELS FOR ALL MODELS
admin.site.register(Contact , Contact_List_Display_Default)
admin.site.register(Portfolio)




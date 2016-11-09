from django.contrib import admin
# from django.contrib.contenttypes.models import ContentType

# Register your models here.
from .models.lote import Lote
from .models.manzana import Manzana
from .models.socio import Socio
from .models.socio_lote import SocioLote

# admin.site.register(ContentType)


class LoteInline(admin.TabularInline):
    model = Lote
    extra = 1


class ManzanaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['manzana']}), ]
    inlines = [LoteInline]

admin.site.register(Lote)
admin.site.register(Manzana, ManzanaAdmin)
# admin.site.register(ManzanaLote)
# admin.site.register(RelacionManzanaLote, RelacionManzanaLoteAdmin)
# admin.site.register(RelacionManzanaLote)
admin.site.register(Socio)
admin.site.register(SocioLote)

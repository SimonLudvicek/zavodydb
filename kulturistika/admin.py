from django.contrib import admin

# Import modelů ze souboru models.py
from .models import Zavodnik
from .models import Sponzor
from .models import Organizace
from .models import Trener
from .models import Soutez
from .models import Oceneni

# Registrace nového modelu v administraci
admin.site.register(Zavodnik)
admin.site.register(Sponzor)
admin.site.register(Organizace)
admin.site.register(Trener)
admin.site.register(Soutez)
admin.site.register(Oceneni)



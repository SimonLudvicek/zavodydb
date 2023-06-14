# Import knihovny models (součást balíčku django.db), která obsahuje programové prostředky
# pro vytváření modelů


from django.db import models

# -------------------------------------------------------------------------------------
# Modely-třídy, které tvoří datovou strukturu aplikace
# -------------------------------------------------------------------------------------
class Zavodnik(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=50,
        unique=False,
        verbose_name='Jméno Závodníka',
        help_text='Zadejte jméno závodníka')
    surname = models.CharField(max_length=60,
                            unique=False,
                            verbose_name='Přijmení Závodníka',
                            help_text='Zadejte příjmení závodníka')
    birth = models.DateField(null=True,
        blank=True,
        verbose_name='Datum Narozeni',
        help_text='Zadejte, prosím, datum ve formátu: <em>den.měsíc.rok</em>')
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        verbose_name='Pohlaví',
        help_text='Vyberte pohlaví závodníka'
    )


    weight = models.IntegerField(
        verbose_name='Váha',
        help_text='Zadejte váhu závodníka v kilogramech'
    )
    description = models.TextField(
        verbose_name='Popis',
        help_text='Zadejte popis závodníka',
        max_length=1000
    )
    age = models.IntegerField(
        verbose_name='Věk',
        help_text='Zadejte věk závodníka'
    )
    trener = models.ManyToManyField('Trener')
    awards = models.ManyToManyField('Oceneni')

    class Meta:

        verbose_name = 'Závodník'
        verbose_name_plural = 'Závodníci'
        ordering = ['name']

    def __str__(self):

        return self.name

class Sponzor(models.Model):
    residence = models.CharField(
        max_length=100,
        verbose_name='Sídliště',
        help_text='Zadejte místo sídliště sponzora'
    )
    email = models.EmailField(
        max_length=254,
        verbose_name='Email',
        help_text='Zadejte emailovou adresu sponzora'
    )
    date_of_establishment = models.DateField(
        verbose_name='Datum Založení',
        help_text='Zadejte datum založení ve formátu: <em>den.měsíc.rok</em>'
    )

    class Meta:

        verbose_name = 'Sponzor'
        verbose_name_plural = 'Sponzoři'
        ordering = ['residence']

    def __str__(self):

        return self.residence

class Organizace(models.Model):
    name = models.CharField(max_length=200,
                            unique=True,
                            verbose_name='Jméno organizace',
                            help_text='Zadejte jméno organizace')
    zavodnik_count = models.IntegerField(
        verbose_name='Počet Závodníků',
        help_text='Zadejte počet závodníků v organizaci'
    )
    oceneni_count = models.IntegerField(
        verbose_name='Počet Ocenění',
        help_text='Zadejte počet ocenění, které organizace obdržela'
    )
    residence = models.CharField(
        max_length=100,
        verbose_name='Bydliště',
        help_text='Zadejte místo bydliště organizace'
    )

    class Meta:

        verbose_name = 'Organizace'
        verbose_name_plural = 'Organizace'
        ordering = ['name']

    def __str__(self):

        return self.name

class Trener(models.Model):
    name = models.CharField(max_length=50,
                            unique=False,
                            verbose_name='Jméno trenéra',
                            help_text='Zadejte jméno trenéra')
    surname = models.CharField(max_length=60,
                               unique=False,
                               verbose_name='Přijmení trenéra',
                               help_text='Zadejte příjmení trenéra')
    birth = models.DateField(null=True,
                             blank=True,
                             verbose_name='Datum Narozeni',
                             help_text='Zadejte, prosím, datum ve formátu: <em>den.měsíc.rok</em>')
    description = models.TextField(
        verbose_name='Popis',
        help_text='Zadejte popis trenéra',
        max_length=1000
    )

    class Meta:

        verbose_name = 'Trenér'
        verbose_name_plural = 'Trenéři'
        ordering = ['name']

    def __str__(self):

        return self.name

class Soutez(models.Model):
    venue = models.CharField(
        max_length=100,
        verbose_name='Místo konání',
        help_text='Zadejte místo konání soutěže'
    )
    contestant_count = models.IntegerField(
        verbose_name='Počet soutěžících',
        help_text='Zadejte počet soutěžících ve soutěži'
    )
    pricepool = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Cena (v CZK)',
        help_text='Zadejte výši ceny (v Kč) pro soutěž'
    )

    class Meta:

        verbose_name = 'Soutěž'
        verbose_name_plural = 'Soutěže'
        ordering = ['venue']

    def __str__(self):

        return self.venue

class Oceneni(models.Model):
    AWARD_CHOICES = (
        ('pohár', 'Pohár'),
        ('medaile', 'Medaile'),
        ('diplom', 'Diplom'),
    )

    type = models.CharField(
        max_length=10,
        choices=AWARD_CHOICES,
        verbose_name='Typ ocenění',
        help_text='Vyberte typ ocenění'
    )
    award_count = models.IntegerField(
        verbose_name='Počet ocenění',
        help_text='Zadejte počet ocenění'
    )

    class Meta:

        verbose_name = 'Ocenění'
        verbose_name_plural = 'Ocenění'
        ordering = ['award_count']

    def __str__(self):

        return self.type
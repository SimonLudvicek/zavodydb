# Generated by Django 4.2.2 on 2023-06-14 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oceneni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('pohár', 'Pohár'), ('medaile', 'Medaile'), ('diplom', 'Diplom')], help_text='Vyberte typ ocenění', max_length=10, verbose_name='Typ ocenění')),
                ('award_count', models.IntegerField(help_text='Zadejte počet ocenění', verbose_name='Počet ocenění')),
            ],
            options={
                'verbose_name': 'Ocenění',
                'verbose_name_plural': 'Ocenění',
                'ordering': ['award_count'],
            },
        ),
        migrations.CreateModel(
            name='Organizace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Zadejte jméno organizace', max_length=200, unique=True, verbose_name='Jméno organizace')),
                ('zavodnik_count', models.IntegerField(help_text='Zadejte počet závodníků v organizaci', verbose_name='Počet Závodníků')),
                ('oceneni_count', models.IntegerField(help_text='Zadejte počet ocenění, které organizace obdržela', verbose_name='Počet Ocenění')),
                ('residence', models.CharField(help_text='Zadejte místo bydliště organizace', max_length=100, verbose_name='Bydliště')),
            ],
            options={
                'verbose_name': 'Organizace',
                'verbose_name_plural': 'Organizace',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Soutez',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(help_text='Zadejte místo konání soutěže', max_length=100, verbose_name='Místo konání')),
                ('contestant_count', models.IntegerField(help_text='Zadejte počet soutěžících ve soutěži', verbose_name='Počet soutěžících')),
                ('pricepool', models.DecimalField(decimal_places=2, help_text='Zadejte výši ceny (v Kč) pro soutěž', max_digits=10, verbose_name='Cena (v CZK)')),
            ],
            options={
                'verbose_name': 'Soutěž',
                'verbose_name_plural': 'Soutěže',
                'ordering': ['venue'],
            },
        ),
        migrations.CreateModel(
            name='Sponzor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('residence', models.CharField(help_text='Zadejte místo sídliště sponzora', max_length=100, verbose_name='Sídliště')),
                ('email', models.EmailField(help_text='Zadejte emailovou adresu sponzora', max_length=254, verbose_name='Email')),
                ('date_of_establishment', models.DateField(help_text='Zadejte datum založení ve formátu: <em>den.měsíc.rok</em>', verbose_name='Datum Založení')),
            ],
            options={
                'verbose_name': 'Sponzor',
                'verbose_name_plural': 'Sponzoři',
                'ordering': ['residence'],
            },
        ),
        migrations.CreateModel(
            name='Trener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Zadejte jméno trenéra', max_length=50, verbose_name='Jméno trenéra')),
                ('surname', models.CharField(help_text='Zadejte příjmení trenéra', max_length=60, verbose_name='Přijmení trenéra')),
                ('birth', models.DateField(blank=True, help_text='Zadejte, prosím, datum ve formátu: <em>den.měsíc.rok</em>', null=True, verbose_name='Datum Narozeni')),
                ('description', models.TextField(help_text='Zadejte popis trenéra', max_length=1000, verbose_name='Popis')),
            ],
            options={
                'verbose_name': 'Trenér',
                'verbose_name_plural': 'Trenéři',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Zavodnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Zadejte jméno závodníka', max_length=50, verbose_name='Jméno Závodníka')),
                ('surname', models.CharField(help_text='Zadejte příjmení závodníka', max_length=60, verbose_name='Přijmení Závodníka')),
                ('birth', models.DateField(blank=True, help_text='Zadejte, prosím, datum ve formátu: <em>den.měsíc.rok</em>', null=True, verbose_name='Datum Narozeni')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], help_text='Vyberte pohlaví závodníka', max_length=1, verbose_name='Pohlaví')),
                ('weight', models.IntegerField(help_text='Zadejte váhu závodníka v kilogramech', verbose_name='Váha')),
                ('description', models.TextField(help_text='Zadejte popis závodníka', max_length=1000, verbose_name='Popis')),
                ('age', models.IntegerField(help_text='Zadejte věk závodníka', verbose_name='Věk')),
            ],
            options={
                'verbose_name': 'Závodník',
                'verbose_name_plural': 'Závodníci',
                'ordering': ['name'],
            },
        ),
    ]

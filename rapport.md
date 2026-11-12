# Faglig Fornyelse – Undersøgelse af Django Framework

**Projekt:** Django Product Website  
**Teknologi:** Python og Django  
**Fag:** Faglig Fornyelse

## 1. Introduktion

I dette projekt har jeg valgt at undersøge og arbejde med Django, som er et webframework baseret på Python.

Mit udgangspunkt var, at jeg først havde lært grundlæggende Python gennem et Python for Beginners-forløb. Efterfølgende ønskede jeg at lære, hvordan jeg kunne bruge Python til at udvikle en rigtig hjemmeside.

Derfor valgte jeg at arbejde med Django for at få en bedre forståelse af webudvikling, backend-programmering og databaser.

Formålet med projektet var at lære en ny teknologi gennem selvstændig research og bruge min nye viden til at udvikle et konkret produkt.

Jeg har udviklet en produktbaseret hjemmeside med tre hovedsider:

- Homepage
- Product Page
- Product Detail Page

Hjemmesiden er ikke fuldt udfyldt med produkter endnu, men de vigtigste funktioner virker.

## 2. Hvad er Django?

Django er et open-source webframework, som er udviklet med Python. Det bruges til at udvikle dynamiske websites og webapplikationer.

Et framework er en samling af værktøjer og funktioner, som hjælper udviklere med at bygge software uden at skulle programmere alle funktioner fra bunden.

Django indeholder blandt andet:

- Databasehåndtering.
- URL-routing.
- Administration gennem Django Admin.
- Håndtering af HTTP-forespørgsler.
- Templates til visning af dynamisk indhold.
- Indbyggede sikkerhedsfunktioner.

En af de største fordele ved Django er, at det giver en struktureret måde at organisere en webapplikation på.

Django anvender en arkitektur, der kaldes Model-View-Template (MVT). Den hjælper med at opdele projektet i forskellige ansvarsområder.

## 3. Teknologier i mit projekt

Jeg har brugt følgende teknologier:

**Python:** Programmeringssproget, som Django er baseret på.

**Django:** Frameworket, som håndterer backend, routing, databasekommunikation og templates.

**SQLite:** Databasen, hvor produktinformationen bliver gemt.

**HTML:** Bruges til at opbygge hjemmesidens struktur.

**CSS:** Bruges til at style hjemmesiden.

**Bootstrap:** Bruges til layout, styling og responsive komponenter.

Kombinationen af disse teknologier gør det muligt at udvikle en hjemmeside, hvor frontend, backend og database arbejder sammen.

## 4. Hvordan fungerer mit Django-projekt?

En vigtig del af min læring har været at forstå, hvordan de forskellige dele af Django arbejder sammen.

Django anvender MVT-arkitekturen:

### Model

Modellerne er defineret i `models.py`.

Her opretter man strukturen for de data, som skal gemmes i databasen.

I mit projekt bruger jeg en Product-model til at håndtere produkter.

### View

Views er defineret i `views.py`.

De håndterer brugerens forespørgsler og henter de relevante data fra databasen.

For at hente alle produkter bruger jeg:

```python
Product.objects.all()
```

Dette er en del af Djangos ORM (Object-Relational Mapping).

ORM gør det muligt at arbejde med databasen gennem Python-kode i stedet for at skrive SQL-forespørgsler direkte.

### Template

Templates er HTML-filer, som bruges til at vise information til brugeren.

Django sender data fra views videre til templates, så produkterne kan vises dynamisk på hjemmesiden.

## 5. Database og Django Admin

I mit projekt bruger jeg SQLite som database.

Jeg har oprettet min produktmodel i `models.py` og bruger Django Admin til at administrere produkterne.

Django Admin er et indbygget administrationssystem, hvor man kan oprette, redigere og administrere data gennem en webbaseret brugergrænseflade.

Det betyder, at jeg ikke behøver at ændre HTML- eller Python-koden, hver gang jeg vil tilføje et nyt produkt.

Jeg har også arbejdet med migrations.

Jeg bruger følgende kommandoer:

```bash
python manage.py makemigrations
python manage.py migrate
```

`makemigrations` opretter migrationsfiler baseret på ændringer i modellerne.

`migrate` udfører ændringerne i databasen.

Dette har hjulpet mig med at forstå forbindelsen mellem Python-modeller og databaser.

## 6. Dynamiske produktsider og URL-routing

En vigtig funktion i mit projekt er produktdetaljesiden.

Når brugeren klikker på et produkt, skal hjemmesiden vise information om netop dette produkt.

Jeg bruger produktets ID i URL'en til at identificere det rigtige produkt.

Eksempel:

```text
/products/1/
/products/2/
```

I Django bruger jeg `get_object_or_404()` til at hente produktet:

```python
product = get_object_or_404(Product, id=id)
```

Denne funktion søger efter produktet i databasen.

Hvis produktet findes, returneres det til brugeren. Hvis det ikke findes, returnerer Django en 404-fejl.

Jeg bruger også Django Template Language til at oprette dynamiske links:

```html
<a href="{% url 'product_detail' product.id %}">
    View Product
</a>
```

Det gør det muligt at generere links automatisk ud fra produktets ID.

## 7. Research og læringsproces

Under projektet har jeg arbejdet selvstændigt med at lære Django.

En af mine største udfordringer var at finde de rigtige læringsressourcer.

Der findes mange Django-tutorials på internettet, og nogle af dem er meget lange. Det var derfor svært at finde information, som passede præcist til de funktioner, jeg ønskede at udvikle.

For at lære teknologien brugte jeg forskellige ressourcer:

- YouTube-tutorials.
- Djangos officielle dokumentation.
- ChatGPT og andre AI-værktøjer.
- Praktiske eksperimenter med min egen kode.
- Hjælp fra andre.

Jeg fandt ud af, at det er vigtigt ikke kun at følge en tutorial, men også at forstå koden og bruge den nye viden i sit eget projekt.

Jeg brugte blandt andet AI til at få forklaringer på kode og forstå forskellige funktioner.

Det er dog vigtigt at kontrollere AI-genererede svar, fordi de ikke altid er korrekte eller passer til ens konkrete projekt.

## 8. Test af projektet

Jeg har testet hjemmesidens vigtigste funktioner manuelt i browseren.

Jeg har blandt andet kontrolleret:

- At forsiden åbner korrekt.
- At produktsiden viser produkterne fra databasen.
- At klik på et produkt åbner den rigtige detaljeside.
- At produktets ID fungerer i URL'en.
- At en forespørgsel på et produkt, som ikke findes, giver en 404-fejl.

Testene viste, at de vigtigste funktioner i hjemmesiden virker.

## 9. Fordele og begrænsninger ved Django

### Fordele

Jeg synes, at Django gør webudvikling nemmere, fordi det giver en samlet struktur til arbejdet med backend, databaser og frontend-integration.

Nogle af de største fordele er:

- Django har mange indbyggede funktioner.
- Det er nemt at arbejde med databaser gennem ORM.
- Django Admin gør det nemt at administrere data.
- URL-routing gør navigationen struktureret.
- Frameworket hjælper med at organisere koden.

Jeg synes især, at det er praktisk, at Django samler mange af de nødvendige backend-værktøjer i ét framework.

### Begrænsninger

Selvom Django har mange fordele, er der også nogle begrænsninger.

For begyndere kan Django være svært at lære, fordi der er mange forskellige filer og funktioner, som skal forstås.

Det kan eksempelvis tage tid at forstå forbindelsen mellem `models.py`, `views.py`, `urls.py` og templates.

Django kan også være mere omfattende end nødvendigt til meget små og simple websites.

Derudover kræver udvikling med Django, at man har en grundlæggende forståelse af Python og webudvikling.

## 10. Konklusion

Gennem dette projekt har jeg fået praktisk erfaring med Django og lært, hvordan man kan bruge Python til at udvikle en dynamisk hjemmeside.

Jeg har lært at arbejde med modeller, databaser, Django Admin, ORM, URL-routing og templates.

Jeg har også fået en bedre forståelse af, hvordan frontend, backend og database arbejder sammen.

En af de vigtigste ting, jeg har lært, er, hvordan man selvstændigt kan undersøge en ny teknologi og bruge forskellige læringsressourcer til at løse praktiske problemer.

Jeg synes, Django er et nyttigt framework, fordi det gør det nemmere at organisere og udvikle webapplikationer.

Projektet har givet mig et godt grundlag for at arbejde videre med Python og backend-udvikling i fremtiden.

## 11. Kilder og dokumentation

- Django Documentation: https://docs.djangoproject.com/
- Python Documentation: https://docs.python.org/3/
- Bootstrap Documentation: https://getbootstrap.com/docs/
- YouTube-tutorials om Python og Django.
- ChatGPT brugt som hjælp til forståelse og forklaring af kode.
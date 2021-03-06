# Generated by Django 2.1.7 on 2019-02-21 17:26

from django.db import migrations


def create_florida_counties(apps, schema_editor):
    County = apps.get_model('dsnap_rules', 'County')

    FLORIDA_COUNTIES = [
        "Alachua",
        "Baker",
        "Bay",
        "Bradford",
        "Brevard",
        "Broward",
        "Calhoun",
        "Charlotte",
        "Citrus",
        "Clay",
        "Collier",
        "Columbia",
        "DeSoto",
        "Dixie",
        "Duval",
        "Escambia",
        "Flagler",
        "Franklin",
        "Gadsden",
        "Gilchrist",
        "Glades",
        "Gulf",
        "Hamilton",
        "Hardee",
        "Hendry",
        "Hernando",
        "Highlands",
        "Hillsborough",
        "Holmes",
        "Indian River",
        "Jackson",
        "Jefferson",
        "Lafayette",
        "Lake",
        "Lee",
        "Leon",
        "Levy",
        "Liberty",
        "Madison",
        "Manatee",
        "Marion",
        "Martin",
        "Miami-Dade",
        "Monroe",
        "Nassau",
        "Okaloosa",
        "Okeechobee",
        "Orange",
        "Osceola",
        "Palm Beach",
        "Pasco",
        "Pinellas",
        "Polk",
        "Putnam",
        "Santa Rosa",
        "Sarasota",
        "Seminole",
        "St. Johns",
        "St. Lucie",
        "Sumter",
        "Suwannee",
        "Taylor",
        "Union",
        "Volusia",
        "Wakulla",
        "Walton",
        "Washington",
    ]

    State = apps.get_model('dsnap_rules', 'State')
    florida = State.objects.get(abbreviation='FL')
    for name in FLORIDA_COUNTIES:
        county = County(name=name, state=florida)
        county.save()

class Migration(migrations.Migration):

    dependencies = [
        ('dsnap_rules', '0002_auto_20190221_1645'),
    ]

    operations = [
        migrations.RunPython(create_florida_counties),
    ]

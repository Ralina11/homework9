from django.core.management import BaseCommand
import json
from main.models import Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        category_data = []

        with open('data.json', encoding='utf-8') as file:
            data = json.load(file)

        Category.objects.all().delete()

        for raw in data:
            if raw["model"] == "main.category":
                category_data.append(Category(**raw["fields"]))
        Category.objects.bulk_create(category_data)



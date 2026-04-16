from django.core.management.base import BaseCommand
from datetime import datetime
from actors.models import Actor
import csv  


class Command(BaseCommand):
    help = 'Importa atores a partir de um arquivo CSV'

    def add_arguments(self, parser):
        parser.add_argument(
                'file_name',
                type=str, 
                help='Caminho para o arquivo CSV contendo os atores'
            )
    
    
    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date() if row['birthday'] else None
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(f'Ator: {name}'))

                Actor.objects.create(
                    name=name, 
                    birthday=birthday,
                    nationality=nationality,
                )
        self.stdout.write(self.style.SUCCESS('Atores importados com sucesso!'))
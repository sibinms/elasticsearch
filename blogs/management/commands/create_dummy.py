# CreateDummyArticles.py
import uuid
import random
from django.core.management.base import BaseCommand
from blogs.models import Article


class Command(BaseCommand):
    help = 'Create 1M records of Article with dummy data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating 1 million dummy articles...'))

        batch_size = 100  # Adjust the batch size based on your system's memory constraints

        for batch in range(0, 1000000, batch_size):
            articles_batch = []

            for i in range(batch, batch + batch_size):
                uuid_val = uuid.uuid4()
                title_val = f'Dummy Title {random.randint(1, 100)}'
                content_val = f'Dummy Content {random.randint(1, 100)}'

                article = Article(
                    uuid=uuid_val,
                    title=title_val,
                    content=content_val
                )
                articles_batch.append(article)

            Article.objects.bulk_create(articles_batch)

            self.stdout.write(self.style.SUCCESS(f'Created batch {batch} - {batch + batch_size}'))

        self.stdout.write(self.style.SUCCESS('Successfully created 1 million dummy articles.'))

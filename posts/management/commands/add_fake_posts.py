from django.core.management.base import BaseCommand
from posts.utils import created_posts

class Command(BaseCommand):
    help = 'create fake posts'

    def handle(self, *args, **options):
        count = options.get('count')
        created_posts(count)
        self.stdout.write('Posts has been created')

    def add_arguments(self, parser):
        parser.add_argument(
            '-c',
            '--count',
            type=int,
            default=10,
            dest='count',
            help='Amount of posts to generate'
        )
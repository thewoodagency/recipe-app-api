import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for DB...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('DB is not available, waiting 1 second')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('DB is available'))

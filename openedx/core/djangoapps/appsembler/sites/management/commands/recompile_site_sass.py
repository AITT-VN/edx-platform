from django.core.management.base import BaseCommand

from openedx.core.djangoapps.site_configuration.models import SiteConfiguration


class Command(BaseCommand):
    help = "Recompiles SASS for all microsites"

    def handle(self, *args, **options):
        for site in SiteConfiguration.objects.all():
            site.compile_microsite_sass()

import os
from django.conf import settings
from django.core.management.base import BaseCommand
from xbrowse_server.base.models import Project, Individual

class Command(BaseCommand):

    def handle(self, *args, **options):

        project_id = args[0]
        project = Project.objects.get(project_id=project_id)

        file_map = {}
        for path in os.listdir(args[1]):
            sample = path.replace('.bam.csv', '')
            sample = sample.replace('.', '')
            sample = sample.replace('-', '')
            file_map[sample] = os.path.abspath(os.path.join(args[1], path))

        for indiv in project.get_individuals():
            sample = indiv.indiv_id.replace('-', '')
            if sample in file_map:
                indiv.exome_depth_file = file_map[sample]
                indiv.save()
                settings.CNV_STORE.add_sample(str(indiv.pk), open(indiv.exome_depth_file))
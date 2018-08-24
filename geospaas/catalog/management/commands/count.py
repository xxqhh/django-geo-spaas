from geospaas.utils import ProcessingBaseCommand

class Command(ProcessingBaseCommand):
    help = 'Dataset statistics'

    def handle(self, *args, **options):
        # find input datasets
        inp_datasets = self.find_datasets(**options)
        self.stdout.write('Found %d matching datasets' % inp_datasets.count())
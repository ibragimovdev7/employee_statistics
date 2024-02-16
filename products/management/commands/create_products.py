from products.models import Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        nam = ['ULTRATOVUSH TEKSHIRUVI (UZI)', 'KOLPOSKOP',
               'RAQAMLI NARKOZ APPARATI',
               'C02 FRAKSIYON LAZER APPARATI',
               'RAQAMLI MIKROSKOP',
               'MIKROTOM',
               'EZOFAGOGASTRODUODENOSKOPIYA (EFGDS)',
               'TRIPAN BIYOPSIYA USKUNASI',
               'ELEKTROKARDIOGRAFIYA (EKG)',
               'ELEKTROENSEFAL;OGRAFIYA (EEG)',
               'RAQAMLI RENTGEN',
               'S-DUGA RENTGEN',
               'ARTROSKOP',
               'DUODENOSKOP',
               'BRONXOSKOP',
               'GISTEROSKOP',
               'GASTROSKOP',
               'KOLONOSKOP',
               'LAPAROSKOP',
               'MAMMOGRAF',
               'LOR KOMBAYN',
               'TRAKSION KROVAT',
               'ELEKTRO-JARROHLIK USKUNASI',
               'FRAKSION LAZER USKUNASI',
               'FIZIOTERAPIYA USKUNALARI',
               ]
        for i in range(len(nam)):
            Product.objects.create(
                name=nam[i],
                price=((i+2)*70)
            )

        print('Products have created Successfully...!')

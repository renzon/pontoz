from datetime import datetime
from decimal import Decimal
from itertools import cycle

from db.segments import GAS, SUPER
from db.tables import Partner, Session, Region, Store, Transaction

# Partners
posto_flex = Partner(name='Posto Flex', segment=GAS)
posto_noflex = Partner(name='Posto NoFlex', segment=GAS)
fartura = Partner(name='Fartura', segment=SUPER)

session = Session()

session.add(posto_flex)
session.add(posto_noflex)
session.add(fartura)
session.commit()

# Criação de Regionais
regionais_posto_flex = [Region(name='Fortaleza', partner_id=posto_flex.id),
                        Region(name='São Paulo', partner_id=posto_flex.id)]
regional_posto_no_flex = Region(name='Fortaleza', partner_id=posto_noflex.id)
regional_fartura = Region(name='Fortaleza', partner_id=fartura.id)

todas_regionais = list(regionais_posto_flex)
todas_regionais.append(regional_posto_no_flex)
todas_regionais.append(regional_fartura)
session.add_all(todas_regionais)
session.commit()

# Criação de Lojas
lojas_flex_fortaleza = [Store(name=f'Posto {i}', region_id=regionais_posto_flex[0].id) for i in range(1, 3)]
loja_flex_sp = Store(name='Posto 3', region_id=regionais_posto_flex[1].id)
loja_noflex_fortaleza = Store(name='Posto 4', region_id=regional_posto_no_flex.id)
loja_fartura_fortaleza = Store(name='Fartura 5', region_id=regional_fartura.id)

todas_lojas = list(lojas_flex_fortaleza)
todas_lojas.append(loja_flex_sp)
todas_lojas.append(loja_noflex_fortaleza)
todas_lojas.append(loja_fartura_fortaleza)

session.add_all(todas_lojas)
session.commit()

cycle_flex_fortaleza_stores = cycle(lojas_flex_fortaleza)
cycle_days = cycle(range(1, 28))
cycle_hours = cycle(range(1, 23))
cycle_minutes = cycle(range(60))

# Criação de Transações
for month in range(1, 13):
    for _, store, day, hour, minute in zip(range(month), cycle_flex_fortaleza_stores, cycle_days, cycle_hours,
                                           cycle_minutes):
        session.add(
            Transaction(
                store_id=store.id,
                sale=Decimal('1.00'),
                pointz_sale=Decimal('0.00'),
                creation=datetime(2017, month, day, hour, minute)
            )
        )
    for _, store, day, hour, minute in zip(range(month + 12), cycle_flex_fortaleza_stores, cycle_days, cycle_hours,
                                           cycle_minutes):
        session.add(
            Transaction(
                store_id=store.id,
                sale=Decimal('0.00'),
                pointz_sale=Decimal('1.00'),
                creation=datetime(2017, month, day, hour, minute)
            )
        )

# Acrescentando loja de regional sp do posto flex

session.add(
    Transaction(
        store_id=loja_flex_sp.id,
        sale=Decimal('12.00'),
        pointz_sale=Decimal('24.00'),
        creation=datetime(2017, 1, 1, 1, 1)
    )
)

# Acrescentando loja de de fortaleza de posto um ano depois e antes de 2017
for year in [2016, 2018]:
    session.add(
        Transaction(
            store_id=lojas_flex_fortaleza[0].id,
            sale=Decimal('12.00'),
            pointz_sale=Decimal('24.00'),
            creation=datetime(year, 1, 1, 1, 1)
        )
    )

# Acrescentando Outro Parceiro do Segmento GAS
session.add(
    Transaction(
        store_id=loja_noflex_fortaleza.id,
        sale=Decimal('12.00'),
        pointz_sale=Decimal('24.00'),
        creation=datetime(2017, 1, 1, 1, 1)
    )
)
# Acrescentando Outro Parceiro do Segmento SUPER
session.add(
    Transaction(
        store_id=loja_fartura_fortaleza.id,
        sale=Decimal('12.00'),
        pointz_sale=Decimal('24.00'),
        creation=datetime(2017, 1, 1, 1, 1)
    )
)

session.commit()

session.close()

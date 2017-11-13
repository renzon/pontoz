from db.segments import GAS
from db.tables import Partner, Session

posto_flex = Partner(name='Posto Flex', segment=GAS)

session = Session()

session.add(posto_flex)

session.commit()
session.close()

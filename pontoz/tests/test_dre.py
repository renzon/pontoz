from os import path

import pytest


@pytest.fixture(scope='module')
def dre_content():
    curr_dir = path.dirname(__file__)
    project_dir = path.join(curr_dir, '..', '..')
    project_dir = path.abspath(project_dir)
    dre_file_path = path.join(project_dir, 'contrib', 'dre-sample.html')
    dre_file = open(dre_file_path, 'r')
    return '\n'.join(dre_file.readlines())


EXPECTED_CONTENTS = [
    '<title>Posto Flex</title>',
    '<th>Valor da Moeda Base</th>', '<td>R$ 0,018</td>',
    '<th>jan-17</th>',
    '<th>fev-17</th>', '<th>mar-17</th>', '<th>abr-17</th>', '<th>mai-17</th>', '<th>jun-17</th>',
    '<th>jul-17</th>',
    '<th>ago-17</th>', '<th>set-17</th>', '<th>out-17</th>', '<th>nov-17</th>', '<th>dez-17</th>',
    '<th>Total Período</th>',
    '<td>Vendas</td>', '<td>Vendas com Pontoz</td>',
    '% Participação nas Vendas', '1300%', '700%', '500%', '400%', '340%', '300%', '271%', '250%', '233%', '220%',
    '209%', '200%', '285%',
    '(-) Emissão de Moeda Base',
    '<td>R$ 13,86</td>',
    'Investimento / Faturamento',

]

EXPECTED_CONTENTS.extend(f'<td>R$ {i},00</td>' for i in range(1, 25))  # Sales
EXPECTED_CONTENTS.extend(f'<td>R$ 1,{i}</td>' for i in range(10, 22))  # Pontoz Sales
EXPECTED_CONTENTS.extend(f'<td>{i}%</td>' for i in range(3, 9))  # Investimento / Faturamento


@pytest.mark.parametrize(
    'content',
    EXPECTED_CONTENTS

)
def test_dre_content(content, dre_content):
    assert content in dre_content

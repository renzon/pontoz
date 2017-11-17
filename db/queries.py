def get_transactions_with_id_greater_than(id, limit=100):
    """Get transactions grater than id and ordered by id so it can be used to fetch transactions in batch.
    One can fetch the first transaction defined by limit and use the last transaction's id to get the next
    batch:

    Ex:

    result=get_transactions_with_id_greater_than(0)
    while result:
        print(result)
        # Next batch
        id=result[-1].id
        result= get_transactions_with_id_greater_than(id)

    See get_transactions_batches

    :param id: transaction botton limit id
    :param limit: limit of transaction per batch, default is 100
    :return: list for transactions
    """
    return 0

def get_transactions_batches(id, limit=100):
    """Returns batches fo transactions with primary keys greater than id. Each batch has a max of transactions
    defined by limit param

    :param id: bottom stating id
    :param limit: limit of transactions per batch
    :return: iterator where each element is a batch of transactions
    """


if __name__ == '__main__':
    for batch in get_transactions_batches(0):
        print(batch)

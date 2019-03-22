# References:
# https://github.com/Hribek25/IOTA101

import iota
from iota.crypto.addresses import AddressGenerator
from iota.crypto.types import Seed
from pprint import pprint
import time

#node_config = {
#    'url': 'https://nodes.thetangle.org:443',
#    'min_weight_magnitude': 12
#}

node_config = {
    'url': 'https://nodes.devnet.iota.org:443',
    'min_weight_magnitude': 9
}

security_level = 2

def generate_seed():
    return Seed.random()

def generate_addresses(seed, count):
    generator = AddressGenerator(seed=seed, security_level=security_level)
    return generator.get_addresses(0, count) # index, count

def create_data_transaction(address, msg):
    """Creates a meta (data-only) IOTA transaction to an IOTA address
    """
    return iota.ProposedTransaction(address=address, message=iota.TryteString.from_unicode(msg),
             tag=iota.Tag(b'DIECPYOTAWORKSHOP'), value=0)

def create_bundle(transactions):
    """Creates an IOTA bundle from a list of transactions"""
    bundle = iota.ProposedBundle(transactions=transactions)
    bundle.finalize()
    return bundle

def perform_pow(bundle):
    """Performs a proof of work on a bundle"""
    api = iota.Iota(node_config['url'])

    # depth: how many milestones to go in the past
    # Higher value has better network, but requires more resources
    tips = api.get_transactions_to_approve(depth=2)
    att = api.attach_to_tangle(trunk_transaction=tips['trunkTransaction'], # first tip
              branch_transaction=tips['branchTransaction'], # second tip
              trytes=bundle.as_tryte_strings(),
              min_weight_magnitude=node_config['min_weight_magnitude'])

    res = api.broadcast_and_store(att['trytes'])
    return res, att

if __name__ == "__main__":
    seed = generate_seed()
    print('Seed:', seed)
    addresses = generate_addresses(seed, 1)
    pprint(addresses)

    tx = create_data_transaction(addresses[0], 'hello')
    pprint(vars(tx))

    pb = create_bundle([tx])
    print('Bundle hash', pb.hash)

    start = time.time()
    res, att = perform_pow(pb)

    # show what has been broadcasted - hash transaction + nonce (POW)
    print("Final bundle including POW and branch/trunk transactions:")
    for t in att['trytes']:
        pprint(vars(iota.Transaction.from_tryte_string(t)))
        print("")

    print('Broadcast result:')
    pprint(res)

    end = time.time()
    print('Elapsed Time:', end - start, 's')
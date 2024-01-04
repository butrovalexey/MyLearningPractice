import web3
import json

class poliklinika() :
    ganache_url = "HTTP://127.0.0.1:8545"
    w3 = web3.Web3(web3.HTTPProvider(ganache_url))

    address_contract = '0xd9145CCE52D386f254917e481eB44e9943F39138'
    address_contract = web3.Web3.to_checksum_address('0xd9145CCE52D386f254917e481eB44e9943F39138')
    with open("abi.json", "r") as file:
        abi = json.load(file)

    contract = w3.eth.contract(address = address_contract, abi = abi)

    def __init__(self):
        pass

    def patient_registration(self, address, pat_name):
        self.contract.functions.patient_registration(address, pat_name).transact({'from': "0xd9145CCE52D386f254917e481eB44e9943F39138"})

    def doctor_registration(self, address, doc_name, specialization):
        self.contract.functions.doctor_registration(address, doc_name, specialization).transact({'from': "0xd9145CCE52D386f254917e481eB44e9943F39138"})

    def doctor_appointment(self, adres1, adres2, time, diag, ill_nam):
        self.contract.functions.doctor_appointment(adres1, adres2, time, diag, ill_nam).transact({'from': "0xd9145CCE52D386f254917e481eB44e9943F39138"})

    def ill_statistics(self, what_diagnose):
        return self.contract.functions.ill_statistics(what_diagnose).call()

    def print_info(self, special):
        return self.contract.functions.print_info(special).call()

Pol = poliklinika()

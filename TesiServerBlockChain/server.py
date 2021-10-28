import flwr as fl
from typing import *
import numpy as np
from datetime import datetime
from cryptography.fernet import Fernet
from flwr.common import parameters_to_weights
from encrypting import encrypt
import os
import pymongo, json
import requests as r
NUM_OF_ROUNDS = 6

class CustomStrategy(fl.server.strategy.FedAvg):
    def aggregate_fit(
        self,
        rnd: int,
        results: List[Tuple[fl.server.client_proxy.ClientProxy, fl.common.FitRes]],
        failures: List[BaseException],
    ) -> Optional[fl.common.Weights]:
        aggregated_weights = super().aggregate_fit(rnd, results, failures)
        return aggregated_weights


    def aggregate_evaluate(
        self,
        rnd: int,
        results: List[Tuple[fl.server.client_proxy.ClientProxy, fl.common.EvaluateRes]],
        failures: List[BaseException],
    ) -> Optional[float]:
        """Aggregate evaluation losses using weighted average."""
        if not results:
            return None

        # Weigh accuracy of each client by number of examples used
        accuracies = [r.metrics["accuracy"] * r.num_examples for _, r in results]
       
        examples = [r.num_examples for _, r in results]

        # Aggregate and print custom metric
        accuracy_aggregated = sum(accuracies) / sum(examples)
        print(f"Round {rnd} accuracy aggregated from client results: {accuracy_aggregated}")
        # Call aggregate_evaluate from base class (FedAvg)
        return super().aggregate_evaluate(rnd, results, failures)

strategy = CustomStrategy()
print("+++++++++++++++++++++++++++++++++++++++++++++")
print("*                                           *")
print("*                Avvio il sever             *")
print("*                                           *")
print("+++++++++++++++++++++++++++++++++++++++++++++\n")
fl.server.start_server('192.168.37.137:5040',config={"num_rounds": NUM_OF_ROUNDS}, strategy= strategy)

encrypt('parametri_client0.npz')
encrypt('parametri_client1.npz')
print("File criptati")

print("Salvo la chiave in blockchain")

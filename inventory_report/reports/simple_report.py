from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(products: list):
        fabrication_date = min(
            [product["data_de_fabricacao"] for product in products]
        )

        today = datetime.now().isoformat()

        valid_date = min(
            [product["data_de_validade"]
                for product in products
                if product["data_de_validade"] > today]
        )

        company, _ = Counter(
            [product["nome_da_empresa"] for product in products]
        ).most_common()[0]

        return (
            f"Data de fabricação mais antiga: {fabrication_date}\n"
            f"Data de validade mais próxima: {valid_date}\n"
            f"Empresa com mais produtos: {company}"
        )

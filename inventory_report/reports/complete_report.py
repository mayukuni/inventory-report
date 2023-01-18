from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:
    @staticmethod
    def generate(list: list):
        simple_report = SimpleReport.generate(list)

        products = {}
        for product in list:
            if product["nome_da_empresa"] in products:
                products[product["nome_da_empresa"]] += 1
            else:
                products[product["nome_da_empresa"]] = 1

            stock_products = ''
        for key, value in products.items():
            stock_products += f"- {key}: {value}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{stock_products}"
        )

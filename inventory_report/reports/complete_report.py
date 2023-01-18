from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport:
    @staticmethod
    def generate(list):
        simple_report = SimpleReport.generate(list)
        
        products = Counter(item['nome_da_empresa'] for item in list)
        
        stock_products = ''
        for company in products:
            stock_products += f"{company}: {products[company]}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{stock_products}"
        )
        

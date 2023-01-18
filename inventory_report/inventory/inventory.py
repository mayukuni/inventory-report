from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @staticmethod
    def import_data(path, type):
        data = []
        if "csv" in path:
            with open(path, encoding="utf-8") as file:
                data = list(csv.DictReader(file))
        elif "json" in path:
            with open(path) as file:
                data = json.load(file)

        if type == 'simples':
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)

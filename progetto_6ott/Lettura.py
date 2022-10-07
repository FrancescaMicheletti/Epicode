import csv
import json


def read_csv_as_dict(file_path):
    """
    Legge un file CSV e inserisce i dati in un dizionario
    :param file_path: file path of csv
    :return: data read from file
    """
    with open(file_path, mode='r') as csv_file:
        data = csv.DictReader(csv_file)
    return data


def read_csv_as_list(file_path, delimiter=","):
    """
    Legge un file CSV e inserisce i dati in una lista di liste (lista di righe)
    :param file_path: file path of csv
    :param delimiter: delimiter used in the csv file
    :return: data read from file
    """
    with open(file_path) as csv_file:
        data = csv.reader(csv_file, delimiter=delimiter)
    return data


def read_json(file_path):
    """
    Legge un file JSON e inserisce i dati in un dizionario
    :param file_path: file path of json
    :return: data read from file
    """
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


if __name__ == '__main__':
    read_csv_as_dict('/scrivere/il/percorso/del/file/csv')
    read_csv_as_list('/scrivere/il/percorso/del/file/csv', ',')
    read_json('/scrivere/il/percorso/del/file/json')
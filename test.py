import csv
import subprocess
import shlex

TRAINING_DATA_FILENAME = 'test.json'


def index():

    # get all ids from index file
    with open("/Users/Nick/Develop/Git/discovery/_docs/index.csv", newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        index_ids = [row[0] for row in csv_reader]

    return index_ids


def train():
    # get all ids in training csv
    with open("/Users/Nick/Develop/Git/discovery/_docs/training.csv", newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        train_ids = [[row[i] for i in range(1, len(row), 2) if row[i]] for row in csv_reader]

    return train_ids


def runtest():
    train_ids = train()
    ids = [l for s in train_ids for l in s]

    for x in set(ids):

        curl_cmd = 'curl -u "75f48542-23da-4e17-a5ed-af780c16cc92":"q6e5a4U4nsqS" "https://gateway.watsonplatform.net/discovery/api/v1/environments/af3e2cb0-4fee-419a-933c-256a0d473266/collections/bb18e626-4fda-4989-b8b5-44095c2cd542/documents/{}?version=2017-09-01"'.format(x)

        process = subprocess.Popen(shlex.split(curl_cmd), stdout=subprocess.PIPE)
        output = process.communicate()

        print(output)

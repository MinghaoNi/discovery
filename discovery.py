#!/usr/bin/env python3
# [pep8] max-line-length = 120
import os
import csv
import json
import subprocess
import time
import shlex

# TODO: Replace with your own credentials
CRENDIALS = {'username': '75f48542-23da-4e17-a5ed-af780c16cc92',
             'password': 'q6e5a4U4nsqS'}

VERSON = '2017-09-01'
BASE_URL = 'https://gateway.watsonplatform.net/discovery/api'


def upload(csv_file, environment_id, collection_id, debug=False):
    """upload csv file to collection
    **PLEASE CHECK THE ENCODING OF CSV FILE.**
    It is ALWAYS a good practise to save a csv/txt file in UTF-8 encoding.

    :param csv_file: path of csv file
    :type csv_file: string of directory
    :param environment_id: id of environment to upload to
    :type environment_id: string
    :param collection_id: id of collection to upload to
    :type collection_id: string
    """

    ADD_DOCUMNET_URL = '/v1/environments/{}/collections/{}/documents'.format(environment_id, collection_id)

    # open the csv file
    row_upload_file = 'row.json'
    with open(csv_file, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')

        for row in csv_reader:

            dict_row = {'id': row[0],
                        'question': row[1],
                        'answer': row[2]}
            json_row = json.dumps(dict_row)
            # save each row as a json file, row.json
            with open(row_upload_file, 'w') as uploadfile:
                uploadfile.write(json_row)

            # generate curl command
            url = BASE_URL + ADD_DOCUMNET_URL + '/{}?version={}'\
                .format(dict_row['id'], VERSON)

            curl_cmd = 'curl -X POST -u "{}":"{}" -F file=@{} "{}"'\
                       .format(CRENDIALS['username'], CRENDIALS['password'], row_upload_file, url)

            # upload row
            print("**Upload Q&A: {}**".format(dict_row['id']))
            process = subprocess.Popen(shlex.split(curl_cmd), stdout=subprocess.PIPE)
            output = process.communicate()

            if debug:
                print(output)

            time.sleep(0.1)

    print("**Upload Successfully!**")
    # remove temporary json file
    if os.path.exists(row_upload_file):
        os.remove(row_upload_file)
        print("Temporary File {} Removed!".format(row_upload_file))


def train(csv_file, environment_id, collection_id, debug=False):
    """upload csv file to train the discovery
    **PLEASE CHECK THE ENCODING OF CSV FILE.**
    It is ALWAYS a good practise to save a csv/txt file in UTF-8 encoding.

    :param csv_file: path of csv file
    :type csv_file: string of directory
    :param environment_id: id of environment to upload to
    :type environment_id: string
    :param collection_id: id of collection to upload to
    :type collection_id: string
    """

    TRAIN_URL = '/v1/environments/{}/collections/{}/training_data?version={}'.\
                format(environment_id, collection_id, VERSON)

    train_query_file = 'train.json'
    url = BASE_URL + TRAIN_URL
    with open(csv_file, newline='') as csvfile:
        question_relevance = csv.reader(csvfile, delimiter=',')

        # upload training data
        print("Uploading Training Data ...")
        for row in question_relevance:
            train_query = {'natural_language_query': row[0].replace(r"'", r"\'"),
                           'examples': [{'document_id': row[i],
                                         'relevance': int(row[i+1])}
                                        for i in range(1, len(row), 2) if row[i]]}

            with open(train_query_file, 'w') as train_file:
                json.dump(train_query, train_file)

            curl_cmd = 'curl -X POST -u "{}":"{}" -H "Content-Type: application/json" -d@{} "{}"'\
                       .format(CRENDIALS['username'], CRENDIALS['password'], train_query_file, url)

            process = subprocess.Popen(shlex.split(curl_cmd), stdout=subprocess.PIPE)
            output = process.communicate()

            if debug:
                print(output)

            time.sleep(0.1)

    print("Training Data Upload Complete!")
    # remove temporary json file
    if os.path.exists(train_query_file):
        os.remove(train_query_file)
        print("Temporary File {} Removed!".format(train_query_file))


if __name__ == '__main__':

    upload(csv_file='_docs/index.csv',
           environment_id='af3e2cb0-4fee-419a-933c-256a0d473266',
           collection_id='33d51e38-40f4-4355-bb0e-a81619d137b3')

    train(csv_file='_docs/training.csv',
          environment_id='af3e2cb0-4fee-419a-933c-256a0d473266',
          collection_id='33d51e38-40f4-4355-bb0e-a81619d137b3')

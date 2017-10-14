#!/usr/bin/env python3
# max-line-length = 120
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

            dict_row = {'id': int(row[0]),
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


if __name__ == '__main__':

    upload(csv_file='_docs/index.csv',
           environment_id='af3e2cb0-4fee-419a-933c-256a0d473266',
           collection_id='6072d7a3-91cb-4bbb-b6eb-597916af93c4')

#!/usr/bin/python
import argparse
import json
import requests
import sys


def main():
    with open(FLAGS.schema_file_path, 'r') as reader:
        schema = reader.read().replace('\n', '').replace("'", '')
        schema = schema.replace('"', r'\"')
        myobj = '{ "schema": "' + schema + '"}'

        headers = {'content-type': 'application/vnd.schemaregistry.v1+json'}

        x = requests.post('{url}/subjects/{topic}/versions'.format(url=FLAGS.schema_registry_url, topic=FLAGS.topic_name), data = myobj, headers=headers)

        print(x.text)
   
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--schema_registry_url',
                        type=str,
                        help="URL do Schema Registry.",
                        default='http://192.168.2.93:8081')
    parser.add_argument('--topic_name',
                        type=str,
                        default='topic-test')
    parser.add_argument('--schema_file_path',
                        type=str,
                        help="Path absoluto para o arquivo de schema avsc.",
                        default='C:\\development\\schema-registry-utils\\t_xomni_soe.avsc')
    parser.add_argument('--schema_type',
                        type=str,
                        default='AVRO')
    FLAGS, unparsed = parser.parse_known_args()

    main()
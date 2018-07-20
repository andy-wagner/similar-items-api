#!/usr/bin/env python3

import connexion
import nltk
from app import encoder


def main():
    nltk.download('punkt')
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={
        'title': 'similar items API'})
    app.run(server='tornado', port=8080)


if __name__ == '__main__':
    print("Starting App ...")
    main()

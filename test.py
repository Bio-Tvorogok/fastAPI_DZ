import json
import requests


def test():
    result = requests.post('http://127.0.0.1:8000/data', data=json.dumps({'foo': 'bar'}))
    assert result.status_code == 201

    result = requests.post('http://127.0.0.1:8000/data', data='{error')
    assert result.status_code == 400


if __name__ == '__main__':
    test()

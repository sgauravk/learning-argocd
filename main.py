from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/<username>', methods=['GET'])
def user_gists(username):
    page = request.args.get('page', default = 1, type=int)
    per_page = request.args.get('per_page', default = 10, type=int)

    try:
        response = requests.get(f'https://api.github.com/users/{username}/gists?page={page}&per_page={per_page}')
        response_body = response.json()
        return jsonify(response_body), response.status_code

    except requests.exceptions.RequestException as error:
        return jsonify({"error": str(error)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

from flask import Flask, request, jsonify
import tiktoken

app = Flask(__name__)

def num_tokens_from_string(string: str, encoding_name: str) -> int:
  """Returns the number of tokens in a text string."""
  encoding = tiktoken.get_encoding(encoding_name)
  num_tokens = len(encoding.encode(string))
  return num_tokens

@app.route('/tokens', methods=['POST'])
def get_num_tokens():
  data = request.get_json()
  text = data.get('text', '')

  # Use the provided encoding or default to 'cl100k_base'
  encoding_name = data.get('encoding', 'cl100k_base')

  tokens_count = num_tokens_from_string(text, encoding_name)
  return jsonify(tokens=tokens_count)

if __name__ == "__main__":
  app.run(host="0.0.0.0")

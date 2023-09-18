# 🔢 TikToken Web Service

A lightweight Flask-based web service that leverages the `tiktoken` library to count the number of tokens in a given text string. Especially useful for understanding text input sizes in the context of OpenAI API limits.

## 🚀 Features
- Token counting using `tiktoken`.
- Default token model: `cl100k_base`.
- Containerized deployment using Docker.

## 🛠️ Installation

### Requirements
- Python 3.9+
- Docker

### Setup & Running Locally

1. Clone the repository.

2. Build the Docker image:
   ```bash
   docker build -t tiktoken-service .
   ```

3. Run the service:
   ```bash
   docker run -p 5000:5000 tiktoken-service
   ```

The service should now be running at `http://localhost:5000`.

## 📝 API Usage

**Endpoint**: `POST /tokens`

**Payload**:
```json
{
    "text": "Your text here",
    "encoding": "optional_encoding_name"
}
```

**Response**:
```json
{
    "tokens": token_count
}
```

*Note*: If you don't specify an encoding, it defaults to `cl100k_base`.

## 🧪 Testing

We use `pytest` for unit testing. To run tests:

1. Ensure you have pytest installed:
   ```bash
   pip install pytest
   ```

2. Run the tests:
   ```bash
   pytest tests/
   ```

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 🙏 Acknowledgments

Thanks to OpenAI for the `tiktoken` library and the community for valuable inputs.

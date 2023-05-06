# This example doesn't use openai library. However, using the openai package has its own advantages:
# - Easier integration with OpenAI API features, as it's the official package.
# - Built-in error handling and request/response formatting.
# - Simplified usage, without the need to manage URLs and headers manually.
import requests
import os
import re
import textwrap
import threading
import json

# Get your API key from the environment variable
api_key = os.environ["OPENAI_API_KEY"]

# Define the base URL for the OpenAI API
base_url = "https://api.openai.com/v1/chat/completions"

def comment_callback(address, view, response):
    response = "\n".join(textwrap.wrap(response, 80, replace_whitespace=False))
    print(response)
    print("done!")

def query_model(query, cb, max_tokens=2500, model_name='gpt-3.5-turbo', temperature=0):
    """
    Function which sends a query to gpt-3.5-turbo and calls a callback when the response is available.
    Blocks until the response is received
    :param query: The request to send to gpt-3.5-turbo
    :param cb: Tu function to which the response will be passed to.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "messages": [
            {"role": "user", "content": query}
        ],
        "model": model_name,
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    try:
        response = requests.post(base_url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()

        print(str(response_json["choices"][0]['message']["content"]))

        print('-------------------------------- DEBUG --------------------------------')
        print(response_json)

    except requests.exceptions.HTTPError as e:
        # Handle specific error cases here, such as context length exceeded
        print(("ChatGPT could not complete the request: {error}").format(error=str(e)))
        return

    except requests.exceptions.RequestException as e:
        print(("ChatGPT could not complete the request: {error}").format(error=str(e)))
        return

# -----------------------------------------------------------------------------

def query_model_async(query, cb):
    t = threading.Thread(target=query_model, args=[query, cb])
    t.start()

    # what conditionals for this code snippet:

if __name__ == '__main__':
    query_model_async('''
    I have the following code : 
    ```python
      with ThreadPoolExecutor(max_workers=threads) as self.__pool:
            for anydesk_id in self.__ids:
                future = self.__pool.submit(self.__check_id, anydesk_id)
                results.append(future)

            for f in as_completed(results):
                anydesk_id, status = f.result()
                if status:
                    with open(self._OUTPUT_FILES[status], "a+") as f:
                        f.write(    str(anydesk_id))
    ```                        
    How to recall `__check_id` function if it failed?
    ''', cb=comment_callback)
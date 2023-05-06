import openai
import re
import textwrap
import threading
import json

# Set your API key here, or put in in the OPENAI_API_KEY environment variable.
openai.api_key = os.environ["OPENAI_API_KEY"]

def comment_callback(address, view, response):
    response = "\n".join(textwrap.wrap(response, 80, replace_whitespace=False))
    print(response)
    print("done!")


def query_model(query, cb, max_tokens=2500, model_name="gpt-3.5-turbo"):
    """
    Function which sends a query to gpt-3.5-turbo and calls a callback when the response is available.
    Blocks until the response is received
    :param query: The request to send to gpt-3.5-turbo
    :param cb: Tu function to which the response will be passed to.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[
                {"role": "user", "content": query}
            ]
        )

        print(str(response["choices"][0]['message']["content"]))

        print('-------------------------------- DEBUG --------------------------------')
        print(response)


    except openai.InvalidRequestError as e:
        # Context length exceeded. Determine the max number of tokens we can ask for and retry.
        m = re.search(r'maximum context length is (\d+) tokens, however you requested \d+ tokens \((\d+) in your '
                      r'prompt;', str(e))
        if not m:
            print(("ChatGPT could not complete the request: {error}").format(error=str(e)))
            return
        (hard_limit, prompt_tokens) = (int(m.group(1)), int(m.group(2)))
        max_tokens = hard_limit - prompt_tokens
        if max_tokens >= 750:
            print(_("Context length exceeded! Reducing the completion tokens to "
                    "{max_tokens}...").format(max_tokens=max_tokens))
            query_model(query, cb, max_tokens)
        else:
            print("Unfortunately, this function is too big to be analyzed with the model's current API limits.")

    except openai.OpenAIError as e:
        print(("ChatGPT could not complete the request: {error}").format(error=str(e)))
    except Exception as e:
        print(("General exception encountered while running the query: {error}").format(error=str(e)))

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
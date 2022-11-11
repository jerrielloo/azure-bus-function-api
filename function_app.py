# function_app.py
import azure.functions as func


@app.write_blob(arg_name="msg", path="output-container/{name}",
                connection="AzureWebJobsStorage")

def test_function(req: func.HttpRequest,
                  msg: func.Out[str]) -> str:

    message = req.params.get('body')
    msg.set(message)
    return message
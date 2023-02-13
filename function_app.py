import azure.functions as func
import logging
import keywords_extraction
import image_creation

app = func.FunctionApp()

# Learn more at aka.ms/pythonprogrammingmodel

# Get started by running the following code to create a function using a HTTP trigger.

@app.function_name(name="hello")
@app.route(route="helloworld", auth_level=func.AuthLevel.ANONYMOUS)
def helloworld(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
            "Hello World, call this api by appending parameter 'name={your name}' ",
            status_code=200
        )

@app.function_name(name="keywords")
@app.route(route="keywords", auth_level=func.AuthLevel.ANONYMOUS)
def extract_keywords(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    text = req.params.get('text')
    if not text:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            text = req_body.get('text')

    if text:
        keywords = keywords_extraction.extract_keywords(text=text)
        return func.HttpResponse("{ keywords:" + keywords + "}")
    else:
        return func.HttpResponse(
             "No text found in request body",
             status_code=200
        )

@app.function_name(name="image")
@app.route(route="image", auth_level=func.AuthLevel.ANONYMOUS)
def extract_keywords(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    description = req.params.get('description')
    if not description:
        try:
           req_body = req.get_json()
        except ValueError:
            pass
        else:
            description = req_body.get('description')
    if description:
        image_url = image_creation.create_Image(description=description)
        return func.HttpResponse("{ image_url:" + image_url + "}")
    else:
        return func.HttpResponse(
             "No description found in request body, cannot generate image",
             status_code=200
        )

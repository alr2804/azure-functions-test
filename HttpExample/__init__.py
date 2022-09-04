import logging

import azure.functions as func
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    

    name = req.params.get('name')
    url = req.params.get('url')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
            url = req_body.get('url')
    
    if url:
        logging.info("sample test case started")
        driver = webdriver.Chrome("./driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(url)
        s = driver.title
        driver.close()

        return func.HttpResponse("Page title: " + s)
    
    else:
        if name:
            return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
        else:
            return func.HttpResponse(
                "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
                status_code=200
            )

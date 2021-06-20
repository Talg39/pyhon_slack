import sys
import requests
import validators


def is_valid(val):
    valid = validators.url(val)
    if valid:
        return True
    else:
        return False


def get_url(url):
    try:
        results = requests.head(url)
        return results
    except:
        print("===== Something went wrong, we couldn't get url status =====")
        sys.exit()


def decipher_status(statusCode):
    switcher = {
        200: "OK",
        301: "Permanent Redirect - 301",
        302: "Temporary Redirect - 302",
        404: "Not Found - 404",
        410: "Gone - 410",
        500: "Internal Server Error - 500",
        503: "Service Unavailable - 503"
    }
    # print(switcher.get(statusCode, "Status code is not recognized as valid"))
    return switcher.get(statusCode)

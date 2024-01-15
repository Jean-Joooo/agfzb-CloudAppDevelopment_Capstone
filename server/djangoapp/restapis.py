import requests
import json
from .models import CarDealer
from requests.auth import HTTPBasicAuth

def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)

    return results


# Create a `post_request` to make HTTP POST requests
def post_request(url, json_payload, **kwargs):
    url =  "https://jeanjosephag-5000.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/api/post_review"
    response = requests.post(url, params=kwargs, json=json_payload)
    return response

def get_dealer_reviews_from_cf(url, **kwargs):
    results = []
    id = kwargs.get("id")
    if id:
        json_result = get_request(url, id=id)
    else:
        json_result = get_request(url)
    print(json_result, "96")
    if json_result:
        if isinstance(json_result, list):  # Check if json_result is a list
            reviews = json_result
        else:
            reviews = json_result["data"]["docs"]

        # Check if 'reviews' is a list of one dictionary
        if isinstance(reviews, list) and len(reviews) == 1 and isinstance(reviews[0], dict):
            reviews = reviews[0]

        for dealer_review in reviews:
            print("dealer_review--------------------", dealer_review)  # Print dealer_review
            if isinstance(dealer_review, str):  # Check if dealer_review is a string
                try:
                    dealer_review = json.loads(dealer_review)
                except json.JSONDecodeError:
                    continue  # Skip this iteration if the JSON decoding fails

            review_obj = DealerReview(
                dealership=dealer_review.get("dealership"),
                name=dealer_review.get("name"),
                purchase=dealer_review.get("purchase"),
                review=dealer_review.get("review"),
                purchase_date=dealer_review.get("purchase_date"),
                car_make=dealer_review.get("car_make"),
                car_model=dealer_review.get("car_model"),
                car_year=dealer_review.get("car_year"),
                sentiment='',
                id=dealer_review.get("id")
            )

            sentiment = analyze_review_sentiments(review_obj.review)
            print(sentiment)
            review_obj.sentiment = sentiment
            results.append(review_obj)

    return results

    # def get_dealer_by_id_from_cf(url, dealerId):

def get_dealer_by_id_from_cf(url, id):
    json_result = get_request(url, id=id)
    # print('json_result from line 54',json_result)

    if json_result:
        dealers = json_result
        dealer_doc = dealers[0]
        dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"],
                                id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"], full_name=dealer_doc["full_name"],
                                st=dealer_doc["st"], zip=dealer_doc["zip"], short_name=dealer_doc.get("short_name"))
    return dealer_obj


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative
import http.client
import json
import Models

with open('survey.json', 'r') as f:
    payload = json.load(f)

survey = Models.Survey()
for survey_title, survey_data in payload.items():
    survey.title = survey_title
    survey.pages = []
    for page_title, page_data in survey_data.items():
        page = Models.Page()
        page.title = page_title
        page.questions = []
        survey.pages.append(page)
        for question_title, question_data in page_data.items():
            question = Models.Question()
            question.title = question_title
            question.description = question_data["Description"]
            question.answers = question_data["Answers"]
            page.questions.append(question)

# Convert the survey object back to JSON
survey_json = json.dumps(survey, default=lambda o: o.__dict__, indent=2)
print(survey_json)

# Establish connection and send HTTP request
conn = http.client.HTTPSConnection("api.surveymonkey.com")
access_token = ("tOt-QCvM5tKO73Krcx3Kwekc9nCmSm82KvuKtbZnIRIwNBklRJ9nl89uo5G0ltp7S99kJHH1ctKmUxzhSwxMeUxWeXtea0TY1vXCgVUyQACiKDS8IKwAJsONwSuyDcAq")

headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Authorization': f"Bearer {access_token}"
}

conn.request("POST", "/v3/surveys", json.dumps(payload), headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

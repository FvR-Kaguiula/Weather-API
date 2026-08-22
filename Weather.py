import requests

url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

querystring = {"EXAMPLECOORDS"}

headers = {
	"x-rapidapi-key": "EXAMPLEAPIACCESS",
	"x-rapidapi-host": "weatherbit-v1-mashape.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

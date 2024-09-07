import requests

url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

querystring = {"lon":"38.5","lat":"-78.5","units":"imperial","lang":"en"}

headers = {
	"x-rapidapi-key": "dd44b94613msh2c82005f6597c3fp17fafcjsnf6fe00f40a2c",
	"x-rapidapi-host": "weatherbit-v1-mashape.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

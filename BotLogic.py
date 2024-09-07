def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


def get_weather_info_url():    
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"
    querystring = {"lat":"35.5","lon":"-78.5","units":"imperial","lang":"es"}
    headers = {
	"x-rapidapi-key": "dd44b94613msh2c82005f6597c3fp17fafcjsnf6fe00f40a2c",
	"x-rapidapi-host": "weatherbit-v1-mashape.p.rapidapi.com"
}
    res = requests.get(url, headers=headers, params=querystring)
    data = res.json()
    return data

import asyncio
from pyppeteer import launch
import sys
from geopy import geocoders
from bs4 import BeautifulSoup
from prettytable import PrettyTable



def windy(place):
    """
    Validation of the input and function calls
    """

    base_url = f'https://www.windy.com/'
    latitude, longitude = get_lat_long(place)
    base_url = base_url + f"{latitude}/{longitude}/"
    asyncio.get_event_loop().run_until_complete(main(base_url))



def get_lat_long(place):
    """
    Parameters : name of the place
    Action : To return the lattitude and longitude of a given place.
    """
    try:
        gn = geocoders.GeoNames(username = "ganeshprasadbg")
        place_details = gn.geocode(place)
    except Exception as e:
        raise ValueError("Geopy Timeout Exception, Try Again in a bit")
    if place_details == None:

        raise ValueError("Invalid Place Name")
    print("*" * 30)
    print("Place : ", place_details)
    print("Latitude", place_details.latitude)
    print("Longitude", place_details.longitude)
    return str(round(place_details.latitude,3)), str(round(place_details.longitude,3))

def get_hour_wise_data(hours, temperatures, winds):
    """
    Parameters : Unsorted Hour, Temperature and wind
    Action : Sort received data based on hour of the day
    output : Sorted data based on hour of the day
    """

    total_hours = []
    daily_hour = []

    total_temperature = []
    daily_temperature = []

    total_wind = []
    daily_wind = []

    for hour, temperature, wind in zip(hours, temperatures, winds):

        if str(hour).startswith("0AM"):

            total_hours.append(daily_hour)
            daily_hour = []
            daily_hour.append(str(hour))

            total_temperature.append(daily_temperature)
            daily_temperature = []
            daily_temperature.append(str(temperature))

            total_wind.append(daily_wind)
            daily_wind = []
            daily_wind.append(str(wind))
        else:

            daily_hour.append(str(hour))
            daily_temperature.append(str(temperature))
            daily_wind.append(str(wind))

    total_hours.append(daily_hour)
    total_temperature.append(daily_temperature)
    total_wind.append(daily_wind)

    return total_hours, total_temperature, total_wind


async def main(base_url):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(base_url)

    grab_element = await page.waitForSelector('.forecast-table')
    grab_html = await page.evaluate('(element) => element.innerHTML', grab_element)

    data = []
    soup = BeautifulSoup(grab_html, features= 'lxml')
    table = soup.find('table', attrs={"class" : "grab"})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    if len(data[0]) == 0 :
        raise Exception("pyppeteer.errors.NetworkError: Protocol error Runtime.callFunctionOn: Target closed, Please Retry")


    days = data[0]
    total_hours, total_temperature, total_wind = get_hour_wise_data(data[1],data[3],data[5])

    for day, hour, temperature, wind in zip(days, total_hours, total_temperature, total_wind):
        print(f"\n On {day}: \n")
        t = PrettyTable(["Hour"]+hour)
        t.add_row(["Temperature (celcius)"]+temperature)
        t.add_row(["Wind (knots)"]+wind)
        print(t)


    await browser.close()

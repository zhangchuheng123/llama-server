import requests

message = """
You are an HVAC administrator. Your primary objective is to fine-tune the actions to maintain the temperature in each room close to the target temperature, while maximizing the rewards as many as possible.

Currently, outside temperature is lower than the target temperature 22 degree Celsius. To optimize HVAC control, adhere to the following guidelines:
1. Actions should be represented as a list, with each integer value ranging from 0 to 100.
2. The length of the actions list should correspond to the number of rooms, arranged in the same order.
3. If room temperature is higher than the target temperature, the larger the difference between room temperature and the target temperature, the lower the action should be.
4. If room temperature is lower than the target temperature, the larger the difference between room temperature and the target temperature, the higher the action should be.
5. You could find the best actions room by room.
For your reference, 4 demonstrations from experts are provided below.

        Expert Demonstration 1 
        Description: 
    You are the HVAC administrator responsible for managing a building of type OfficeLarge located in PortAngeles, where the climate is Cold and Dry. 

    The building has 23 rooms in total.
    Currently, temperature in each room is as follows:
       Room 1: -19 degrees Celsius 
       Room 2: -3 degrees Celsius 
       Room 3: -26 degrees Celsius 
       Room 4: -20 degrees Celsius 
       Room 5: -30 degrees Celsius 
       Room 6: -9 degrees Celsius 
       Room 7: -13 degrees Celsius 
       Room 8: -35 degrees Celsius 
       Room 9: -8 degrees Celsius 
       Room 10: 2 degrees Celsius 
       Room 11: -31 degrees Celsius 
       Room 12: -20 degrees Celsius 
       Room 13: -36 degrees Celsius 
       Room 14: -4 degrees Celsius 
       Room 15: -2 degrees Celsius 
       Room 16: -24 degrees Celsius 
       Room 17: -20 degrees Celsius 
       Room 18: -35 degrees Celsius 
       Room 19: -10 degrees Celsius 
       Room 20: -18 degrees Celsius 
       Room 21: -25 degrees Celsius 
       Room 22: -16 degrees Celsius 
       Room 23: 21 degrees Celsius 
    The external climate conditions are as follows:
       Outside Temperature: 3 degrees Celsius. 
       Global Horizontal Irradiance: 0 
       Ground Temperature: 9 degrees Celsius
       Occupant Power: 0 KW 
       Target Temperature: 22 degrees Celsius 

        Actions: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        Outcomes: After taking the above actions, temperature in each room becomes: 
       Room 1: 5 degree Celsius 
       Room 2: 7 degree Celsius 
       Room 3: 3 degree Celsius 
       Room 4: 5 degree Celsius 
       Room 5: 6 degree Celsius 
       Room 6: 5 degree Celsius 
       Room 7: 10 degree Celsius 
       Room 8: 11 degree Celsius 
       Room 9: 3 degree Celsius 
       Room 10: 2 degree Celsius 
       Room 11: 4 degree Celsius 
       Room 12: 5 degree Celsius 
       Room 13: 4 degree Celsius 
       Room 14: 8 degree Celsius 
       Room 15: 10 degree Celsius 
       Room 16: 3 degree Celsius 
       Room 17: 2 degree Celsius 
       Room 18: 4 degree Celsius 
       Room 19: 6 degree Celsius 
       Room 20: 4 degree Celsius 
       Room 21: 8 degree Celsius 
       Room 22: 10 degree Celsius 
       Room 23: 3 degree Celsius 
The action for Room 1 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 2 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 3 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 4 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 5 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 6 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 7 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 8 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 9 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 10 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 11 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 12 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 13 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 14 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 15 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 16 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 17 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 18 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 19 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 20 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 21 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 22 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 23 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 


        Expert Demonstration 2 
        Description: 
    You are the HVAC administrator responsible for managing a building of type OfficeLarge located in PortAngeles, where the climate is Cold and Dry. 

    The building has 23 rooms in total.
    Currently, temperature in each room is as follows:
       Room 1: -18 degrees Celsius 
       Room 2: 16 degrees Celsius 
       Room 3: 19 degrees Celsius 
       Room 4: -9 degrees Celsius 
       Room 5: 17 degrees Celsius 
       Room 6: -2 degrees Celsius 
       Room 7: 19 degrees Celsius 
       Room 8: 5 degrees Celsius 
       Room 9: 0 degrees Celsius 
       Room 10: -18 degrees Celsius 
       Room 11: -38 degrees Celsius 
       Room 12: 16 degrees Celsius 
       Room 13: -36 degrees Celsius 
       Room 14: 10 degrees Celsius 
       Room 15: 11 degrees Celsius 
       Room 16: -11 degrees Celsius 
       Room 17: -7 degrees Celsius 
       Room 18: 12 degrees Celsius 
       Room 19: -30 degrees Celsius 
       Room 20: -5 degrees Celsius 
       Room 21: -9 degrees Celsius 
       Room 22: -11 degrees Celsius 
       Room 23: 19 degrees Celsius 
    The external climate conditions are as follows:
       Outside Temperature: 3 degrees Celsius. 
       Global Horizontal Irradiance: 0 
       Ground Temperature: 9 degrees Celsius
       Occupant Power: 0 KW 
       Target Temperature: 22 degrees Celsius 

        Actions: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        Outcomes: After taking the above actions, temperature in each room becomes: 
       Room 1: 9 degree Celsius 
       Room 2: 11 degree Celsius 
       Room 3: 9 degree Celsius 
       Room 4: 11 degree Celsius 
       Room 5: 12 degree Celsius 
       Room 6: 11 degree Celsius 
       Room 7: 15 degree Celsius 
       Room 8: 17 degree Celsius 
       Room 9: 8 degree Celsius 
       Room 10: 7 degree Celsius 
       Room 11: 9 degree Celsius 
       Room 12: 10 degree Celsius 
       Room 13: 9 degree Celsius 
       Room 14: 12 degree Celsius 
       Room 15: 14 degree Celsius 
       Room 16: 7 degree Celsius 
       Room 17: 7 degree Celsius 
       Room 18: 8 degree Celsius 
       Room 19: 10 degree Celsius 
       Room 20: 8 degree Celsius 
       Room 21: 12 degree Celsius 
       Room 22: 14 degree Celsius 
       Room 23: 7 degree Celsius 
The action for Room 1 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 2 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 3 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 4 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 5 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 6 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 7 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 8 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 9 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 10 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 11 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 12 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 13 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 14 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 15 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 16 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 17 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 18 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 19 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 20 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 21 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 22 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 23 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 


        Expert Demonstration 3 
        Description: 
    You are the HVAC administrator responsible for managing a building of type OfficeLarge located in Dubai, where the climate is Warm and Dry. 

    The building has 23 rooms in total.
    Currently, temperature in each room is as follows:
       Room 1: -37 degrees Celsius 
       Room 2: -31 degrees Celsius 
       Room 3: -11 degrees Celsius 
       Room 4: -5 degrees Celsius 
       Room 5: -5 degrees Celsius 
       Room 6: -34 degrees Celsius 
       Room 7: -16 degrees Celsius 
       Room 8: 8 degrees Celsius 
       Room 9: -13 degrees Celsius 
       Room 10: 1 degrees Celsius 
       Room 11: -35 degrees Celsius 
       Room 12: -14 degrees Celsius 
       Room 13: -11 degrees Celsius 
       Room 14: 18 degrees Celsius 
       Room 15: -18 degrees Celsius 
       Room 16: -37 degrees Celsius 
       Room 17: -20 degrees Celsius 
       Room 18: -17 degrees Celsius 
       Room 19: 0 degrees Celsius 
       Room 20: -8 degrees Celsius 
       Room 21: -20 degrees Celsius 
       Room 22: 6 degrees Celsius 
       Room 23: -7 degrees Celsius 
    The external climate conditions are as follows:
       Outside Temperature: 7 degrees Celsius. 
       Global Horizontal Irradiance: 0 
       Ground Temperature: 30 degrees Celsius
       Occupant Power: 0 KW 
       Target Temperature: 22 degrees Celsius 

        Actions: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        Outcomes: After taking the above actions, temperature in each room becomes: 
       Room 1: 18 degree Celsius 
       Room 2: 19 degree Celsius 
       Room 3: 10 degree Celsius 
       Room 4: 12 degree Celsius 
       Room 5: 13 degree Celsius 
       Room 6: 12 degree Celsius 
       Room 7: 16 degree Celsius 
       Room 8: 18 degree Celsius 
       Room 9: 7 degree Celsius 
       Room 10: 3 degree Celsius 
       Room 11: 6 degree Celsius 
       Room 12: 7 degree Celsius 
       Room 13: 6 degree Celsius 
       Room 14: 10 degree Celsius 
       Room 15: 11 degree Celsius 
       Room 16: 3 degree Celsius 
       Room 17: 1 degree Celsius 
       Room 18: 4 degree Celsius 
       Room 19: 5 degree Celsius 
       Room 20: 4 degree Celsius 
       Room 21: 8 degree Celsius 
       Room 22: 9 degree Celsius 
       Room 23: 1 degree Celsius 
The action for Room 1 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 2 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 3 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 4 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 5 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 6 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 7 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 8 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 9 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 10 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 11 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 12 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 13 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 14 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 15 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 16 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 17 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 18 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 19 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 20 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 21 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 22 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 23 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 


        Expert Demonstration 4 
        Description: 
    You are the HVAC administrator responsible for managing a building of type OfficeLarge located in GreatFalls, where the climate is Mixed and Dry. 

    The building has 23 rooms in total.
    Currently, temperature in each room is as follows:
       Room 1: -3 degrees Celsius 
       Room 2: -19 degrees Celsius 
       Room 3: -24 degrees Celsius 
       Room 4: -29 degrees Celsius 
       Room 5: -10 degrees Celsius 
       Room 6: -1 degrees Celsius 
       Room 7: -37 degrees Celsius 
       Room 8: 20 degrees Celsius 
       Room 9: 16 degrees Celsius 
       Room 10: 11 degrees Celsius 
       Room 11: 11 degrees Celsius 
       Room 12: 12 degrees Celsius 
       Room 13: -3 degrees Celsius 
       Room 14: -37 degrees Celsius 
       Room 15: -17 degrees Celsius 
       Room 16: -14 degrees Celsius 
       Room 17: 12 degrees Celsius 
       Room 18: 12 degrees Celsius 
       Room 19: -19 degrees Celsius 
       Room 20: -28 degrees Celsius 
       Room 21: -36 degrees Celsius 
       Room 22: -26 degrees Celsius 
       Room 23: -8 degrees Celsius 
    The external climate conditions are as follows:
       Outside Temperature: 3 degrees Celsius. 
       Global Horizontal Irradiance: 0 
       Ground Temperature: 9 degrees Celsius
       Occupant Power: 0 KW 
       Target Temperature: 22 degrees Celsius 

        Actions: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        Outcomes: After taking the above actions, temperature in each room becomes: 
       Room 1: 8 degree Celsius 
       Room 2: 9 degree Celsius 
       Room 3: 8 degree Celsius 
       Room 4: 9 degree Celsius 
       Room 5: 10 degree Celsius 
       Room 6: 9 degree Celsius 
       Room 7: 13 degree Celsius 
       Room 8: 15 degree Celsius 
       Room 9: 8 degree Celsius 
       Room 10: 8 degree Celsius 
       Room 11: 10 degree Celsius 
       Room 12: 11 degree Celsius 
       Room 13: 10 degree Celsius 
       Room 14: 13 degree Celsius 
       Room 15: 15 degree Celsius 
       Room 16: 9 degree Celsius 
       Room 17: 8 degree Celsius 
       Room 18: 10 degree Celsius 
       Room 19: 11 degree Celsius 
       Room 20: 10 degree Celsius 
       Room 21: 13 degree Celsius 
       Room 22: 16 degree Celsius 
       Room 23: 8 degree Celsius 
The action for Room 1 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 2 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 3 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 4 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 5 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 6 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 7 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 8 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 9 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 10 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 11 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 12 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 13 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 14 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 15 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 16 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 17 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 18 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 19 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 20 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 21 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 22 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 
The action for Room 23 shall be increased as its temperature is lower than the target temperature 22 degree Celsius. 


Please decide opening of the valve in each room based on the following description:
Description: 
    You are the HVAC administrator responsible for managing a building of type OfficeMedium located in InternationalFalls, where the climate is Cool and Dry. 

    The building has 18 rooms in total.
    Currently, temperature in each room is as follows:
       Room 1: -31 degrees Celsius 
       Room 2: 17 degrees Celsius 
       Room 3: 8 degrees Celsius 
       Room 4: -29 degrees Celsius 
       Room 5: -12 degrees Celsius 
       Room 6: -37 degrees Celsius 
       Room 7: -6 degrees Celsius 
       Room 8: -35 degrees Celsius 
       Room 9: -28 degrees Celsius 
       Room 10: 18 degrees Celsius 
       Room 11: -20 degrees Celsius 
       Room 12: 19 degrees Celsius 
       Room 13: -24 degrees Celsius 
       Room 14: 10 degrees Celsius 
       Room 15: -13 degrees Celsius 
       Room 16: -2 degrees Celsius 
       Room 17: -14 degrees Celsius 
       Room 18: -27 degrees Celsius 
    The external climate conditions are as follows:
       Outside Temperature: 3 degrees Celsius. 
       Global Horizontal Irradiance: 0 
       Ground Temperature: 5 degrees Celsius
       Occupant Power: 0 KW 
       Target Temperature: 22 degrees Celsius 

Actions:
"""

api_key = "653880d85b6e4a209206c263d7c3cc7a"
headers = {"Content-Type": "application/json", "api-key": api_key}
data = {
    "messages": [{"role": "user", "content": message}],
    "max_tokens": 2000,
    "temperature": 0.7,
    "n": 1,
}


port = 5330
url = 'http://localhost:{port}/api/completion'.format(port=port)
res = requests.post(url, json=data, headers=headers, timeout=30)
response = resp_json["choices"][0]["message"]["content"]
print(response)

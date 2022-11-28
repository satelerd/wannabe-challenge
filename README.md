# Wannabe Challenge

This is a technical challenge to validate my ability as a Backend Software Engineer, which consists in:

- You have to choose the stack you will use and why you chose it.
- The API must have documentation on how to use it as if you are delivering this API to a Frontend Developer.
- We must integrate with a PostgreSQL database and build seeders to populate the database with the data we attach to this email.
- Proper use of git. Please don ́t upload your project to GitHub with just one commit; we want to see how you use GitHub and how you document each change in your code.

### Disclaimer
I started this project with Django because I misunderstood the challenge, and I thought that I could have chosen any stack I wanted. 
But then I realized that I had to use a NodeJS based stack, so I tried to change it to KOA. I didn't have much time to do it, taking into account that I had to learn the framework almost from scratch, so I didn't finish it.

Despite that, I don´t think I did a bad job... And the Django version is similar to the KOA version, so it's still a good representation of my skills.

## Challenge - Second try (NodeJS)

### Stack
I chose to use KOA because I have a good source of documentation and I also wanted to learn more about it.

### Why I didn't finish?
As I said before, I started learning KOA from scratch, so this is my first project using it. 
Learning a new language, framework (like in this case), or library, is always a challenge that comes with its learning curve, and the first project doesn't always go as planned.

So, I did manage to implement the "easy" methods to all endpoints, that is, the GET and DELETE methods, but I didn't have enough time to get the POST and PUT methods working correctly. I'm having problems with parsing the request body, which I feel like it can't be a very difficult bug, but I didn't have enough time to fix it.
Also, I tried to connect the API to a PostgreSQL database, and I kinda managed to do it, but there are some problems with the connection.

I know I can do it if I keep trying, but there is a deadline, so I decided to send it as it is.

-------------

(The following is the same as the README from the Django version)


## Challenge - First try (Django)

### Stack
This project was built using the Django Rest Framework.
I chose this stack because I find it very reasonable to build the type of REST API needed for this challenge. This is because it's easy to start developing (from scratch) and it has a readable code which makes it easy to setup and to understand.

### Documentation

#### Usage
To access the API you will need to:
1. Install the dependencies needed for the project: 
    ```
    pip install django
    pip install djangorestframework
    ```

2. Edit the `./wannabe/settings.py` file and change the `DATABASES` variable (line 80) to match your PostgreSQL database settings.

3. Run the following commands:
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

Then you should be able to access the endpoints at http://127.0.0.1:8000/api/the_endpoint_here/

#### API Endpoints
The API dives into 3 main sections (airports, airlines, and flights). Each one with its own endpoints and can use the GET, POST, PUT, and DELETE methods.
- /api/airports:

    example application/json content:
    ```
    {
        "iata_code": "string",
        "airport": "string",
        "city": "string",
        "state": "string",
        "country": "string",
        "latitude": float,
        "longitude": float
    }
    ```
    

- /api/airlines

    example application/json content:
    ```
    {
        "iata_code": "string",
        "airline": "string"
    }
    ```


- /api/flights

    example application/json content:
    ```
    {
        "year": int,
        "month": int,
        "day": int,
        "day_of_week": int,
        "airline": string,
        "flight_number": int,
        "tail_number": "string",
        "origin_airport": "string",
        "destination_airport": "string",
        "scheduled_departure": "string",
        "departure_time": "string",
        "departure_delay": float,
        "taxi_out": float,
        "wheels_off": "string",
        "scheduled_time": float,
        "elapsed_time": float,
        "air_time": float,
        "distance": float,
        "wheels_on": "string",
        "taxi_in": float,
        "scheduled_arrival": "string",
        "arrival_time": "string",
        "arrival_delay": float,
        "diverted": boolean,
        "cancelled": boolean,
        "cancellation_reason": "string",
        "air_system_delay": float,
        "security_delay": float,
        "airline_delay": float,
        "late_aircraft_delay": float,
        "weather_delay": float
    }
    ```


###### Example js fetch POST request
```
fetch("http://127.0.0.1:8000/api/airline", {
  "method": "POST",
  "headers": { "Content-Type": "application/json" },
  "body": JSON.stringify({
    "iata_code": "XX",
    "airline": "xXairlineXx"
  })
})
.then(response => { console.log(response); })
.catch(err => { console.error(err); });

```

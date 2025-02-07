import sys

def get_city_population_html(city_name):
    city_populations = {
        "London": "9,000,000",
        "Paris": "2,100,000",
        "Tokyo": "14,000,000",
        "New York": "8,800,000",
        "Sydney": "5,300,000"
    }

    if city_name in city_populations:
        population = city_populations[city_name]
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>City Population - {city_name}</title>
        </head>
        <body>
            <h1>Population of {city_name}</h1>
            <p>The population of {city_name} is: <strong>{population}</strong>.</p>
        </body>
        </html>
        """
        return html_content
    else:
        error_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>City Not Found</title>
        </head>
        <body>
            <h1>City Not Found</h1>
            <p>Sorry, information for the city <strong>"{city_name}"</strong> is not available in this demo.</p>
        </body>
        </html>
        """
        return error_html

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide a city name as a command-line argument.")
        sys.exit(1)

    city_name_input = sys.argv[1]
    html_output = get_city_population_html(city_name_input)
    print(html_output) # Output the generated HTML to stdout
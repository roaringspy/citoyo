import sys

def get_city_population_html(city_name):
    """
    Generates a simple HTML string containing the city name and its population.
    For demonstration purposes, population data is hardcoded.

    Args:
        city_name: The name of the city (string).

    Returns:
        A string containing HTML, or an error message in HTML if city is not found.
    """

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
            <p>The approximate population of {city_name} is: <strong>{population}</strong>.</p>
            <p><small><i>(Note: This data is for demonstration purposes only and may not be accurate.)</i></small></p>
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
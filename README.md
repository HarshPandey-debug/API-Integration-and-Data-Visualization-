# API Integration and Data Visualization

## Overview
This Python script fetches real-time weather data from the **OpenWeatherMap API**, processes it, and visualizes the temperature trends using **Matplotlib** and **Seaborn**.

## Features
- Integrates with the **OpenWeatherMap API**.
- Retrieves real-time weather forecast data.
- Parses and processes JSON responses.
- Visualizes temperature trends with **Matplotlib** and **Seaborn**.

## Prerequisites
Ensure you have the required dependencies installed:

```sh
pip install requests matplotlib seaborn
```

## API Key Setup
1. Get your free API key from [OpenWeatherMap](https://home.openweathermap.org/api_keys).
2. Replace `YOUR_API_KEY` in the script with your actual API key.

## Usage
1. Open the script file and modify the `CITY` variable if needed:

```python
CITY = "New Delhi"
```

2. Run the script:

```sh
python api_data_viz.py
```

3. The script fetches the weather data and plots a temperature trend visualization.

## Troubleshooting
### API Key Errors
- Ensure your API key is correct and active.
- If you receive a **401 Unauthorized** error, check if the API key is properly set.

### KeyError in Data Processing
- If `KeyError` occurs, print the JSON response to check its structure:

```python
print(data)
```
- Adjust the key names based on the API response format.

## Customization
- Modify the `cnt` parameter in the API request to change the number of forecast entries fetched:

```python
params = {"q": CITY, "appid": API_KEY, "units": "metric", "cnt": 10}
```

- Change the visualization style:

```python
sns.set_style("whitegrid")
```

## License
This project is open-source. Feel free to modify and improve it.

---




# Sea Level Predictor

In this project, you will analyze a dataset of the global average sea level change since 1880. You will use the data to predict the sea level change through year 2050.

Use the data to complete the following tasks:

- Use Pandas to import the data from `epa-sea-level.csv`.
- Use matplotlib to create a scatter plot using the `Year` column as the x-axis and the `CSIRO Adjusted Sea Level` column as the y-axis.
- Use the `linregress` function from `scipy.stats` to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year **2050** to predict the sea level rise in 2050.
- Plot a new line of best fit just using the data from **year 2000** through the most recent year in the dataset. Make the line also go through the year **2050** to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
- The x-axis label should be **Year**.
- The y-axis label should be **Sea Level (inches)**.
- The title should be **Rise in Sea Level**.
- The boilerplate already includes commands to save and return the image.

## Development

Write your code in `sea_level_predictor.py`.

You can use `main.py` to test your function before submitting.

Run the project:

```bash
python main.py
```

The generated graph will be saved as:

```
sea_level_plot.png
```

## Testing

The unit tests for this project are in `test_module.py`.

Run the tests using:

```bash
python -m unittest test_module.py
```

or

```bash
pytest
```

## Project Structure

```
.
├── epa-sea-level.csv
├── main.py
├── sea_level_predictor.py
├── test_module.py
└── README.md
```

## Libraries Used

- pandas
- matplotlib
- scipy
- numpy

Install dependencies:

```bash
pip install pandas matplotlib scipy numpy
```

## Data Source

Global Average Absolute Sea Level Change (1880–2014)

Source:
- US Environmental Protection Agency (EPA)
- CSIRO (2015)
- NOAA (2015)

## Expected Output

The generated visualization should include:

- Scatter plot of all sea level observations.
- Regression line using the complete dataset (1880–2050).
- Regression line using data from 2000 onward (2000–2050).
- Title: **Rise in Sea Level**
- X-axis label: **Year**
- Y-axis label: **Sea Level (inches)**

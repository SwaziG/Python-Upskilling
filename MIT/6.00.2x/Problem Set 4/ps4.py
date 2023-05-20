import numpy as np
import pylab
import re

# Set line width
pylab.rcParams['lines.linewidth'] = 4
# Set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
# Set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
# Set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
# Set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
# Set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
# Set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
# Set size of markers
pylab.rcParams['lines.markersize'] = 10
# Set number of examples shown in legends
pylab.rcParams['legend.numpoints'] = 1

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

INTERVAL_1 = list(range(1961, 2006))
INTERVAL_2 = list(range(2006, 2016))
ALL = list(range(1961, 2016))

"""
Begin helper code
"""
class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature
            
        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a numpy 1-d array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return np.array(temperatures)

    def get_monthly_temp(self, city, month, year):
        """
        Get the monthly temperature for the given city year.

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            year: the year to get the data for (int)

        Returns:
            a numpy 1-d array of daily temperatures for the specified month and
            city
        """        
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        for day in range(1, 32):
            if day in self.rawdata[city][year][month]:
                temperatures.append(self.rawdata[city][year][month][day])
        return np.array(temperatures)
    
    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]

# daily = Climate('data.csv')
# print(daily.get_daily_temp('PORTLAND',8,10,1975))

"""
End helper code
"""

# Problem 1
def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).
    Args:
        x: a list with length N, representing the x-coords of N sample points
        y: a list with length N, representing the y-coords of N sample points
        degs: a list of degrees of the fitting polynomial
    Returns:
        a list of numpy arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    models = []
    for d in degs:
        model = np.polyfit(np.array(x), np.array(y), d)
        models.append(model)
    return models

## print(generate_models([1961, 1962, 1963],[4.4,5.5,6.6],[1, 2]))

# Problem 2
def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """
    error = ((np.array(estimated) - np.array(y)) ** 2).sum()
    meanError = error / len(y)
    return float(1 - (meanError / np.var(y)))

## print(r_squared([32.0, 42.0, 31.3, 22.0, 33.0], [32.3, 42.1, 31.2, 22.1, 34.0]))

# Outside of scope of PS4

def labelPlot():
    """
    Set the title, x-label, and y-label for the plot of the measured displacement of a spring.
    """
    pylab.title('Temperature Readings')
    pylab.xlabel('Year')
    pylab.ylabel('Temperature in Deg C')

# Problem 3
def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-square for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points
    Args:
        x: a list of length N, representing the x-coords of N sample points
        y: a list of length N, representing the y-coords of N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a numpy array storing the coefficients of
            a polynomial.
    Returns:
        None
    """
    for model in models:
        xVals = pylab.array(x)
        yVals = pylab.array(y)
        pylab.plot(xVals, yVals, 'bo', label='Measured points')

        estYVals = pylab.polyval(model, xVals)
        pylab.plot(xVals, estYVals, 'r',label='Linear fit, r**2 = ' + str(round(r_squared(yVals, estYVals), 5)))
        
        labelPlot()
        pylab.title(f'Degree = {len(model)-1} \n R-square = {round(r_squared(yVals, estYVals), 5)}')
        pylab.legend(loc='best')

### Begining of program
raw_data = Climate('data.csv')

# Problem 3
# y = []
# x = INTERVAL_1
# for year in INTERVAL_1:
#     y.append(raw_data.get_daily_temp('BOSTON', 1, 10, year))
# models = generate_models(x, y, [1])
# evaluate_models_on_training(x, y, models)


# Problem 4: FILL IN MISSING CODE TO GENERATE y VALUES
# x1 = INTERVAL_1
# x2 = INTERVAL_2

# # interval 1 1960 - 2005 'BOSTON'
# y = []
# for year in INTERVAL_1:
#     y.append(np.mean(raw_data.get_yearly_temp('BOSTON', year)))

# models = generate_models(x1, y, [1])    
# evaluate_models_on_training(x1, y, models)

# # interval 2 2005 - 2016 'BOSTON'
# pylab.figure()
# y = []
# for year in INTERVAL_2:
#     y.append(np.mean(raw_data.get_yearly_temp('BOSTON', year)))

# models = generate_models(x2, y, [1])    
# evaluate_models_on_training(x2, y, models)

'''
self experimentation outside of problemset scope
'''

# Combined 'BOSTON'
# xA = ALL
# pylab.figure()
# y = []
# for year in ALL:
#     y.append(np.mean(raw_data.get_yearly_temp('BOSTON', year)))

# models = generate_models(xA, y, [1])    
# evaluate_models_on_training(xA, y, models)

# # Combined All
# xA = ALL
# pylab.figure()
# y = []
# for year in ALL:
#     C = []
#     for city in CITIES:
#         C.append(np.mean(raw_data.get_yearly_temp(city, year)))
#     y.append(np.mean(C))
# print(f'The temperature rise over the past {len(y)} years is {round(float(y[-1])-float(y[0]),2)} degrees celcius')
# models = generate_models(xA, y, [1])    
# evaluate_models_on_training(xA, y, models)
# pylab.title(f'The temperature rise over {len(y)} years \n is {round(float(y[-1])-float(y[0]),2)} degrees celcius')
# pylab.figure()

#Comparing years using trends from the other years
# xi = list(range(1, 13))
# year1 = 2001
# year2 = 2004
# City1 = 'BALTIMORE'

# y1 = []
# for month in range(1, 13):
#     y1.append(np.mean(raw_data.get_monthly_temp(City1, month, year1)))

# models1 = generate_models(xi, y1, [2])    
# #evaluate_models_on_training(xi, y1, models1)
# #pylab.title(f'{year1} temps for {City1}')

# y2 = []
# for month in range(1, 13):
#     y2.append(np.mean(raw_data.get_monthly_temp(City1, month, year2)))

# models2 = generate_models(xi, y2, [2])    
# evaluate_models_on_training(xi, y2, models1)
# pylab.title(f'{year2} temps for {City1}')


#Comparing years using trends from the other years
x1 = INTERVAL_1
x2 = INTERVAL_2
xi = list(range(1, 13))

City = 'BALTIMORE'
# Training
y1 = []
for month in range(1, 13):
    m = []
    for year in INTERVAL_1:
        m.append(np.mean(raw_data.get_monthly_temp(City, month, year)))
        
    y1.append(np.mean(m))

model1 = generate_models(xi, y1, [2])    
evaluate_models_on_training(xi, y1, model1)
pylab.title(f'{1960} to {2004} Temps for {City}')

# Testing
pylab.figure()
y2 = []
for month in range(1, 13):
    m = []
    for year in INTERVAL_2:
        m.append(np.mean(raw_data.get_monthly_temp(City, month, year)))
        
    y2.append(np.mean(m))

model2 = generate_models(xi, y2, [2])    
evaluate_models_on_training(xi, y2, model2)
pylab.title(f'{2005} to {2016} Temps for {City}')

# using training on testing
pylab.figure()
evaluate_models_on_training(xi, y2, model1)
pylab.title("Using the model from Training to develope \n the best fit and using it on testing")

# xi = list(range(1, 13))
# year = 2001
# City2 = 'SAN JUAN'
# y2 = []
# for month in range(1, 13):
#     y2.append(np.mean(raw_data.get_monthly_temp(City2, month, year)))

# models2 = generate_models(xi, y2, [2])    
# evaluate_models_on_training(xi, y2, models2)
# pylab.title(f'{year} temps for {City2}')
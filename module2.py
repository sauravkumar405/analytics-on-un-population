
from matplotlib import pyplot as plt


def function(DataSet):
    """This function takes input a list of dictionaries and filters out
    countries and population of Asean countries in the year 2014.

    Args:
        DataSet [list[dict]]: list of dictionaries where every
        element of the list is a record of country's population corresponding
        to the respective year
    """
    asean = ["Brunei Darussalam", "Cambodia", "Indonesia", "Laos", "Malaysia",
             "Myanmar", "Philippines", "Singapore", "Thailand",
             "Vietnam"]
    countries = []
    population = []
    
    for entry in DataSet:
        if (entry['Year'] == '2014') and (entry['Region'] in asean):
            countries.append(entry['Region'])
            population.append(entry['Population'])

    plt.bar(countries, population)
    plt.xlabel("ASEAN Countries")
    plt.ylabel("Population")
    plt.title("Population of ASEAN Countries in 2014")
    plt.show()

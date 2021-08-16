
from matplotlib import pyplot as plt


def function(DataSet):
    """This function takes input a list of dictionaries and filters out
    population of India over years."

    Args:
        DataSet (list[dict]): list of dictionaries where every
        element of the list is a record of country's population corresponding
        to the respective year.
    """
    population = []
    years = []
    # Iterating through the DataSet entry
    for entry in DataSet:
        if entry['Region'] == "India":
            population.append(entry['Population'])
            years.append(entry['Year'])
            
    # Dicing the data for improved visibility
    population = population[::3]
    years = years[::3]
    
    # Plotting the data via matplotlib function
    plt.bar(years, population, width=0.5)
    plt.xlabel("Years")
    plt.ylabel("Population")
    plt.title("Population of India vs Years")
    plt.show()

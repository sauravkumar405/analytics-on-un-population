
from matplotlib import pyplot as plt


def function(DataSet):
    """This function takes input a list of dictionaries and filters out
    population of SAARC Countries over years."

    Args:
        DataSet [list[dict]]: list of dictionaries where every
        element of the list is a record of country's population corresponding
        to the respective year
    """
    saarc = ["Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives",
             "Nepal", "Sri Lanka", "Pakistan"]

    years_hashmap: dict[str:float] = {}

    for entry in DataSet:
        if entry['Region'] in saarc:
            if entry['Year'] in years_hashmap.keys():
                years_hashmap[entry['Year']] += float(entry['Population'])
            else:
                years_hashmap[entry['Year']] = float(entry['Population'])
    years: list[str] = list(years_hashmap.keys())[::3]
    total_population: list[float] = list(years_hashmap.values())[::3]

    plt.bar(years, total_population, width=0.8)
    plt.xlabel("Years")
    plt.ylabel("Population")
    plt.title("Over the years, Total Population of SAARC countries")
    plt.show()

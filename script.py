from pandas import DataFrame
from numpy import array as npArray, int8
from matplotlib.pyplot import subplots, tight_layout, show


def array_to_dataframe(array):
    return DataFrame(array)


def display_dataframe(df):
    fig, axes = subplots(
        nrows=1,
        ncols=df.shape[1],
        figsize=(10, 10)
    )
    # Iterates through the Dataframe's columns and create a graph for each column
    for i, j in enumerate(df.columns):
        axes[i].plot(df[j])
        axes[i].set_title(f'Column {j}')

    # Display the graphs
    tight_layout()
    show()

def run():
    x = int8(input('Enter your number: '))
    X = [(x + i) for i in range(1000)]
    y = []
    for i in X:
        y.append([i**2, (-i)**3 + 3*i**2 -2*i + 1, i-9])

    my_array = npArray(y)
    df = array_to_dataframe(my_array)
    display_dataframe(df)


if __name__ == '__main__':
    run()
def ecdf(dataframe_column):
    # import numpy and matplotlib
    import numpy as np
    import matplotlib.pyplot as plt

    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(dataframe_column)

    # x-data for the ECDF: x
    x = np.sort(dataframe_column)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    #type in x-label
    x_label_name = str(input())

    # Generate plot
    _ = plt.plot(x, y, marker='.', linestyle='none')

    # Label the axes
    _ = plt.xlabel(x_label_name)
    _ = plt.ylabel('ECDF')

    # Display the plot
    plt.show()


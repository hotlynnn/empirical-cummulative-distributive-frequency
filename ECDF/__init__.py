def ECDF(dataframe_column_name):
    # import numpy and matplotlib
    import numpy as np
    import matplotlib.pyplot as plt

    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(dataframe_column_name)

    # x-data for the ECDF: x
    x = np.sort(dataframe_column_name)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    # type in x-label
    x_label_name = str(input())

    # Generate plot
    _ = plt.plot(x, y, marker='.', linestyle='none')

    # Label the axes
    _ = plt.xlabel(x_label_name)
    _ = plt.ylabel('ECDF')

    # Specify array of percentiles: percentiles
    percentiles = np.array([5, 25, 50, 75, 97.5])

    # Compute percentiles: ptiles_vers
    ptiles_vers = np.percentile(dataframe_column_name, percentiles)

    # Print the result
    #print(ptiles_vers)

    # Overlay percentiles as red x's
    _ = plt.plot(ptiles_vers, percentiles/100, marker='D', color='red',
            linestyle='none')

    # Show the plot within a margin of 0.02
    plt.margins(0.02)
    plt.show()

"""
GNSS Ocean Experiment: Travel Path Visualization
------------------------------------------------

This script visualizes GNSS receiver trajectories recorded during
ocean field trials. Raw ECEF coordinates are converted to geodetic
Latitude–Longitude–Altitude (LLA) coordinates and plotted to analyze
receiver motion and path consistency.

Such trajectory visualization is useful for:
    - GNSS data validation
    - Field experiment analysis
    - Identifying anomalies in positioning data
"""

import pandas as pd
import matplotlib.pyplot as plt
from pyproj import CRS, Transformer


def load_gnss_datasets(file_paths):
    """
    Load multiple GNSS datasets from CSV files.

    Parameters
    ----------
    file_paths : list of str
        Paths to GNSS CSV files.

    Returns
    -------
    list of pd.DataFrame
        Loaded GNSS datasets.
    """
    return [pd.read_csv(file) for file in file_paths]


def ecef_to_lla_converter():
    """
    Create a reusable ECEF to LLA coordinate transformer.

    Returns
    -------
    Transformer
        PyProj transformer for coordinate conversion.
    """
    ecef_crs = CRS.from_epsg(4978)   # WGS84 ECEF
    lla_crs = CRS.from_epsg(4326)    # WGS84 LLA
    return Transformer.from_crs(ecef_crs, lla_crs, always_xy=True)


def plot_gnss_trajectories(data_list, titles):
    """
    Plot GNSS travel paths from multiple datasets.

    Parameters
    ----------
    data_list : list of pd.DataFrame
        GNSS datasets containing ECEF coordinates (X, Y, Z).
    titles : list of str
        Titles for each subplot.
    """

    transformer = ecef_to_lla_converter()

    fig, axes = plt.subplots(1, len(data_list), figsize=(18, 6))

    for ax, data, title in zip(axes, data_list, titles):

        # Convert ECEF to Latitude and Longitude (vectorized)
        lon, lat, alt = transformer.transform(
            data['X'].values,
            data['Y'].values,
            data['Z'].values
        )

        # Plot trajectory
        ax.plot(lon, lat, linewidth=1.8, label='Travel Path')
        ax.scatter(lon[0], lat[0], color='red', s=40, label='Start')
        ax.scatter(lon[-1], lat[-1], color='green', s=40, label='End')

        # Plot formatting
        ax.set_title(title, fontsize=13)
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    # ------------------------------------------------------
    # GNSS Ocean Experiment Datasets
    # ------------------------------------------------------
    file_paths = [
        "gps_data_Travel_To.csv",
        "gps_data_Travel_Mid.csv",
        "gps_data_Travel_Fro.csv"
    ]

    titles = [
        "Ocean Field Trial: Travel To",
        "Ocean Field Trial: Mid Trajectory",
        "Ocean Field Trial: Travel From"
    ]

    gnss_data = load_gnss_datasets(file_paths)

    # ------------------------------------------------------
    # Visualize GNSS Trajectories
    # ------------------------------------------------------
    plot_gnss_trajectories(gnss_data, titles)

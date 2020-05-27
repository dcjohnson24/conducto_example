import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import argparse


# Check out pd.tseries.offsets.__all__ for a list of resample options
def plot(df: pd.DataFrame, resample: str=None, save: bool=False) -> None:
    df = df.rename(columns={'Date (mm/dd/yy)': 'Date',
                            'Precipitation (inches)': 'Precipitation'})
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')
    title = 'Daily Rainfall\n 1976-2003'
    if resample:
        df = df.reset_index().resample(resample, on='Date').median()
        # Get the string of the resampling frequency
        freq_str = str(pd.tseries.frequencies.to_offset(resample)).strip('<>')
        title = f'{freq_str} Median Rainfall\n 1976-2003'
    ax = df.plot(legend=None)
    ax.set_ylabel('Precipitation (inches)')
    ax.set_title(title)
    if save:
        print(f'Saving plot to {Path.cwd()}')
        plt.savefig('rainfall_data.png')
    plt.show()


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('--path', type=str, help='path to data file')
    parse.add_argument('--resample',
                       type=str,
                       help="resampling rate e.g. 'M(onthly)', 'W(eekly)',\
                            'A(nnually)'")
    parse.add_argument('--save', action='store_true',
                       help='Whether to save a .png file of the plot.\
                             Defaults to False', default=False)
    args = parse.parse_args()
    path = args.path
    resample = args.resample
    save = args.save

    if path is None:
        path = Path('Data') / 'FEF_HQ_dailyppt.csv'
    df = pd.read_csv(path)
    plot(df, resample=resample, save=save)


if __name__ == '__main__':
    main()

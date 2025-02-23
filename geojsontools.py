import click


@click.group()
def geojson():
    pass


@geojson.command()
@click.option('-m', '--max-rows', type=int, help='Number of Rows to split file into')
@click.argument('filename')
def split_geojson(max_rows, filename):
    print('Splitting GeoJSON file')
    print(f"max Rows: {max_rows}")
    print(f"filename: {filename}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    geojson()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

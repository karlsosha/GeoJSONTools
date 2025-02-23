import click


@click.group()
def geojson():
    pass


@geojson.command()
@click.option('--max-rows', '-m')
def splitgeojson():
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    geojson()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import click
import logging

from .crystal_processing.process_image_folder import process_image_folder
from .data.segment_droplets import segment_droplets_to_file

@click.group()
@click.version_option()
def cli():
    pass

@cli.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False))
@click.option('-c', '--check-segmentation', is_flag=True, help="Displays the segmented image to check accuracy")
@click.option('-o', '--save-overlay', is_flag=True, help="Save images with crystal detection overlay")
@click.option('-p', '--save-plot', is_flag=True, help="Generate and save plots of crystal contents over time")
@click.option('-v', '--verbose', count=True, help="Increase verbosity level")
def process(directory, check_segmentation, save_overlay, save_plot, verbose):
    '''Process a directory containing a timeseries of images'''

    # Setup logging
    if verbose == 1:
        logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
    elif verbose >= 2:
        logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.WARNING, format='%(levelname)s - %(message)s')

    logging.info("Processing directory: %s", directory)

    process_image_folder(directory, show_plot=save_plot, save_overlay=save_overlay)


@cli.command()
@click.argument('directory', type=click.Path(exists=True))
@click.option('-o', '--save-overlay', is_flag=True, help="Save segmented overlay to disk")
@click.option('-v', '--verbose', count=True, help="Increase verbosity level")
def segment(directory, save_overlay, verbose):
    '''Segment an image or directory of images and saves extracted droplets to disk'''

    # Setup logging
    if verbose == 1:
        logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
    elif verbose >= 2:
        logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.WARNING, format='%(levelname)s - %(message)s')

    logging.info("Extracting droplets from: %s", directory)
    segment_droplets_to_file(directory)

@cli.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False))
@click.option('-m', '--model', type=click.Choice(['svm', 'cnn', 'cnn-transfer']), help="Type of model to train")
@click.option('-v', '--verbose', count=True, help="Increase verbosity level")
def train(directory, model, verbose):
    '''Train a model from a directory of labeled images'''

    raise NotImplementedError("Training from the command line is not implemented yet.")
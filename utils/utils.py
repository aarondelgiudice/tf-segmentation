import argparse
import sys

import matplotlib.pyplot as plt


def parse_args(defaults, args=None):
    p = argparse.ArgumentParser(description=sys.argv[0], add_help=False)

    # add any missing required arguments
    required_args = {
        "logging": 1,
        "message": "",
        "verbose": 0,
    }

    for k, v in required_args.items():
        if k not in defaults.keys():
            p.add_argument(
                f"--{k}", default=v,
                type=type(v) if v is not None else str)

    # add default arguments
    for k, v in defaults.items():
        p.add_argument(
            f"--{k}", default=v,
            type=type(v) if v is not None else str)

    # parse CLI arguments if provided, if not use defaults
    if args is not None:
        p = p.parse_args(args)
    else:
        p = p.parse_args()

    # return dictionary
    return vars(p)


def visualize(savefig=None, title=None, **kwargs):
    plt.figure(figsize=(15, 20))

    for i, (k, v) in enumerate(kwargs.items()):
        plt.subplot(1, len(kwargs.keys()), i + 1)
        plt.title(k.title())
        plt.imshow(v)
        plt.axis('off')

    if title is not None:
        plt.suptitle(title.title())

    if savefig is not None:
        plt.savefig(savefig)

    plt.show()
    plt.close()
    return

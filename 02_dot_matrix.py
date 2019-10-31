# library
import seaborn as sns
import pandas as pd
import numpy as np
import argparse

import matplotlib.pyplot as plt


def watson_crick(x_, y_, alphabet=None):
    """
    fun assigns 1 if input string
    is in alphabet, otherwise
    it returns 0.

    parameters:
    x_ = nt_x
    y_ = nt_y
    alphabet = list of nt combinations
    """
    if not alphabet:
        alphabet = ["AT", "GC", "CG", "TA"]
    pair = x_ + y_
    if pair in alphabet:
        return 1
    return 0


def make_set_hm(args):
    """
    fun creates a metrics of nt bindings
    according to watson crick rules.
    output is a metrics of 0 or 1 (not bind
    or bind)

    parameters
    args = parser with user specific paramenters
    """
    seq_x = args.x_seq
    seq_y = args.y_seq

    len_x = len(seq_x)
    len_y = len(seq_y)

    metrics = np.zeros((len_x, len_y))

    for i_bind in range(0, len_x):
        for i_micro in range(0, len_y):
            metrics[i_bind, i_micro] = watson_crick(
                seq_x[i_bind], seq_y[i_micro], alphabet=args.alphabet
            )

    m_out = pd.DataFrame(metrics, columns=list(seq_y), index=list(seq_x))

    return m_out


# final_with_binding_and_mirna_seq
def make_2d(args):
    """
    fun plots 2D metrics of watson-crick binding
    rules of sequence x and y as heatmap

    parameters
    args = parser with user specific paramenters
    """
    # Create binding site - mirna interaction metrics
    df = make_set_hm(args)
    # Default heatmap: just a visualization of this square matrix
    ax = sns.heatmap(
        df, xticklabels=True, yticklabels=True, annot=False, cbar=False, vmin=0, vmax=1
    )
    return ax


def get_arguments():
    """
    fun parse arguments from
    command line and returns
    the argument objct
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--x", type=str, dest="x_seq", help="nt sequence on axis x", required=True
    )
    parser.add_argument(
        "--y", type=str, dest="y_seq", help="nt sequence on axis y", required=True
    )
    parser.add_argument(
        "--o", type=str, dest="file_name", required=False, default="2D_matrix"
    )
    parser.add_argument(
        "--alphabet",
        type=str,
        dest="alphabet",
        help="user specific aphabet for matrix",
        required=False,
        default=None,
    )

    args = parser.parse_args()
    if args.alphabet:
        args.alphabet = args.alphabet.split(",")
    return args


if __name__ == "__main__":
    args = get_arguments()
    fig, ax = plt.subplots(figsize=(20, 20))
    ax = make_2d(args)
    fig.savefig(f"./{args.file_name}.png")

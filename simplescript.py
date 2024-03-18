import argparse

parser = argparse.ArgumentParser(description='CLAM Evaluation Script')
parser.add_argument('--data_input', type=str, default=None,
                    help='data directory')
args = parser.parse_args()
print(args.data_input)

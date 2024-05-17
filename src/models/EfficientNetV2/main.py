import argparse, sys, os
from torchvision.models import efficientnet_v2_s, EfficientNet_V2_S_Weights
from torchvision.datasets import StanfordCars

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from src.utils import main

if __name__ == "__main__":

    parser = argparse.ArgumentParser("")
    parser.add_argument("--config", required = True, type = str, help = "Path to the configuration file")
    parser.add_argument("--run_name", required = False, type = str, help = "Name of the run")
    args = parser.parse_args()
    main(args = args,
         model_function = efficientnet_v2_s,
         weights = EfficientNet_V2_S_Weights.DEFAULT,
         dataset_function = StanfordCars,
         dataset_name = "StanfordCars",
         num_classes = 196)
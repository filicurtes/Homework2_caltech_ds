from caltech_dataset import Caltech

def main():
   train = Caltech("101_ObjectCategories", split='train')
   print(f"Length of the dataset {train.__len__}
   variable = list(train.targets.values())
   variable = sorted(variable)
   print(variable)


if __name__ == "__main__":
    main()

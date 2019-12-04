from extract_embeddings import *
from train_model import *
from recognize import *
import os

def main():
    path = './images'
    target = max([os.path.join(path, basename) for basename in os.listdir(path)], key=os.path.getctime)
    
    recognize(target)
    
    # whenever the users (professor, students) logging in
#    extract_embeddings()
#    train_model()

if __name__ == "__main__":
    main()

import os

root = "/home/ldlmdl/Documents/phngen/"
src_dir = root + 'src/'
data_dir = src_dir + "data/"

prolific_path = src_dir + "prolific.csv"
qualtrics_path = src_dir + "qualtrics.csv"
out_path = src_dir + "clean_data.csv"



def mk(dir): 
    os.makedirs(dir, exist_ok = True)

if __name__ == '__main__':
    # For all paths defined, run mk()
    for name, value in globals().copy().items():
        if isinstance(value, str) and not name.startswith("__") and os.path.isdir(value):
            globals()[name] = mk(value)
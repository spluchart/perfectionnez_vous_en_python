import os

def launch_analysis(data_file):
    '''



    '''
    directory = os.path.dirname(os.path.dirname(__file__))
    path_to_file = os.path.join(directory, "data", data_file)
    with open(path_to_file, 'r') as file:
        preview = file.readline()
        
    print("Apparently we managed to read the file. Here is a preview: {}".format(preview))


def main():
    launch_analysis('nosdeputes.fr_deputes_en_mandat_2018-06-25.csv')
    
if __name__ == "__main__":    
    main()
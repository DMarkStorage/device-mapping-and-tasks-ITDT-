import subprocess
import json, re
import pandas as pd
from docopt import docopt
from prettytable import PrettyTable

def get_args():
	"""Function to get command line arguments.

	Defines arguments needed to run this program.

	:return: Dictionary with arguments
	:rtype: dict
	"""
	
	usage = """
	Usage:
        itdt6.py -l <LIB> --vtask
        itdt6.py -l <LIB> --vlogs
        itdt6.py -l <LIB> --vdrives
        itdt6.py -l <LIB> --vlibrary
        itdt6.py -l <LIB> --slots
        itdt6.py -l <LIB> --nodecards
        itdt6.py -l <LIB> --datacart
        itdt6.py -l <LIB> --diagcart
        itdt6.py -l <LIB> --Accessors
        itdt6.py -l <LIB> --cleaningcart


		itdt6.py --version
		itdt6.py -h | --help

	Options:
		-h --help            Show this message and exit


	"""

	args = docopt(usage)
	return args	

def get_devices():
    """Function that will get all the devices"""
    output = subprocess.check_output(['device_scan', '-t', 'changer']).decode('utf-8')

    return output

def mapping(output):
    """This map the device and vendor info into lib"""

    # Split the file contents by each device
    devices = output.split('\n\n')
    # print(output)
    e = 1

    # Create an empty list to store the extracted information
    data = []
    # Create an empty list of device mapped to lib
    mapped =[]
    # # Loop through each device and extract the device and vendor info
    for device in devices:
        """ search for the pattern "Device=\[(.*?)\]", where (.*?) is anycharacter inside 
                 the square brackets [], from the string DEVICE.
                 
                 The program will get the characters inside the brackets and have it as 
                 a value for 'MATCH1'
                 
                 Similarly, we can find Vendor using regex with pattern
                 """ 
        match1 = re.search(r"Device=\[(.*?)\]", device)
        if match1:
            device_ = match1.group(1)

        match2 = re.search(r"Vendor info =	\[(.*?)\]", device)
        if match2:
            vendor = match2.group(1)
            """The match1 will be the device and the match2 will be the vendor info.
                Each time RE will find the match device and vendor will be appended to the 
                list named DATA
            """
            data.append([device_,vendor])


    for i in range(len(data)):

        if data[i][1] == '1803130000078AA3410':
            lib = '1'
        elif data[i][1] == '1803130000078AA3390':
            lib = '2'
        elif data[i][1] == '1901130000078AA4040':
            lib = '3'

        if i == 0:
            mapped.append([data[i][0],data[i][1],lib])
            
        else:
            if data[i][1] == data[i-1][1]:
                mapped.append([data[i][0],data[i][1],lib])
            else:
                e = e+1
                mapped.append([data[i][0],data[i][1],lib])

    # Create dataframe for mapping
    df = pd.DataFrame(mapped, columns=['devices', 'vendor', 'lib'])
    df = df.drop_duplicates(subset='lib', keep='first').reset_index(drop=True)

    return df

def get_mapped(df):
    """Create dictionary for the mapped data"""
       
    out = {row['lib']:[row['devices'], row['vendor']] for idx, row in df.iterrows()}
    return out

def get_command(driver, url):
    command = ['/opt/ITDT/itdt', '-f', driver, 'ros', 'GET', url]
    try:

        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, error = process.communicate()

        if error:
            print(f"Error: {error.decode('utf-8')}")
            exit(1)
        
        # Load the contents as JSON
        return json.loads(output.decode('utf-8'))

    except subprocess.CalledProcessError:
        return "Error running command."
    except FileNotFoundError:
        return "command not found."

def display(data):
    # Extract the field names (keys) from the first dictionary
    field_names = data[0].keys()

    # Create a PrettyTable with the extracted keys as field names
    table = PrettyTable(field_names)

    # Add rows to the table with values from the data
    for item in data:
        row = [item[key] for key in field_names]
        table.add_row(row)

    # Display the PrettyTable
    print(table)



def main(args):
    lib = args['<LIB>']
    output = get_devices()
    # print(type(output))

    data = mapping(output)
    # print(data)
    map_lib = get_mapped(data)
    # search for the lib that user enter from the DICT


    if lib in map_lib:
        # Get just one value from the search output
        driver = map_lib[lib][0]
        if args['--vtask']:
            url = "/v1/tasks"
            result = get_command(driver,url)
            display(result)

        if args['--vlogs']:
            url = "/v1/logs"
            result = get_command(driver,url)
            display(result)    

        if args['--vdrives']:
            url = "/v1/drives"
            result = get_command(driver,url)
            display(result)
            
        if args['--vlibrary']:
            url = "/v1/library"
            result = get_command(driver,url)
            display(result)

        if args['--slots']:
            url = "/v1/slots"
            result = get_command(driver,url)
            display(result)

        if args['--nodecards']:
            url = "/v1/nodeCards"
            result = get_command(driver,url)
            display(result)

        if args['--datacart']:
            url = "/v1/dataCartridges"
            result = get_command(driver,url)
            display(result)

        if args['--diagcart']:
            url = "/v1/diagnosticCartridges"
            result = get_command(driver,url)
            display(result)

        if args['--Accessors']:
            url = "/v1/accessors"
            result = get_command(driver,url)
            display(result)

        if args['--cleaningcart']:
            url = "/v1/cleaningCartridges"
            result = get_command(driver,url)
            display(result)
            
            
    else:
        print('The Lib you entered is not on the devices!')

    

if __name__ == '__main__':
    ARGS = get_args()
    main(ARGS)

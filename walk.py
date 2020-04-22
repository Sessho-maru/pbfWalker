from datetime import datetime
import sys
import os
import re

timestamps = []
markernames = []
processed_files_count = 0

def convert_ms_to_human_readable(ms):
	ms = int(ms)
	s = (ms / 1000) % 60
	s = int(s)
	m = (ms / ( 1000*60 )) % 60
	m = int(m)
	h = (ms / ( 1000*60*60 )) % 24
	h = int(h)
	return [h, m, s, ms % 1000]

def sort_by_first_int_key(foldername_or_filename):
    return int(re.findall('[0-9]+', foldername_or_filename)[0])

print("Source directory: ", file=sys.stderr)
src_directory = sys.stdin.readline().rstrip('\n')
src_directory_splited = src_directory.split('\\')
output_txt =  src_directory_splited[len(src_directory_splited) - 1] + '_converted' + '.txt'
output = open(output_txt, 'wb')

for root, content_folders, files in os.walk(src_directory):
    try:
        content_folders.sort(key=lambda folder_name: sort_by_first_int_key(folder_name))
    except IndexError:
        error_message = 'Every folder name must be numbered' + '\n'
        output.write(error_message.encode('UTF-16'))
        break

    root_seperated_by_slash = root.split('\\')
    foldername_contain_content_folder = root_seperated_by_slash[len(root_seperated_by_slash) - 2]
    content_folder_name = root.split('\\'+ foldername_contain_content_folder +'\\')

    if len(content_folder_name) > 1:
        content_folder_name[1] += '\n'
        output.write(content_folder_name[1].encode('UTF-16'))
            
        try:
            files.sort(key=lambda file_name: sort_by_first_int_key(file_name))
        except IndexError:
            error_message = 'Every file name must be numbered' + '\n'
            output.write(error_message.encode('UTF-16'))
            break

        for file in files:
            if '.pbf' in file:
                pbf_file_name = '\t' + file + '\n'
                output.write(pbf_file_name.encode('UTF-16'))
                with open (os.path.join(root, file), 'r', encoding='UTF-16') as raw:
                    raw_string = raw.read().replace('\x00', '')

                    timestamps = re.findall('[0-9]=[0-9]+', raw_string)
                    markernames = re.findall('\*.+\*', raw_string)

                    timestamp_makername_pair = {}
                    for i in range(0, len(timestamps)):
                        timestamp_makername_pair[timestamps[i].split('=')[1]] = markernames[i].replace('*', '')
                    for x in timestamp_makername_pair:
                        data = convert_ms_to_human_readable(x)
                        content_time_and_markername = '\t\t' + str(data[0]) + ':' + str(data[1]) + ':' + str(data[2]) + '.' + str(data[3]) +  '\n' + '\t\t\t' +  timestamp_makername_pair[x] + '\n'
                        output.write(content_time_and_markername.encode('UTF-16'))
                    
                output.write('\n'.encode('UTF-16'))
                processed_files_count = processed_files_count + 1
        output.write('\n'.encode('UTF-16'))

dateTimeObj = datetime.now()
message = str(processed_files_count) + ' files converted' + ' at ' + dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")
output.write(message.encode('UTF-16'))
output.close()
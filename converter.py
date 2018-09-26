import re

# re_string     keyname             val_start   val_stop
datagram_keys = (
('1-3:0.2.8',   "DSRM_version",     11,        12),
('0-0:1.0.0',   "date_time",        11,        23)
)

def read_datagram(datagram):
    for line in datagram:
        for re_str, keyname, val_start, val_stop in datagram_keys:
            if re.match(re_str, line):
                print(val_start, val_stop)
#                print(line[val_start,val_stop])
    return None




if __name__ == '__main__':
    output_file = []
    with open('sample_datagram') as file:
        for line in file:
            output_file.append(line)
    read_datagram(output_file)

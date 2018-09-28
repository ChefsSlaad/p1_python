import re

# re_dting     keyname             how to process
datagram_keys = (
('1-3:0.2.8',   "DSRM_version",       'int'),
('0-0:1.0.0',   "date_time",          'date-time'),
('0-0:96.1.1',  "e-serialnum",        'int'),
('1-0:1.8.1',   "tarif_1_delivered",  'kWh'),
('1-0:1.8.2',   "tarif_2_delivered",  'kWh'),
('1-0:2.8.1',   "tarif_1_returned",   'kWh'),
('1-0:2.8.2',   "tarif_2_returned",   'kWh'),
('0-0:96.14.0', "actual_tarif",       'int'),
('1-0:1.7.0',   "power_delivering",   'kW'),
('1-0:2.7.0',   "power_returning",    'kW'),
('0-0:96.7.21', "total_power_fails",  'int'),
('0-0:96.7.9',  "long_power_fails",   'int'),
('1-0:99.97.0', "power_fail_log",     'fail-log'),  # not sure what the output should look like
('1-0:32.32.0', "voltage_sags_L1",    'int'),
('1-0:52.32.0', "voltage_sags_L2",    'int'),
('1-0:72.32.0', "voltage_sags_L3",    'int'),
('1-0:32.36.0', "voltage_swells_L1",  'int'),
('1-0:52.36.0', "voltage_swells_L2",  'int'),
('1-0:72.36.0', "voltage_swells_L3",  'int'),
('0-0:96.13.0', "text_message",       'string'),
('1-0:32.7.0',  "voltage_L1",         'Volts'),
('1-0:52.7.0',  "voltage_L2",         'Volts'),
('1-0:72.7.0',  "voltage_L3",         'Volts'),
('1-0:31.7.0',  "current_L1",         'Amps'),
('1-0:51.7.0',  "current_L2",         'Amps'),
('1-0:71.7.0',  "current_L3",         'Amps'),
('1-0:21.7.0',  "power_L1_+P",        'kW'),
('1-0:41.7.0',  "power_L2_+P",        'kW'),
('1-0:61.7.0',  "power_L3_+P",        'kW'),
('1-0:21.7.0',  "power_L1_-P",        'kW'),
('1-0:21.7.0',  "power_L2_-P",        'kW'),
('1-0:21.7.0',  "power_L3_-P",        'kW'),
('0-1:24.1.0',  "device_type",        'int'),
('0-1:96.1.0',  "g-serialnum",        'int'),
('0-1:24.2.1',  "gas_delivered",      'gas-reading')
)

def read_datagram(datagram):
    result = {}
    for line in datagram:
        for re_str, keyname, type in datagram_keys:
            if re.match(re_str, line):
                if type in ('int', 'kWh', 'kW', 'Volts', 'Amps', 'string'):
                    result[keyname] = read_line(line, type)
                elif type == 'date-time':
                    dt_tuple, dt_str = read_date_time(line)
                    result['date_time_str'] = dt_str
                    result[keyname] = dt_tuple
                else:
                    result[keyname] = None
                break
#    print(result)
    return result

def read_line(line, type = 'int'):
    between_brackets = '\(.*?\)' #characters betweem brackets ()
    match = re.search(between_brackets, line) #return the stings
    if type == 'string':
        return match.group()[1:-1] #remove brackets
    if type == 'int':
        return int(match.group()[1:-1]) #remove brackets, convert to integer
    elif type == 'Amps':
        return int(match.group()[1:-3]) #remove brackets, *kwh, convert to float
    elif type == 'kWh':
        return float(match.group()[1:-5]) #remove brackets, *kwh, convert to float
    elif type == 'kW':
        return float(match.group()[1:-4]) #remove brackets, *kwh, convert to float
    elif type == 'Volts':
        return float(match.group()[1:-3]) #remove brackets, *kwh, convert to float

def read_kWh(line):
    return read_int(line, type='kWh')

def read_date_time(line):
    between_brackets = '\(.*?\)' #characters betweem brackets ()
    match = re.search(between_brackets, line)
    dt = match.group()[1:-1] # format bis YYMMDDHHMMSS. drop the summer/winter time indicator
    dt_tuple = (dt[0:2], dt[2:4], dt[4:6], dt[6:8], dt[8:10], dt[10:12])
    date_time_tuple = tuple(int(x) for x in dt_tuple)
    date_time_str = "".join("".join(x) for x in zip(dt_tuple, tuple(list('-- ::+'))))[:-1]
    return date_time_tuple,  date_time_str

if __name__ == '__main__':
    output_file = []
    with open('sample_datagram') as file:
        for line in file:
            output_file.append(line)
    print(read_datagram(output_file))

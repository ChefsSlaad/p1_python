import re

# re_string     keyname             how to process
datagram_keys = (
('1-3:0.2.8',   "DSRM_version",       'int'),
('0-0:1.0.0',   "date_time",          'date-time'),
('0-0:96.1.1',  "e-serialnum",        'int'),
('1-0:1.8.1',   "tarif_1_delivered",  'kWh'),
('1-0:1.8.2',   "tarif_2_delivered",  'kWh'),
('1-0:2.8.1',   "tarif_1_returned",   'kWh'),
('1-0:2.8.2',   "tarif_2_returned",   'kWh'),
('0-0:96.14.0', "actual_tarif",       'int'),
('1-0:1.7.0',   "power_delivered",    'kWh'),
('1-0:2.7.0',   "power_returned",     'kWh'),
('0-0:96.7.21', "total_power_fails",  'int'),
('0-0:96.7.9',  "long_power_fails",   'int'),
('1-0:99.97.0', "power_fail_log",     'special'),  # not sure what the output should look like
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
('1-0:21.7.0',  "power_L1_+P",        'kWh'),
('1-0:41.7.0',  "power_L2_+P",        'kWh'),
('1-0:61.7.0',  "power_L3_+P",        'kWh'),
('1-0:21.7.0',  "power_L1_-P",        'kWh'),
('1-0:21.7.0',  "power_L2_-P",        'kWh'),
('1-0:21.7.0',  "power_L3_-P",        'kWh'),
('0-1:24.1.0',  "device_type",        'int'),
('0-1:96.1.0',  "g-serialnum",        'int'),
('0-1:24.2.1',  "gas_delivered",      'special')
)

def read_datagram(datagram):
    result = {}
    for line in datagram:
        for re_str, keyname, type in datagram_keys:
            if re.match(re_str, line):
                if type == 'int':
                    processed_value = read_int(line)
                result[keyname] = processed_value
                break
    print(result)
    return result

def read_int(line):
    between_brackets = '\(.*?\)' #characters betweem brackets ()
    match = re.search(between_brackets, line).group() #return the stings
    return int(match[1:-1]) #remove brackets, convert to integer

if __name__ == '__main__':
    output_file = []
    with open('sample_datagram') as file:
        for line in file:
            output_file.append(line)
    read_datagram(output_file)

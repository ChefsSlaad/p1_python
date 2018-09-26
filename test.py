import unittest
import converter

class read_results(unittest.TestCase):
    expected_output = {
            "DSRM_version":       50,
            "date_time":          1515439537,
            "date_time_str":      "2018-01-08 20:25:37",
            "e-seriemummer":      000000000,
            "tarif_1_delivered":  0.855,
            "tarif_2_delivered":  0.693,
            "tarif_1_returned":   0.084,
            "tarif_2_returned":   0.000,
            "actual_tarif":       2,
            "power_delivered":    0.134,
            "power_returned":     0.000,
            "total_power_fails":  8,
            "long_power_fails":   4,
            "power_fail_log":     None,  # not sure what the output should look like
            "voltage_sags_L1":    3,
            "voltage_sags_L2":    3,
            "voltage_sags_L3":    2,
            "voltage_swels_L1":   0,
            "voltage_swels_L2":   0,
            "voltage_swels_L3":   0,
            "text_message":       "",
            "voltage_L1":         229.0,
            "voltage_l2":         226.0,
            "voltage_l3":         229.0,
            "current_L1":         0,
            "current_L2":         0,
            "current_L3":         0,
            "power_L1_+P":        0.094,
            "power_L2_+P":        0.040,
            "power_L3_+P":        0.000,
            "power_L1_-P":        0.000,
            "power_L2_-P":        0.000,
            "power_L3_-P":        0.000,
            "device_type":        3,
            "g-serienummer":      000000000,
            "gas_read_time":      1515441300,
            "gas_read_time_str":  "2018-01-08-20:55:00",
            "gas_delivered":      1290
            }

    def test_read_frombytes(self):
        filename = 'sample_datagram'
        with open(filename) as f:
            output_file = f.read()
        output = converter.read_datagram(output_file)
        self.assertEqual(output, self.expected_output)

if __name__ == '__main__':
    unittest.main()

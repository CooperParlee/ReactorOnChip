import configparser

class Config:
    def create_config():
        config = configparser.ConfigParser()
        # Add sections and key-value pairs
        config['General'] = {
            'debug': 'True',
            'log_level': 'info'
        }
        config['Simulation'] = {
            'fluid_parcels': '25',
            'global_noise': '0.05',
            'sleep_time': '0.05',
        }
        config['Modbus'] = {
            'address': '127.0.0.1',
            'port': '5020',
            'num_di': '100',
            'num_co': '100',
            'num_hr': '100',
            'num_ir': '100',
        }
        # Write the configuration to a file
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def readConfig():
        config = configparser.ConfigParser()

        config.read('config.ini')

        # access specific values from the config

        config_values ={
            # General
            'debug': config.getboolean('General', 'debug'),
            'log_level': config.get('General', 'log_level'),

            # Simulation
            'fluid_parcels': config.getint('Simulation', 'fluid_parcels'),
            'global_noise': config.getfloat('Simulation', 'global_noise'),
            'sleep_time': config.getfloat('Simulation', 'sleep_time'),
            
            # Modbus
            'address': config.get('Modbus', 'address'),
            'port': config.getint('Modbus', 'port'),
            'num_di': config.getint('Modbus', 'num_di'),
            'num_co': config.getint('Modbus', 'num_co'),
            'num_hr': config.getint('Modbus', 'num_hr'),
            'num_ir': config.getint('Modbus', 'num_ir'),

        }

        return config_values


    if __name__ == "__main__":
        create_config()
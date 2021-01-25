import configparser
import uvicorn


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('development.ini')

if 'main:APP' in config.sections():
        development_params = config['main:APP']
        uvicorn.run(
            'main:APP',
            host=development_params.get('host', '127.0.0.1'),
            port=development_params.getint('port', 8000),
            log_level=development_params.get('log_level', 'debug'),
            reload=development_params.get('reload', True)
        )

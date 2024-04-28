import yaml

with open('config.yaml') as conf_file:
    data = yaml.safe_load(conf_file)
    BOT_TOKEN = data['BOT_TOKEN']
    CRYPTO_BOT_TOKEN = data['CRYPTOBOTTOKEN']
    BOT_ADMIN = data['BOT_ADMIN']
    HOST = data['HOST']
    PORT = data['PORT']
    USER = data['USER']
    PASSWORD = data['PASSWORD']
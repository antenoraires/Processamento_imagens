import yaml
from processamento_imagens import control

# Abre e lê o arquivo YAML
with open('processamento_imagens/assents/config.yaml', 'r') as file:
    config = yaml.safe_load(file)
print(config['img'])

for img in config['img'].keys():
	data_img = control.read_img(img)

data = control.read_img(config['img']['img1'])

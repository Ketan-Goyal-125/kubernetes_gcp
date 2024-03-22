import base64
from st2common.runners.base_action import Action
from kubernetes import client, config as conf

class K8sClient(Action):
    def __init__(self,config=None):

        super(K8sClient, self).__init__(config=config)
        encoded_kube_config = self.config['encode'] 

        decoded_kube_config = base64.b64decode(encoded_kube_config.encode('utf-8')).decode('utf-8')

        with open('temp_kube_config', 'w') as f:
            f.write(decoded_kube_config)
        
        conf.load_kube_config(config_file='temp_kube_config')

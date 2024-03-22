
from lib.k8s import K8sClient
from kubernetes import client, config

class CreateNamespace(K8sClient):
    def run(self,config_override=None):
        try:
            # Create Kubernetes client
            k8s_client = client.CoreV1Api()

            # Define the namespace body
            namespace_body = client.V1Namespace(metadata=client.V1ObjectMeta(name="example-namespace"))

            # Create the namespace
            created_namespace = k8s_client.create_namespace(namespace_body)

            return (True, f"Namespace created successfully: {created_namespace.metadata.name}")
        except Exception as e:
            return (False, f"Error creating namespace: {e}")
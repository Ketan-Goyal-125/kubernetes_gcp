import os
from lib.k8s import K8sClient
from kubernetes import client, config

class PatchHPA(K8sClient):
    def run(self,body,name,namespace="default",config_override=None):
        try:
            # Create Kubernetes client
            k8s_client = client.CoreV1Api()

            # Define the namespace body
            hpaClient = client.AutoscalingV2Api()

            # Create the namespace
            patched_hpa = hpaClient.patch_namespaced_horizontal_pod_autoscaler(name = name,namespace = namespace,body = body)

            return (True, f"HPA patched successfully: {patched_hpa.metadata.name}")
        except Exception as e:
            return (False, f"Error creating namespace: {e}")
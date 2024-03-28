from kubernetes import client, config
from lib.k8s import K8sClient


class PatchDeploymentAction(K8sClient):
    def run(self, deployment_name, namespace, patch):
        # Load Kubernetes configuration from default location
        api_instance = client.AppsV1Api()

        # Construct the patch request body
        patch_body = {"spec": patch}

        try:
            # Patch the Deployment
            api_instance.patch_namespaced_deployment(
                name=deployment_name,
                namespace=namespace,
                body=patch_body
            )
            return True, f"Deployment {deployment_name} patched successfully."
        except Exception as e:
            return False, f"Failed to patch Deployment {deployment_name}: {str(e)}"

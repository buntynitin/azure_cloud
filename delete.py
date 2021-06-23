from azure.storage.blob import ContainerClient


def delete(connection_string, container_name, blob_name):
    container_client = ContainerClient.from_connection_string(connection_string, container_name)
    container_client.delete_blob(blob=blob_name)

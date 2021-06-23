from azure.storage.blob import ContainerClient


def download(connection_string, container_name, blob_name):
    container_client = ContainerClient.from_connection_string(connection_string, container_name)
    blob_client = container_client.get_blob_client(blob_name)
    bytes_content = blob_client.download_blob().readall()
    return bytes_content

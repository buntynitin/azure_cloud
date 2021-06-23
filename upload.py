import os
from azure.storage.blob import ContainerClient


def upload(file, connection_string, container_name, auto_delete):
    container_client = ContainerClient.from_connection_string(connection_string, container_name)
    print("Uploading files .....")
    blob_client = container_client.get_blob_client(os.path.basename(file))
    with open(file, "rb") as data:
        blob_client.upload_blob(data)
        print(f'{file} uploaded to blob storage')
    if auto_delete:
        os.remove(file)
        print(f'{file} deleted from local storage')
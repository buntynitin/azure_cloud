from azure.storage.blob import ContainerClient


def ls(connection_string, container_name):
    file_list = []
    container_client = ContainerClient.from_connection_string(connection_string, container_name)
    for blob in container_client.list_blobs():
        file_list.append({
            'name': blob.name,
            'size': blob.size,
            'creation_time': blob.creation_time.strftime("%m/%d/%Y, %H:%M:%S"),
            'last_modified': blob.last_modified.strftime("%m/%d/%Y, %H:%M:%S")
        })
    return file_list


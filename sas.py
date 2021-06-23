from datetime import datetime
from azure.storage.blob import generate_blob_sas, generate_container_sas, BlobSasPermissions, ContainerSasPermissions


def download_blob_sas(account_name: str, account_key: str, container_name: str, blob_name: str,
                      expiration_time: datetime) -> str:
    sas = generate_blob_sas(account_name=account_name,
                            account_key=account_key,
                            container_name=container_name,
                            blob_name=blob_name,
                            permission=BlobSasPermissions(read=True),
                            expiry=expiration_time)

    sas_url = 'https://' + account_name + '.blob.core.windows.net/' + container_name + '/' + blob_name + '?' + sas
    return sas_url


def upload_blob_sas(account_name: str, account_key: str, container_name: str, blob_name: str,
                    expiration_time: datetime) -> str:
    sas = generate_container_sas(account_name=account_name,
                                 account_key=account_key,
                                 container_name=container_name,
                                 permission=ContainerSasPermissions(write=True),
                                 expiry=expiration_time)

    sas_url = 'https://' + account_name + '.blob.core.windows.net/' + container_name + '/' + blob_name + '?' + sas
    return sas_url

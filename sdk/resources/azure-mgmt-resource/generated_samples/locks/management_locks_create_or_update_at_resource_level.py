# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.resource import ManagementLockClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-resource
# USAGE
    python management_locks_create_or_update_at_resource_level.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ManagementLockClient(
        credential=DefaultAzureCredential(),
        subscription_id="subscriptionId",
    )

    response = client.management_locks.create_or_update_at_resource_level(
        resource_group_name="resourcegroupname",
        resource_provider_namespace="Microsoft.Storage",
        parent_resource_path="parentResourcePath",
        resource_type="storageAccounts",
        resource_name="teststorageaccount",
        lock_name="testlock",
        parameters={"properties": {"level": "ReadOnly"}},
    )
    print(response)


# x-ms-original-file: specification/resources/resource-manager/Microsoft.Authorization/stable/2016-09-01/examples/ManagementLocks_CreateOrUpdateAtResourceLevel.json
if __name__ == "__main__":
    main()

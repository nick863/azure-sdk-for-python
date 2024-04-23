# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.cdn import CdnManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-cdn
# USAGE
    python check_name_availability.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = CdnManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="SUBSCRIPTION_ID",
    )

    response = client.check_name_availability(
        check_name_availability_input={"name": "sampleName", "type": "Microsoft.Cdn/Profiles/Endpoints"},
    )
    print(response)


# x-ms-original-file: specification/cdn/resource-manager/Microsoft.Cdn/stable/2024-02-01/examples/CheckNameAvailability.json
if __name__ == "__main__":
    main()

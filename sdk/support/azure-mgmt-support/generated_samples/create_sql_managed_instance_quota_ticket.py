# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.support import MicrosoftSupport

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-support
# USAGE
    python create_sql_managed_instance_quota_ticket.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MicrosoftSupport(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.support_tickets.begin_create(
        support_ticket_name="testticket",
        create_support_ticket_parameters={
            "properties": {
                "advancedDiagnosticConsent": "Yes",
                "contactDetails": {
                    "country": "usa",
                    "firstName": "abc",
                    "lastName": "xyz",
                    "preferredContactMethod": "email",
                    "preferredSupportLanguage": "en-US",
                    "preferredTimeZone": "Pacific Standard Time",
                    "primaryEmailAddress": "abc@contoso.com",
                },
                "description": "my description",
                "problemClassificationId": "/providers/Microsoft.Support/services/quota_service_guid/problemClassifications/sql_managedinstance_problemClassification_guid",
                "quotaTicketDetails": {
                    "quotaChangeRequestSubType": "SQLMI",
                    "quotaChangeRequestVersion": "1.0",
                    "quotaChangeRequests": [
                        {"payload": '{"NewLimit":200, "Metadata":null, "Type":"vCore"}', "region": "EastUS"},
                        {"payload": '{"NewLimit":200, "Metadata":null, "Type":"Subnet"}', "region": "EastUS"},
                    ],
                },
                "serviceId": "/providers/Microsoft.Support/services/quota_service_guid",
                "severity": "moderate",
                "supportPlanId": "U291cmNlOlNDTSxDbGFyaWZ5SW5zdGFsbGF0aW9uU2l0ZUlkOjcsTGluZUl0ZW1JZDo5ODY1NzIyOSxDb250cmFjdElkOjk4NjU5MTk0LFN1YnNjcmlwdGlvbklkOjc2Y2I3N2ZhLThiMTctNGVhYi05NDkzLWI2NWRhY2U5OTgxMyw=",
                "title": "my title",
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/support/resource-manager/Microsoft.Support/preview/2023-06-01-preview/examples/CreateSqlManagedInstanceQuotaTicket.json
if __name__ == "__main__":
    main()

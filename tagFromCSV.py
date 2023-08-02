"""
Python3 Script to Tag Exsiting Virtual Machines in Azure

Authentication via Azure CLI Credentials

CSV List Order "SUBSCRIPTIONID","ID","NAME","PROTECTIONSTATE","VAULTNAME","POLICYNAME"
"""

import os
import csv
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import TagsPatchResource

credential = AzureCliCredential()

with open ('UpdateTags.csv', 'r') as csv_file:
    csvReader = csv.reader(csv_file, delimiter=',' )
    next(csvReader)
    for row in csvReader:
        if (row[3] == "ProtectionConfigured"):  
            tags = {
                "VaultName": row[4],
                "Policy": row[5]
            }
           
            subscriptionId = f"{row[0]}"
            resClient = ResourceManagementClient(credential, subscriptionId)
            
            tagPatchResource = TagsPatchResource(
                 operation="Merge",
                 properties={'tags': tags}
            )

            resource = resClient.resources.get_by_id(f"{row[1]}", "2022-11-01")

            resClient.tags.begin_update_at_scope(f"{resource.id}", tagPatchResource)

            print(f"Tags {tagPatchResource.properties.tags} were added to existing tags on resource with ID: {row[1]}")
        else:
            tags = {
                "Vault": "No Vault",
                "Policy": "No Backup"
            }            
            subscriptionId = f"{row[0]}"
            
            resClient = ResourceManagementClient(credential, subscriptionId)
            
            tagPatchResource = TagsPatchResource(
                 operation="Merge",
                 properties={'tags': tags}
            )
            resource = resClient.resources.get_by_id(f"{row[1]}", "2022-11-01")
            resClient.tags.begin_update_at_scope(f"{resource.id}", tagPatchResource)

            print(f"Tags {tagPatchResource.properties.tags} were added to existing tags on resource with ID: {resource.id}")


print("________________________________________________DONE__________________________________________________")

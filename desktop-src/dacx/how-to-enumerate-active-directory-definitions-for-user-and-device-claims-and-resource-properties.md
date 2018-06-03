---
title: How to read Dynamic Access Control objects using LDAP
description: This code sample will enumerate all of the Dynamic Access Control objects in Active Directory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 17425694-AFC9-448A-8C97-F841850F6ED8
ms.prod: windows-server-dev
ms.technology: dynamic-access-control
ms.tgt_platform: multiple
keywords:
- Dynamic Access Control developer extensibility DACx , enumerate definitions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to read Dynamic Access Control objects using LDAP

This code sample will enumerate all of the Dynamic Access Control objects in Active Directory.

### Prerequisites

-   C# and .NET Framework programming
-   Basic understanding of the [System.DirectoryServices.Protocols](https://msdn.microsoft.com/library/system.directoryservices.protocols.aspx) namespace, objects and methods.

> [!Note]  
> This example contains queries that use Active Directory Schema attributes, such as **msDS-ClaimAttributeSource**. For information about specific attributes in the example, see [All Attributes](https://msdn.microsoft.com/library/ms675090.aspx).

 

## Instructions

### Step 1:


```CSharp
/*********************************************** 
*  
* Find all of the Claim Types in the directory.
* 
***********************************************/

// Create a new Ldap endpoint with an empty server.  This call will use the 
// Standard DC locator methods to locate a Domain Controller.
var endpoint = new System.DirectoryServices.Protocols.LdapDirectoryIdentifier(string.Empty);

// Create a new Ldap connection.
var ldap_connection = new System.DirectoryServices.Protocols.LdapConnection(endpoint);

// Create a search request to locate the Configuration Naming Context for the forest.
var request = new System.DirectoryServices.Protocols.SearchRequest(
    "",
    "objectClass=*",
    System.DirectoryServices.Protocols.SearchScope.Base,
    new string[] { "configurationNamingContext" });

// Execute the search and cast the response as a SearchResponse
var response = (System.DirectoryServices.Protocols.SearchResponse)ldap_connection.SendRequest(request);

// Get the Configuration container DN for the forest.
string configuration_dn = response.Entries[0].Attributes["configurationNamingContext"][0].ToString();

// Calculate the Claims Configuration DN based on the Configuration DN.
string claims_dn =
    string.Format("CN=Claim Types,CN=Claims Configuration,CN=Services,{0}", configuration_dn);

// Create a new search request for Claim Types.
request = new System.DirectoryServices.Protocols.SearchRequest(
    claims_dn,
    "(cn=*)",
        System.DirectoryServices.Protocols.SearchScope.OneLevel,
        new string[] 
        {
            "name",
            "description",
            "displayname",
            "enabled",
            "msDS-ClaimAttributeSource",
            "msDS-ClaimSource",
            "msDS-ClaimTypeAppliesToClass",
            "msDS-ClaimSourceType",
            "msDS-ClaimIsSingleValued",
            "msDS-ClaimPossibleValues",
            "msDS-ClaimValueType",
            "msDS-ClaimIsValueSpaceRestricted"
        });

// Execute the search and cast the response as a SearchResponse
response = (System.DirectoryServices.Protocols.SearchResponse)ldap_connection.SendRequest(request);

// Enumerate the results
foreach (System.DirectoryServices.Protocols.SearchResultEntry entry in response.Entries)
{
    string claim_id = entry.Attributes["name"][0].ToString();
}

/*********************************************** 
*  
* Find all of the Resource Properties in the directory.
* 
***********************************************/

// Calculate the Resource Property Container DN based on the Configuration DN.
string resource_properties_dn = 
    string.Format("CN=Resource Properties,CN=Claims Configuration,CN=Services,{0}", configuration_dn);

// Create a new search request for Resource Properties.
request = new System.DirectoryServices.Protocols.SearchRequest(
    resource_properties_dn,
    "(cn=*)",
        System.DirectoryServices.Protocols.SearchScope.OneLevel,
        new string[] 
        {
            "name",
            "description",
            "displayname",
            "enabled",
            "msDS-IsUsedAsResourceSecurityAttribute",
            "msDS-ClaimSharesPossibleValuesWith",
            "msDS-ValueTypeReference",
            "msDS-MembersOfResourcePropertyListBL",
            "msDS-ClaimPossibleValues",
            "msDS-AppliesToResourceTypes"

        });

// Execute the search and cast the response as a SearchResponse
response = (System.DirectoryServices.Protocols.SearchResponse)ldap_connection.SendRequest(request);

// Enumerate the results
foreach (System.DirectoryServices.Protocols.SearchResultEntry entry in response.Entries)
{
    string rp_id = entry.Attributes["name"][0].ToString();
}

/*********************************************** 
*  
* Find all of the Central Access Rules in the directory.
* 
***********************************************/

// Calculate the Central Access Rules Container DN based on the Configuration DN.
string car_dn =
    string.Format("CN=Central Access Rules,CN=Claims Configuration,CN=Services,{0}", configuration_dn);

// Create a new search request for Resource Properties.
request = new System.DirectoryServices.Protocols.SearchRequest(
    car_dn,
    "(cn=*)",
        System.DirectoryServices.Protocols.SearchScope.OneLevel,
        new string[] 
        {
            "name",
            "description",
            "displayname",
            "enabled",
            "msAuthz-EffectiveSecurityPolicy",
            "msAuthz-LastEffectiveSecurityPolicy",
            "msAuthz-ProposedSecurityPolicy",
            "msAuthz-ResourceCondition"
        });

// Execute the search and cast the response as a SearchResponse
response = (System.DirectoryServices.Protocols.SearchResponse)ldap_connection.SendRequest(request);

// Enumerate the results
foreach (System.DirectoryServices.Protocols.SearchResultEntry entry in response.Entries)
{
    string car_id = entry.Attributes["name"][0].ToString();
}

/*********************************************** 
*  
* Find all of the Central Access Policies in the directory.
* 
***********************************************/

// Calculate the Central Access Policies Container DN based on the Configuration DN.
string cap_dn =
    string.Format("CN=Central Access Policies,CN=Claims Configuration,CN=Services,{0}", configuration_dn);

// Create a new search request for Resource Properties.
request = new System.DirectoryServices.Protocols.SearchRequest(
    cap_dn,
    "(cn=*)",
        System.DirectoryServices.Protocols.SearchScope.OneLevel,
        new string[] 
        {
            "name",
            "description",
            "displayname",
            "enabled",
            "msAuthz-EffectiveSecurityPolicy",
            "msAuthz-LastEffectiveSecurityPolicy",
            "msAuthz-ProposedSecurityPolicy",
            "msAuthz-ResourceCondition"
        });

// Execute the search and cast the response as a SearchResponse
response = (System.DirectoryServices.Protocols.SearchResponse)ldap_connection.SendRequest(request);

// Enumerate the results
foreach (System.DirectoryServices.Protocols.SearchResultEntry entry in response.Entries)
{
    string cap_id = entry.Attributes["name"][0].ToString();
}
```



## Related topics

<dl> <dt>

[System.DirectoryServices.Protocols](https://msdn.microsoft.com/library/system.directoryservices.protocols.aspx)
</dt> <dt>

[Introduction to System.DirecotoryServices.Protocols](https://msdn.microsoft.com/library/bb332056.aspx)
</dt> </dl>

 

 





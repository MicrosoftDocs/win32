---
title: Dynamic Access Control objects in Active Directory
description: All the objects mentioned in this scenario live in configuration naming context in Active Directory, the objects will be replicated throughout the entire forest.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 40001833-2131-406A-AE86-49B9C55AAD38
ms.prod: windows-server-dev
ms.technology: dynamic-access-control
ms.tgt_platform: multiple
keywords:
- Dynamic Access Control developer extensibility DACx , containers
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic Access Control objects in Active Directory

All the objects mentioned in this scenario live in configuration naming context in Active Directory, the objects will be replicated throughout the entire forest. If you create your own objects of these types, they must be defined only in the Configuration Partition in the appropriate containers to be considered valid and work in the expected manner. In order to get the most recent information about the object, you should use ReadRootDSE call to interact with Active Directory.

All objects that are related with central access policies are stored in [Active Directory Configuration Naming Context](https://TechNet.Microsoft.Com/library/aa998375.aspx) on TechNet.

These objects make up the [Dynamic Access Control Central Access Policy Scenario](https://TechNet.Microsoft.Com/library/hh831425.aspx):

-   Claim Type (msDS-ClaimType)

    This container holds the definitions for user claims and device claims that map what AD attributes would be added to the user’s Kerberos token to be used for authorization decisions.

-   Resource Property (msDS-ResourceProperty)

    This container holds the definitions for the resource properties. These resource properties can be assigned to files on file servers across the organization so that they can be used for authorization and data management.

-   Resource Property List (msDS-ResourcePropertyList)

    This container holds lists of resource properties (including a default in-box list). You can use a list of resource properties with the combination of group policy to show only specific properties in the Windows classification UI.

-   Central Access Rule (msAuthz-CentralAccessRule)

    This container holds access rules that can be used for access control that reflects business policies (for example: Users can only access files that belong to their department). These access rules are referenced in central access policies that get applied across file servers in the organization.

-   Central Access Policy (msAuthz-CentralAccessPolicy)

    This container holds central access policies. Each central access policy references multiple central access rules. A central access policy can be applied to one or more file servers/shares across the organization.

## Instructions

### Protect from accidental deletion

-   All the objects mentioned in this document contribute to access control, thus, it is recommended that you protect them from accidental deletion during their creation by default. For more information, see [Guarding Against Accidental Bulk Deletions in Active Directory](https://TechNet.Microsoft.Com/library/cc773347.aspx) on TechNet.

## Related topics

<dl> <dt>

[How to use central access policies for dynamic access control (Intro Page)](how-to-use-central-access-policies-for-dynamic-access-control.md)
</dt> </dl>

 

 





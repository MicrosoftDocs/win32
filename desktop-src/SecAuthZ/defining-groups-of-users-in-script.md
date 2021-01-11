---
description: An IAzApplicationGroup object represents a group of users. Roles can then be assigned to this group of users collectively. An IAzApplicationGroup object can also include other IAzApplicationGroup objects as members.
ms.assetid: 8b445419-7316-4034-b742-a05845af1862
title: Defining Groups of Users in Script
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Defining Groups of Users in Script

In Authorization Manager, an [**IAzApplicationGroup**](/windows/desktop/api/Azroles/nn-azroles-iazapplicationgroup) object represents a group of users. Roles can then be assigned to this group of users collectively. An **IAzApplicationGroup** object can also include other **IAzApplicationGroup** objects as members. For more information about application groups, see [Users and Groups](users-and-groups.md).

A group can be defined either by explicit lists of members and nonmembers or by a [*Lightweight Directory Access Protocol*](/windows/desktop/SecGloss/l-gly) (LDAP) query. The following examples show how to create each type of application group:

-   [Creating a Basic Group](#creating-a-basic-group)
-   [Creating an LDAP Query Group](#creating-an-ldap-query-group)

## Creating a Basic Group

A basic application group is defined by the members included in the [**Members**](/windows/desktop/api/Azroles/nf-azroles-iazapplicationgroup-get_members) and [**NonMembers**](/windows/desktop/api/Azroles/nf-azroles-iazapplicationgroup-get_nonmembers) properties of the [**IAzApplicationGroup**](/windows/desktop/api/Azroles/nn-azroles-iazapplicationgroup) object that represents the group. Users and groups listed in the **Members** property are included in the application group, and users and groups listed in the **NonMembers** property are excluded from the application group. Being listed in the **NonMembers** property supersedes being listed in the **Members** property.

The following example shows how to create a basic application group and add all local users as members of that group. The example assumes that there is an existing XML policy store named MyStore.xml in the root directory of drive C.


```VB
'  Create the AzAuthorizationStore object.
Dim AzManStore
Set AzManStore = CreateObject("AzRoles.AzAuthorizationStore")

'  Initialize the authorization store.
AzManStore.Initialize 2, "msxml://C:\MyStore.xml"

'  Create an application object in the store.
Dim expenseApp
Set expenseApp= AzManStore.OpenApplication("Expense")

'  Create an application group object.
Dim appGroup
Set appGroup = expenseApp.CreateApplicationGroup("Trusted Users")

'  Add a well-known SID for all local users to the group.
appGroup.AddMember("S-1-1-0")

'  Save the application group to the store.
appGroup.Submit
```



## Creating an LDAP Query Group

An LDAP query group has a membership defined by the query contained in the value of its [**LdapQuery**](/windows/desktop/api/Azroles/nf-azroles-iazapplicationgroup-get_ldapquery) property.

The following example shows how to create an LDAP query application group and add all users as members of that group. The example assumes that there is an existing XML policy store named MyStore.xml in the root directory of drive C.


```VB
'  Create the AzAuthorizationStore object.
Dim AzManStore
Set AzManStore = CreateObject("AzRoles.AzAuthorizationStore")

'  Initialize the authorization store.
AzManStore.Initialize 2, "msxml://C:\MyStore.xml"

'  Create an application object in the store.
Dim expenseApp
Set expenseApp= AzManStore.OpenApplication("Expense")

'  Create an application group object.
Dim appGroup
Set appGroup = expenseApp.CreateApplicationGroup("LDAP Trusted Users")

'  Set the Type property of the group to two
'  (AZ_GROUPTYPE_LDAP_QUERY).
appGroup.Type = 2

'  Add LDAP query for all users.
appGroup.LdapQuery = ("&(objectCategory=person)(objectClass=user)")

'  Save the application group to the store.
appGroup.Submit

```



 

 

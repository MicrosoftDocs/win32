---
description: You can delegate the administration of the authorization policy stores that are stored in Active Directory.
ms.assetid: a7b43dfe-f03e-4795-bbd3-746eb3449fd0
title: Delegating the Defining of Permissions in Script
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Delegating the Defining of Permissions in Script

You can delegate the administration of authorization policy stores that are stored in Active Directory. Administration can be delegated to users and groups at the store, application, or scope level.

At each level, there is a list of administrators and readers. Administrators of a store, application, or scope can read and modify the policy store at the delegated level. Readers can read the policy store at the delegated level but cannot modify the store.

A user or group that is either an administrator or a reader of an application must also be added as a delegated user of the policy store that contains that application. Similarly, a user or group that is an administrator or a reader of a scope must be added as a delegated user of the application that contains that scope.

**To delegate administration of a scope**

1.  Add the user or group to the list of delegated users of the store that contains the scope by calling the [**AddDelegatedPolicyUser**](/windows/desktop/api/Azroles/nf-azroles-iazauthorizationstore-adddelegatedpolicyuser) method of the [**AzAuthorizationStore**](/windows/desktop/api/Azroles/nn-azroles-iazauthorizationstore) object that contains the scope.
2.  Add the user or group to the list of delegated users of the application that contains the scope by calling the [**AddDelegatedPolicyUser**](/windows/desktop/api/Azroles/nf-azroles-iazapplication-adddelegatedpolicyuser) method of the [**IAzApplication**](/windows/desktop/api/Azroles/nn-azroles-iazapplication) object that contains the scope.
3.  Add the user or group to the list of administrators of the scope by calling the [**AddPolicyAdministrator**](/windows/desktop/api/Azroles/nf-azroles-iazscope-addpolicyadministrator) method of the [**IAzScope**](/windows/desktop/api/Azroles/nn-azroles-iazscope) object.

> [!Note]  
> XML-based policy stores do not support delegation at any level.

 

If a scope within an authorization store that is stored in Active Directory contains task definitions that include authorization rules or role definitions that include authorization rules, the scope cannot be delegated.

The following example shows how to delegate administration of an application. The example assumes that there is an existing Active Directory authorization policy store at the specified location, that this policy store contains an application named Expense, and that this application contains no tasks with business rule scripts.


```VB
'  Create the AzAuthorizationStore object.
Dim AzManStore
Set AzManStore = CreateObject("AzRoles.AzAuthorizationStore")

'  Initialize the authorization store.
AzManStore.Initialize 2, _
    "msldap://CN=MyStore,CN=Program Data,DC=authmanager,DC=com"

'  Create an application object in the store.
Dim expenseApp
Set expenseApp= AzManStore.OpenApplication("Expense")

'  Add a delegated policy user to the store.
AzManStore.AddDelegatedPolicyUserName("ExampleDomain\\UserName")

'  Add the user as an administrator of the application.
expenseApp.AddPolicyAdministratorName("ExampleDomain\\UserName")

'  Save changes to the store.
AzManStore.Submit
```



 

 




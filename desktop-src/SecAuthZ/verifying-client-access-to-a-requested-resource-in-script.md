---
Description: Call the IAzClientContextAccessCheck method to check whether the client has access to one or more operations.
ms.assetid: cf1070fe-3737-4ae6-a8ef-f0782418a1d5
title: Verifying Client Access to a Requested Resource in Script
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Verifying Client Access to a Requested Resource in Script

Call the [**AccessCheck**](/windows/win32/Azroles/nf-azroles-iazclientcontext-accesscheck?branch=master) method of an [**IAzClientContext**](/windows/win32/Azroles/nn-azroles-iazclientcontext?branch=master) object to check whether the client has access to one or more operations. For information about creating an **IAzClientContext** object, see [Establishing a Client Context in Script](establishing-a-client-context-in-script.md).

A client might have membership in more than one role, and an operation might be assigned to more than one task, so Authorization Manager checks for all roles and tasks. If any role to which the client belongs contains any task that contains an operation, access to that operation is granted.

To check access for only a single role to which the client belongs, set the [**RoleForAccessCheck**](/windows/win32/Azroles/nf-azroles-iazclientcontext-get_roleforaccesscheck?branch=master) property of the [**IAzClientContext**](/windows/win32/Azroles/nn-azroles-iazclientcontext?branch=master) object.

When initializing the authorization policy store for access check, you must pass zero as the value of the *lFlags* parameter of the [**Initialize**](/windows/win32/Azroles/nf-azroles-iazauthorizationstore-initialize?branch=master) method of the [**AzAuthorizationStore**](/windows/win32/Azroles/nn-azroles-iazauthorizationstore?branch=master) object.

It is also possible to apply business logic at run time to qualify access. For information about qualifying access with business logic, see [Qualifying Access with Business Logic in Script](qualifying-access-with-business-logic-in-script.md).

The following example shows how to check a client's access to an operation. The example assumes that there is an existing XML policy store named MyStore.xml in the root directory of drive C, and that this store contains an application named Expense and an operation named UseFormControl.


```VB
<%@ Language=VBScript %>
<%
'  Create the AzAuthorizationStore object.
Dim AzManStore
Set AzManStore = CreateObject("AzRoles.AzAuthorizationStore")

'  Initialize the authorization store.
AzManStore.Initialize 0, "msxml://C:\MyStore.xml"

'  Open the application object in the store.
Dim expenseApp
Set expenseApp = AzManStore.OpenApplication("Expense")

'  Create a client context.
Dim clientName
clientName = Request.ServerVariables("LOGON_USER")
Dim clientContext
Set clientContext = _
    expenseApp.InitializeClientContextFromName(clientName)

'  Open the operation to check.
Dim formOperation
Set formOperation = expenseApp.OpenOperation("UseFormControl")

'  Get the ID of the operation.
Dim operationID
operationID = formOperation.OperationID

'  Check access.
Dim Operations(1)
Operations(0) = operationID
Dim Results

Results = _
    clientContext.AccessCheck("UseFormControl", Empty, Operations)

%>
```



 

 




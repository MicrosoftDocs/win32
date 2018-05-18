---
Description: 'To establish a client context in Script, an application can create a client context with a handle to a token, a domain and user name, or a string representation of the security identifier of the client.'
ms.assetid: '94fb79e4-7e9f-4fef-8ca5-b2000a92efab'
title: Establishing a Client Context in Script
---

# Establishing a Client Context in Script

In Authorization Manager, an application determines whether a client is given access to an operation by calling the [**AccessCheck**](iazclientcontext-accesscheck.md) method of an [**IAzClientContext**](iazclientcontext.md) object, which represents a client context.

An application can create a client context with a handle to a token, a domain and user name, or a string representation of the [*security identifier*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-identifier-gly) (SID) of the client.

Use the [**InitializeClientContextFromToken**](iazapplication-initializeclientcontextfromtoken.md), [**InitializeClientContextFromName**](iazapplication-initializeclientcontextfromname.md), and [**InitializeClientContextFromStringSid**](iazapplication-initializeclientcontextfromstringsid.md) methods of an [**IAzApplication**](iazapplication.md) object to create a client context.

The following example shows how to create an [**IAzClientContext**](iazclientcontext.md) object from a client name. The example assumes that there is an existing XML policy store named MyStore.xml in the root directory of drive C, and that this store contains an application named Expense.


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

%>
```



 

 




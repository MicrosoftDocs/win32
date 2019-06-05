---
Description: Explains the use of impersonation tokens in access control.
ms.assetid: 74fcb0e3-303a-4a5e-9eb6-2aad3a4944db
title: Impersonation Tokens
ms.topic: article
ms.date: 05/31/2018
---

# Impersonation Tokens

An impersonating thread has two [*access tokens*](https://docs.microsoft.com/windows/desktop/SecGloss/a-gly):

-   A [*primary access token*](https://docs.microsoft.com/windows/desktop/SecGloss/p-gly) that describes the [*security context*](https://docs.microsoft.com/windows/desktop/SecGloss/s-gly) of the server. To get a handle to this token, call the [**OpenProcessToken**](https://msdn.microsoft.com/en-us/library/Aa379295(v=VS.85).aspx) function.
-   An impersonation access token that describes the security context of the client being impersonated. To get a handle to this token, call the [**OpenThreadToken**](https://msdn.microsoft.com/en-us/library/Aa379296(v=VS.85).aspx) function.

A server can use the [*impersonation token*](https://docs.microsoft.com/windows/desktop/SecGloss/i-gly) in the following functions:

-   In the [**AccessCheck**](https://msdn.microsoft.com/en-us/library/Aa374815(v=VS.85).aspx), [**AccessCheckByType**](https://msdn.microsoft.com/en-us/library/Aa374826(v=VS.85).aspx), and [**AccessCheckByTypeResultList**](https://msdn.microsoft.com/en-us/library/Aa374836(v=VS.85).aspx) functions to determine whether a [*security descriptor*](https://docs.microsoft.com/windows/desktop/SecGloss/s-gly) allows the client a set of access rights.
-   In the [**AdjustTokenPrivileges**](https://msdn.microsoft.com/en-us/library/Aa375202(v=VS.85).aspx) function to enable or disable the client's privileges.
-   In the [**PrivilegeCheck**](https://msdn.microsoft.com/en-us/library/Aa379304(v=VS.85).aspx) function to determine whether a set of privileges are enabled in the client's token.
-   In functions that generate entries in the security event log, such as [**ObjectOpenAuditAlarm**](/windows/desktop/api/Winbase/nf-winbase-objectopenauditalarma) or [**PrivilegedServiceAuditAlarm**](/windows/desktop/api/Winbase/nf-winbase-privilegedserviceauditalarma). These functions use an impersonation token to get information about the client for the log entry.

 

 




---
Description: 'Explains the use of impersonation tokens in access control.'
ms.assetid: '74fcb0e3-303a-4a5e-9eb6-2aad3a4944db'
title: Impersonation Tokens
---

# Impersonation Tokens

An impersonating thread has two [*access tokens*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-token-gly):

-   A [*primary access token*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-primary-token-gly) that describes the [*security context*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-context-gly) of the server. To get a handle to this token, call the [**OpenProcessToken**](openprocesstoken.md) function.
-   An impersonation access token that describes the security context of the client being impersonated. To get a handle to this token, call the [**OpenThreadToken**](openthreadtoken.md) function.

A server can use the [*impersonation token*](https://msdn.microsoft.com/library/windows/desktop/ms721588#-security-impersonation-token-gly) in the following functions:

-   In the [**AccessCheck**](accesscheck.md), [**AccessCheckByType**](accesscheckbytype.md), and [**AccessCheckByTypeResultList**](accesscheckbytyperesultlist.md) functions to determine whether a [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly) allows the client a set of access rights.
-   In the [**AdjustTokenPrivileges**](adjusttokenprivileges.md) function to enable or disable the client's privileges.
-   In the [**PrivilegeCheck**](privilegecheck.md) function to determine whether a set of privileges are enabled in the client's token.
-   In functions that generate entries in the security event log, such as [**ObjectOpenAuditAlarm**](objectopenauditalarm.md) or [**PrivilegedServiceAuditAlarm**](privilegedserviceauditalarm.md). These functions use an impersonation token to get information about the client for the log entry.

 

 




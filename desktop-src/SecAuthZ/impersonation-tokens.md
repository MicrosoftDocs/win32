---
Description: Explains the use of impersonation tokens in access control.
ms.assetid: 74fcb0e3-303a-4a5e-9eb6-2aad3a4944db
title: Impersonation Tokens
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Impersonation Tokens

An impersonating thread has two [*access tokens*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-token-gly):

-   A [*primary access token*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-primary-token-gly) that describes the [*security context*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-context-gly) of the server. To get a handle to this token, call the [**OpenProcessToken**](/windows/win32/Winbase/nf-ntifs-ntopenprocesstoken?branch=master) function.
-   An impersonation access token that describes the security context of the client being impersonated. To get a handle to this token, call the [**OpenThreadToken**](/windows/win32/Winbase/nf-ntifs-ntopenthreadtoken?branch=master) function.

A server can use the [*impersonation token*](https://msdn.microsoft.com/library/windows/desktop/ms721588#-security-impersonation-token-gly) in the following functions:

-   In the [**AccessCheck**](/windows/win32/Winbase/nf-ntifs-ntaccesscheckandauditalarm?branch=master), [**AccessCheckByType**](/windows/win32/Winbase/nf-ntifs-ntaccesscheckbytypeandauditalarm?branch=master), and [**AccessCheckByTypeResultList**](/windows/win32/Winbase/nf-ntifs-ntaccesscheckbytyperesultlistandauditalarm?branch=master) functions to determine whether a [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly) allows the client a set of access rights.
-   In the [**AdjustTokenPrivileges**](adjusttokenprivileges.md) function to enable or disable the client's privileges.
-   In the [**PrivilegeCheck**](/windows/win32/Winbase/nf-ntifs-ntprivilegecheck?branch=master) function to determine whether a set of privileges are enabled in the client's token.
-   In functions that generate entries in the security event log, such as [**ObjectOpenAuditAlarm**](/windows/win32/Winbase/nf-winbase-objectopenauditalarma?branch=master) or [**PrivilegedServiceAuditAlarm**](/windows/win32/Winbase/nf-winbase-privilegedserviceauditalarma?branch=master). These functions use an impersonation token to get information about the client for the log entry.

 

 




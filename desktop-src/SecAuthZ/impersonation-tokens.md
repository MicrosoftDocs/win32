---
Description: Explains the use of impersonation tokens in access control.
ms.assetid: 74fcb0e3-303a-4a5e-9eb6-2aad3a4944db
title: Impersonation Tokens
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Impersonation Tokens

An impersonating thread has two [*access tokens*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-token-gly):

-   A [*primary access token*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-primary-token-gly) that describes the [*security context*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-context-gly) of the server. To get a handle to this token, call the [**OpenProcessToken**](/windows/desktop/api/Winbase/nf-ntifs-ntopenprocesstoken) function.
-   An impersonation access token that describes the security context of the client being impersonated. To get a handle to this token, call the [**OpenThreadToken**](/windows/desktop/api/Winbase/nf-ntifs-ntopenthreadtoken) function.

A server can use the [*impersonation token*](https://msdn.microsoft.com/library/windows/desktop/ms721588#-security-impersonation-token-gly) in the following functions:

-   In the [**AccessCheck**](/windows/desktop/api/Winbase/nf-ntifs-ntaccesscheckandauditalarm), [**AccessCheckByType**](/windows/desktop/api/Winbase/nf-ntifs-ntaccesscheckbytypeandauditalarm), and [**AccessCheckByTypeResultList**](/windows/desktop/api/Winbase/nf-ntifs-ntaccesscheckbytyperesultlistandauditalarm) functions to determine whether a [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly) allows the client a set of access rights.
-   In the [**AdjustTokenPrivileges**](https://www.bing.com/search?q=**AdjustTokenPrivileges**) function to enable or disable the client's privileges.
-   In the [**PrivilegeCheck**](/windows/desktop/api/Winbase/nf-ntifs-ntprivilegecheck) function to determine whether a set of privileges are enabled in the client's token.
-   In functions that generate entries in the security event log, such as [**ObjectOpenAuditAlarm**](/windows/desktop/api/Winbase/nf-winbase-objectopenauditalarma) or [**PrivilegedServiceAuditAlarm**](/windows/desktop/api/Winbase/nf-winbase-privilegedserviceauditalarma). These functions use an impersonation token to get information about the client for the log entry.

 

 




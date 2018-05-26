---
Description: A protected server can use the following functions to generate audit reports in the security event log.
ms.assetid: 4edee246-4fa7-4947-9737-34198f36e3ab
title: Auditing Access To Private Objects
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Auditing Access To Private Objects

A protected server can use the following functions to generate audit reports in the security event log.



| Function                                                                                                     | Description                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AccessCheckAndAuditAlarm**](/windows/win32/Winbase/nf-winbase-accesscheckandauditalarma?branch=master)                                                 | Same as the [**AccessCheck**](/windows/win32/Winbase/nf-ntifs-ntaccesscheckandauditalarm?branch=master) function except that it can generate audit messages for failed or successful access attempts.                                                                            |
| [**AccessCheckByTypeAndAuditAlarm**](/windows/win32/Winbase/nf-winbase-accesscheckbytypeandauditalarma?branch=master)                                     | Same as the [**AccessCheckByType**](/windows/win32/Winbase/nf-ntifs-ntaccesscheckbytypeandauditalarm?branch=master) function except that it can generate audit messages for failed or successful access attempts.                                                                |
| [**AccessCheckByTypeResultListAndAuditAlarm**](/windows/win32/Winbase/nf-winbase-accesscheckbytyperesultlistandauditalarma?branch=master)                 | Same as the [**AccessCheckByTypeResultList**](/windows/win32/Winbase/nf-ntifs-ntaccesscheckbytyperesultlistandauditalarm?branch=master) function except that it can generate audit messages for failed or successful access attempts.                                            |
| [**AccessCheckByTypeResultListAndAuditAlarmByHandle**](/windows/win32/Winbase/nf-winbase-accesscheckbytyperesultlistandauditalarmbyhandlea?branch=master) | Same as the [**AccessCheckByTypeResultListAndAuditAlarm**](/windows/win32/Winbase/nf-winbase-accesscheckbytyperesultlistandauditalarma?branch=master) function except that it allows the calling thread to perform the access check before impersonating the client. |
| [**ObjectCloseAuditAlarm**](/windows/win32/Winbase/nf-winbase-objectcloseauditalarma?branch=master)                                                       | Generates an audit message to indicate that a client tried to close a private object.                                                                                                                                   |
| [**ObjectDeleteAuditAlarm**](/windows/win32/Winbase/nf-winbase-objectopenauditalarma?branch=master)                                                       | Generates an audit message to indicate that a client tried to delete a private object.                                                                                                                                  |
| [**ObjectOpenAuditAlarm**](/windows/win32/Winbase/nf-winbase-objectopenauditalarma?branch=master)                                                         | Generates an audit message to indicate that a client tried to open or create a private object.                                                                                                                          |
| [**ObjectPrivilegeAuditAlarm**](/windows/win32/Winbase/nf-winbase-objectprivilegeauditalarma?branch=master)                                               | Generates an audit message to indicate that a client tried to use a specified set of privileges in conjunction with an attempt to access a private object.                                                              |
| [**PrivilegedServiceAuditAlarm**](/windows/win32/Winbase/nf-winbase-privilegedserviceauditalarma?branch=master)                                           | Generates an audit message to indicate that a client tried to use a specified set of privileges.                                                                                                                        |



 

 

 




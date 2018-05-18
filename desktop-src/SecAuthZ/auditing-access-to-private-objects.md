---
Description: 'A protected server can use the following functions to generate audit reports in the security event log.'
ms.assetid: '4edee246-4fa7-4947-9737-34198f36e3ab'
title: Auditing Access To Private Objects
---

# Auditing Access To Private Objects

A protected server can use the following functions to generate audit reports in the security event log.



| Function                                                                                                     | Description                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AccessCheckAndAuditAlarm**](accesscheckandauditalarm.md)                                                 | Same as the [**AccessCheck**](accesscheck.md) function except that it can generate audit messages for failed or successful access attempts.                                                                            |
| [**AccessCheckByTypeAndAuditAlarm**](accesscheckbytypeandauditalarm.md)                                     | Same as the [**AccessCheckByType**](accesscheckbytype.md) function except that it can generate audit messages for failed or successful access attempts.                                                                |
| [**AccessCheckByTypeResultListAndAuditAlarm**](accesscheckbytyperesultlistandauditalarm.md)                 | Same as the [**AccessCheckByTypeResultList**](accesscheckbytyperesultlist.md) function except that it can generate audit messages for failed or successful access attempts.                                            |
| [**AccessCheckByTypeResultListAndAuditAlarmByHandle**](accesscheckbytyperesultlistandauditalarmbyhandle.md) | Same as the [**AccessCheckByTypeResultListAndAuditAlarm**](accesscheckbytyperesultlistandauditalarm.md) function except that it allows the calling thread to perform the access check before impersonating the client. |
| [**ObjectCloseAuditAlarm**](objectcloseauditalarm.md)                                                       | Generates an audit message to indicate that a client tried to close a private object.                                                                                                                                   |
| [**ObjectDeleteAuditAlarm**](objectopenauditalarm.md)                                                       | Generates an audit message to indicate that a client tried to delete a private object.                                                                                                                                  |
| [**ObjectOpenAuditAlarm**](objectopenauditalarm.md)                                                         | Generates an audit message to indicate that a client tried to open or create a private object.                                                                                                                          |
| [**ObjectPrivilegeAuditAlarm**](objectprivilegeauditalarm.md)                                               | Generates an audit message to indicate that a client tried to use a specified set of privileges in conjunction with an attempt to access a private object.                                                              |
| [**PrivilegedServiceAuditAlarm**](privilegedserviceauditalarm.md)                                           | Generates an audit message to indicate that a client tried to use a specified set of privileges.                                                                                                                        |



 

 

 




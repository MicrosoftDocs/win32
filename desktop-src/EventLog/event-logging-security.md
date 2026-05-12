---
description: The Security log is designed for use by the system. However, users can read and clear the Security log if they have been granted the SE\_SECURITY\_NAME privilege (the &\#0034;manage auditing and security log&\#0034; user right). For more information, see Privileges.
ms.assetid: 861be39a-012e-473b-a2d3-2a8c7ba3adaa
title: Event Logging Security
ms.topic: reference
ms.date: 05/31/2018
---

# Event Logging Security

> [!Note]  
> The Event Logging API was designed for applications that run on the Windows Server 2003, Windows XP, or Windows 2000 operating system. In Windows Vista, the event logging infrastructure was redesigned. Applications that are designed to run on the Windows Vista or later operating systems should now use [Windows Event Log](/windows/desktop/WES/windows-event-log).

The **Security** log is designed for use by the system. However, users can read and clear the **Security** log if they have been granted the SE\_SECURITY\_NAME privilege (the "manage auditing and security log" user right). For more information, see [Privileges](/windows/desktop/SecAuthZ/privileges).

Only the Local Security Authority (Lsass.exe) has write permission for the **Security** log. No other account can request this privilege. To write an event to the **Security** log, use the [**AuthzReportSecurityEvent**](/windows/desktop/api/authz/nf-authz-authzreportsecurityevent) function.

Access to the **Application** log, the **System** log, and custom logs is restricted. The system grants access based on the access rights granted to the account under which the thread is running. The following table shows which types of access are required by the event logging functions.

| Access right                 | Description                                                                                            |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| ELF\_LOGFILE\_CLEAR (0x0004) | Required by [**ClearEventLog**](/windows/desktop/api/Winbase/nf-winbase-cleareventloga).                                                    |
| ELF\_LOGFILE\_READ (0x0001)  | Required by [**OpenBackupEventLog**](/windows/desktop/api/Winbase/nf-winbase-openbackupeventloga) and [**OpenEventLog**](/windows/desktop/api/Winbase/nf-winbase-openeventloga). |
| ELF\_LOGFILE\_WRITE (0x0002) | Required by [**RegisterEventSource**](/windows/desktop/api/Winbase/nf-winbase-registereventsourcea).                                        |

Use the **CustomSD** registry value to configure the security of the **Application** log, the **System** log, and custom logs. For more information, see [Eventlog Key](eventlog-key.md).

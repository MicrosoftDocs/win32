---
description: The Security log is designed for use by the system. However, users can read and clear the Security log if they have been granted the SE\_SECURITY\_NAME privilege (the &\#0034;manage auditing and security log&\#0034; user right). For more information, see Privileges.
ms.assetid: 861be39a-012e-473b-a2d3-2a8c7ba3adaa
title: Event Logging Security
ms.topic: article
ms.date: 05/31/2018
---

# Event Logging Security

The **Security** log is designed for use by the system. However, users can read and clear the **Security** log if they have been granted the SE\_SECURITY\_NAME privilege (the "manage auditing and security log" user right). For more information, see [Privileges](/windows/desktop/SecAuthZ/privileges).

Only the Local Security Authority (Lsass.exe) has write permission for the **Security** log. No other account can request this privilege. To write an event to the **Security** log, use the [**AuthzReportSecurityEvent**](/windows/desktop/api/authz/nf-authz-authzreportsecurityevent) function.

Access to the **Application** log, the **System** log, and custom logs is restricted. The system grants access based on the access rights granted to the account under which the thread is running. The following table shows which types of access are required by the event logging functions.



| Access right                 | Description                                                                                            |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| ELF\_LOGFILE\_CLEAR (0x0004) | Required by [**ClearEventLog**](/windows/desktop/api/Winbase/nf-winbase-cleareventloga).                                                    |
| ELF\_LOGFILE\_READ (0x0001)  | Required by [**OpenBackupEventLog**](/windows/desktop/api/Winbase/nf-winbase-openbackupeventloga) and [**OpenEventLog**](/windows/desktop/api/Winbase/nf-winbase-openeventloga). |
| ELF\_LOGFILE\_WRITE (0x0002) | Required by [**RegisterEventSource**](/windows/desktop/api/Winbase/nf-winbase-registereventsourcea).                                        |



 

Use the **CustomSD** registry value to configure the security of the **Application** log, the **System** log, and custom logs. For more information, see [Eventlog Key](eventlog-key.md).

**Windows XP/2000:** The following table describes the access rights granted for each account on each log.

| Log             | Account                 | Read | Write | Clear |
|-----------------|-------------------------|------|-------|-------|
| **Application** | Administrators (system) | X    | X     | X     |
|                 | Administrators (domain) | X    | X     | X     |
|                 | LocalSystem             | X    | X     | X     |
|                 | Interactive user        | X    | X     |       |
| **System**      | Administrators (system) | X    | X     | X     |
|                 | Administrators (domain) | X    |       | X     |
|                 | LocalSystem             | X    | X     | X     |
|                 | Interactive user        | X    |       |       |
| *Custom*        | Administrators (system) | X    | X     | X     |
|                 | Administrators (domain) | X    | X     | X     |
|                 | LocalSystem             | X    | X     | X     |
|                 | Interactive user        | X    | X     |       |



 

To grant access to the members of the Guest account, change the following registry value:

**HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Services**\\**EventLog**\\*Log*\\**RestrictGuestAccess**

 

 

---
title: Tracking Changes
description: Some applications must maintain consistency between specific data stored in the Active Directory directory service and other data.
ms.assetid: f4539482-1170-4c0c-b817-b39e58049d39
ms.tgt_platform: multiple
keywords:
- Active Directory,using,tracking changes
ms.topic: article
ms.date: 05/31/2018
---

# Tracking Changes

Some applications must maintain consistency between specific data stored in the Active Directory directory service and other data. The other data might be stored in the directory, in a SQL Server table, in a file, or in the registry. When data stored in the directory changes, the other data may be required to change in order to remain consistent. Applications that have this requirement include:

This section does not cover mechanisms used by monitoring applications. These are applications that monitor directory changes not for the purpose of maintaining consistent data between separate stores, but as a system management tool. Although monitoring applications can use the same mechanisms that support change-tracking applications, the following mechanisms are specifically designed for monitoring applications:

-   Security auditing. By modifying the system access-control list (SACL) portion of an object security descriptor, you can cause accesses to the object on a given domain controller to generate audit records in the security event log on that DC. You can audit reads, writes, or both; you can audit the entire object or specific attributes. For more information, see [Retrieving an Object's SACL](retrieving-an-objectampaposs-sacl.md) and [Audit Generation](/windows/desktop/SecAuthZ/audit-generation).
-   Event logging. By modifying registry settings on a given domain controller, you can change the kinds of events logged to the directory service event log. Specifically, to log all modifications, set the **8 Directory Access** value under the following registry key to 4.

    ```
    HKEY_LOCAL_MACHINE
       SYSTEM
          CurrentControlSet
             Services
                NTDS
                   Diagnostics
    ```

    For more information, see [Event Logging](/windows/desktop/EventLog/event-logging).

-   Event tracing. Windows 2000 introduced an Event Tracing API for tracing and logging interesting events in software or hardware. The Windows operating system, and Active Directory Domain Services in particular, support the use of event tracing for capacity planning and detailed performance analysis. For more information, see [Event Tracing](/windows/desktop/ETW/event-tracing-portal) and [Event Tracing in ADSI](/windows/desktop/ADSI/adsi-and-etw).

This section includes the following topics:

-   [Overview of Change Tracking Techniques](overview-of-change-tracking-techniques.md)
-   [Change Notifications in Active Directory Domain Services](change-notifications-in-active-directory-domain-services.md)
-   [Polling for Changes Using the DirSync Control](polling-for-changes-using-the-dirsync-control.md)
-   [Polling for Changes Using USNChanged](polling-for-changes-using-usnchanged.md)

 

 
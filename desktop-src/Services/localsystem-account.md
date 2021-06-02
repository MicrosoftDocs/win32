---
description: The LocalSystem account is a predefined local account used by the service control manager.
ms.assetid: 692bceb6-f5bd-4b83-ab3b-ef8099dc84e1
title: LocalSystem Account
ms.topic: article
ms.date: 05/31/2018
---

# LocalSystem Account

The LocalSystem account is a predefined local account used by the service control manager. This account is not recognized by the security subsystem, so you cannot specify its name in a call to the [**LookupAccountName**](/windows/desktop/api/winbase/nf-winbase-lookupaccountnamea) function. It has extensive privileges on the local computer, and acts as the computer on the network. Its token includes the NT AUTHORITY\\SYSTEM and BUILTIN\\Administrators SIDs; these accounts have access to most system objects. The name of the account in all locales is .\\LocalSystem. The name, LocalSystem or *ComputerName*\\LocalSystem can also be used. This account does not have a password. If you specify the LocalSystem account in a call to the [**CreateService**](/windows/desktop/api/Winsvc/nf-winsvc-createservicea) or [**ChangeServiceConfig**](/windows/desktop/api/Winsvc/nf-winsvc-changeserviceconfiga) function, any password information you provide is ignored.

A service that runs in the context of the LocalSystem account inherits the security context of the SCM. The user SID is created from the **SECURITY\_LOCAL\_SYSTEM\_RID** value. The account is not associated with any logged-on user account. This has several implications:

-   The registry key **HKEY\_CURRENT\_USER** is associated with the default user, not the current user. To access another user's profile, impersonate the user, then access **HKEY\_CURRENT\_USER**.
-   The service can open the registry key **HKEY\_LOCAL\_MACHINE\\SECURITY**.
-   The service presents the computer's credentials to remote servers.
-   If the service opens a command window and runs a batch file, the user could hit CTRL+C to terminate the batch file and gain access to a command window with LocalSystem permissions.

The LocalSystem account has the following privileges:

-   **SE\_ASSIGNPRIMARYTOKEN\_NAME** (disabled)
-   **SE\_AUDIT\_NAME** (enabled)
-   **SE\_BACKUP\_NAME** (disabled)
-   **SE\_CHANGE\_NOTIFY\_NAME** (enabled)
-   **SE\_CREATE\_GLOBAL\_NAME** (enabled)
-   **SE\_CREATE\_PAGEFILE\_NAME** (enabled)
-   **SE\_CREATE\_PERMANENT\_NAME** (enabled)
-   **SE\_CREATE\_TOKEN\_NAME** (disabled)
-   **SE\_DEBUG\_NAME** (enabled)
-   **SE\_IMPERSONATE\_NAME** (enabled)
-   **SE\_INC\_BASE\_PRIORITY\_NAME** (enabled)
-   **SE\_INCREASE\_QUOTA\_NAME** (disabled)
-   **SE\_LOAD\_DRIVER\_NAME** (disabled)
-   **SE\_LOCK\_MEMORY\_NAME** (enabled)
-   **SE\_MANAGE\_VOLUME\_NAME** (disabled)
-   **SE\_PROF\_SINGLE\_PROCESS\_NAME** (enabled)
-   **SE\_RESTORE\_NAME** (disabled)
-   **SE\_SECURITY\_NAME** (disabled)
-   **SE\_SHUTDOWN\_NAME** (disabled)
-   **SE\_SYSTEM\_ENVIRONMENT\_NAME** (disabled)
-   **SE\_SYSTEMTIME\_NAME** (disabled)
-   **SE\_TAKE\_OWNERSHIP\_NAME** (disabled)
-   **SE\_TCB\_NAME** (enabled)
-   **SE\_UNDOCK\_NAME** (disabled)

Most services do not need such a high privilege level. If your service does not need these privileges, and it is not an interactive service, consider using the [LocalService account](localservice-account.md) or the [NetworkService account](networkservice-account.md). For more information, see [Service Security and Access Rights](service-security-and-access-rights.md).

 

 

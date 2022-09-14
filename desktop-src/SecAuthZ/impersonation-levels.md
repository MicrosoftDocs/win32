---
description: The SECURITY\_IMPERSONATION\_LEVEL enumeration defines four impersonation levels that determine the operations a server can perform in the clients context.
ms.assetid: ae152dbf-44f0-417f-a85e-09bf60dcfcb0
title: Impersonation Levels (Authorization)
ms.topic: article
ms.date: 05/31/2018
---

# Impersonation Levels (Authorization)

The [**SECURITY\_IMPERSONATION\_LEVEL**](/windows/desktop/api/Winnt/ne-winnt-security_impersonation_level) enumeration defines four impersonation levels that determine the operations a server can perform in the client's context.



| Impersonation level    | Description                                                                                      |
|------------------------|--------------------------------------------------------------------------------------------------|
| SecurityAnonymous      | The server cannot impersonate or identify the client.                                            |
| SecurityIdentification | The server can get the identity and privileges of the client, but cannot impersonate the client. |
| SecurityImpersonation  | The server can impersonate the client's security context on the local system.                    |
| SecurityDelegation     | The server can impersonate the client's security context on remote systems.                      |



 

The client of a named pipe, RPC, or DDE connection can control the impersonation level. For example, a named pipe client can call the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) function to open a handle to a named pipe and specify the server's impersonation level.

When the named pipe, RPC, or DDE connection is remote, the flags passed to [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) to set the impersonation level are ignored. In this case, the impersonation level of the client is determined by the impersonation levels enabled by the server, which is set by a flag on the server's account in the directory service. For example, if the server is enabled for delegation, the client's impersonation level will also be set to delegation even if the flags passed to **CreateFile** specify the identification impersonation level.

DDE clients use the [**DdeSetQualityOfService**](/windows/win32/api/dde/nf-dde-ddesetqualityofservice) function with the [**SECURITY\_QUALITY\_OF\_SERVICE**](/windows/desktop/api/Winnt/ns-winnt-security_quality_of_service) structure to specify the impersonation level. The SecurityImpersonation level is the default for named pipe, RPC, and DDE servers. The [**ImpersonateSelf**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-impersonateself), [**DuplicateToken**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-duplicatetoken), and [**DuplicateTokenEx**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-duplicatetokenex) functions allow the caller to specify an impersonation level. Use the [**GetTokenInformation**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-gettokeninformation) function to retrieve the impersonation level of an [*access token*](/windows/desktop/SecGloss/a-gly).

At the SecurityImpersonation level, most of the thread's actions occur in the security context of the thread's [*impersonation token*](/windows/desktop/SecGloss/i-gly) rather than in the [*primary token*](/windows/desktop/SecGloss/p-gly) of the [*process*](/windows/desktop/SecGloss/p-gly) that owns the thread. For example, if an impersonating thread opens a [securable object](securable-objects.md), the system uses the impersonation token to check the thread's access. Similarly, if an impersonating thread creates a new object, for example by calling the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) function, the owner of the new object is the default owner from the client's [*access token*](/windows/desktop/SecGloss/a-gly).

However, the system uses the primary token of the process rather than the impersonation token of the calling thread in the following situations:

-   If an impersonating thread calls the [**CreateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa) function, the new process always inherits the primary token of the process.
-   For functions that require the SE\_TCB\_NAME privilege, such as the [**LogonUser**](/windows/desktop/api/winbase/nf-winbase-logonusera) function, the system always checks for the privilege in the primary token of the process.
-   For functions that require the SE\_AUDIT\_NAME privilege, such as the [**ObjectOpenAuditAlarm**](/windows/desktop/api/Winbase/nf-winbase-objectopenauditalarma) function, the system always checks for the privilege in the primary token of the process.
-   In a call to the [**OpenThreadToken**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-openthreadtoken) function, a thread can specify whether the function uses the impersonation token or the primary token to determine whether to grant the requested access.

 

 

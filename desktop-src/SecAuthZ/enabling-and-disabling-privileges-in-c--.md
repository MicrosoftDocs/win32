---
description: Enabling a privilege in an access token allows the process to perform system-level actions that it could not previously.
ms.assetid: aa2d3fe7-01ee-4243-b72c-3e8b90068e22
title: Enabling and Disabling Privileges in C++
ms.topic: article
ms.date: 05/31/2018
---

# Enabling and Disabling Privileges in C++

Enabling a privilege in an access token allows the process to perform system-level actions that it could not previously. Your application should thoroughly verify that the privilege is appropriate to the type of account, especially for the following powerful privileges.



| Privilege constant           | String value                  | Display name                        |
|------------------------------|-------------------------------|-------------------------------------|
| SE\_ASSIGNPRIMARYTOKEN\_NAME | SeAssignPrimaryTokenPrivilege | Replace a process-level token       |
| SE\_BACKUP\_NAME             | SeBackupPrivilege             | Back up files and directories       |
| SE\_DEBUG\_NAME              | SeDebugPrivilege              | Debug programs                      |
| SE\_INCREASE\_QUOTA\_NAME    | SeIncreaseQuotaPrivilege      | Adjust memory quotas for a process  |
| SE\_TCB\_NAME                | SeTcbPrivilege                | Act as part of the operating system |



 

Before enabling any of these potentially dangerous privileges, determine that functions or operations in your code actually require the privileges. For example, very few functions in the operating system actually require the **SeTcbPrivilege**. For a list of all the available privileges, see [Privilege Constants](authorization-constants.md).

The following example shows how to enable or disable a privilege in an [*access token*](/windows/desktop/SecGloss/a-gly). The example calls the [**LookupPrivilegeValue**](/windows/desktop/api/Winbase/nf-winbase-lookupprivilegevaluea) function to get the [*locally unique identifier*](/windows/desktop/SecGloss/l-gly) (LUID) that the local system uses to identify the privilege. Then the example calls the [**AdjustTokenPrivileges**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-adjusttokenprivileges) function, which either enables or disables the privilege that depends on the value of the *bEnablePrivilege* parameter.


```C++
#include <windows.h>
#include <stdio.h>
#pragma comment(lib, "advapi32.lib")

BOOL SetPrivilege(
    HANDLE hToken,          // access token handle
    LPCTSTR lpszPrivilege,  // name of privilege to enable/disable
    BOOL bEnablePrivilege   // to enable or disable privilege
    ) 
{
    TOKEN_PRIVILEGES tp;
    LUID luid;

    if ( !LookupPrivilegeValue( 
            NULL,            // lookup privilege on local system
            lpszPrivilege,   // privilege to lookup 
            &luid ) )        // receives LUID of privilege
    {
        printf("LookupPrivilegeValue error: %u\n", GetLastError() ); 
        return FALSE; 
    }

    tp.PrivilegeCount = 1;
    tp.Privileges[0].Luid = luid;
    if (bEnablePrivilege)
        tp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED;
    else
        tp.Privileges[0].Attributes = 0;

    // Enable the privilege or disable all privileges.

    if ( !AdjustTokenPrivileges(
           hToken, 
           FALSE, 
           &tp, 
           sizeof(TOKEN_PRIVILEGES), 
           (PTOKEN_PRIVILEGES) NULL, 
           (PDWORD) NULL) )
    { 
          printf("AdjustTokenPrivileges error: %u\n", GetLastError() ); 
          return FALSE; 
    } 

    if (GetLastError() == ERROR_NOT_ALL_ASSIGNED)

    {
          printf("The token does not have the specified privilege. \n");
          return FALSE;
    } 

    return TRUE;
}

```



 


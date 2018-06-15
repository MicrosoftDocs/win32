---
Description: Enabling a privilege in an access token allows the process to perform system-level actions that it could not previously.
ms.assetid: aa2d3fe7-01ee-4243-b72c-3e8b90068e22
title: Enabling and Disabling Privileges in C++
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enabling and Disabling Privileges in C++

Enabling a privilege in an access token allows the process to perform system-level actions that it could not previously. Your application should thoroughly verify that the privilege is appropriate to the type of account, especially for the following powerful privileges.



| Privilege constant/string                                            | Display name                        |
|----------------------------------------------------------------------|-------------------------------------|
| SE\_ASSIGNPRIMARYTOKEN\_NAMESeAssignPrimaryTokenPrivilege<br/> | Replace a process-level token       |
| SE\_BACKUP\_NAMESeBackupPrivilege<br/>                         | Back up files and directories       |
| SE\_DEBUG\_NAMESeDebugPrivilege<br/>                           | Debug programs                      |
| SE\_INCREASE\_QUOTA\_NAMESeIncreaseQuotaPrivilege<br/>         | Adjust memory quotas for a process  |
| SE\_TCB\_NAMESeTcbPrivilege<br/>                               | Act as part of the operating system |



 

Before enabling any of these potentially dangerous privileges, determine that functions or operations in your code actually require the privileges. For example, very few functions in the operating system actually require the **SeTcbPrivilege**. For a list of all the available privileges, see [Privilege Constants](authorization-constants.md).

The following example shows how to enable or disable a privilege in an [*access token*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-token-gly). The example calls the [**LookupPrivilegeValue**](/windows/desktop/api/Winbase/nf-winbase-lookupprivilegevaluea) function to get the [*locally unique identifier*](https://msdn.microsoft.com/library/windows/desktop/ms721592#-security-locally-unique-identifier-gly) (LUID) that the local system uses to identify the privilege. Then the example calls the [**AdjustTokenPrivileges**](https://msdn.microsoft.com/en-us/library/Aa375202(v=VS.85).aspx) function, which either enables or disables the privilege that depends on the value of the *bEnablePrivilege* parameter.


```C++
#include <windows.h>
#include <stdio.h>
#pragma comment(lib, "cmcfg32.lib")

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
            &amp;luid ) )        // receives LUID of privilege
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
           &amp;tp, 
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



 

 





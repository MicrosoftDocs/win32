---
description: The following example uses the ExitWindowsEx function to shut down the system.
ms.assetid: bf8723aa-1c7f-4761-9034-d5a9447a4bc4
title: How to Shut Down the System
ms.topic: article
ms.date: 05/31/2018
---

# How to Shut Down the System

The following example uses the [**ExitWindowsEx**](/windows/desktop/api/Winuser/nf-winuser-exitwindowsex) function to shut down the system. Shutting down flushes file buffers to disk and brings the system to a condition in which it is safe to turn off the computer. The application must first enable the SE\_SHUTDOWN\_NAME privilege. For more information, see [Privileges](../secauthz/privileges.md).


```C++
#include <windows.h>

#pragma comment(lib, "user32.lib")
#pragma comment(lib, "advapi32.lib")

BOOL MySystemShutdown()
{
   HANDLE hToken; 
   TOKEN_PRIVILEGES tkp; 
 
   // Get a token for this process. 
 
   if (!OpenProcessToken(GetCurrentProcess(), 
        TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, &hToken)) 
      return( FALSE ); 
 
   // Get the LUID for the shutdown privilege. 
 
   LookupPrivilegeValue(NULL, SE_SHUTDOWN_NAME, 
        &tkp.Privileges[0].Luid); 
 
   tkp.PrivilegeCount = 1;  // one privilege to set    
   tkp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED; 
 
   // Get the shutdown privilege for this process. 
 
   AdjustTokenPrivileges(hToken, FALSE, &tkp, 0, 
        (PTOKEN_PRIVILEGES)NULL, 0); 
 
   if (GetLastError() != ERROR_SUCCESS) 
      return FALSE; 
 
   // Shut down the system and force all applications to close. 
 
   if (!ExitWindowsEx(EWX_SHUTDOWN | EWX_FORCE, 
               SHTDN_REASON_MAJOR_OPERATINGSYSTEM |
               SHTDN_REASON_MINOR_UPGRADE |
               SHTDN_REASON_FLAG_PLANNED)) 
      return FALSE; 

   //shutdown was successful
   return TRUE;
}
```



The final parameter in the call to [**ExitWindowsEx**](/windows/desktop/api/Winuser/nf-winuser-exitwindowsex) indicates that the system was shut down for a planning update of the operating system. For more information, see [System Shutdown Reason Codes](system-shutdown-reason-codes.md).

## Related topics

<dl> <dt>

[Shutting Down](shutting-down.md)
</dt> </dl>

 

 

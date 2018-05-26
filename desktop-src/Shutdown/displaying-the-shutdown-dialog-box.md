---
Description: The following example reboots the local system using the InitiateSystemShutdown function.
ms.assetid: 928c2d48-daa5-4c27-816b-766adedba7eb
title: Displaying the Shutdown Dialog Box
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Displaying the Shutdown Dialog Box

The following example reboots the local system using the [**InitiateSystemShutdown**](/windows/win32/Winreg/nf-winreg-initiatesystemshutdowna?branch=master) function. The system displays a dialog box with a custom message and a message to the user to close applications within the specified time-out interval (30 seconds). After the time-out interval elapses, the system is restarted.

The application must enable the SE\_SHUTDOWN\_NAME privilege before calling [**InitiateSystemShutdown**](/windows/win32/Winreg/nf-winreg-initiatesystemshutdowna?branch=master). For more information, see [Privileges](security.privileges).


```C++
#include <windows.h>

#pragma comment( lib, "advapi32.lib" )

BOOL MySystemShutdown( LPTSTR lpMsg )
{
   HANDLE hToken;              // handle to process token 
   TOKEN_PRIVILEGES tkp;       // pointer to token structure 
 
   BOOL fResult;               // system shutdown flag 
 
   // Get the current process token handle so we can get shutdown 
   // privilege. 
 
   if (!OpenProcessToken(GetCurrentProcess(), 
        TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, &amp;hToken)) 
      return FALSE; 
 
   // Get the LUID for shutdown privilege. 
 
   LookupPrivilegeValue(NULL, SE_SHUTDOWN_NAME, 
        &amp;tkp.Privileges[0].Luid); 
 
   tkp.PrivilegeCount = 1;  // one privilege to set    
   tkp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED; 
 
   // Get shutdown privilege for this process. 
 
   AdjustTokenPrivileges(hToken, FALSE, &amp;tkp, 0, 
      (PTOKEN_PRIVILEGES) NULL, 0); 
 
   // Cannot test the return value of AdjustTokenPrivileges. 
 
   if (GetLastError() != ERROR_SUCCESS) 
      return FALSE; 
 
   // Display the shutdown dialog box and start the countdown. 
 
   fResult = InitiateSystemShutdown( 
      NULL,    // shut down local computer 
      lpMsg,   // message for user
      30,      // time-out period, in seconds 
      FALSE,   // ask user to close apps 
      TRUE);   // reboot after shutdown 
 
   if (!fResult) 
      return FALSE; 
 
   // Disable shutdown privilege. 
 
   tkp.Privileges[0].Attributes = 0; 
   AdjustTokenPrivileges(hToken, FALSE, &amp;tkp, 0, 
        (PTOKEN_PRIVILEGES) NULL, 0); 
 
   return TRUE; 
}
```



If the [**AbortSystemShutdown**](/windows/win32/Winreg/nf-winreg-abortsystemshutdowna?branch=master) function is executed in the time-out period specified by [**InitiateSystemShutdown**](/windows/win32/Winreg/nf-winreg-initiatesystemshutdowna?branch=master), the system does not shut down. For example, if PreventSystemShutdown is called after MySystemShutdown, the system closes the dialog box and does not restart the system.


```C++
#include <windows.h>

#pragma comment( lib, "advapi32.lib" )

BOOL PreventSystemShutdown()
{
   HANDLE hToken;              // handle to process token 
   TOKEN_PRIVILEGES tkp;       // pointer to token structure 
 
   // Get the current process token handle  so we can get shutdown 
   // privilege. 
 
   if (!OpenProcessToken(GetCurrentProcess(), 
         TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, &amp;hToken)) 
      return FALSE; 
 
   // Get the LUID for shutdown privilege. 
 
   LookupPrivilegeValue(NULL, SE_SHUTDOWN_NAME, 
         &amp;tkp.Privileges[0].Luid); 
 
   tkp.PrivilegeCount = 1;  // one privilege to set    
   tkp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED; 
 
   // Get shutdown privilege for this process. 
 
   AdjustTokenPrivileges(hToken, FALSE, &amp;tkp, 0, 
        (PTOKEN_PRIVILEGES)NULL, 0); 
 
   if (GetLastError() != ERROR_SUCCESS) 
      return FALSE; 
 
   // Prevent the system from shutting down. 
 
   if ( !AbortSystemShutdown(NULL) ) 
      return FALSE; 
 
   // Disable shutdown privilege. 
 
   tkp.Privileges[0].Attributes = 0; 
   AdjustTokenPrivileges(hToken, FALSE, &amp;tkp, 0, 
       (PTOKEN_PRIVILEGES) NULL, 0); 
 
   return TRUE;
}
```



 

 




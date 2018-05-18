---
Description: 'The following example locks the workstation using the LockWorkStation function. The system displays the Lock Workstation dialog box. The dialog box text says that the workstation is in use and has been locked by the user.'
ms.assetid: '7cbf9a0a-dfab-42e6-9a71-bb240121f59f'
title: How to Lock the Workstation
---

# How to Lock the Workstation

The following example locks the workstation using the [**LockWorkStation**](lockworkstation.md) function. The system displays the **Lock Workstation** dialog box. The dialog box text says that the workstation is in use and has been locked by the user.


```C++
#include <windows.h>
#include <stdio.h>

#pragma comment( lib, "user32.lib" )

void main()
{
    // Lock the workstation.

    if( !LockWorkStation() )
        printf ("LockWorkStation failed with %d\n", GetLastError());
}
```



To determine whether the workstation is locked, test whether your window is visible.

The workstation can be unlocked by the user or an administrator. To unlock the system, press Ctrl+Alt+Del and log in. To receive notification when the user logs in, use the [**WTSRegisterSessionNotification**](termserv.wtsregistersessionnotification) function to register to receive [**WM\_WTSSESSION\_CHANGE**](termserv.wm_wtssession_change) messages. When this message is received, check whether the *wParam* parameter is equal to WTS\_SESSION\_LOCK.

 

 




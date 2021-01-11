---
description: The following example uses the ExitWindows function to log off the current user.
ms.assetid: 74be3505-c4bd-4ae2-aaed-700382839006
title: How to Log Off the Current User
ms.topic: article
ms.date: 05/31/2018
---

# How to Log Off the Current User

The following example uses the [**ExitWindows**](/windows/desktop/api/Winuser/nf-winuser-exitwindows) function to log off the current user.

``` syntax
// Log off the current user. 

ExitWindows(0, 0);
```

The following example uses the [**ExitWindowsEx**](/windows/desktop/api/Winuser/nf-winuser-exitwindowsex) function to log off the current user.

``` syntax
// Log off the current user. 

ExitWindowsEx(EWX_LOGOFF, 0);
```

The application receives the [**WM\_QUERYENDSESSION**](wm-queryendsession.md) message and displays a dialog box asking the whether it is OK to end the session. If the user clicks **Yes**, the system logs off the user. If the user clicks **No**, the logoff is canceled.

``` syntax
// Process the message in the window procedure. 

case WM_QUERYENDSESSION:  
{ 
    int r; 
    r = MessageBox(NULL,(LPCWSTR)L"End the session?",(LPCWSTR)L"WM_QUERYENDSESSION",MB_YESNO);
 
    // Return TRUE to continue, FALSE to stop. 
 
    return r == IDYES; 
    break; 
}
```

## Related topics

<dl> <dt>

[Logging Off](logging-off.md)
</dt> </dl>

 

 




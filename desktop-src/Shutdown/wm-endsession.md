---
description: The WM\_ENDSESSION message is sent to an application after the system processes the results of the WM\_QUERYENDSESSION message. The WM\_ENDSESSION message informs the application whether the session is ending.
ms.assetid: 9bf04f24-da1e-4680-a47b-28e9c500635e
title: WM_ENDSESSION message (WinUser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_ENDSESSION message

The **WM\_ENDSESSION** message is sent to an application after the system processes the results of the [**WM\_QUERYENDSESSION**](wm-queryendsession.md) message. The **WM\_ENDSESSION** message informs the application whether the session is ending.

A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
LRESULT CALLBACK WindowProc( 
  HWND hwnd,      // handle to window 
  UINT uMsg,      // message identifier 
  WPARAM wParam,  // end-session option 
  LPARAM lParam   // logoff option
);
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

A handle to the window.

</dd> <dt>

*uMsg* 
</dt> <dd>

The **WM\_ENDSESSION** identifier.

</dd> <dt>

*wParam* 
</dt> <dd>

If the session is being ended, this parameter is **TRUE**; the session can end any time after all applications have returned from processing this message. Otherwise, it is **FALSE**.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter can be one or more of the following values. If this parameter is 0, the system is shutting down or restarting (it is not possible to determine which event is occurring).



| Value                                                                                                                                                                                                                                           | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ENDSESSION_CLOSEAPP"></span><span id="endsession_closeapp"></span><dl> <dt>**ENDSESSION\_CLOSEAPP**</dt> <dt>0x1</dt> </dl>        | If *wParam* is **TRUE**, the application must shut down. Any data should be saved automatically without prompting the user (for more information, see Remarks). The Restart Manager sends this message when the application is using a file that needs to be replaced, when it must service the system, or when system resources are exhausted. The application will be restarted if it has registered for restart using the [**RegisterApplicationRestart**](/windows/win32/api/winbase/nf-winbase-registerapplicationrestart) function. For more information, see [Guidelines for Applications](../rstmgr/guidelines-for-applications.md). <br/> If *wParam* is **FALSE**, the application should not shut down.<br/> |
| <span id="ENDSESSION_CRITICAL"></span><span id="endsession_critical"></span><dl> <dt>**ENDSESSION\_CRITICAL**</dt> <dt>0x40000000</dt> </dl> | The application is forced to shut down.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <span id="ENDSESSION_LOGOFF"></span><span id="endsession_logoff"></span><dl> <dt>**ENDSESSION\_LOGOFF**</dt> <dt>0x80000000</dt> </dl>       | The user is logging off. For more information, see [Logging Off](logging-off.md).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |



 

Note that this parameter is a bit mask. To test for this value, use a bit-wise operation; do not test for equality.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

Applications that have unsaved data could save the data to a temporary location and restore it the next time the application starts. It is recommended that applications save their data and state frequently; for example, automatically save data between save operations initiated by the user to reduce the amount of data to be saved at shutdown.

The application need not call the [**DestroyWindow**](/windows/win32/api/winuser/nf-winuser-destroywindow) or [**PostQuitMessage**](/windows/win32/api/winuser/nf-winuser-postquitmessage) function when the session is ending.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps \| UWP apps\]<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps \| UWP apps\]<br/>                                              |
| Header<br/>                   | <dl> <dt>WinUser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Logging Off](logging-off.md)
</dt> <dt>

[Shutting Down](shutting-down.md)
</dt> <dt>

[**DestroyWindow**](/windows/win32/api/winuser/nf-winuser-destroywindow)
</dt> <dt>

[**PostQuitMessage**](/windows/win32/api/winuser/nf-winuser-postquitmessage)
</dt> <dt>

[**SetProcessShutdownParameters**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessshutdownparameters)
</dt> <dt>

[**WM\_QUERYENDSESSION**](wm-queryendsession.md)
</dt> </dl>

 

 

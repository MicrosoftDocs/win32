---
description: Notifies applications that the system, typically a battery-powered personal computer, is about to enter a suspended mode.
ms.assetid: ceaa5ca4-799e-4801-96cd-aeea3dfd7d52
title: WM_POWER message (WinUser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_POWER message

Notifies applications that the system, typically a battery-powered personal computer, is about to enter a suspended mode.

> [!Note]  
> The **WM\_POWER** message is obsolete. It is provided only for compatibility with 16-bit Windows-based applications. Applications should use the [**WM\_POWERBROADCAST**](wm-powerbroadcast.md) message.

 

A window receives this message through its **WindowProc** function.


```C++
LRESULT CALLBACK WindowProc
  HWND   hwnd,    // handle to window
  UINT   uMsg,    // WM_POWER
  WPARAM wParam,  // power-event notification
  LPARAM lParam   // not used
); 
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

A handle to window.

</dd> <dt>

*uMsg* 
</dt> <dd>

The **WM\_POWER** message identifier.

</dd> <dt>

*wParam* 
</dt> <dd>

The power-event notification. This parameter can be one of the following values.



| Value                                                                                                                                                                        | Meaning                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PWR_CRITICALRESUME"></span><span id="pwr_criticalresume"></span><dl> <dt>**PWR\_CRITICALRESUME**</dt> </dl> | Indicates that the system is resuming operation after entering suspended mode without first broadcasting a **PWR\_SUSPENDREQUEST** notification message to the application. An application should perform any necessary recovery actions.<br/>                                                   |
| <span id="PWR_SUSPENDREQUEST"></span><span id="pwr_suspendrequest"></span><dl> <dt>**PWR\_SUSPENDREQUEST**</dt> </dl> | Indicates that the system is about to enter suspended mode.<br/>                                                                                                                                                                                                                                 |
| <span id="PWR_SUSPENDRESUME"></span><span id="pwr_suspendresume"></span><dl> <dt>**PWR\_SUSPENDRESUME**</dt> </dl>    | Indicates that the system is resuming operation after having entered suspended mode normally that is, the system broadcast a **PWR\_SUSPENDREQUEST** notification message to the application before the system was suspended. An application should perform any necessary recovery actions.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The value an application returns depends on the value of the *wParam* parameter. If *wParam* is **PWR\_SUSPENDREQUEST**, the return value is **PWR\_FAIL** to prevent the system from entering the suspended state; otherwise, it is **PWR\_OK**. If *wParam* is **PWR\_SUSPENDRESUME** or **PWR\_CRITICALRESUME**, the return value is zero.

## Remarks

This message is broadcast only to an application that is running on a system that conforms to the Advanced Power Management (APM) basic input/output system (BIOS) specification. The message is broadcast by the power-management driver to each window returned by the **EnumWindows** function.

The suspended mode is the state in which the greatest amount of power savings occurs, but all operational data and parameters are preserved. Random-access memory (RAM) contents are preserved, but many devices are likely to be turned off.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>WinUser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**WM\_POWERBROADCAST**](wm-powerbroadcast.md)
</dt> </dl>

 

 





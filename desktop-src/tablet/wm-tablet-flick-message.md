---
description: Sent when a user performs a pen flick. A window receives this message through its WindowProc function.
ms.assetid: 9433aadf-3440-4249-8f2c-3e22ebc949fb
title: WM_TABLET_FLICK message (Tpcshrd.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_TABLET\_FLICK message

Sent when a user performs a pen flick. A window receives this message through its [*WindowProc*](/windows/win32/api/winuser/nc-winuser-wndproc) function.


```C++
#define WM_TABLET_DEFBASE  0x02C0
#define WM_TABLET_FLICK    (WM_TABLET_DEFBASE + 11)     
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A [**FLICK\_DATA Structure**](/windows/desktop/api/tabflicks/ns-tabflicks-flick_data) that contains information about the pen flick that occurred.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**FLICK\_POINT Structure**](/windows/desktop/api/tabflicks/ns-tabflicks-flick_point) that specifies where the pen flick occurred.

</dd> </dl>

## Remarks

A pen flick is a unidirectional pen gesture that requires the user to contact the digitizer in a quick, straight flicking motion. A flick is characterized by high speed and a high degree of straightness. A flick is identified by its direction. Flicks can be made in eight directions corresponding to the cardinal and secondary compass directions.

When a pen flick occurs, Windows first notifies an application by sending a **WM\_TABLET\_FLICK** message, which a window receives through its [*WindowProc*](/windows/win32/api/winuser/nc-winuser-wndproc) function. Return the **FLICK\_WM\_HANDLED\_MASK** constant, described in [Flicks Constants](flicks-constants.md), to indicate that the application responded to the **WM\_TABLET\_FLICK** message. If the application does not return **FLICK\_WM\_HANDLED\_MASK**, Windows performs the default action specified in the flicks control panel by sending a follow-up notification, such as [**WM\_APPCOMMAND**](../inputdev/wm-appcommand.md), [**WM\_VSCROLL**](../controls/wm-vscroll.md), or [**WM\_KEYDOWN**](../inputdev/wm-keydown.md), depending on which action is associated with the pen flick.

Use caution when handling the **WM\_TABLET\_FLICK** message. **WM\_TABLET\_FLICK** is passed via the [**SendMessageTimeout**](/windows/win32/api/winuser/nf-winuser-sendmessagetimeouta) function. If you call methods on a COM interface, that object must be within the same process. If not, COM throws an exception.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Tpcshrd.h</dt> </dl> |



## See also

<dl> <dt>

[**flick\_data structure**](/windows/desktop/api/tabflicks/ns-tabflicks-flick_data)
</dt> <dt>

[**wm\_tablet\_flick message**](wm-tablet-flick-message.md)
</dt> <dt>

[flicks gestures](flicks-gestures.md)
</dt> <dt>

[responding to pen flicks](/previous-versions/windows/desktop/ms703447(v=vs.85))
</dt> </dl>

 

 

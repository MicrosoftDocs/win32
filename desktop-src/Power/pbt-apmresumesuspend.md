---
description: Notifies applications that the system has resumed operation after being suspended.
ms.assetid: 9058a2ff-9b8e-48e5-accb-4810c8598294
title: PBT_APMRESUMESUSPEND event (WinUser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PBT_APMRESUMESUSPEND event

Notifies applications that the system has resumed operation after being suspended.

A window receives this event through the [**WM\_POWERBROADCAST**](wm-powerbroadcast.md) message. The *wParam* and *lParam* parameters are set as described following.

```C++
LRESULT 
CALLBACK 
WindowProc( HWND hwnd,      // handle to window
            UINT uMsg,      // WM_POWERBROADCAST
            WPARAM wParam,  // PBT_APMRESUMESUSPEND
            LPARAM lParam); // zero
```

## Parameters

*hwnd* 

A handle to window.

*uMsg*

| Value                                                                                                                                                                                                                                                                   | Meaning                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| <span id="WM_POWERBROADCAST"></span><span id="wm_powerbroadcast"></span><dl> <dt>**[**WM\_POWERBROADCAST**](wm-powerbroadcast.md)**</dt> <dt>536 (0x218)</dt> </dl> | Message identifier.<br/> |

*wParam*

| Value                                                                                                                                                                                                                                           | Meaning                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| <span id="PBT_APMRESUMESUSPEND"></span><span id="pbt_apmresumesuspend"></span><dl> <dt>**PBT\_APMRESUMESUSPEND**</dt> <dt>7 (0x7)</dt> </dl> | Event identifier.<br/> |

*lParam* 

Reserved; must be zero.

## Return value

No return value.

## Remarks

An application can receive this event only if it received the [PBT\_APMSUSPEND](pbt-apmsuspend.md) event before the computer was suspended. Otherwise, the application will receive a [PBT\_APMRESUMECRITICAL](pbt-apmresumecritical.md) event.

If the system wakes due to user activity (such as pressing the power button) or if the system detects user interaction at the physical console (such as mouse or keyboard input) after waking unattended, the system first broadcasts the [PBT\_APMRESUMEAUTOMATIC](pbt-apmresumeautomatic.md) event, then it broadcasts the PBT\_APMRESUMESUSPEND event. In addition, the system turns on the display. Your application should reopen files that it closed when the system entered sleep and prepare for user input.

If the system wakes due to an external wake signal (remote wake), the system broadcasts only the [PBT\_APMRESUMEAUTOMATIC](pbt-apmresumeautomatic.md) event. The PBT\_APMRESUMESUSPEND event is not sent.

## Requirements

| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>WinUser.h (include Windows.h)</dt> </dl> |

## See also

* [System Wake-up Events](system-wake-up-events.md)
* [Power Management Events](power-management-events.md)
* [PBT_APMSUSPEND](pbt-apmsuspend.md)
* [PBT_APMRESUMECRITICAL](pbt-apmresumecritical.md)
* [WM_POWERBROADCAST](wm-powerbroadcast.md)

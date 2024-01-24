---
description: Notifies applications that the computer is about to enter a suspended state.
ms.assetid: 61b177a0-4cff-4740-bed8-a46c06c43be8
title: PBT_APMSUSPEND event (WinUser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PBT_APMSUSPEND event

Notifies applications that the computer is about to enter a suspended state. This event is typically broadcast when all applications and installable drivers have returned **TRUE** to a previous [PBT\_APMQUERYSUSPEND](pbt-apmquerysuspend.md) event.

A window receives this event through the [**WM\_POWERBROADCAST**](wm-powerbroadcast.md) message. The *wParam* and *lParam* parameters are set as described following.

```C++
LRESULT 
CALLBACK 
WindowProc( HWND hwnd,      // handle to window
            UINT uMsg,      // WM_POWERBROADCAST
            WPARAM wParam,  // PBT_APMSUSPEND
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

| Value                                                                                                                                                                                                                         | Meaning                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| <span id="PBT_APMSUSPEND"></span><span id="pbt_apmsuspend"></span><dl> <dt>**PBT\_APMSUSPEND**</dt> <dt>4 (0x4)</dt> </dl> | Event identifier.<br/> |

*lParam* 

Reserved: must be zero.

## Return value

No return value.

## Remarks

An application should process this event by completing all tasks necessary to save data.

The system allows approximately two seconds for an application to handle this notification. If an application is still performing operations after its time allotment has expired, the system may interrupt the application.

## Requirements

| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>WinUser.h (include Windows.h)</dt> </dl> |

## See also

* [System sleep criteria](system-sleep-criteria.md)
* [System wake-up events](system-wake-up-events.md)
* [Power management events](power-management-events.md)
* [PBT_APMQUERYSUSPEND](pbt-apmquerysuspend.md)
* [SetSystemPowerState](/windows/desktop/api/WinBase/nf-winbase-setsystempowerstate)
* [WM_POWERBROADCAST](wm-powerbroadcast.md)

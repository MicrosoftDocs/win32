---
description: Power setting change event sent with a WM\_POWERBROADCAST window message or in a HandlerEx notification callback for services.
ms.assetid: 0bcadb85-47c5-48a9-b3f9-f0a1ca60b503
title: PBT_POWERSETTINGCHANGE event (WinUser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PBT_POWERSETTINGCHANGE event

Power setting change event sent with a [**WM\_POWERBROADCAST**](wm-powerbroadcast.md) window message or in a [**HandlerEx**](/windows/desktop/api/winsvc/nc-winsvc-lphandler_function_ex) notification callback for services.

```C++
LRESULT 
CALLBACK 
WindowProc( HWND hwnd,      // handle to window
            UINT uMsg,      // WM_POWERBROADCAST
            WPARAM wParam,  // PBT_POWERSETTINGCHANGE
            LPARAM lParam); // Pointer to POWERBROADCAST_SETTING
```

## Parameters

*hwnd* 

A handle to window.

*uMsg*

| Value                                                                                                                                                                                                                                                                   | Meaning                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| <span id="WM_POWERBROADCAST"></span><span id="wm_powerbroadcast"></span><dl> <dt>**[**WM\_POWERBROADCAST**](wm-powerbroadcast.md)**</dt> <dt>536 (0x218)</dt> </dl> | Message identifier.<br/> |

*wParam*

| Value                                                                                                                                                                                                                                                        | Meaning                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| <span id="PBT_POWERSETTINGCHANGE"></span><span id="pbt_powersettingchange"></span><dl> <dt>**PBT\_POWERSETTINGCHANGE**</dt> <dt>32787 (0x8013)</dt> </dl> | Event identifier.<br/> |

*lParam*

Pointer to a [**POWERBROADCAST\_SETTING**](/windows/desktop/api/WinUser/ns-winuser-powerbroadcast_setting) structure.

## Return value

No return value.

## Requirements

| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>WinUser.h (include Windows.h)</dt> </dl> |

## See also

* [Power Management Events](power-management-events.md)
* [HandlerEx](/windows/desktop/api/winsvc/nc-winsvc-lphandler_function_ex)
* [WM_POWERBROADCAST](wm-powerbroadcast.md)
* [POWERBROADCAST_SETTING](/windows/desktop/api/WinUser/ns-winuser-powerbroadcast_setting)

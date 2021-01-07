---
description: Notifies applications that the APM BIOS has signaled an APM OEM event.
ms.assetid: 3251ac00-41f1-44e9-a579-fa31e7c7d2ff
title: PBT_APMOEMEVENT event (WinUser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PBT\_APMOEMEVENT event

\[PBT\_APMOEMEVENT is available for use in the operating systems specified in the Requirements section. Support for this event was removed in Windows Vista.\]

Notifies applications that the APM BIOS has signaled an APM OEM event.

A window receives this event through the [**WM\_POWERBROADCAST**](wm-powerbroadcast.md) message. The *wParam* and *lParam* parameters are set as described following.


```C++
LRESULT 
CALLBACK 
WindowProc( HWND   hwnd,    // handle to window
            UINT   uMsg,    // WM_POWERBROADCAST
            WPARAM wParam,  // PBT_APMOEMEVENT
            LPARAM lParam); // OEM event code
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

A handle to window.

</dd> <dt>*uMsg* </dt> <dd> 

| Value                                                                                                                                                                                                                                                                   | Meaning                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| <span id="WM_POWERBROADCAST"></span><span id="wm_powerbroadcast"></span><dl> <dt>**[**WM\_POWERBROADCAST**](wm-powerbroadcast.md)**</dt> <dt>536 (0x218)</dt> </dl> | Message identifier.<br/> |



 

</dd> <dt>*wParam* </dt> <dd> 

| Value                                                                                                                                                                                                                             | Meaning                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| <span id="PBT_APMOEMEVENT"></span><span id="pbt_apmoemevent"></span><dl> <dt>**PBT\_APMOEMEVENT**</dt> <dt>11 (0xB)</dt> </dl> | Event identifier.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

The OEM-defined event code that was signaled by the system's APM BIOS. OEM event codes are in the range 0200h - 02FFh.

</dd> </dl>

## Return value

No return value.

## Remarks

Because not all APM BIOS implementations provide OEM event notifications, this event may never be broadcast on some computers.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| End of client support<br/>    | Windows XP<br/>                                                                                    |
| End of server support<br/>    | Windows Server 2003<br/>                                                                           |
| Header<br/>                   | <dl> <dt>WinUser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Power Management Events](power-management-events.md)
</dt> <dt>

[**WM\_POWERBROADCAST**](wm-powerbroadcast.md)
</dt> </dl>

 

 





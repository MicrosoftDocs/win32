---
description: Notifies applications that the system has resumed operation.
ms.assetid: f2997905-26c9-4884-ae79-64df5ce6bc55
title: PBT_APMRESUMECRITICAL event (WinUser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PBT\_APMRESUMECRITICAL event

\[PBT\_APMRESUMECRITICAL is available for use in the operating systems specified in the Requirements section. Support for this event was removed in Windows Vista. Use [PBT\_APMRESUMEAUTOMATIC](pbt-apmresumeautomatic.md) instead.\]

Notifies applications that the system has resumed operation. This event can indicate that some or all applications did not receive a [PBT\_APMSUSPEND](pbt-apmsuspend.md) event. For example, this event can be broadcast after a critical suspension caused by a failing battery.

A window receives this event through the [**WM\_POWERBROADCAST**](wm-powerbroadcast.md) message. The *wParam* and *lParam* parameters are set as described following.


```C++
LRESULT 
CALLBACK 
WindowProc( HWND   hwnd,    // handle to window
            UINT   uMsg,    // WM_POWERBROADCAST
            WPARAM wParam,  // PBT_APMRESUMECRITICAL
            LPARAM lParam); // zero
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

| Value                                                                                                                                                                                                                                              | Meaning                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| <span id="PBT_APMRESUMECRITICAL"></span><span id="pbt_apmresumecritical"></span><dl> <dt>**PBT\_APMRESUMECRITICAL**</dt> <dt>6 (0x6)</dt> </dl> | Event identifier.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Reserved; must be zero.

</dd> </dl>

## Return value

No return value.

## Remarks

Because a critical suspension occurs without prior notification, resources and data previously available may not be present when the application receives this event. The application should attempt to restore its state to the best of its ability. While in a critical suspension, the system maintains the state of the DRAM and local hard disks, but may not maintain net connections. An application may need to take action with respect to files that were open on the network before critical suspension.

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

[System Wake-up Events](system-wake-up-events.md)
</dt> <dt>

[Power Management Events](power-management-events.md)
</dt> <dt>

[**WM\_POWERBROADCAST**](wm-powerbroadcast.md)
</dt> </dl>

 

 





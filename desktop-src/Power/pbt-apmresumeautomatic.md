---
description: Notifies applications that the system is resuming from sleep or hibernation. This event is delivered every time the system resumes and does not indicate whether a user is present.
ms.assetid: cd331f79-b64d-479e-aea8-5118ccc87224
title: PBT_APMRESUMEAUTOMATIC event (WinUser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PBT\_APMRESUMEAUTOMATIC event

Notifies applications that the system is resuming from sleep or hibernation. This event is delivered every time the system resumes and does not indicate whether a user is present.

A window receives this event through the [**WM\_POWERBROADCAST**](wm-powerbroadcast.md) message. The *wParam* and *lParam* parameters are set as described following.

> [!Note]  
> In Windows 10, version 1507 systems or later, if the system is resuming from sleep only to immediately enter hibernation, this event is not delivered. A [**WM\_POWERBROADCAST**](wm-powerbroadcast.md) message is not sent in this case.

 


```C++
LRESULT 
CALLBACK 
WindowProc( HWND hwnd,      // handle to window
            UINT uMsg,      // WM_POWERBROADCAST
            WPARAM wParam,  // PBT_APMRESUMEAUTOMATIC
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

| Value                                                                                                                                                                                                                                                   | Meaning                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| <span id="PBT_APMRESUMEAUTOMATIC"></span><span id="pbt_apmresumeautomatic"></span><dl> <dt>**PBT\_APMRESUMEAUTOMATIC**</dt> <dt>18 (0x12)</dt> </dl> | Event identifier.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Reserved; must be zero.

</dd> </dl>

## Return value

No return value.

## Remarks

If the system detects any user activity after broadcasting PBT\_APMRESUMEAUTOMATIC, it will broadcast a [PBT\_APMRESUMESUSPEND](pbt-apmresumesuspend.md) event to let applications know they can resume full interaction with the user.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>WinUser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[System Wake-up Events](system-wake-up-events.md)
</dt> <dt>

[Power Management Events](power-management-events.md)
</dt> <dt>

[PBT\_APMRESUMESUSPEND](pbt-apmresumesuspend.md)
</dt> <dt>

[**WM\_POWERBROADCAST**](wm-powerbroadcast.md)
</dt> </dl>

 

 





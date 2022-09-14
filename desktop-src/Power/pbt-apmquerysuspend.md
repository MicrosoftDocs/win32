---
description: Requests permission to suspend the computer. An application that grants permission should carry out preparations for the suspension before returning.
ms.assetid: 83cb0fdc-437e-4d03-87f0-6a416281c0d5
title: PBT_APMQUERYSUSPEND event (WinUser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PBT\_APMQUERYSUSPEND event

\[PBT\_APMQUERYSUSPEND is available for use in the operating systems specified in the Requirements section. Support for this event was removed in Windows Vista. Use [**SetThreadExecutionState**](/windows/desktop/api/Winbase/nf-winbase-setthreadexecutionstate) instead.\]

Requests permission to suspend the computer. An application that grants permission should carry out preparations for the suspension before returning.

A window receives this event through the [**WM\_POWERBROADCAST**](wm-powerbroadcast.md) message. The *wParam* and *lParam* parameters are set as described following.


```C++
LRESULT 
CALLBACK 
WindowProc( HWND   hwnd,    // handle to window
            UINT   uMsg,    // WM_POWERBROADCAST
            WPARAM wParam,  // PBT_APMQUERYSUSPEND
            LPARAM lParam); // action flags
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

| Value                                                                                                                                                                                                                                        | Meaning                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| <span id="PBT_APMQUERYSUSPEND"></span><span id="pbt_apmquerysuspend"></span><dl> <dt>**PBT\_APMQUERYSUSPEND**</dt> <dt>0 (0x0)</dt> </dl> | Event identifier.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

The action flags. If bit 0 is 1, the application can prompt the user for directions on how to prepare for the suspension; otherwise, the application must prepare without user interaction. All other bit values are reserved.

</dd> </dl>

## Return value

Return **TRUE** to grant the request to suspend. To deny the request, return **BROADCAST\_QUERY\_DENY**.

## Remarks

An application should process this event as quickly as possible. The application can prompt the user for directions on how to prepare for suspension only if bit 0 in the *Flags* parameter is set. However, if this message is issued because the user is closing the laptop lid, it will not be possible to prompt the user. Applications should respect that the user expects a certain behavior when they close the laptop lid or press the power button and allow the transition to succeed.

The system allows approximately 20 seconds for an application to remove the [**WM\_POWERBROADCAST**](wm-powerbroadcast.md) message that is sending the PBT\_APMQUERYSUSPEND event from the application's message queue. If an application does not remove the message from its queue in less than 20 seconds, the system will assume that the application is in a non-responsive state, and that the application agrees to the sleep request. Applications that do not process their message queues may have their operations interrupted. After it removes the message from the message queue, an application can take as much time as needed to perform any required operations before entering the sleep state. Any operations that could take longer then 20 seconds should be performed at this time, since the system allows only 20 seconds for operations to complete during [PBT\_APMSUSPEND](pbt-apmsuspend.md) processing.

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

[PBT\_APMSUSPEND](pbt-apmsuspend.md)
</dt> <dt>

[**WM\_POWERBROADCAST**](wm-powerbroadcast.md)
</dt> </dl>

 

 





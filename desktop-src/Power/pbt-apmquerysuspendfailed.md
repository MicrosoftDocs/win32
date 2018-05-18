---
Description: 'Notifies applications that permission to suspend the computer was denied.'
ms.assetid: '0f68628f-9d38-45ca-9487-95bf62075e00'
title: 'PBT\_APMQUERYSUSPENDFAILED event'
---

# PBT\_APMQUERYSUSPENDFAILED event

\[PBT\_APMQUERYSUSPENDFAILED is available for use in the operating systems specified in the Requirements section. Support for this event was removed in Windows Vista. Use [**SetThreadExecutionState**](setthreadexecutionstate.md) instead.\]

Notifies applications that permission to suspend the computer was denied. This event is broadcast if any application or driver returned **BROADCAST\_QUERY\_DENY** to a previous [PBT\_APMQUERYSUSPEND](pbt-apmquerysuspend.md) event.

A window receives this event through the [**WM\_POWERBROADCAST**](wm-powerbroadcast.md) message. The *wParam* and *lParam* parameters are set as described following.


```C++
LRESULT 
CALLBACK 
WindowProc( HWND   hwnd,    // handle to window
            UINT   uMsg,    // WM_POWERBROADCAST
            WPARAM wParam,  // PBT_APMQUERYSUSPENDFAILED
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

| Value                                                                                                                                                                                                                                                          | Meaning                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| <span id="PBT_APMQUERYSUSPENDFAILED"></span><span id="pbt_apmquerysuspendfailed"></span><dl> <dt>**PBT\_APMQUERYSUSPENDFAILED**</dt> <dt>2 (0x2)</dt> </dl> | Event identifier.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Reserved; must be zero.

</dd> </dl>

## Return value

No return value.

## Remarks

Applications typically respond to this event by resuming normal operation.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| End of client support<br/>    | Windows XP<br/>                                                                                    |
| End of server support<br/>    | Windows Server 2003<br/>                                                                           |
| Header<br/>                   | <dl> <dt>WinUser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Power Management](power-management-portal.md)
</dt> <dt>

[Power Management Events](power-management-events.md)
</dt> <dt>

[PBT\_APMQUERYSUSPEND](pbt-apmquerysuspend.md)
</dt> <dt>

[**WM\_POWERBROADCAST**](wm-powerbroadcast.md)
</dt> </dl>

 

 





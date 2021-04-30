---
description: The system broadcasts the DBT\_CONFIGCHANGECANCELED device event when a request to change the current configuration (dock or undock) has been canceled.
ms.assetid: b4b1455c-9a04-4fa0-a3fa-ed991f278c0c
title: DBT_CONFIGCHANGECANCELED event (Dbt.h)
ms.topic: reference
ms.date: 05/31/2018
---

# DBT\_CONFIGCHANGECANCELED event

The system broadcasts the DBT\_CONFIGCHANGECANCELED device event when a request to change the current configuration (dock or undock) has been canceled.

To broadcast this device event, the system uses the [**WM\_DEVICECHANGE**](wm-devicechange.md) message with *wParam* set to DBT\_CONFIGCHANGECANCELED and *lParam* set to zero.


```C++
LRESULT CALLBACK WindowProc(
  HWND hwnd,       // handle to window
  UINT uMsg,       // WM_DEVICECHANGE
  WPARAM wParam,   // device-change event
  LPARAM lParam    // event-specific data
);
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

A handle to a window.

</dd> <dt>

*uMsg* 
</dt> <dd>

The [**WM\_DEVICECHANGE**](wm-devicechange.md) message identifier.

</dd> <dt>

*wParam* 
</dt> <dd>

Set to DBT\_CONFIGCHANGECANCELED.

</dd> <dt>

*lParam* 
</dt> <dd>

Set to zero.

</dd> </dl>

## Return value

Return **TRUE**.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                   |
| Header<br/>                   | <dl> <dt>Dbt.h</dt> </dl> |



## See also

<dl> <dt>

[Device Events](device-events.md)
</dt> <dt>

[Device Management Events](device-management-events.md)
</dt> <dt>

[**WM\_DEVICECHANGE**](wm-devicechange.md)
</dt> </dl>

 

 





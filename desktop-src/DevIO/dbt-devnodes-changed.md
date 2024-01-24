---
description: The system broadcasts the DBT\_DEVNODES\_CHANGED device event when a device has been added to or removed from the system. Applications that maintain lists of devices in the system should refresh their lists.
ms.assetid: 62acc633-7dad-4792-a5a2-1f95356479d1
title: DBT_DEVNODES_CHANGED event (Dbt.h)
ms.topic: reference
ms.date: 05/31/2018
---

# DBT\_DEVNODES\_CHANGED event

The system broadcasts the DBT\_DEVNODES\_CHANGED device event when a device has been added to or removed from the system. Applications that maintain lists of devices in the system should refresh their lists.

To broadcast this device event, the system uses the [**WM\_DEVICECHANGE**](wm-devicechange.md) message with *wParam* set to DBT\_DEVNODES\_CHANGED and *lParam* set to zero.


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

Set to DBT\_DEVNODES\_CHANGED.

</dd> <dt>

*lParam* 
</dt> <dd>

Set to zero.

</dd> </dl>

## Return value

Return **TRUE**.

## Remarks

There is no additional information about which device has been added to or removed from the system. Applications that require more information should register for device notification using the [**RegisterDeviceNotification**](/windows/desktop/api/Winuser/nf-winuser-registerdevicenotificationa) function.

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

[**DEV\_BROADCAST\_HDR**](/windows/desktop/api/Dbt/ns-dbt-dev_broadcast_hdr)
</dt> <dt>

[**WM\_DEVICECHANGE**](wm-devicechange.md)
</dt> </dl>

 

 





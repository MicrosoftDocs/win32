---
Description: The system sends the DBT\_CUSTOMEVENT device event when a driver-defined custom event has occurred.
ms.assetid: 6e66fa93-0cd7-4202-83eb-cddc668525ae
title: DBT\_CUSTOMEVENT event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DBT\_CUSTOMEVENT event

The system sends the DBT\_CUSTOMEVENT device event when a driver-defined custom event has occurred.

To broadcast this device event, the system uses the [**WM\_DEVICECHANGE**](wm-devicechange.md) message with *wParam* set to DBT\_CUSTOMEVENT and *lParam* set as described following.


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

Set to DBT\_CUSTOMEVENT.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a structure identifying the device. The structure consists of an event-independent header, followed by event-dependent members that describe the device. To use this structure, treat the structure as a [**DEV\_BROADCAST\_HDR**](/windows/win32/Dbt/ns-dbt-_dev_broadcast_hdr?branch=master) structure, then check its **dbch\_devicetype** member to determine the device type.

</dd> </dl>

## Return value

Return **TRUE**.

## Requirements



|                                     |                                                                                  |
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

[**DEV\_BROADCAST\_HDR**](/windows/win32/Dbt/ns-dbt-_dev_broadcast_hdr?branch=master)
</dt> <dt>

[**WM\_DEVICECHANGE**](wm-devicechange.md)
</dt> </dl>

 

 





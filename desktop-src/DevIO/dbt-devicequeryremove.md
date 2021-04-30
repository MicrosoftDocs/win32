---
description: The system broadcasts the DBT\_DEVICEQUERYREMOVE device event to request permission to remove a device or piece of media.
ms.assetid: a0e9aa57-da0e-4e9c-99d0-5502040d2664
title: DBT_DEVICEQUERYREMOVE event (Dbt.h)
ms.topic: reference
ms.date: 05/31/2018
---

# DBT\_DEVICEQUERYREMOVE event

The system broadcasts the DBT\_DEVICEQUERYREMOVE device event to request permission to remove a device or piece of media. This message is the last chance for applications and drivers to prepare for this removal. However, any application can deny this request and cancel the operation.

To broadcast this device event, the system uses the [**WM\_DEVICECHANGE**](wm-devicechange.md) message with *wParam* set to DBT\_DEVICEQUERYREMOVE and *lParam* set as described following.


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

Set to DBT\_DEVICEQUERYREMOVE.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a structure identifying the device to remove. The structure consists of an event-independent header, followed by event-dependent members that describe the device. To use this structure, treat the structure as a [**DEV\_BROADCAST\_HDR**](/windows/desktop/api/Dbt/ns-dbt-dev_broadcast_hdr) structure, then check its **dbch\_devicetype** member to determine the device type.

</dd> </dl>

## Return value

Return **TRUE** to grant permission to remove a device.

Return BROADCAST\_QUERY\_DENY to deny permission to remove a device.

## Remarks

You must close all handles to the device or the device removal will fail.

## Examples

For an example, see [Processing a Request to Remove a Device](processing-a-request-to-remove-a-device.md).

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

 

 





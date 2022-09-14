---
description: The system broadcasts the DBT\_DEVICEREMOVEPENDING device event when a device or piece of media is being removed and is no longer available for use.
ms.assetid: 28cb4481-8961-4896-9608-afccba9a2bfe
title: DBT_DEVICEREMOVEPENDING event (Dbt.h)
ms.topic: reference
ms.date: 05/31/2018
---

# DBT\_DEVICEREMOVEPENDING event

The system broadcasts the DBT\_DEVICEREMOVEPENDING device event when a device or piece of media is being removed and is no longer available for use.

To broadcast this device event, the system uses the [**WM\_DEVICECHANGE**](wm-devicechange.md) message with *wParam* set to DBT\_DEVICEREMOVEPENDING and *lParam* set as described following.


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

Set to DBT\_DEVICEREMOVEPENDING.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a structure identifying the device. The structure consists of an event-independent header, followed by event-dependent members that describe the device. To use this structure, treat the structure as a [**DEV\_BROADCAST\_HDR**](/windows/desktop/api/Dbt/ns-dbt-dev_broadcast_hdr) structure, then check its **dbch\_devicetype** member to determine the device type.

</dd> </dl>

## Return value

Return **TRUE**.

## Remarks

The system may broadcast a DBT\_DEVICEREMOVEPENDING message without sending a corresponding [DBT\_DEVICEQUERYREMOVE](dbt-devicequeryremove.md) message. In such cases, the applications and drivers must recover from the loss of the device as best they can.

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

 

 





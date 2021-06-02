---
description: Notifies an application of a change to the hardware configuration of a device or the computer.
ms.assetid: b64a3983-ee75-4199-9778-1e5b7cec59e4
title: WM_DEVICECHANGE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_DEVICECHANGE message

Notifies an application of a change to the hardware configuration of a device or the computer.

A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.

```C++
LRESULT CALLBACK WindowProc(HWND   hwnd,     // handle to window
                            UINT   uMsg,     // WM_DEVICECHANGE
                            WPARAM wParam,   // device-change event
                            LPARAM lParam ); // event-specific data
```

## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

A handle to the window.

</dd> <dt>

*uMsg* 
</dt> <dd>

The **WM\_DEVICECHANGE** identifier.

</dd> <dt>

*wParam* 
</dt> <dd>

The event that has occurred. This parameter can be one of the following values from the Dbt.h header file.

| Value | Meaning |
|-------|---------|
| **[DBT\_DEVNODES\_CHANGED](dbt-devnodes-changed.md)**</br>0x0007 | A device has been added to or removed from the system. |
| **[DBT\_QUERYCHANGECONFIG](dbt-querychangeconfig.md)**</br>0x0017 | Permission is requested to change the current configuration (dock or undock). |
| **[DBT\_CONFIGCHANGED](dbt-configchanged.md)**</br>0x0018 | The current configuration has changed, due to a dock or undock. |
| **[DBT\_CONFIGCHANGECANCELED](dbt-configchangecanceled.md)**</br>0x0019 | A request to change the current configuration (dock or undock) has been canceled. |
| **[DBT\_DEVICEARRIVAL](dbt-devicearrival.md)**</br>0x8000 | A device or piece of media has been inserted and is now available. |
| **[DBT\_DEVICEQUERYREMOVE](dbt-devicequeryremove.md)**</br>0x8001 | Permission is requested to remove a device or piece of media. Any application can deny this request and cancel the removal. |
| **[DBT\_DEVICEQUERYREMOVEFAILED](dbt-devicequeryremovefailed.md)**</br>0x8002 | A request to remove a device or piece of media has been canceled. |
| **[DBT\_DEVICEREMOVEPENDING](dbt-deviceremovepending.md)**</br>0x8003 | A device or piece of media is about to be removed. Cannot be denied. |
| **[DBT\_DEVICEREMOVECOMPLETE](dbt-deviceremovecomplete.md)**</br>0x8004 | A device or piece of media has been removed. |
| **[DBT\_DEVICETYPESPECIFIC](dbt-devicetypespecific.md)**</br>0x8005 | A device-specific event has occurred. |
| **[DBT\_CUSTOMEVENT](dbt-customevent.md)**</br>0x8006 | A custom event has occurred. |
| **[DBT\_USERDEFINED](dbt-userdefined.md)**</br>0xFFFF | The meaning of this message is user-defined. |

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a structure that contains event-specific data. Its format depends on the value of the *wParam* parameter. For more information, refer to the documentation for each event.

</dd> </dl>

## Return value

Return **TRUE** to grant the request.

Return **BROADCAST\_QUERY\_DENY** to deny the request.

## Remarks

For devices that offer software-controllable features, such as ejection and locking, the system typically sends a [DBT\_DEVICEREMOVEPENDING](dbt-deviceremovepending.md) message to let applications and device drivers end their use of the device gracefully. If the system forcibly removes a device, it may not send a [DBT\_DEVICEQUERYREMOVE](dbt-devicequeryremove.md) message before doing so.

## Requirements

| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Minimum supported client | Windows XP |
| Minimum supported server | Windows Server 2003|
| Header | <dl> <dt>Winuser.h (include Windows.h or Dbt.h)</dt> </dl> |

## See also

<dl> <dt>

[DBT\_CONFIGCHANGECANCELED](dbt-configchangecanceled.md)
</dt> <dt>

[DBT\_CONFIGCHANGED](dbt-configchanged.md)
</dt> <dt>

[DBT\_CUSTOMEVENT](dbt-customevent.md)
</dt> <dt>

[DBT\_DEVICEARRIVAL](dbt-devicearrival.md)
</dt> <dt>

[DBT\_DEVICEQUERYREMOVE](dbt-devicequeryremove.md)
</dt> <dt>

[DBT\_DEVICEQUERYREMOVEFAILED](dbt-devicequeryremovefailed.md)
</dt> <dt>

[DBT\_DEVICEREMOVECOMPLETE](dbt-deviceremovecomplete.md)
</dt> <dt>

[DBT\_DEVICEREMOVEPENDING](dbt-deviceremovepending.md)
</dt> <dt>

[DBT\_DEVICETYPESPECIFIC](dbt-devicetypespecific.md)
</dt> <dt>

[DBT\_DEVNODES\_CHANGED](dbt-devnodes-changed.md)
</dt> <dt>

[DBT\_QUERYCHANGECONFIG](dbt-querychangeconfig.md)
</dt> <dt>

[DBT\_USERDEFINED](dbt-userdefined.md)
</dt> </dl>

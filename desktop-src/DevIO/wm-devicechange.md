---
Description: Notifies an application of a change to the hardware configuration of a device or the computer.
ms.assetid: b64a3983-ee75-4199-9778-1e5b7cec59e4
title: WM_DEVICECHANGE message
ms.topic: article
ms.date: 05/31/2018
---

# WM\_DEVICECHANGE message

Notifies an application of a change to the hardware configuration of a device or the computer.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633573) function.


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



| Value                                                                                                                                                                                                                                                                                                  | Meaning                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DBT_CONFIGCHANGECANCELED"></span><span id="dbt_configchangecanceled"></span><dl> <dt>**[DBT\_CONFIGCHANGECANCELED](dbt-configchangecanceled.md)**</dt> <dt>0x0019</dt> </dl>             | A request to change the current configuration (dock or undock) has been canceled.<br/>                                           |
| <span id="DBT_CONFIGCHANGED"></span><span id="dbt_configchanged"></span><dl> <dt>**[DBT\_CONFIGCHANGED](dbt-configchanged.md)**</dt> <dt>0x0018</dt> </dl>                                         | The current configuration has changed, due to a dock or undock.<br/>                                                             |
| <span id="DBT_CUSTOMEVENT"></span><span id="dbt_customevent"></span><dl> <dt>**[DBT\_CUSTOMEVENT](dbt-customevent.md)**</dt> <dt>0x8006</dt> </dl>                                                 | A custom event has occurred.<br/>                                                                                                |
| <span id="DBT_DEVICEARRIVAL"></span><span id="dbt_devicearrival"></span><dl> <dt>**[DBT\_DEVICEARRIVAL](dbt-devicearrival.md)**</dt> <dt>0x8000</dt> </dl>                                         | A device or piece of media has been inserted and is now available.<br/>                                                          |
| <span id="DBT_DEVICEQUERYREMOVE"></span><span id="dbt_devicequeryremove"></span><dl> <dt>**[DBT\_DEVICEQUERYREMOVE](dbt-devicequeryremove.md)**</dt> <dt>0x8001</dt> </dl>                         | Permission is requested to remove a device or piece of media. Any application can deny this request and cancel the removal.<br/> |
| <span id="DBT_DEVICEQUERYREMOVEFAILED"></span><span id="dbt_devicequeryremovefailed"></span><dl> <dt>**[DBT\_DEVICEQUERYREMOVEFAILED](dbt-devicequeryremovefailed.md)**</dt> <dt>0x8002</dt> </dl> | A request to remove a device or piece of media has been canceled.<br/>                                                           |
| <span id="DBT_DEVICEREMOVECOMPLETE"></span><span id="dbt_deviceremovecomplete"></span><dl> <dt>**[DBT\_DEVICEREMOVECOMPLETE](dbt-deviceremovecomplete.md)**</dt> <dt>0x8004</dt> </dl>             | A device or piece of media has been removed.<br/>                                                                                |
| <span id="DBT_DEVICEREMOVEPENDING"></span><span id="dbt_deviceremovepending"></span><dl> <dt>**[DBT\_DEVICEREMOVEPENDING](dbt-deviceremovepending.md)**</dt> <dt>0x8003</dt> </dl>                 | A device or piece of media is about to be removed. Cannot be denied.<br/>                                                        |
| <span id="DBT_DEVICETYPESPECIFIC"></span><span id="dbt_devicetypespecific"></span><dl> <dt>**[DBT\_DEVICETYPESPECIFIC](dbt-devicetypespecific.md)**</dt> <dt>0x8005</dt> </dl>                     | A device-specific event has occurred.<br/>                                                                                       |
| <span id="DBT_DEVNODES_CHANGED"></span><span id="dbt_devnodes_changed"></span><dl> <dt>**[DBT\_DEVNODES\_CHANGED](dbt-devnodes-changed.md)**</dt> <dt>0x0007</dt> </dl>                            | A device has been added to or removed from the system.<br/>                                                                      |
| <span id="DBT_QUERYCHANGECONFIG"></span><span id="dbt_querychangeconfig"></span><dl> <dt>**[DBT\_QUERYCHANGECONFIG](dbt-querychangeconfig.md)**</dt> <dt>0x0017</dt> </dl>                         | Permission is requested to change the current configuration (dock or undock).<br/>                                               |
| <span id="DBT_USERDEFINED"></span><span id="dbt_userdefined"></span><dl> <dt>**[DBT\_USERDEFINED](dbt-userdefined.md)**</dt> <dt>0xFFFF</dt> </dl>                                                 | The meaning of this message is user-defined.<br/>                                                                                |



 

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



|                                     |                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                                             |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                                                    |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h or Dbt.h)</dt> </dl> |



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

 

 





---
description: System-level event generated on a Parental Controls setting change.
ms.assetid: 2540c3cc-96d0-4e01-a525-4da4a857cb58
title: WPCEVENT_SYS_SETTINGCHANGE event (Wpcevent.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WPCEVENT\_SYS\_SETTINGCHANGE event

System-level event generated on a Parental Controls setting change.


```C++
const EVENT_DESCRIPTOR WPCEVENT_SYS_SETTINGCHANGE = {0x1, 0x0, 0x10, 0x4, 0x15, 0x1, 0x8000000000000010};
```



## Parameters

<dl> <dt>

*Class* 
</dt> <dd>

The class that is generating the event.

</dd> <dt>

*Setting* 
</dt> <dd>

A value of the **WPC\_SETTINGS** enumeration.

</dd> <dt>

*Owner* 
</dt> <dd>

The security identifier of the user who is generating the event.

</dd> <dt>

*OldVal* 
</dt> <dd>

The previous value of this setting, if deleted or changed.

</dd> <dt>

*NewVal* 
</dt> <dd>

The new value of this setting, if added or changed.

</dd> <dt>

*Reason* 
</dt> <dd>

A value of the [**WPCFLAG\_ISBLOCKED**](/windows/win32/api/wpcevent/ne-wpcevent-wpcflag_isblocked) enumeration that indicates information about what events are blocked from use and what controls are in place.

</dd> <dt>

*Optional* 
</dt> <dd>

An optional field.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | None supported<br/>                                                             |
| Header<br/>                   | <dl> <dt>Wpcevent.h</dt> </dl> |



## See also

<dl> <dt>

[Using Logging APIs for Parental Controls](using-logging-apis-for-parental-controls.md)
</dt> <dt>

[**WPC\_ARGS\_CONVERSATIONINITEVENT**](/windows/win32/api/wpcevent/ne-wpcevent-wpc_args_conversationinitevent)
</dt> </dl>

 

 





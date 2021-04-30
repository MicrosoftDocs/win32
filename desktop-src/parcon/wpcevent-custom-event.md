---
description: Per-user event that supports up to three fields.
ms.assetid: e6cf8008-b896-453b-9946-a6b3d94a991a
title: WPCEVENT_CUSTOM event (Wpcevent.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WPCEVENT\_CUSTOM event

Per-user event that supports up to three fields.

Events are displayed in the **Activity Viewer** in the **Other** section with the following hierarchy:

1.  Publisher

2.  Application

3.  Event


```C++
const EVENT_DESCRIPTOR WPCEVENT_CUSTOM = {0xd, 0x0, 0x10, 0x4, 0x17, 0xd, 0x8000000000000030};
```



## Parameters

<dl> <dt>

*Publisher* 
</dt> <dd>

The publisher of the event (for example, a company name).

</dd> <dt>

*AppName* 
</dt> <dd>

The name of the application that is generating the event.

</dd> <dt>

*AppVersion* 
</dt> <dd>

The version of the application that is generating the event.

</dd> <dt>

*Event* 
</dt> <dd>

The name for the event.

</dd> <dt>

*Value1* 
</dt> <dd>

Custom field 1.

</dd> <dt>

*Value2* 
</dt> <dd>

Custom field 2.

</dd> <dt>

*Value3* 
</dt> <dd>

Custom field 3.

</dd> <dt>

*Blocked* 
</dt> <dd>

A value of the [**WPCFLAG\_ISBLOCKED**](/windows/win32/api/wpcevent/ne-wpcevent-wpcflag_isblocked) enumeration that indicates information about what events are blocked from use and what controls are in place.

</dd> <dt>

*Reason* 
</dt> <dd>

A custom string that provides extra information about the reason for blocking or not blocking.

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

 

 





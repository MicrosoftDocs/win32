---
description: Per-user event provided for logging initiation of conversations by Instant Messaging clients.
ms.assetid: b2cd1d37-9993-4990-83b7-b147a109e4af
title: WPCEVENT_IM_INVITATION event (Wpcevent.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WPCEVENT\_IM\_INVITATION event

Per-user event provided for logging initiation of conversations by Instant Messaging clients.


```C++
const EVENT_DESCRIPTOR WPCEVENT_IM_INVITATION = {0x7, 0x0, 0x10, 0x4, 0x16, 0x7, 0x8000000000000030};
```



## Parameters

<dl> <dt>

*AppName* 
</dt> <dd>

The name of the application that is generating the event.

</dd> <dt>

*AppVersion* 
</dt> <dd>

The version string for the application that is generating the event.

</dd> <dt>

*AccountName* 
</dt> <dd>

The instant messaging account identity string.

</dd> <dt>

*ConvID* 
</dt> <dd>

The identifier for the conversation.

</dd> <dt>

*RequestingIP* 
</dt> <dd>

A string that contains the IP address of the computer that is sending the invitation.

</dd> <dt>

*Sender* 
</dt> <dd>

The instant messaging account identity string for the account that is issuing the invitation.

</dd> <dt>

*Reason* 
</dt> <dd>

A value of the [**WPCFLAG\_ISBLOCKED**](/windows/win32/api/wpcevent/ne-wpcevent-wpcflag_isblocked) enumeration that indicates information about what events are blocked from use and what controls are in place.

</dd> <dt>

*RecipCount* 
</dt> <dd>

The count of recipients who are receiving the invitation and who have identities defined in the recipient field.

</dd> <dt>

*Recipient* 
</dt> <dd>

A delimited string that contains instant messaging account identity strings for the recipients of the invitation.

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

 

 




